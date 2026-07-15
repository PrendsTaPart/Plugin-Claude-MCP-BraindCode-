#!/usr/bin/env python3
"""Lecture d'un A/B test : uplift + verdict honnête (stdlib uniquement).

Le modèle ne conclut JAMAIS de tête : ce script calcule les taux, l'uplift
relatif et un test z à deux proportions (math stdlib), puis rend un verdict
PASS / FAIL / INCONCLUSIF — sans inventer de significativité.

Entrée (fichier JSON en argument, ou stdin) :
    {"controle": {"n": 1000, "conversions": 50},
     "variante": {"n": 1000, "conversions": 65},
     "seuil_min_echantillon": 300}          // optionnel (défaut 300)

Verdict :
- INCONCLUSIF si min(n) < seuil (échantillon insuffisant) OU |z| < 1.96 ;
- PASS  si variante significativement meilleure (z >= 1.96) ;
- FAIL  si variante significativement pire (z <= -1.96).
Sortie (stdout, JSON). Code : 0.
"""
import json
import math
import sys


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def taux(c, n):
    return c / n if n else 0.0


def analyser(data):
    ctrl = data.get("controle") or {}
    var = data.get("variante") or {}
    seuil = data.get("seuil_min_echantillon", 300)

    n1, c1 = ctrl.get("n", 0) or 0, ctrl.get("conversions", 0) or 0
    n2, c2 = var.get("n", 0) or 0, var.get("conversions", 0) or 0
    p1, p2 = taux(c1, n1), taux(c2, n2)

    uplift = round((p2 - p1) / p1, 4) if p1 else None

    z = None
    if n1 and n2:
        p = (c1 + c2) / (n1 + n2)
        denom = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2)) if 0 < p < 1 else 0
        z = round((p2 - p1) / denom, 3) if denom else None

    if min(n1, n2) < seuil or z is None:
        verdict = "INCONCLUSIF"
        raison = "échantillon insuffisant" if min(n1, n2) < seuil else "z non calculable"
    elif z >= 1.96:
        verdict, raison = "PASS", "variante significativement meilleure (|z|>=1.96)"
    elif z <= -1.96:
        verdict, raison = "FAIL", "variante significativement pire (|z|>=1.96)"
    else:
        verdict, raison = "INCONCLUSIF", "différence non significative (|z|<1.96)"

    return {
        "taux_controle": round(p1, 4),
        "taux_variante": round(p2, 4),
        "uplift_relatif": uplift,
        "z": z,
        "verdict": verdict,
        "raison": raison,
        "note": ("test z à deux proportions, seuil |z|>=1.96 (~95%). "
                 "Directionnel : pas un substitut à un outil stats complet."),
    }


def main():
    print(json.dumps(analyser(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
