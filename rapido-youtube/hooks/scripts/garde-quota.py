#!/usr/bin/env python3
"""Hook PreToolUse — aucun envoi sans lecture fraîche du quota.

Sur les 9 outils d'envoi (un envoi complet chacun) :
- deny si AUCUN yt_get_quota_status n'a été lu dans les 30 dernières
  minutes (journal .claude/state/youtube-session.json, alimenté en
  PostToolUse par journal-youtube.py) ;
- deny si le dernier risque lu vaut will_fail ;
- ask si le dernier risque lu vaut tight ;
- allow sinon (les autres gardes — chaîne, public — jouent en plus).

Fail-closed : journal illisible = deny. Clés de test réservées au harnais
CI : session_test, maintenant_test.
"""
import datetime
import json
import os
import re
import sys

ETAT = os.path.join(".claude", "state", "youtube-session.json")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"(yt_[A-Za-z0-9_]+)$")
ENVOIS = {"yt_publish_video", "yt_schedule_video",
          "yt_register_uploaded_video", "yt_bulk_schedule",
          "yt_publish_clip", "yt_retry_video", "yt_retry_videos",
          "yt_retry_failed_items", "yt_queue_autopilot"}
FRAICHEUR_MIN = 30


def deny(raison):
    print(f"[garde-quota] REFUS : {raison}", file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        deny("entrée illisible (fail-closed)")
    m = RX.match(data.get("tool_name", ""))
    if not m or m.group(1) not in ENVOIS:
        sys.exit(0)
    etat = data.get("session_test")
    if not isinstance(etat, dict):
        try:
            etat = json.load(open(ETAT, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            etat = {}
    quota = etat.get("quota") or {}
    ts, risque = quota.get("ts"), quota.get("risk")
    if not ts:
        deny("aucune lecture de yt_get_quota_status dans la session — lire "
             "le quota d'abord (quota du jour, réservations sous 24 h, "
             "disponible réel, risque), puis revenir.")
    try:
        lu = datetime.datetime.fromisoformat(str(ts))
        maintenant = datetime.datetime.fromisoformat(
            str(data["maintenant_test"])) if data.get("maintenant_test") \
            else datetime.datetime.now()
        age = (maintenant - lu).total_seconds() / 60
    except Exception:  # noqa: BLE001
        deny("horodatage de la dernière lecture de quota illisible "
             "(fail-closed) — relire yt_get_quota_status.")
    if age > FRAICHEUR_MIN:
        deny(f"la dernière lecture du quota date de {age:.0f} min "
             f"(> {FRAICHEUR_MIN}) — relire yt_get_quota_status avant "
             "d'envoyer.")
    if risque == "will_fail":
        deny("le dernier risque lu vaut will_fail : le disponible réel ne "
             "couvre pas les publications déjà réservées — aucun envoi. "
             "Vérifier le planning sous 24 h (yt_list_schedule) et "
             "reporter/annuler avant d'ajouter quoi que ce soit.")
    if risque == "tight":
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse", "permissionDecision": "ask",
            "permissionDecisionReason":
                f"[garde-quota] risque TIGHT au dernier relevé "
                f"({age:.0f} min) : l'envoi {m.group(1)} peut passer mais "
                "serre le quota du jour. Confirmer cet envoi précis."}}))
        sys.exit(0)
    sys.exit(0)


if __name__ == "__main__":
    main()
