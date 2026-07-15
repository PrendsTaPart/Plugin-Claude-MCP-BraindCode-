#!/usr/bin/env python3
"""PreToolUse — garde-voix : confirmation FORCÉE avant clonage / voice design.

Cloner une voix réelle ou concevoir une voix (voice design) engage les ToS
ElevenLabs : **consentement écrit obligatoire** pour une voix humaine réelle
(la plateforme peut bannir sinon). Ce garde force une confirmation (ask) avec
rappel explicite du consentement et du chemin d'archivage du document.

Contrat hook : ask = exit 0 + stdout JSON ; allow = exit 0 sans stdout.
Stdlib uniquement, sans réseau. Noms d'outils exacts à confirmer en E0.
"""
import json
import sys

DECLENCHEURS = ("clone", "voice_design", "design_voice", "create_voice")


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
        return 0  # allow — ni clonage ni voice design
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                f"🎙️ Création/clonage de voix ({tool}) : confirmation requise (garde-voix "
                "rapido-elevenlabs). Pour une VOIX HUMAINE RÉELLE, le **consentement écrit** "
                "est OBLIGATOIRE (ToS ElevenLabs — risque de bannissement) : archiver le "
                "document et consigner son chemin dans la fiche voix (identite-vocale.md). "
                "Ne cloner que des voix propres ou dûment autorisées. Avatar Mika (HeyGen) : "
                "ne pas cloner sans vérifier la licence HeyGen."
            ),
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
