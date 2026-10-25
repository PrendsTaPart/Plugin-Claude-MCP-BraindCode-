#!/usr/bin/env python3
"""Garde-fou PreToolUse du plugin foodeatup-tutoriel. Stdlib uniquement.

Deux actes de gouvernance de l'Académie passent par une confirmation humaine :
- admin_publish_toggle : publier/dépublier un contenu visible des apprenants —
  la règle serveur (contenus IA en brouillon, un humain valide) s'applique
  aussi depuis Claude ;
- admin_user_role_set : changer le rôle d'un compte (apprenant/formateur/admin)
  est un acte de gouvernance, jamais un effet de bord.
Tout le reste passe (les créations restent en brouillon côté serveur).
"""
import json
import sys

GOUVERNANCE = {
    "admin_publish_toggle": "publie ou dépublie un contenu visible des apprenants",
    "admin_user_role_set": "change le rôle d'un compte de l'Académie",
}


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    tool_name = str(data.get("tool_name", ""))
    parts = tool_name.split("__")
    if len(parts) < 3 or parts[0] != "mcp":
        sys.exit(0)
    outil = "__".join(parts[2:])
    if outil in GOUVERNANCE:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": (
                    f"« {outil} » {GOUVERNANCE[outil]}. Confirmation humaine "
                    "requise — récapituler le contenu/le compte et l'effet "
                    "avant (plugin foodeatup-tutoriel)."
                ),
            }
        }, ensure_ascii=False))
        sys.exit(0)
    sys.exit(0)


if __name__ == "__main__":
    main()
