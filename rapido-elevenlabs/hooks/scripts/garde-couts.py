#!/usr/bin/env python3
"""PreToolUse — garde-couts audio : tout ElevenLabs consomme des crédits.

Une boucle de régénération (TTS, SFX, musique, doublage, voice design) peut
épuiser l'allocation mensuelle en une après-midi. Ce garde force une
confirmation (ask) sur une génération audio TANT QUE le coût n'a pas été pris
en compte dans le tour — marqueur `cout_confirme: true` (ou `check_subscription`
faite et coût présenté). Sinon → ask pédagogique.

Contrat hook : ask = exit 0 + stdout JSON ; allow = exit 0 sans stdout.
Stdlib uniquement, sans réseau. Noms d'outils exacts à confirmer en E0.
"""
import json
import os
import sys

# Sous-chaînes des outils GÉNÉRATIFS (payants) — à figer sur les vrais noms en E0.
GENERATIFS = ("text_to_speech", "tts", "sound_effect", "soundscape", "music",
              "voice_design", "design_voice", "speech_to_speech", "dubbing",
              "isolate", "voice_change")


def suffixe(tool):
    return tool.split("__")[-1] if tool else ""


def est_generatif(tool):
    s = suffixe(tool).lower()
    return any(k in s for k in GENERATIFS)


def plafond_kb():
    """Plafond audio optionnel dans ./rapido-kb/budget-media.md (sinon None)."""
    chemin = os.path.join("rapido-kb", "budget-media.md")
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                if "audio" in ligne.lower() and "plafond" in ligne.lower():
                    return ligne.strip()
    except OSError:
        return None
    return None


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool = data.get("tool_name", "") or ""
    ti = data.get("tool_input") or {}
    if not est_generatif(tool):
        return 0  # allow — outil non génératif (lecture, list_voices…)
    if ti.get("cout_confirme") or ti.get("cost_confirmed"):
        return 0  # allow — coût pris en compte et confirmé
    plafond = plafond_kb()
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                f"💳 Génération audio payante ({tool}) : coût non confirmé dans ce tour "
                "(garde-couts rapido-elevenlabs). Vérifier `check_subscription` (crédits "
                "restants / plan), présenter le coût, éviter les boucles de régénération, "
                "puis relancer avec le marqueur `cout_confirme: true`."
                + (f" Plafond audio KB : {plafond}" if plafond else "")
            ),
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
