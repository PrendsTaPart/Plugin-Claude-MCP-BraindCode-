#!/usr/bin/env python3
"""Garde-fou déterministe : force la confirmation (ask) pour tout outil qui
ENVOIE ou REND VISIBLE à l'extérieur (email, SMS, newsletter, lancement de
campagne, planification). Réutilise le pattern garde-envois : le matcher
hooks.json gate les outils concernés, ce script pose l'ask. Exit 0 + JSON = ask.
Stdlib uniquement, aucun appel réseau."""
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
            f"Envoi ou action visible par le client ({tool}) : confirmation "
            "humaine explicite requise (relation client — récapituler "
            "destinataire/contenu/date avant d'envoyer ; brouillon par défaut)."
        ),
    }
}))
sys.exit(0)
