#!/usr/bin/env python3
"""garde-budget-ads — garde-fou déterministe du plugin rapido-leadmagnet.

Toute création/activation Meta déclenchée dans le contexte lead magnet passe par
une CONFIRMATION (ask) rappelant : campagne en PAUSED, coût max récapitulé,
activation sur confirmation écrite séparée. Défense en profondeur qui s'ajoute
aux hooks de rapido-meta-ads (plafond-budget, garde-argent-reel) — indépendante
du modèle.

Ne bloque jamais en dur (aucun deny) : la publicité n'est pas interdite, elle est
confirmée. Contrat : ask = exit 0 + JSON stdout ; allow = exit 0 sans stdout.
Aucune I/O réseau, aucun secret.
"""
import json
import re
import sys

# Outils Meta qui engagent une dépense ou activent une entité.
RX_META_ARGENT = re.compile(
    r"facebook-ads__(ads_create_campaign|ads_create_ad_set|ads_create_ad|"
    r"ads_activate_entity|ads_boost_ig_post|ads_update_entity)$",
    re.IGNORECASE,
)


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
    if RX_META_ARGENT.search(outil):
        demander(
            "Meta = argent réel (contexte lead magnet). La campagne doit être créée "
            "en PAUSED, le coût max récapitulé, et l'activation confirmée par écrit "
            "dans un tour séparé. Confirmez avant de continuer."
        )
    sys.exit(0)  # allow


if __name__ == "__main__":
    main()
