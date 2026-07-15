#!/usr/bin/env python3
"""PreToolUse — garde-coûts DataForSEO (facturation À L'APPEL).

DataForSEO facture chaque requête. Une requête volumineuse (backlinks bulk, SERP
en volume, Labs) peut coûter cher. Ce garde force une confirmation (ask) sur les
familles coûteuses TANT QUE le coût n'a pas été pris en compte dans le tour —
marqueur `cout_confirme: true` (le coût estimé a été annoncé et validé). Le volume
récurrent (rank tracking) doit vivre en n8n, pas en appels conversationnels.

Contrat hook : ask = exit 0 + stdout JSON ; allow = exit 0 sans stdout.
Stdlib uniquement, sans réseau. Noms d'outils exacts à confirmer à la connexion.
"""
import json
import sys

# Familles DataForSEO facturées (sous-chaînes) — à figer sur les vrais noms.
COUTEUX = ("backlinks", "serp", "labs", "keywords_data", "on_page", "onpage",
           "content_analysis", "bulk", "domain_analytics")


def suffixe(tool):
    return tool.split("__")[-1] if tool else ""


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool = data.get("tool_name", "") or ""
    ti = data.get("tool_input") or {}
    if "dataforseo" not in tool.lower():
        return 0  # allow — pas DataForSEO
    s = suffixe(tool).lower()
    if not any(k in s for k in COUTEUX):
        return 0  # allow — famille non facturée en volume
    if ti.get("cout_confirme") or ti.get("cost_confirmed"):
        return 0  # allow — coût estimé annoncé et validé
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                f"💳 Requête DataForSEO facturée ({tool}) : coût non confirmé dans ce "
                "tour (garde-couts-seo rapido-seo). DataForSEO facture À L'APPEL — "
                "annoncer le coût estimé (unités × tarif), vérifier le plafond "
                "`./rapido-kb/` (budget DataForSEO mensuel), puis relancer avec le "
                "marqueur `cout_confirme: true`. Le volume récurrent (rank tracking) "
                "doit vivre en n8n, pas en conversationnel."
            ),
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
