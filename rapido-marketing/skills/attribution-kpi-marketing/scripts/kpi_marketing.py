#!/usr/bin/env python3
"""KPI marketing par canal + attribution simple (stdlib uniquement).

Repli quand le skill catalogue-kpi (rapido-startup) n'est pas installé. Le
modèle NE calcule JAMAIS de tête : ce script agrège les compteurs réels par
canal (dépense, clients, revenu, contacts premier/dernier point) et sort CAC,
LTGP, ROI + la part d'attribution selon un modèle SIMPLE et ASSUMÉ (premier ou
dernier point de contact — pas de multi-touch probabiliste inventé).

Entrée (fichier JSON en argument, ou stdin) :
    {"modele": "dernier",                 // "premier" | "dernier"
     "canaux": [
        {"canal": "referral", "depense": 500, "clients": 10,
         "revenu_brut": 6000, "cout_livraison": 2000,
         "contacts_premier": 8, "contacts_dernier": 10}, ...]}

Sortie (stdout, JSON) : par canal CAC, LTGP, ROI, part d'attribution ; total ;
rappel des limites du modèle. Code : 0.
"""
import json
import sys


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def ratio(num, den):
    return round(num / den, 2) if den else None


def analyser(data):
    modele = data.get("modele", "dernier")
    champ = "contacts_premier" if modele == "premier" else "contacts_dernier"
    canaux = data.get("canaux") or []

    total_attrib = sum((c.get(champ) or 0) for c in canaux) or 1
    lignes = []
    for c in canaux:
        dep = c.get("depense", 0) or 0
        cli = c.get("clients", 0) or 0
        rev = c.get("revenu_brut", 0) or 0
        cout = c.get("cout_livraison", 0) or 0
        attrib = c.get(champ) or 0
        lignes.append({
            "canal": c.get("canal", "?"),
            "CAC": ratio(dep, cli),                       # coût / client
            "LTGP": ratio(rev - cout, cli),               # marge brute / client
            "ROI": ratio(rev - dep, dep),                 # (revenu - dépense)/dépense
            "attribution_pct": round(100 * attrib / total_attrib, 1),
            "modele_attribution": modele,
        })
    return {
        "formules": {
            "CAC": "dépense / clients",
            "LTGP": "(revenu_brut - cout_livraison) / clients",
            "ROI": "(revenu_brut - dépense) / dépense",
            "attribution_pct": f"contacts ({modele} point) du canal / total * 100",
        },
        "limites": ("attribution SINGLE-TOUCH (premier OU dernier point) — "
                    "modèle simple et assumé ; pas de multi-touch probabiliste. "
                    "Le serveur n'expose pas d'attribution multi-touch (cf. M0)."),
        "par_canal": lignes,
    }


def main():
    print(json.dumps(analyser(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
