#!/usr/bin/env python3
"""garde-voix-marque — garde-fou déterministe du plugin rapido-copywriter.

Toute création de brouillon social (`create_draft_tool` RapidoCMS) passe par une
CONFIRMATION rappelant les deux passes obligatoires : gate **voix de marque**
(`rapidocms:brand-review`) et passe **anti-voix-ia** (`reference/anti-voix-ia.md`).
Le plugin ne publie jamais directement — uniquement des brouillons.

Ne bloque jamais en dur (aucun deny). Contrat : ask = exit 0 + JSON stdout ;
allow = exit 0 sans stdout. Aucune I/O réseau, aucun secret.
"""
import json
import re
import sys

RX_DRAFT = re.compile(r"(rapidocms__)?create_draft_tool$", re.IGNORECASE)


def demander(raison):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": raison,
        }
    }))
    sys.exit(0)


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (ValueError, TypeError):
        sys.exit(0)
    outil = data.get("tool_name") or ""
    if RX_DRAFT.search(outil):
        demander(
            "Brouillon social : la passe anti-voix-ia (reference/anti-voix-ia.md) et "
            "le gate voix de marque (rapidocms:brand-review) ont-ils été passés ? "
            "Le plugin ne publie jamais — brouillon uniquement, confirmé."
        )
    sys.exit(0)


if __name__ == "__main__":
    main()
