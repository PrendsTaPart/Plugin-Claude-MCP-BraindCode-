#!/usr/bin/env python3
"""Hook PreToolUse — crédits Lovable.

- ask sur create_project, remix_project et respond_to_approval (crédits
  consommés, ou décision d'une pause qui doit venir de l'humain) ;
- ask sur send_message si AUCUNE étape n'a été démarrée par
  start_prompt_step dans la session (journal .claude/state/build-session.json,
  alimenté en PostToolUse par journal-build.py) : un message hors plan
  d'exécution consomme des crédits sans carte Build ouverte ;
- allow sur send_message quand une étape est en cours.

Clé de test réservée au harnais CI : session_test (le modèle ne contrôle
que tool_input, jamais la racine du payload).
"""
import json
import os
import re
import sys

ETAT = os.path.join(".claude", "state", "build-session.json")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Ll]ovable__([A-Za-z0-9_-]+)$")
TOUJOURS_ASK = {
    "create_project": "crée un projet Lovable — crédits consommés, création asynchrone",
    "remix_project": "duplique un projet — crédits consommés",
    "respond_to_approval": "répond à une pause Lovable — la décision doit être celle de l'humain, montrée telle quelle",
}


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": f"[garde-credits-lovable] {raison}"}}))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    m = RX.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil = m.group(1)
    if outil in TOUJOURS_ASK:
        ask(f"{outil} : {TOUJOURS_ASK[outil]}. Confirmer.")
    if outil == "send_message":
        etat = data.get("session_test")
        if not isinstance(etat, dict):
            try:
                etat = json.load(open(ETAT, encoding="utf-8"))
            except Exception:  # noqa: BLE001
                etat = {}
        if not etat.get("start_prompt_step"):
            ask("send_message sans étape Build démarrée dans la session "
                "(aucun start_prompt_step au journal) : crédits consommés "
                "hors plan d'exécution. Ouvrir la carte d'abord, ou "
                "confirmer ce message hors plan.")
    sys.exit(0)


if __name__ == "__main__":
    main()
