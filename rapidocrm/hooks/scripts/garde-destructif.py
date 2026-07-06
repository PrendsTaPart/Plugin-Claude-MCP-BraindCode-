#!/usr/bin/env python3
"""Garde-fou déterministe rapidocrm :
- deny (exit 2 + stderr) : transition de statut de facture interdite (DGFiP) ;
- ask (exit 0 + JSON) : tout autre outil destructif/irréversible matché.
Aucun appel réseau."""
import json
import sys

# Table DGFiP : seuls statuts CIBLES autorisés pour un changement de statut de
# facture. Transitions valides : brouillon -> en_attente -> payee ;
# en_attente -> en_retard -> payee. "brouillon" n'est jamais une cible (pas de
# rétrogradation) et une facture émise ne se supprime pas (avoir).
STATUTS_FACTURE_CIBLES_AUTORISES = {"en_attente", "payee", "en_retard"}

try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

tool = data.get("tool_name", "outil inconnu")
tool_input = data.get("tool_input") or {}

if tool.endswith("update_invoice_status"):
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

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": (
            f"Action destructrice ou irréversible ({tool}) : "
            "confirmation utilisateur requise (garde-fou du plugin rapidocrm)."
        ),
    }
}))
sys.exit(0)
