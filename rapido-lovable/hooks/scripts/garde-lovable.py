#!/usr/bin/env python3
"""Garde-fou déterministe (rapido-lovable) : force la confirmation (ask) pour les actions
sensibles (sorties partagées, déploiement, écrasement, périmètre large).
exit 0 + JSON = ask. Aucun appel réseau. Fail-open si stdin illisible."""
import json, sys
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)
tool = data.get("tool_name", "outil inconnu")
print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "PreToolUse", "permissionDecision": "ask",
    "permissionDecisionReason": (
        f"Action sensible (rapido-lovable) : {tool} — récapituler le périmètre "
        "(projet/skill/knowledge/export concerné) puis confirmer.")}}))
sys.exit(0)
