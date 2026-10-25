#!/usr/bin/env python3
"""Normalise des numéros français en E.164 et détecte les mobiles.

Règles affichées (et appliquées) :
- on retire espaces, points, tirets, parenthèses ;
- `0XXXXXXXXX` (10 chiffres) → `+33XXXXXXXXX` ;
- `33XXXXXXXXX` ou `+33XXXXXXXXX` → `+33XXXXXXXXX` ;
- tout autre indicatif `+…` est gardé tel quel (non français) ;
- mobile français = `+336…` ou `+337…` (seuls numéros acceptés en SMS) ;
- un numéro qui ne rentre dans aucun cas est INVALIDE : il ne part jamais.

Usage :
    python3 normaliser_telephone.py 0612345678 "01 44 55 66 77"
    python3 normaliser_telephone.py --json liste.json   # ["num", …]
Sortie : une ligne par numéro — entrée, E.164 (ou INVALIDE), mobile oui/non.
Stdlib uniquement ; aucun numéro n'est deviné ni complété.
"""
import json
import re
import sys

RX_NETTOYAGE = re.compile(r"[ .\-() ]")


def normaliser(num):
    """E.164 ou None si le numéro n'est pas exploitable."""
    if not isinstance(num, str):
        return None
    n = RX_NETTOYAGE.sub("", num.strip())
    if re.fullmatch(r"0[1-9]\d{8}", n):
        return "+33" + n[1:]
    if re.fullmatch(r"33[1-9]\d{8}", n):
        return "+" + n
    if re.fullmatch(r"\+33[1-9]\d{8}", n):
        return n
    if re.fullmatch(r"\+[1-9]\d{6,14}", n):
        return n  # E.164 non français : gardé, mais jamais « mobile FR »
    return None


def est_mobile_fr(e164):
    return bool(e164) and e164.startswith(("+336", "+337"))


def main(argv):
    if len(argv) >= 3 and argv[1] == "--json":
        nums = json.load(open(argv[2], encoding="utf-8"))
    else:
        nums = argv[1:] or [l.strip() for l in sys.stdin if l.strip()]
    if not nums:
        print(__doc__)
        return 2
    invalides = 0
    for num in nums:
        e164 = normaliser(num)
        if e164 is None:
            invalides += 1
            print(f"{num}\tINVALIDE\t—")
        else:
            print(f"{num}\t{e164}\t{'mobile FR' if est_mobile_fr(e164) else 'non mobile'}")
    print(f"# {len(nums)} numéro(s), {invalides} invalide(s) — "
          "les invalides ne partent jamais, ils se corrigent (update_client).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
