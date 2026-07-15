#!/usr/bin/env python3
"""Analyse des clients gagnés → distribution des segments (stdlib uniquement).

Le modèle NE calcule JAMAIS de tête : ce script compte les fréquences par
dimension d'ENTREPRISE (secteur, taille, canal d'acquisition, région, techno)
sur les clients réellement gagnés (données RapidoCRM : list_entreprises,
get_top_clients, get_conversion_par_canal), et remonte les combinaisons
dominantes = base factuelle de l'ICP.

Entrée (fichier JSON en argument, ou stdin) :
    {"clients": [
        {"nom": "Resto A", "secteur": "restauration", "taille": "TPE",
         "canal": "referral", "region": "IDF", "techno": "foodeatup"}, ...],
     "conversion_par_canal": [               // optionnel (get_conversion_par_canal)
        {"canal": "referral", "taux": 0.12}, ...]}
  Champs absents → comptés en "inconnu" (jamais inventés).

Sortie (stdout, JSON) : effectif total, distribution triée par dimension (part
en %), top combinaisons (secteur+taille), et rappel des taux de conversion par
canal si fournis. Code de sortie : 0.
"""
import json
import sys
from collections import Counter

DIMENSIONS = ["secteur", "taille", "canal", "region", "techno"]


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def distribution(clients, champ):
    c = Counter((cl.get(champ) or "inconnu") for cl in clients)
    total = sum(c.values()) or 1
    return [
        {"valeur": v, "effectif": n, "part_pct": round(100 * n / total, 1)}
        for v, n in c.most_common()
    ]


def analyser(data):
    clients = data.get("clients") or []
    n = len(clients)
    dist = {d: distribution(clients, d) for d in DIMENSIONS}

    combos = Counter(
        f"{(cl.get('secteur') or 'inconnu')} / {(cl.get('taille') or 'inconnu')}"
        for cl in clients
    )
    top_combos = [
        {"segment": seg, "effectif": k,
         "part_pct": round(100 * k / (n or 1), 1)}
        for seg, k in combos.most_common(5)
    ]

    conv = data.get("conversion_par_canal") or []
    return {
        "total_clients": n,
        "formule": "part_pct = effectif de la valeur / total clients * 100",
        "distribution": dist,
        "top_segments_secteur_taille": top_combos,
        "conversion_par_canal": conv,
        "note": ("segments à confirmer avec la KB (offres/personas) avant "
                 "d'en faire l'ICP — le script ne décide pas, il mesure."),
    }


def main():
    print(json.dumps(analyser(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
