#!/usr/bin/env python3
"""Hook PreToolUse — les alias dépréciés du serveur YouTube sont refusés.

Le serveur expose chaque outil deux fois : yt_<nom> (officiel) et <nom>
(alias déprécié, retiré le 2026-12-31). Deny sur tout appel d'un alias,
avec LE NOM À UTILISER. Source : docs/inventaires/
rapido-youtube-alias-deprecies.txt — fail-closed : liste illisible = tout
nom sans préfixe yt_ est refusé.
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
ALIAS = os.path.join(RACINE, "docs", "inventaires",
                     "rapido-youtube-alias-deprecies.txt")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"([A-Za-z0-9_]+)$")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    m = RX.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil = m.group(1)
    if outil.startswith("yt_"):
        sys.exit(0)
    try:
        connus = {l.split("\t")[0].strip() for l in open(ALIAS, encoding="utf-8")
                  if l.strip() and not l.startswith("#")}
        precision = ("alias déprécié, retiré le 2026-12-31"
                     if outil in connus else
                     "nom sans préfixe yt_ (fail-closed : seul yt_ est admis)")
    except Exception:  # noqa: BLE001
        precision = "nom sans préfixe yt_ (liste des alias illisible — fail-closed)"
    print(f"[alias-deprecies] REFUS : « {outil} » est un {precision}. "
          f"Utiliser le nom officiel « yt_{outil} » — le plugin n'appelle "
          "jamais un alias.", file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
