#!/usr/bin/env python3
"""PreToolUse — garde-appels : confirmation FORCÉE avant un appel sortant.

`make_outbound_call` (ElevenLabs) passe un VRAI appel téléphonique. Ce garde
force une confirmation (ask) : l'appelant doit avoir en tête le numéro
provisionné, le destinataire, le script, et la plage horaire autorisée
(10h-20h par défaut, réglable en KB). Prospection à froid vocale = INTERDITE
(règle du skill agent-vocal-jarvis), ce garde ne l'autorise jamais silencieusement.

Contrat hook : ask = exit 0 + stdout JSON ; allow = exit 0 sans stdout.
Stdlib uniquement, sans réseau. Noms d'outils exacts à confirmer en E0.
"""
import json
import sys

DECLENCHEURS = ("outbound_call", "make_call", "place_call")


def suffixe(tool):
    return tool.split("__")[-1] if tool else ""


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool = data.get("tool_name", "") or ""
    s = suffixe(tool).lower()
    if not any(k in s for k in DECLENCHEURS):
        return 0  # allow — pas un appel sortant
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                f"📞 Appel vocal sortant ({tool}) : confirmation requise (garde-appels "
                "rapido-elevenlabs). Vérifier AVANT de lancer : (1) numéro provisionné "
                "(list_phone_numbers) ; (2) destinataire et son consentement ; (3) script "
                "d'appel validé ; (4) plage horaire autorisée (10h-20h par défaut, cf. KB). "
                "Cas autorisés : rappel/confirmation de réservation. Prospection à froid "
                "vocale = INTERDITE."
            ),
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
