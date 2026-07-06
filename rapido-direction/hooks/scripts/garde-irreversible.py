#!/usr/bin/env python3
"""Garde-fou rapido-direction : confirmation forcée (ask) sur les opérations
irréversibles ou visibles par des tiers — corbeille/spam Gmail (si un outil
l'expose), suppression Drive (idem), suppression d'événement Calendar (les
participants reçoivent l'annulation). Exit 0 + JSON = ask. Aucun appel réseau."""
import json
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

tool = data.get("tool_name", "outil inconnu")

if "calendar" in tool and tool.endswith("delete_event"):
    raison = ("⚠️ Suppression d'un événement : les participants recevront "
              "l'annulation. Confirmer avec le titre, la date et la liste des "
              "invités concernés.")
else:
    raison = (f"⚠️ Opération irréversible ({tool}) : corbeille/spam/"
              "suppression exigent une confirmation explicite (règle du "
              "plugin rapido-direction : on classe, on ne supprime pas).")

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": raison,
    }
}))
sys.exit(0)
