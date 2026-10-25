#!/usr/bin/env python3
"""Garde de l'autonomie (PreToolUse) — « auto » ne se donne pas tout seul.

- create_task, propose_routine, propose_routine_improvement demandant
  `autonomy_level: "auto"` (où que le champ soit dans les arguments) → ask :
  l'autonomie complète est une décision de l'utilisateur, pas un défaut.
- subscribe_event avec gouvernance/mode « auto » :
  - DENY si les arguments portent un outil DESTRUCTIF connu
    (reference/outils-sensibles.json — règle du serveur : auto refusé si la
    routine contient un outil destructif) ;
  - ask sinon (fail-closed : on ne sait pas toujours, depuis l'appel, ce que
    la routine cible contient — le serveur revérifie, l'humain confirme).

Les champs posés par le modèle ne valent jamais confirmation. Aucun appel
réseau. Testé par scripts/tester-skills.py.
"""
import json
import os
import re
import sys

RACINE_PLUGIN = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
TABLE = os.path.join(RACINE_PLUGIN, "reference", "outils-sensibles.json")
RX_MCP = re.compile(r"^mcp__[Pp]lan[_-]?[Ii]t__([A-Za-z0-9_]+)$")
CIBLES_AUTONOMIE = {"create_task", "propose_routine",
                    "propose_routine_improvement"}


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": raison,
    }}, ensure_ascii=False))
    sys.exit(0)


def deny(raison):
    print(f"garde-autonomie : {raison}", file=sys.stderr)
    sys.exit(2)


def cherche_auto(obj):
    """True si un champ d'autonomie/gouvernance vaut « auto »."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if re.search(r"autonomy|autonomie|governance|gouvernance|mode",
                         k, re.I) and str(v).lower() == "auto":
                return True
            if cherche_auto(v):
                return True
    elif isinstance(obj, list):
        return any(cherche_auto(v) for v in obj)
    return False


def textes(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from textes(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from textes(v)
    elif isinstance(obj, str):
        yield obj


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    m = RX_MCP.match(payload.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil = m.group(1)
    entree = payload.get("tool_input", {})
    if outil in CIBLES_AUTONOMIE and cherche_auto(entree):
        ask(f"« {outil} » demande le niveau d'autonomie AUTO : la routine "
            "agira sans validation à chaque tour — décision de l'utilisateur, "
            "jamais un défaut.")
    if outil == "subscribe_event" and cherche_auto(entree):
        try:
            with open(TABLE, encoding="utf-8") as f:
                destructifs = set(json.load(f).get("destructifs", []))
        except Exception:  # noqa: BLE001
            destructifs = set()
        for texte in textes(entree):
            for d in destructifs:
                if d and d in texte:
                    deny("subscribe_event en AUTO sur une routine qui porte "
                         f"l'outil destructif « {d} » — refusé par la règle "
                         "du serveur ; passer en gouvernance validation.")
        ask("subscribe_event en AUTO : la routine se lancera seule à chaque "
            "événement — accord explicite requis (gouvernance validation "
            "par défaut sinon).")
    sys.exit(0)


if __name__ == "__main__":
    main()
