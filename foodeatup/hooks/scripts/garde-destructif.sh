#!/bin/sh
# Garde-fou déterministe : force la confirmation utilisateur (ask) pour les
# outils MCP destructifs, irréversibles ou sensibles listés dans le matcher de
# hooks.json. Réponse fixe, sans variable ni appel réseau ; l'entrée standard
# n'est pas lue.
echo '{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask", "permissionDecisionReason": "Action destructrice, irréversible ou sensible : confirmation utilisateur requise (garde-fou du plugin foodeatup)."}}'
