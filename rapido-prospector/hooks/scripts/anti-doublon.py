#!/usr/bin/env python3
"""Hook PreToolUse — add_clients sans dédoublonnage = ask.

add_clients enregistre pour de bon. Si la session ne montre NI un passage
de scripts/dedoublonner.py NI une lecture list_clients datées du jour
(marqueurs .claude/state/prospect-session.json, posés par le script de
dédoublonnage et par le journal PostToolUse), l'enregistrement passe par
une question : la base propre est la première règle du plugin.
Clé de test réservée au harnais CI : session_test.
"""
import datetime
import json
import os
import re
import sys

RX_OUTIL = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Pp]rospect__add_clients$")
ETAT = os.path.join(".claude", "state", "prospect-session.json")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    if not RX_OUTIL.match(data.get("tool_name", "")):
        sys.exit(0)
    etat = data.get("session_test")
    if not isinstance(etat, dict):
        try:
            etat = json.load(open(ETAT, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            etat = {}
    aujourdhui = str(data.get("aujourdhui_test")
                     or datetime.date.today().isoformat())
    preuve = any(str(etat.get(cle, "")).startswith(aujourdhui)
                 for cle in ("dedoublonnage", "list_clients"))
    if preuve:
        sys.exit(0)
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason":
            "[anti-doublon] add_clients sans trace de dédoublonnage ni de "
            "list_clients aujourd'hui. Passer d'abord "
            "scripts/dedoublonner.py (rapport nouveaux/doublons/sans contact), "
            "ou confirmer explicitement cet enregistrement direct."}}))
    sys.exit(0)


if __name__ == "__main__":
    main()
