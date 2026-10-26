#!/usr/bin/env python3
"""Hook PreToolUse — la grille de publication ne se remplace pas à l'aveugle.

yt_set_schedule_slots REMPLACE toute la grille :
- ask si la grille n'a pas été LUE dans la session
  (yt_list_schedule_slots au journal, posé en PostToolUse) ;
- ask RENFORCÉ si la liste de créneaux est vide : c'est un EFFACEMENT
  complet, qui exige une confirmation explicite d'effacement ;
- ask sinon, en demandant de montrer la nouvelle grille complète.
Clé de test réservée au harnais CI : session_test.
"""
import json
import os
import re
import sys

ETAT = os.path.join(".claude", "state", "youtube-session.json")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"yt_set_schedule_slots$")


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": f"[garde-grille] {raison}"}}))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    if not RX.match(data.get("tool_name", "")):
        sys.exit(0)
    entree = data.get("tool_input") or {}
    slots = entree.get("slots")
    etat = data.get("session_test")
    if not isinstance(etat, dict):
        try:
            etat = json.load(open(ETAT, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            etat = {}
    if isinstance(slots, list) and not slots:
        ask("yt_set_schedule_slots avec une liste VIDE = EFFACEMENT complet "
            "de la grille de publication. Exiger une confirmation explicite "
            "d'effacement (« oui, efface toute la grille »), pas un simple "
            "accord.")
    if not etat.get("grille_lue"):
        ask("yt_set_schedule_slots REMPLACE toute la grille et elle n'a pas "
            "été lue dans la session : lire yt_list_schedule_slots d'abord, "
            "montrer l'ancienne et la NOUVELLE grille complètes, puis "
            "confirmer.")
    ask("yt_set_schedule_slots REMPLACE toute la grille : montrer la "
        "nouvelle grille complète (tous créneaux, toutes chaînes "
        "concernées) et confirmer.")


if __name__ == "__main__":
    main()
