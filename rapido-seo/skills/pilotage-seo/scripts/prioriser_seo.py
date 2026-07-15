#!/usr/bin/env python3
"""prioriser_seo.py — priorisation ICE des actions SEO (stdlib).

Score ICE = impact × confidence × ease (chaque facteur 1-10). Trie les actions
candidates du PLAN de pilotage-seo. Formule affichée, jamais de tête.

Entrée (stdin ou --fichier) :
  {"actions": [{"titre": "corriger les title dupliqués", "impact": 8,
                "confidence": 9, "ease": 7, "machine": "onpage"}]}
Sortie (stdout, JSON) : actions triées par ICE décroissant + formule.
"""
import argparse
import json
import sys


def ice(a):
    return round(float(a.get("impact", 0)) * float(a.get("confidence", 0))
                 * float(a.get("ease", 0)), 2)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichier")
    args = ap.parse_args(argv)
    try:
        data = json.load(open(args.fichier) if args.fichier else sys.stdin)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Erreur lecture : {e}", file=sys.stderr)
        return 1
    actions = data.get("actions", [])
    for a in actions:
        a["ICE"] = ice(a)
    actions.sort(key=lambda a: a["ICE"], reverse=True)
    print(json.dumps({
        "formule": "ICE = impact × confidence × ease (facteurs 1-10)",
        "actions_triees": actions,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
