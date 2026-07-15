#!/usr/bin/env python3
"""Backlog d'expériences growth scoré ICE (stdlib uniquement).

ICE = Impact × Confidence × Ease (chaque axe noté 1-10). Le modèle ne priorise
JAMAIS de tête : ce script calcule le score ICE et trie le backlog.

Entrée (fichier JSON en argument, ou stdin) :
    {"hypotheses": [
        {"nom": "CTA plus contrasté", "impact": 8, "confidence": 6, "ease": 9},
        ...]}

Sortie (stdout, JSON) : backlog trié par score ICE décroissant. Code : 0.
Score = moyenne(impact, confidence, ease) ; produit affiché pour départager.
"""
import json
import sys


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def borne(x):
    try:
        return max(1, min(10, float(x)))
    except (TypeError, ValueError):
        return 1.0


def scorer(data):
    lignes = []
    for h in (data.get("hypotheses") or []):
        i, c, e = borne(h.get("impact")), borne(h.get("confidence")), borne(h.get("ease"))
        lignes.append({
            "nom": h.get("nom", "?"),
            "impact": i, "confidence": c, "ease": e,
            "score_ice": round((i + c + e) / 3, 2),
            "produit": round(i * c * e, 1),
        })
    lignes.sort(key=lambda x: (x["score_ice"], x["produit"]), reverse=True)
    for rang, l in enumerate(lignes, 1):
        l["rang"] = rang
    return {
        "formule": "score_ice = moyenne(impact, confidence, ease), axes 1-10 ; "
                   "produit = impact*confidence*ease (départage)",
        "backlog_priorise": lignes,
    }


def main():
    print(json.dumps(scorer(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
