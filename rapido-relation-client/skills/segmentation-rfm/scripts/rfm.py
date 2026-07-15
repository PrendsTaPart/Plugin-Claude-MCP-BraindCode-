#!/usr/bin/env python3
"""rfm.py — segmentation RFM (Récence × Fréquence × Montant), stdlib.

Score chaque client sur R, F, M par quintiles (1-5) à partir des factures/commandes
réelles, puis mappe vers un segment. Formule affichée ; aucune donnée inventée.

Entrée (stdin/--fichier) :
  {"clients": [{"nom": "X", "recence_jours": 12, "frequence": 8, "montant": 4200}]}
Sortie : clients avec scores R/F/M (1-5) + segment.
"""
import argparse
import json
import sys

SEGMENTS = [
    # (condition sur (R,F,M) moyenne pondérée FM, libellé)
    ("champions", lambda r, f, m: r >= 4 and (f + m) / 2 >= 4),
    ("fideles", lambda r, f, m: r >= 3 and (f + m) / 2 >= 3),
    ("a_risque", lambda r, f, m: r <= 2 and (f + m) / 2 >= 3),
    ("endormis", lambda r, f, m: r <= 2 and 2 <= (f + m) / 2 < 3),
    ("perdus", lambda r, f, m: r <= 1 and (f + m) / 2 <= 2),
]


def quintiles(valeurs, inverse=False):
    """Retourne une fonction valeur→score 1-5 par rang (5 = meilleur).
    inverse=True pour la récence (moins de jours = meilleur)."""
    tri = sorted(set(valeurs))
    if not tri:
        return lambda v: 3
    n = len(tri)

    def score(v):
        rang = sum(1 for t in tri if t <= v)  # 1..n
        q = int((rang - 1) / n * 5) + 1  # 1..5
        q = min(5, max(1, q))
        return 6 - q if inverse else q
    return score


def segment(r, f, m):
    for nom, cond in SEGMENTS:
        if cond(r, f, m):
            return nom
    return "a_developper"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichier")
    args = ap.parse_args(argv)
    try:
        data = json.load(open(args.fichier) if args.fichier else sys.stdin)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Erreur lecture : {e}", file=sys.stderr)
        return 1
    clients = data.get("clients", [])
    if not clients:
        print(json.dumps({"clients": [], "note": "aucun client fourni"}, ensure_ascii=False))
        return 0
    sr = quintiles([c.get("recence_jours", 0) for c in clients], inverse=True)
    sf = quintiles([c.get("frequence", 0) for c in clients])
    sm = quintiles([c.get("montant", 0) for c in clients])
    out = []
    for c in clients:
        r, f, m = sr(c.get("recence_jours", 0)), sf(c.get("frequence", 0)), sm(c.get("montant", 0))
        out.append({"nom": c.get("nom"), "R": r, "F": f, "M": m, "segment": segment(r, f, m)})
    print(json.dumps({
        "formule": "R/F/M en quintiles 1-5 (R inversé : moins de jours = meilleur) ; segment par règles RFM",
        "clients": out,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
