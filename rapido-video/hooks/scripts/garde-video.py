#!/usr/bin/env python3
"""Garde-fou déterministe (rapido-video) sur les commandes Bash :
- installation lourde (ffmpeg / Whisper / Remotion via bootstrap) → ask avant téléchargement ;
- ajout d'une piste audio → ask pour confirmer que la musique vient du registre autorisé.
exit 0 + JSON = ask ; exit 0 sans sortie = allow. Aucun appel réseau, fail-open."""
import json
import re
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

if data.get("tool_name") != "Bash":
    sys.exit(0)
cmd = ((data.get("tool_input") or {}).get("command") or "").lower()
if not cmd:
    sys.exit(0)

INSTALL = re.compile(
    r"bootstrap_video|apt(-get)?\s+install|pip\s+install|brew\s+install|"
    r"npm\s+(i|install)\b.*(remotion|whisper)|\bwhisper\b.*(install|download)|"
    r"curl\b.*(ffmpeg|whisper|remotion)|\bwget\b")
AUDIO = re.compile(
    r"-i\s+\S+\.(mp3|wav|m4a|aac|ogg|flac)|-filter_complex[^|]*amix|-map\s+\d+:a")

reason = None
if INSTALL.search(cmd):
    reason = ("Installation lourde (ffmpeg / Whisper / Remotion via bootstrap) — "
              "confirmer avant le téléchargement.")
elif AUDIO.search(cmd):
    reason = ("Ajout d'une piste audio — confirmer que la musique provient du "
              "registre autorisé (règle musiques-autorisees), pas d'une source non libre.")

if reason:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": reason}}))
sys.exit(0)
