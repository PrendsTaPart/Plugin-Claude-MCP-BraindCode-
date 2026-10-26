#!/usr/bin/env python3
"""Hook PreToolUse — la chaîne ciblée est toujours explicite.

Ask sur toute publication, planification, opération en lot ou réglage SANS
channel_id explicite, en indiquant la chaîne qui serait ciblée par défaut
(l'active, sinon la favorite — lue au journal de session si disponible).
Ask systématique sur yt_switch_channel et yt_set_favorite_channel (ils
changent la cible de tous les envois suivants).
Clé de test réservée au harnais CI : session_test.
"""
import json
import os
import re
import sys

ETAT = os.path.join(".claude", "state", "youtube-session.json")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"(yt_[A-Za-z0-9_]+)$")
EXIGENT_CHAINE = {
    "yt_publish_video", "yt_schedule_video", "yt_register_uploaded_video",
    "yt_bulk_schedule", "yt_publish_clip", "yt_queue_autopilot",
    "yt_create_bulk_job", "yt_find_replace_descriptions",
    "yt_set_schedule_slots", "yt_set_autopilot",
}
TOUJOURS_ASK = {
    "yt_switch_channel": "change la chaîne ACTIVE — cible par défaut de tous les envois suivants",
    "yt_set_favorite_channel": "change la chaîne FAVORITE (cible de secours)",
}


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": f"[garde-chaine] {raison}"}}))
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
    if outil in TOUJOURS_ASK:
        ask(f"{outil} : {TOUJOURS_ASK[outil]}. Annoncer la chaîne visée "
            "par son NOM et confirmer.")
    if outil in EXIGENT_CHAINE and not entree.get("channel_id"):
        etat = data.get("session_test")
        if not isinstance(etat, dict):
            try:
                etat = json.load(open(ETAT, encoding="utf-8"))
            except Exception:  # noqa: BLE001
                etat = {}
        defaut = etat.get("chaine_active") or etat.get("chaine_favorite") \
            or "inconnue (lire yt_get_channel_status)"
        ask(f"{outil} SANS channel_id : la cible par défaut serait la "
            f"chaîne « {defaut} » (active, sinon favorite). Règle du "
            "plugin : channel_id explicite + nom de la chaîne annoncé — "
            "confirmer cette cible ou préciser la chaîne.")
    sys.exit(0)


if __name__ == "__main__":
    main()
