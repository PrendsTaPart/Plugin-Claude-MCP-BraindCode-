#!/usr/bin/env python3
"""Garde-fou déterministe : force la confirmation utilisateur (ask) pour tout
outil MCP qui ENVOIE ou REND VISIBLE à l'extérieur (email, SMS, newsletter,
lancement de campagne, planification d'envoi/publication, activation de pub).

Ces actions sont irréversibles côté destinataire et visibles par des tiers :
elles n'ont jamais lieu sans accord humain explicite (garde-fous-marketing §a).
Exit 0 + JSON = ask. Aucun appel réseau, stdlib uniquement."""
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
            f"Envoi ou action visible par des tiers ({tool}) : confirmation "
            "humaine explicite requise (garde-fou marketing — récapituler "
            "destinataires/contenu/date/coût avant d'envoyer)."
        ),
    }
}))
sys.exit(0)
