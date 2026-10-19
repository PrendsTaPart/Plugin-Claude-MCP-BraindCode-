#!/bin/sh
# Garde-fou déterministe : force la confirmation utilisateur (ask) pour les
# outils MCP destructifs/irréversibles du plugin. Exit 0 + JSON = ask.
# Shell POSIX uniquement (sed, tr) : aucun appel réseau, aucun fichier lu
# hormis l'entrée standard fournie par Claude Code.

entree=$(cat | tr '\n' ' ')
outil=$(printf '%s' "$entree" \
  | sed -n -E 's/.*"tool_name"[[:space:]]*:[[:space:]]*"([^"]*)".*/\1/p' \
  | tr -cd 'A-Za-z0-9_.-')
[ -n "$outil" ] || outil="outil inconnu"

printf '{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask", "permissionDecisionReason": "Action destructrice, irréversible ou sensible (%s) : confirmation utilisateur requise (garde-fou du plugin foodeatup)."}}\n' "$outil"
exit 0
