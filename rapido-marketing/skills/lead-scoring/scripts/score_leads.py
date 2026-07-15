#!/usr/bin/env python3
"""Lead scoring transparent à 2 axes (fit ICP × engagement) — stdlib uniquement.

Le modèle NE calcule JAMAIS un score de tête : ce script applique des
pondérations ÉDITABLES (définies dans ./rapido-kb/marketing/scoring.md, passées
en entrée) aux données CRM réelles, et sort un score décomposé + une tranche.

Entrée (fichier JSON en argument, ou stdin) :
    {"model": {
        "fit":        {"secteur_cible": 30, "taille_cible": 20, "region_cible": 10},
        "engagement": {"form_submit": 20, "cta_click": 10, "rdv": 30, "email_open": 5},
        "cap_engagement": 3,          // nb max compté par signal (anti-emballement)
        "seuils": {"chaud": 70, "tiede": 40}
     },
     "leads": [
        {"nom": "Prospect A",
         "fit":        {"secteur_cible": true, "taille_cible": true, "region_cible": false},
         "engagement": {"form_submit": 1, "cta_click": 2, "rdv": 0, "email_open": 5}},
        ...]}
  fit = critères booléens (poids ajouté si vrai) ;
  engagement = compteurs (poids * min(compte, cap)).

Sortie (stdout, JSON) : chaque lead avec fit_score, engagement_score, total,
tranche (chaud/tiede/froid) + décomposition ; liste triée par total décroissant.
Code de sortie : 0. Aucune écriture CRM (le skill écrit APRÈS confirmation).
"""
import json
import sys


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def scorer_un(lead, model):
    poids_fit = model.get("fit", {})
    poids_eng = model.get("engagement", {})
    cap = model.get("cap_engagement", 3)

    detail_fit, fit_score = {}, 0
    for critere, poids in poids_fit.items():
        if (lead.get("fit") or {}).get(critere):
            detail_fit[critere] = poids
            fit_score += poids

    detail_eng, eng_score = {}, 0
    for signal, poids in poids_eng.items():
        compte = (lead.get("engagement") or {}).get(signal) or 0
        pts = poids * min(compte, cap)
        if pts:
            detail_eng[signal] = pts
            eng_score += pts

    return fit_score, eng_score, detail_fit, detail_eng


def tranche_de(total, seuils):
    if total >= seuils.get("chaud", 70):
        return "chaud"
    if total >= seuils.get("tiede", 40):
        return "tiede"
    return "froid"


def scorer(data):
    model = data.get("model") or {}
    seuils = model.get("seuils", {"chaud": 70, "tiede": 40})
    lignes = []
    for lead in (data.get("leads") or []):
        fit, eng, df, de = scorer_un(lead, model)
        total = fit + eng
        lignes.append({
            "nom": lead.get("nom", "?"),
            "fit_score": fit,
            "engagement_score": eng,
            "total": total,
            "tranche": tranche_de(total, seuils),
            "detail_fit": df,
            "detail_engagement": de,
        })
    lignes.sort(key=lambda x: x["total"], reverse=True)
    par_tranche = {t: sum(1 for l in lignes if l["tranche"] == t)
                   for t in ("chaud", "tiede", "froid")}
    return {
        "formule": ("total = somme(poids fit si critère vrai) + "
                    "somme(poids engagement * min(compte, cap))"),
        "seuils": seuils,
        "par_tranche": par_tranche,
        "leads": lignes,
    }


def main():
    print(json.dumps(scorer(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
