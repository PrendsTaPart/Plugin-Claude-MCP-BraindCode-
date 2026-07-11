#!/usr/bin/env python3
"""Calculs de KPI (rapido-startup) — stdlib uniquement, fonctions pures.

Usage : echo '{"kpi": "ltv", "entrees": {"arpu": 99, "marge_brute": 0.80,
"churn_mensuel": 0.05}, "seuil": null, "source_seuil": null}' | python3 calcul_kpi.py

Sortie JSON : {kpi, valeur, formule_appliquee, entrees, seuil, statut}.
Les montants sont attendus en UNITÉ PRINCIPALE (euros) : les centimes Stripe
sont convertis AVANT (voir references/formules-kpi.md). Le churn annualisé
est COMPOSÉ (jamais ×12) ; un contrat annuel entre dans le MRR à montant/12.
"""
import json
import math
import sys


# ------------------------------------------------------------ revenus
def mrr(abonnements):
    """Σ abonnements actifs normalisés au mois (annuel ÷ 12)."""
    total = 0.0
    for a in abonnements:
        montant = float(a["montant"])
        periodicite = a.get("periodicite", "mensuel")
        total += montant / 12 if periodicite == "annuel" else montant
    return round(total, 2)


def decompose_mrr(nouveau, expansion, contraction, churn):
    """net new MRR = nouveau + expansion − contraction − churn."""
    return round(float(nouveau) + float(expansion) - float(contraction) - float(churn), 2)


def arpu(mrr_total, clients_actifs):
    return round(float(mrr_total) / float(clients_actifs), 2)


def nrr(mrr_debut, expansion, contraction, churn_mrr):
    """(MRR début + expansion − contraction − churn) ÷ MRR début — base existante seule."""
    return round((float(mrr_debut) + float(expansion) - float(contraction)
                  - float(churn_mrr)) / float(mrr_debut), 4)


# ------------------------------------------------------------ rétention
def churn_rate(clients_debut, clients_perdus):
    return round(float(clients_perdus) / float(clients_debut), 4)


def churn_annualise_compose(churn_mensuel):
    """1 − (1 − churn_mensuel)^12 — COMPOSÉ, jamais ×12."""
    return round(1 - (1 - float(churn_mensuel)) ** 12, 4)


# ------------------------------------------------------------ unit economics
def cac(depenses_acquisition, nouveaux_clients):
    return round(float(depenses_acquisition) / float(nouveaux_clients), 2)


def ltv(arpu_mensuel, marge_brute_ratio, churn_mensuel):
    """ARPU × marge ÷ churn mensuel (ex. réf. : 99 × 0.80 ÷ 0.05 = 1584)."""
    return round(float(arpu_mensuel) * float(marge_brute_ratio) / float(churn_mensuel), 2)


def ltv_cac(ltv_valeur, cac_valeur):
    return round(float(ltv_valeur) / float(cac_valeur), 2)


def cac_payback(cac_valeur, arpu_mensuel, marge_brute_ratio):
    """CAC ÷ (ARPU × marge), en mois — sur la marge, pas le CA."""
    return round(float(cac_valeur) / (float(arpu_mensuel) * float(marge_brute_ratio)), 1)


# ------------------------------------------------------------ rentabilité & trésorerie
def marge_brute(ca, couts_directs):
    return round((float(ca) - float(couts_directs)) / float(ca), 4)


def burn_net(depenses_mois, encaissements_mois):
    return round(float(depenses_mois) - float(encaissements_mois), 2)


def runway(tresorerie, burn_net_mensuel):
    """Trésorerie ÷ burn net, en mois ; burn ≤ 0 → inf (rentable)."""
    b = float(burn_net_mensuel)
    if b <= 0:
        return math.inf
    return round(float(tresorerie) / b, 1)


def rule_of_40(croissance_pct, marge_pct):
    """Somme en POINTS de pourcentage (25 + 10 = 35)."""
    return round(float(croissance_pct) + float(marge_pct), 1)


def break_even_mrr(couts_fixes_mensuels, marge_brute_ratio):
    """MRR de point mort = coûts fixes ÷ marge brute."""
    return round(float(couts_fixes_mensuels) / float(marge_brute_ratio), 2)


def dso(creances_clients, ca_periode, jours_periode):
    return round(float(creances_clients) / float(ca_periode) * float(jours_periode), 1)


# ------------------------------------------------------------ commercial
def velocite_pipeline(nb_opportunites, taux_conversion, panier_moyen, duree_cycle_jours):
    """(opportunités × conversion × panier) ÷ cycle → valeur créée par JOUR."""
    return round(float(nb_opportunites) * float(taux_conversion)
                 * float(panier_moyen) / float(duree_cycle_jours), 2)


def pipeline_coverage(pipeline_pondere, objectif_periode):
    return round(float(pipeline_pondere) / float(objectif_periode), 2)


# ------------------------------------------------------------ restauration & services
def food_cost(cout_matieres, ca_nourriture):
    return round(float(cout_matieres) / float(ca_nourriture), 4)


def ticket_moyen(ca, nb_commandes):
    return round(float(ca) / float(nb_commandes), 2)


def charge_vs_contrat(heures_realisees, heures_contractuelles):
    return round(float(heures_realisees) / float(heures_contractuelles), 4)


def cout_revient_projet(heures, taux_horaire_charge, couts_directs):
    return round(float(heures) * float(taux_horaire_charge) + float(couts_directs), 2)


def taux_conversion_etape(passes, entres):
    """Conversion d'une étape de funnel = passés ÷ entrés (vues → clics →
    soumissions → prospects : appliquer étape par étape)."""
    entres = float(entres)
    if entres <= 0:
        return None
    return round(float(passes) / entres, 4)


# ------------------------------------------------------------ dispatch & seuils
FORMULES = {
    "mrr": (mrr, "MRR = Σ abonnements normalisés au mois (annuel ÷ 12) = {valeur}"),
    "decompose_mrr": (decompose_mrr, "net new MRR = {nouveau} + {expansion} − {contraction} − {churn} = {valeur}"),
    "arpu": (arpu, "ARPU = MRR ÷ clients actifs = {mrr_total} ÷ {clients_actifs} = {valeur}"),
    "nrr": (nrr, "NRR = ({mrr_debut} + {expansion} − {contraction} − {churn_mrr}) ÷ {mrr_debut} = {valeur}"),
    "churn_rate": (churn_rate, "churn = perdus ÷ début = {clients_perdus} ÷ {clients_debut} = {valeur}"),
    "churn_annualise_compose": (churn_annualise_compose, "churn annuel = 1 − (1 − {churn_mensuel})^12 = {valeur} (composé, jamais ×12)"),
    "cac": (cac, "CAC = dépenses acquisition ÷ nouveaux clients = {depenses_acquisition} ÷ {nouveaux_clients} = {valeur}"),
    "ltv": (ltv, "LTV = ARPU × marge ÷ churn = {arpu_mensuel} × {marge_brute_ratio} ÷ {churn_mensuel} = {valeur}"),
    "ltv_cac": (ltv_cac, "LTV:CAC = {ltv_valeur} ÷ {cac_valeur} = {valeur}"),
    "cac_payback": (cac_payback, "payback = CAC ÷ (ARPU × marge) = {cac_valeur} ÷ ({arpu_mensuel} × {marge_brute_ratio}) = {valeur} mois"),
    "marge_brute": (marge_brute, "marge brute = (CA − coûts directs) ÷ CA = ({ca} − {couts_directs}) ÷ {ca} = {valeur}"),
    "burn_net": (burn_net, "burn net = dépenses − encaissements = {depenses_mois} − {encaissements_mois} = {valeur}"),
    "runway": (runway, "runway = trésorerie ÷ burn net = {tresorerie} ÷ {burn_net_mensuel} = {valeur} mois"),
    "rule_of_40": (rule_of_40, "Rule of 40 = croissance + marge = {croissance_pct} + {marge_pct} = {valeur} points"),
    "break_even_mrr": (break_even_mrr, "MRR point mort = coûts fixes ÷ marge = {couts_fixes_mensuels} ÷ {marge_brute_ratio} = {valeur}"),
    "dso": (dso, "DSO = créances ÷ CA × jours = {creances_clients} ÷ {ca_periode} × {jours_periode} = {valeur} jours"),
    "velocite_pipeline": (velocite_pipeline, "vélocité = opps × conversion × panier ÷ cycle = {nb_opportunites} × {taux_conversion} × {panier_moyen} ÷ {duree_cycle_jours} = {valeur}/jour"),
    "pipeline_coverage": (pipeline_coverage, "coverage = pipeline pondéré ÷ objectif = {pipeline_pondere} ÷ {objectif_periode} = {valeur}×"),
    "food_cost": (food_cost, "food cost = coût matières ÷ CA nourriture = {cout_matieres} ÷ {ca_nourriture} = {valeur}"),
    "ticket_moyen": (ticket_moyen, "ticket moyen = CA ÷ commandes = {ca} ÷ {nb_commandes} = {valeur}"),
    "charge_vs_contrat": (charge_vs_contrat, "charge = réalisées ÷ contractuelles = {heures_realisees} ÷ {heures_contractuelles} = {valeur}"),
    "cout_revient_projet": (cout_revient_projet, "coût de revient = heures × taux chargé + coûts directs = {heures} × {taux_horaire_charge} + {couts_directs} = {valeur}"),
    "taux_conversion_etape": (taux_conversion_etape, "conversion étape = passés ÷ entrés = {passes} ÷ {entres} = {valeur}"),
}

# Seuils par défaut (= reference/seuils-defaut.md) — la KB PRIME toujours :
# le seuil passé dans l'entrée JSON écrase ces défauts.
SEUILS_DEFAUT = {
    "ltv_cac": {"type": "min", "valeur": 3.0, "libelle": "sain ≥ 3:1"},
    "cac_payback": {"type": "plage", "min": 5.0, "max": 12.0, "libelle": "5-12 mois"},
    "runway": {"type": "alerte_min", "valeur": 6.0, "cible_min": 12.0, "cible_max": 18.0,
               "libelle": "cible 12-18 mois, alerte < 6"},
    "churn_annualise_compose": {"type": "plage", "min": 0.03, "max": 0.08, "libelle": "B2B sain 3-8 %/an"},
    "marge_brute": {"type": "plage", "min": 0.70, "max": 0.85, "libelle": "SaaS 70-85 %"},
    "food_cost": {"type": "plage", "min": 0.28, "max": 0.35, "libelle": "28-35 %"},
    "rule_of_40": {"type": "min", "valeur": 40.0, "libelle": "≥ 40 points"},
    "dso": {"type": "max", "valeur": 45.0, "libelle": "< 45 jours"},
    "nrr": {"type": "min", "valeur": 1.0, "libelle": "> 100 %"},
    "pipeline_coverage": {"type": "plage", "min": 3.0, "max": 4.0, "libelle": "3-4×"},
}


def statut_vs_seuil(kpi, valeur, seuil):
    if seuil is None or valeur is None or valeur == math.inf:
        return "rentable (burn ≤ 0)" if valeur == math.inf else "sans_seuil"
    t = seuil.get("type")
    if t == "min":
        return "ok" if valeur >= seuil["valeur"] else "alerte"
    if t == "max":
        return "ok" if valeur <= seuil["valeur"] else "alerte"
    if t == "plage":
        if valeur < seuil["min"]:
            return "attention (sous la plage)"
        return "ok" if valeur <= seuil["max"] else "attention (au-dessus de la plage)"
    if t == "alerte_min":  # runway
        if valeur < seuil["valeur"]:
            return "alerte"
        if valeur < seuil.get("cible_min", seuil["valeur"]):
            return "attention"
        return "ok"
    return "sans_seuil"


def calculer(demande):
    kpi = demande["kpi"]
    entrees = demande.get("entrees", {})
    if kpi not in FORMULES:
        raise ValueError(f"KPI inconnu : {kpi} (disponibles : {', '.join(sorted(FORMULES))})")
    fonction, gabarit = FORMULES[kpi]
    valeur = fonction(**entrees)
    seuil = demande.get("seuil") or SEUILS_DEFAUT.get(kpi)
    source_seuil = demande.get("source_seuil") or (
        "seuils-defaut (défaut secteur)" if demande.get("seuil") is None and kpi in SEUILS_DEFAUT else None)
    contexte = {k: (v if not isinstance(v, list) else f"[{len(v)} éléments]") for k, v in entrees.items()}
    contexte["valeur"] = "infini" if valeur == math.inf else valeur
    return {
        "kpi": kpi,
        "valeur": "infini" if valeur == math.inf else valeur,
        "formule_appliquee": gabarit.format(**contexte),
        "entrees": entrees,
        "seuil": ({**seuil, "source": source_seuil} if seuil else None),
        "statut": statut_vs_seuil(kpi, valeur, seuil),
    }


def main():
    try:
        demande = json.load(sys.stdin)
        print(json.dumps(calculer(demande), ensure_ascii=False, indent=2))
        return 0
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"erreur": str(e)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
