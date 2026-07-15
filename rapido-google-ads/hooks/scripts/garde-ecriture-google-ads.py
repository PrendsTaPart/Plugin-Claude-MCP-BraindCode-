#!/usr/bin/env python3
"""PreToolUse — filet écriture Google Ads.

Le MCP officiel Google Ads est LECTURE SEULE by design : ce plugin analyse et
recommande, il n'exécute pas. Ce garde est un **filet** au cas où le serveur
évoluerait vers l'écriture : tout outil dont le nom contient `mutate` ou `create`
force une confirmation (ask) — on ne modifie jamais un compte publicitaire réel
sans accord explicite.

Contrat hook : ask = exit 0 + stdout JSON ; allow = exit 0 sans stdout.
Stdlib uniquement, sans réseau.
"""
import json
import sys

ECRITURE = ("mutate", "create", "update", "remove", "delete")


def suffixe(tool):
    return tool.split("__")[-1] if tool else ""


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool = data.get("tool_name", "") or ""
    if "google-ads" not in tool.lower() and "googleads" not in tool.lower():
        return 0  # allow — pas Google Ads
    s = suffixe(tool).lower()
    if not any(k in s for k in ECRITURE):
        return 0  # allow — lecture
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                f"⚠️ Écriture Google Ads détectée ({tool}) : ce plugin est conçu "
                "LECTURE SEULE (analyse + recommandations, exécution manuelle dans "
                "l'interface Google Ads). Si le serveur expose désormais l'écriture, "
                "confirmer explicitement (argent réel) — budget max annoncé, plafonds "
                "`./rapido-kb/` respectés — avant toute mutation de compte."
            ),
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
