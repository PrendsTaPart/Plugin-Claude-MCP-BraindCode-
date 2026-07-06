#!/usr/bin/env python3
"""Garde-fou déterministe rapido-suite (union des 4 serveurs) :
- deny (exit 2 + stderr) : transition de statut de facture CRM interdite (DGFiP) ;
- ask (exit 0 + JSON) : tout autre outil destructif/irréversible matché.
Aucun appel réseau."""
import json
import sys

# Table DGFiP (factures CRM) : seuls statuts CIBLES autorisés.
# Transitions valides : brouillon -> en_attente -> payee ;
# en_attente -> en_retard -> payee. "brouillon" n'est jamais une cible.
STATUTS_FACTURE_CIBLES_AUTORISES = {"en_attente", "payee", "en_retard"}

try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

tool = data.get("tool_name", "outil inconnu")
tool_input = data.get("tool_input") or {}

# La règle DGFiP ne s'applique qu'aux factures du CRM : les statuts du serveur
# FoodEatUp ne sont pas vérifiés ici (schéma différent).
if tool.startswith("mcp__rapidocrm__") and tool.endswith("update_invoice_status"):
    cible = str(
        tool_input.get("statut") or tool_input.get("status") or ""
    ).strip().lower()
    if cible and cible not in STATUTS_FACTURE_CIBLES_AUTORISES:
        sys.stderr.write(
            f"Transition de facture INTERDITE (règles DGFiP) : statut cible "
            f"'{cible}'. Cibles autorisées : en_attente, payee, en_retard "
            "(brouillon -> en_attente -> payee ; en_attente -> en_retard -> "
            "payee). Une facture 'payee' ne se rétrograde pas et une facture "
            "émise ne se supprime pas : proposer un avoir."
        )
        sys.exit(2)

serveur = tool.split("__")[1] if tool.count("__") >= 2 else "?"

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": (
            f"Action destructrice ou irréversible ({tool}, serveur {serveur}) : "
            "confirmation utilisateur requise (garde-fou du plugin rapido-suite)."
        ),
    }
}))
sys.exit(0)
