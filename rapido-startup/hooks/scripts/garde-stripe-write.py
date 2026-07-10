#!/usr/bin/env python3
"""Garde-fou ARGENT RÉEL (Stripe) : force la confirmation utilisateur (ask)
sur toute écriture Stripe (stripe_api_write — remboursement, création de
facture, coupon, abonnement…). Stripe est en LECTURE SEULE dans les
routines : une écriture n'arrive que sur demande explicite. Double sécurité
avec le flux d'approbation natif du serveur Stripe.
Exit 0 + JSON = ask. Aucun appel réseau."""
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
            f"💸 ÉCRITURE STRIPE ({tool}) : argent réel ou objet de facturation. "
            "Confirmer uniquement après récapitulatif — objet, montant (en "
            "CENTIMES côté API, l'annoncer converti), client concerné. "
            "Rappel : Stripe est en lecture seule dans les routines "
            "(garde-fou du plugin rapido-startup)."
        ),
    }
}))
sys.exit(0)
