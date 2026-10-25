#!/usr/bin/env python3
"""Hook PreToolUse — deploy_project = mise en ligne PUBLIQUE.

Deny tant que le journal de session (.claude/state/build-session.json,
alimenté en PostToolUse à chaque lecture de get_pending_validations) ne
contient pas, pour ce projet, une validation de kind mise_en_ligne lue
comme VALIDÉE. Le message d'erreur invite à ouvrir la demande
(request_human_validation) puis à relire get_pending_validations.
Fail-closed : journal absent ou illisible = deny.
Clé de test réservée au harnais CI : session_test.
"""
import json
import os
import re
import sys

ETAT = os.path.join(".claude", "state", "build-session.json")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Ll]ovable__deploy_project$")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    if not RX.match(data.get("tool_name", "")):
        sys.exit(0)
    etat = data.get("session_test")
    if not isinstance(etat, dict):
        try:
            etat = json.load(open(ETAT, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            etat = {}
    projet = str((data.get("tool_input") or {}).get("project_id", "")) or "?"
    validees = etat.get("validations_mise_en_ligne") or {}
    if isinstance(validees, dict) and validees.get(projet):
        sys.exit(0)  # validation humaine lue comme accordée pour CE projet
    print("[garde-mise-en-ligne] REFUS : deploy_project met l'application "
          f"EN LIGNE publiquement et aucune validation de kind mise_en_ligne "
          f"n'est lue comme validée pour le projet {projet}. Ouvrir la "
          "demande avec request_human_validation (kind mise_en_ligne), puis "
          "relire get_pending_validations — le journal de session enregistre "
          "la validation et ce hook laissera passer.", file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
