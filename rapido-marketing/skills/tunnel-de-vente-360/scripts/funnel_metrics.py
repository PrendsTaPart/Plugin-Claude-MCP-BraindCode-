#!/usr/bin/env python3
"""Métriques d'un tunnel de vente, étape par étape (stdlib uniquement).

Le modèle NE calcule JAMAIS les taux de tête : ce script prend les effectifs
réels de chaque étape du tunnel (impressions/visites/leads/devis/ventes… issus
des soumissions CRM, CTA, pipeline, ventes, get_conversion_par_canal) et sort
les taux de passage étape→étape, le taux global, et le GOULOT (pire passage).

Entrée (fichier JSON en argument, ou stdin) :
    {"etapes": [                       // ORDONNÉES, du haut vers le bas
        {"nom": "impressions", "valeur": 10000},
        {"nom": "visites",     "valeur": 800},
        {"nom": "leads",       "valeur": 120},
        {"nom": "devis",       "valeur": 30},
        {"nom": "ventes",      "valeur": 8}],
     "cibles": {"visites->leads": 0.10}}    // optionnel (taux cible par passage)

Sortie (stdout, JSON) : passages (taux + vs cible), taux global, goulot. Code 0.
"""
import json
import sys


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def taux(num, den):
    return round(num / den, 4) if den else 0.0


def analyser(data):
    etapes = data.get("etapes") or []
    cibles = data.get("cibles") or {}
    passages = []
    for i in range(len(etapes) - 1):
        a, b = etapes[i], etapes[i + 1]
        cle = f"{a.get('nom')}->{b.get('nom')}"
        t = taux(b.get("valeur", 0), a.get("valeur", 0))
        p = {"passage": cle, "de": a.get("valeur", 0),
             "vers": b.get("valeur", 0), "taux": t}
        if cle in cibles:
            p["cible"] = cibles[cle]
            p["vs_cible"] = "au-dessus" if t >= cibles[cle] else "en-dessous"
        passages.append(p)

    goulot = None
    if passages:
        goulot = min(passages, key=lambda x: x["taux"])["passage"]

    global_taux = 0.0
    if len(etapes) >= 2:
        global_taux = taux(etapes[-1].get("valeur", 0),
                           etapes[0].get("valeur", 0))

    return {
        "formule": "taux de passage = effectif étape N+1 / effectif étape N",
        "passages": passages,
        "taux_global": global_taux,
        "goulot": goulot,
        "note": "le goulot = passage au taux le plus faible → priorité d'A/B test",
    }


def main():
    print(json.dumps(analyser(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
