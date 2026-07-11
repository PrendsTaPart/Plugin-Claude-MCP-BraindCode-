#!/usr/bin/env python3
"""Garde-fou déterministe : un exercice forge qui débouche sur Meta Ads
engage de l'ARGENT RÉEL — confirmation forcée (ask) avec rappel de la
règle : création en PAUSED, activation après accord explicite uniquement
(les hooks du plugin rapido-meta-ads restent en filet). Exit 0 + JSON = ask."""
import json
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

tool = data.get("tool_name", "outil inconnu")

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": (
            f"Argent réel ({tool}) : un exercice forge ne dépense jamais seul. "
            "Règle : toute campagne/publicité se crée en PAUSED, l'activation "
            "n'arrive qu'après accord explicite de l'utilisateur "
            "(garde-fous du plugin rapido-meta-ads en filet)."
        ),
    }
}))
sys.exit(0)
