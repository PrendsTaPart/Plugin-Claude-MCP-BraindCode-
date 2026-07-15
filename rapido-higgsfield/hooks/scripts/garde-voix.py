#!/usr/bin/env python3
"""PreToolUse — garde-voix Higgsfield (droits & consentement).

Toute création/clonage/modification/doublage de voix exige une confirmation
explicite que l'utilisateur DÉTIENT les droits ou le consentement sur la voix
concernée. Le hook force la question (permissionDecision "ask").

Contrat hook : ask = exit 0 + JSON hookSpecificOutput.permissionDecision="ask" ;
allow = exit 0 sans sortie. Stdlib uniquement, < 1 s, sans réseau.
"""
import json
import sys

CIBLES = ("create_voice", "voice_change", "dubbing")


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool = data.get("tool_name", "") or ""
    if any(c in tool for c in CIBLES):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                "Voix IA (clonage / doublage / modification) : confirmez que vous "
                "détenez les DROITS ou le CONSENTEMENT sur cette voix — la vôtre, "
                "un collaborateur consentant, ou une licence explicite (Mika/HeyGen "
                "à clarifier). Sans droits, ne pas générer."
            )}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
