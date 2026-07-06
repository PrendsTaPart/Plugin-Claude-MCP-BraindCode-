#!/usr/bin/env python3
"""Garde-fou déterministe : force la confirmation utilisateur (ask) pour les
outils MCP destructifs/irréversibles du plugin (suppressions, annulation de
publication programmée, retrait de post d'une campagne). Exit 0 + JSON = ask.
Aucun appel réseau."""
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
            f"Action destructrice ou irréversible ({tool}) : "
            "confirmation utilisateur requise (garde-fou du plugin rapidocms)."
        ),
    }
}))
sys.exit(0)
