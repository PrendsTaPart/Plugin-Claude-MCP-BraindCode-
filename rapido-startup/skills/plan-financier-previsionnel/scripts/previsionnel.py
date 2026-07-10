#!/usr/bin/env python3
"""Prévisionnel financier 36 mois (rapido-startup) — stdlib uniquement.

Entrée (JSON sur stdin) : les hypothèses canoniques, issues de
./rapido-kb/startup/business-plan/hypotheses.md :
{
  "tresorerie_initiale": 50000, "clients_initiaux": 0,
  "nouveaux_clients_mois": 5, "croissance_mensuelle": 0.10,
  "churn_mensuel": 0.03, "arpu": 99, "cogs_pct": 0.15, "cac": 400,
  "salaires_bruts_mensuels": 8000, "coeff_charges": 1.45,
  "embauches": [{"mois": 7, "brut": 3000}], "couts_fixes_mensuels": 2500,
  "justification_croissance": null,
  "dossier_sortie": "./rapido-kb/startup/business-plan/previsionnel"
}

Garde-fous intégrés (mêmes règles que le hook garde-projection-realiste) :
- churn_mensuel = 0 → REJET (aucune entreprise n'a zéro churn) ;
- croissance > 30 %/mois au-delà du mois 6 → REJET sans
  justification_croissance (texte recopié d'hypotheses.md).

Sorties écrites dans dossier_sortie : previsionnel-base.csv, -upside.csv,
-downside.csv, sensibilite.csv, PREVISIONNEL.md ; synthèse JSON sur stdout.
Salaires CHARGÉS = brut × coeff_charges (~1,45 France). Churn COMPOSÉ mois
par mois. Contrats annuels : à normaliser en ARPU mensuel AVANT (voir
catalogue-kpi). Scénarios ≠ promesses.
"""
import csv
import json
import os
import sys

MOIS = 36
SEUIL_CROISSANCE = 0.30
MOIS_CROISSANCE_LIBRE = 6

COLONNES = ["mois", "nouveaux", "clients", "mrr", "ca", "cogs", "salaires_charges",
            "marketing", "couts_fixes", "charges_totales", "resultat", "tresorerie"]


def valider(h):
    if float(h["churn_mensuel"]) <= 0:
        raise ValueError(
            "REJET garde-projection-realiste : churn = 0 (ou négatif). "
            "Aucune entreprise n'a zéro churn — reprendre l'hypothèse dans "
            "hypotheses.md (le downside stresse déjà le churn).")
    if float(h["croissance_mensuelle"]) > SEUIL_CROISSANCE and not h.get("justification_croissance"):
        raise ValueError(
            f"REJET garde-projection-realiste : croissance "
            f"{float(h['croissance_mensuelle']):.0%}/mois > 30 %/mois au-delà du mois "
            f"{MOIS_CROISSANCE_LIBRE} sans justification_croissance (à recopier "
            "d'hypotheses.md avec sa source).")


def salaires_bruts_du_mois(h, mois):
    total = float(h.get("salaires_bruts_mensuels", 0))
    for e in h.get("embauches", []) or []:
        if mois >= int(e["mois"]):
            total += float(e["brut"])
    return total


def simuler(h):
    """Modèle mois par mois sur 36 mois. Croissance plafonnée à 30 %/mois
    après le mois 6 sauf justification (validée en amont)."""
    churn = float(h["churn_mensuel"])
    croissance = float(h["croissance_mensuelle"])
    arpu = float(h["arpu"])
    cogs_pct = float(h.get("cogs_pct", 0))
    cac = float(h["cac"])
    coeff = float(h.get("coeff_charges", 1.45))
    fixes = float(h.get("couts_fixes_mensuels", 0))
    justifie = bool(h.get("justification_croissance"))

    clients = float(h.get("clients_initiaux", 0))
    treso = float(h.get("tresorerie_initiale", 0))
    lignes = []
    for m in range(1, MOIS + 1):
        taux = croissance
        if m > MOIS_CROISSANCE_LIBRE and croissance > SEUIL_CROISSANCE and not justifie:
            taux = SEUIL_CROISSANCE  # défense en profondeur (déjà rejeté en amont)
        nouveaux = float(h["nouveaux_clients_mois"]) * (1 + taux) ** (m - 1)
        clients = clients * (1 - churn) + nouveaux
        mrr = clients * arpu
        ca = mrr
        cogs = ca * cogs_pct
        salaires = salaires_bruts_du_mois(h, m) * coeff
        marketing = nouveaux * cac
        charges = salaires + marketing + fixes
        resultat = ca - cogs - charges
        treso += resultat
        lignes.append({"mois": m, "nouveaux": round(nouveaux, 1),
                       "clients": round(clients, 1), "mrr": round(mrr, 2),
                       "ca": round(ca, 2), "cogs": round(cogs, 2),
                       "salaires_charges": round(salaires, 2),
                       "marketing": round(marketing, 2),
                       "couts_fixes": round(fixes, 2),
                       "charges_totales": round(charges, 2),
                       "resultat": round(resultat, 2),
                       "tresorerie": round(treso, 2)})
    return lignes


def synthese(lignes):
    point_mort = next((l["mois"] for l in lignes if l["resultat"] >= 0), None)
    creux = min(l["tresorerie"] for l in lignes)
    premier_mois_negatif = next((l["mois"] for l in lignes if l["tresorerie"] < 0), None)
    return {
        "point_mort_mois": point_mort,  # premier mois de résultat >= 0
        "besoin_financement": round(max(0.0, -creux), 2),  # creux de trésorerie max
        "mois_tresorerie_negative": premier_mois_negatif,  # None = jamais sur 36 mois
        "tresorerie_fin_36_mois": lignes[-1]["tresorerie"],
        "mrr_mois_12": lignes[11]["mrr"],
        "mrr_mois_36": lignes[-1]["mrr"],
    }


def scenarios(h):
    base = dict(h)
    upside = dict(h, croissance_mensuelle=float(h["croissance_mensuelle"]) * 1.20)
    downside = dict(h, churn_mensuel=float(h["churn_mensuel"]) + 0.02,
                    cac=float(h["cac"]) * 1.30)
    return {"base": base, "upside": upside, "downside": downside}


def sensibilite(h):
    """Matrice churn × CAC → mois avant trésorerie négative (37 = jamais sur 36 mois)."""
    churn_base = float(h["churn_mensuel"])
    cac_base = float(h["cac"])
    variations_churn = [max(0.001, churn_base + d) for d in (-0.01, 0.0, 0.01, 0.02)]
    variations_cac = [cac_base * f for f in (0.85, 1.0, 1.15, 1.30)]
    matrice = []
    for ch in variations_churn:
        ligne = {"churn": round(ch, 4)}
        for ca_ in variations_cac:
            lignes = simuler(dict(h, churn_mensuel=ch, cac=ca_))
            mois_neg = next((l["mois"] for l in lignes if l["tresorerie"] < 0), 37)
            ligne[f"cac_{round(ca_, 2)}"] = mois_neg
        matrice.append(ligne)
    return matrice


def ecrire_csv(chemin, lignes):
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(lignes[0].keys()))
        w.writeheader()
        w.writerows(lignes)


def tableau_md(lignes, colonnes, pas=3):
    """Tableau markdown ; échantillonné sur `mois` (1, 2, 3, 6…) si pas > 1."""
    if pas <= 1 or "mois" not in lignes[0]:
        vus = lignes
    else:
        vus = [l for l in lignes if l["mois"] in (1, 2) or l["mois"] % pas == 0]
    tete = "| " + " | ".join(colonnes) + " |"
    sep = "|" + "|".join(["---"] * len(colonnes)) + "|"
    corps = ["| " + " | ".join(str(l[c]) for c in colonnes) + " |" for l in vus]
    return "\n".join([tete, sep] + corps)


def ecrire_previsionnel_md(dossier, resultats, matrice, h):
    parts = ["# Prévisionnel financier — 36 mois",
             "",
             "> Généré par plan-financier-previsionnel (rapido-startup) — "
             "**scénarios ≠ promesses** : projections conditionnées aux "
             "hypothèses d'`../hypotheses.md`. Document vivant : à mettre à "
             "jour à chaque jalon. Ceci n'est pas un conseil d'investissement.",
             ""]
    for nom, (lignes, syn) in resultats.items():
        parts += [f"## Scénario {nom}", "",
                  f"- Point mort (résultat ≥ 0) : mois {syn['point_mort_mois'] or '— (pas sur 36 mois)'}",
                  f"- Besoin de financement (creux de trésorerie max) : {syn['besoin_financement']} €",
                  f"- Trésorerie négative à partir du mois : {syn['mois_tresorerie_negative'] or 'jamais (36 mois)'}",
                  f"- MRR mois 12 : {syn['mrr_mois_12']} € — MRR mois 36 : {syn['mrr_mois_36']} €",
                  "",
                  tableau_md(lignes, ["mois", "clients", "mrr", "resultat", "tresorerie"]),
                  "", f"Détail mensuel complet : `previsionnel-{nom}.csv`", ""]
    parts += ["## Sensibilité churn × CAC — mois avant trésorerie négative (37 = jamais)",
              "", tableau_md(matrice, list(matrice[0].keys()), pas=1) if matrice else "", ""]
    with open(os.path.join(dossier, "PREVISIONNEL.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(parts))


def main():
    h = json.load(sys.stdin)
    valider(h)
    dossier = h.get("dossier_sortie", "./rapido-kb/startup/business-plan/previsionnel")
    os.makedirs(dossier, exist_ok=True)
    resultats = {}
    for nom, hyp in scenarios(h).items():
        lignes = simuler(hyp)
        resultats[nom] = (lignes, synthese(lignes))
        ecrire_csv(os.path.join(dossier, f"previsionnel-{nom}.csv"), lignes)
    matrice = sensibilite(h)
    ecrire_csv(os.path.join(dossier, "sensibilite.csv"), matrice)
    ecrire_previsionnel_md(dossier, resultats, matrice, h)
    print(json.dumps({
        "dossier": dossier,
        "scenarios": {nom: syn for nom, (_, syn) in resultats.items()},
        "fichiers": [f"previsionnel-{n}.csv" for n in resultats] + ["sensibilite.csv", "PREVISIONNEL.md"],
        "rappel": "Scénarios ≠ promesses ; document vivant ; pas un conseil d'investissement.",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as e:
        print(json.dumps({"erreur": str(e)}, ensure_ascii=False))
        sys.exit(2)
