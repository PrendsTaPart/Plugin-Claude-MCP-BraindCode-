#!/usr/bin/env python3
"""Garde fail-closed du périmètre Académie (PreToolUse).

Matcher : les outils du serveur « FoodEatUp tutoriel » uniquement
(mcp__*tutoriel*__… — voir hooks.json). Décision :

- outil présent dans la liste embarquée outils-academie.txt → allow (exit 0) ;
- outil ABSENT de la liste (dérive du serveur, outil inconnu) → ask : on ne
  laisse pas passer un outil jamais audité ;
- liste illisible ou vide → ask (fail-closed : l'absence de référentiel ne
  vaut jamais autorisation).

Le serveur est public et en lecture seule : ce garde ne protège pas des
écritures (il n'y en a pas), il protège l'inventaire — tout nouvel outil doit
repasser par l'audit (docs/inventaires/foodeatup-tutoriel-tools-live.txt).
Aucun appel réseau. Testé par scripts/tester-skills.py.
"""
import json
import os
import re
import sys

LISTE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "outils-academie.txt")


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": raison,
    }}))
    sys.exit(0)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001 — stdin illisible : ne jamais bloquer le reste
        sys.exit(0)
    tool = payload.get("tool_name", "")
    m = re.match(r"^mcp__[^_].*__([a-z0-9_]+)$", tool)
    if not m:
        sys.exit(0)  # pas un outil MCP : hors périmètre de ce garde
    outil = m.group(1)
    try:
        with open(LISTE, encoding="utf-8") as f:
            autorises = {l.strip() for l in f
                         if l.strip() and not l.startswith("#")}
    except OSError:
        autorises = set()
    if not autorises:
        ask("garde-perimetre-academie : liste embarquée outils-academie.txt "
            "illisible — fail-closed, confirmation humaine requise.")
    if outil not in autorises:
        ask(f"garde-perimetre-academie : « {outil} » n'est pas dans "
            "l'inventaire vérifié des 36 outils du serveur Académie "
            "(docs/inventaires/foodeatup-tutoriel-tools-live.txt). Serveur "
            "mis à jour ? Re-auditer l'inventaire avant d'utiliser cet outil.")
    sys.exit(0)


if __name__ == "__main__":
    main()
