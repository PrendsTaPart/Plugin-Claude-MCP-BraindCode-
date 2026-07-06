#!/usr/bin/env python3
"""Garde-fou production n8n :
- ask forcé sur publish_workflow (le workflow tournera seul),
  unpublish_workflow / archive_workflow (arrêt d'une automatisation en
  service), et execute_workflow en mode production — Y COMPRIS quand
  executionMode est ABSENT (le défaut du serveur est "production").
- execute_workflow en mode "manual" explicite : libre (c'est le test).
Exit 0 + JSON = ask ; exit 0 sans sortie = allow. Aucun appel réseau."""
import json
import sys


def ask(raison):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": raison,
        }
    }))
    sys.exit(0)


try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

tool = data.get("tool_name", "")
tool_input = data.get("tool_input") or {}

if tool.endswith("publish_workflow"):
    ask("🚀 PUBLICATION = mise en production : ce workflow tournera SEUL "
        "(potentiellement la nuit). Confirmer uniquement après récapitulatif : "
        "déclencheur, fréquence, actions, qui est notifié, ce qui part vers "
        "l'extérieur.")

if tool.endswith("unpublish_workflow"):
    ask("⚠️ Dépublication : une automatisation EN SERVICE va s'arrêter. "
        "Confirmer avec le nom du workflow et l'impact (ce qui ne sera plus "
        "fait automatiquement).")

if tool.endswith("archive_workflow"):
    ask("⚠️ Archivage d'un workflow : confirmer avec le nom et vérifier "
        "qu'il n'est pas publié/en service (et mettre à jour le registre "
        "rapido-kb).")

if tool.endswith("execute_workflow"):
    mode = str(tool_input.get("executionMode") or "").strip().lower()
    if mode != "manual":
        # Absent = "production" par défaut côté serveur.
        ask("⚠️ Exécution en mode PRODUCTION (défaut si executionMode est "
            "omis) : la version PUBLIÉE va s'exécuter avec ses vraies "
            "credentials et ses vrais effets. Pour un test, utiliser "
            "executionMode=\"manual\". Confirmer l'exécution production ?")
    sys.exit(0)  # manual explicite : test, libre

sys.exit(0)
