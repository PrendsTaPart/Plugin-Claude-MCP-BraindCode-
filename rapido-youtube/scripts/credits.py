#!/usr/bin/env python3
"""Coût en crédits d'un plan de travail miniatures, depuis le barème LU.

Formule affichée (et appliquée) :
    coût = Σ (nombre d'opérations × tarif du barème servi)
Le barème vient UNIQUEMENT de la réponse de yt_get_credit_balance (champ
pricing / bareme / costs) — rien n'est codé en dur ; une opération absente
du barème s'affiche « ? » et bloque le verdict.

Usage :
    python3 credits.py balance.json generate=2 edit=1 auto_optimize=1
balance.json : la réponse BRUTE de yt_get_credit_balance. Les opérations
sont les clés du barème servi (ex. generate, edit, inpaint, swap_face,
style, auto_optimize, clone_style, vertical_variant, template). Stdlib.
"""
import json
import sys


def bareme(d):
    for cle in ("pricing", "bareme", "costs", "credit_costs"):
        v = d.get(cle)
        if isinstance(v, dict) and v:
            return v
    return {}


def solde(d):
    for cle in ("balance", "credits", "solde", "remaining"):
        if isinstance(d.get(cle), (int, float)):
            return d[cle]
    return None


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    d = json.load(open(argv[1], encoding="utf-8"))
    tarifs = bareme(d)
    if not tarifs:
        print("Barème absent de la réponse yt_get_credit_balance : aucun "
              "coût n'est estimé (rien n'est codé en dur).")
        return 1
    total, inconnu = 0, []
    for arg in argv[2:]:
        operation, _, n = arg.partition("=")
        n = int(n or 1)
        tarif = tarifs.get(operation)
        if isinstance(tarif, (int, float)):
            print(f"  {operation:18s} {n} × {tarif} = {n * tarif}")
            total += n * tarif
        else:
            inconnu.append(operation)
            print(f"  {operation:18s} {n} × ? (absent du barème servi)")
    s = solde(d)
    print(f"total estimé : {total} crédit(s)"
          + (f" + {len(inconnu)} opération(s) hors barème" if inconnu else ""))
    print(f"solde        : {s if s is not None else '—'}")
    if inconnu:
        print("verdict      : INCOMPLET — demander le tarif manquant au "
              "serveur avant d'engager ces opérations.")
        return 1
    if s is not None and total > s:
        print("verdict      : NE TIENT PAS dans le solde.")
        return 1
    print("verdict      : annoncer ce coût et attendre l'accord avant de "
          "générer (le hook garde-credits questionne au-delà du seuil KB).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
