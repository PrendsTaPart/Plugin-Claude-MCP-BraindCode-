#!/usr/bin/env python3
"""Hook PreToolUse — tout ce qui devient visible du public demande l'accord.

Ask sur :
- une privacy « public » (yt_publish_video, yt_schedule_video,
  yt_register_uploaded_video, yt_bulk_schedule, yt_publish_clip,
  yt_update_video_metadata) ;
- yt_update_video_metadata dans tous les cas (la vidéo peut être EN
  LIGNE — fail-closed, son statut n'est pas vérifiable ici) ;
- yt_start_ab_test (change la miniature visible pendant le test) ;
- yt_reply_to_comment (réponse publique + 50 unités de quota) ;
- yt_schedule_cross_post (publie sur les plateformes connectées) ;
- yt_generate_report (lien de partage public, durée de vie à annoncer) ;
- yt_create_prompt / yt_update_prompt avec is_public.

Les champs posés par le modèle ne valent jamais confirmation humaine.
"""
import json
import re
import sys

RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"(yt_[A-Za-z0-9_]+)$")
AVEC_PRIVACY = {"yt_publish_video", "yt_schedule_video",
                "yt_register_uploaded_video", "yt_bulk_schedule",
                "yt_publish_clip"}
TOUJOURS = {
    "yt_update_video_metadata": "modifie une vidéo potentiellement EN LIGNE — montrer l'avant/après",
    "yt_start_ab_test": "change la miniature VISIBLE pendant le test (48 h par phase par défaut)",
    "yt_reply_to_comment": "réponse PUBLIQUE au nom de la chaîne, et 50 unités de quota",
    "yt_schedule_cross_post": "publie sur les plateformes de distribution connectées",
    "yt_generate_report": "crée un lien de partage PUBLIC — annoncer sa durée de vie",
}


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": f"[garde-public] {raison}"}}))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    m = RX.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil, entree = m.group(1), data.get("tool_input") or {}
    if outil in TOUJOURS:
        ask(f"{outil} : {TOUJOURS[outil]}. Confirmer.")
    if outil in AVEC_PRIVACY and \
            str(entree.get("privacy", "")).lower() == "public":
        ask(f"{outil} en privacy PUBLIC (le défaut serveur est private) : "
            "la vidéo sera visible de tous dès la publication. Confirmer "
            "explicitement ce passage en public.")
    if outil in ("yt_create_prompt", "yt_update_prompt") and \
            entree.get("is_public"):
        ask(f"{outil} avec is_public : le prompt devient visible des autres "
            "utilisateurs — vérifier qu'il ne contient aucune donnée "
            "interne, puis confirmer.")
    sys.exit(0)


if __name__ == "__main__":
    main()
