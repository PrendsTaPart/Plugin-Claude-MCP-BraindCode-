#!/usr/bin/env python3
"""Hook PreToolUse — jamais de lot réel sans aperçu préalable.

- yt_create_bulk_job SANS preview_only : deny si aucun aperçu
  (preview_only) du MÊME type de job sur les MÊMES vidéos n'apparaît au
  journal de session (empreintes posées en PostToolUse) ;
- yt_find_replace_descriptions SANS dry_run : deny si aucun dry_run de la
  MÊME recherche (find/replace/filtres) n'apparaît au journal.

Les appels AVEC preview_only ou dry_run passent (c'est la voie normale).
Un dry_run posé par le modèle ne vaut pas accord : l'aperçu montré à
l'humain reste exigé par les skills. Fail-closed : journal illisible =
deny du lot réel. Clé de test réservée au harnais CI : session_test.
"""
import hashlib
import json
import os
import re
import sys

ETAT = os.path.join(".claude", "state", "youtube-session.json")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"(yt_create_bulk_job|yt_find_replace_descriptions)$")


def empreinte(outil, entree):
    if outil == "yt_create_bulk_job":
        base = {"type": entree.get("type") or entree.get("job_type"),
                "videos": sorted(map(str, entree.get("video_ids") or
                                     entree.get("videos") or [])),
                "channel": entree.get("channel_id")}
    else:
        base = {"find": entree.get("find") or entree.get("search"),
                "replace": entree.get("replace") or entree.get("replacement"),
                "channel": entree.get("channel_id"),
                "filtres": entree.get("filters")}
    return hashlib.md5(json.dumps(base, sort_keys=True,
                                  ensure_ascii=False).encode()).hexdigest()


def deny(raison):
    print(f"[garde-lot] REFUS : {raison}", file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        deny("entrée illisible (fail-closed)")
    m = RX.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil, entree = m.group(1), data.get("tool_input") or {}
    if (outil == "yt_create_bulk_job" and entree.get("preview_only")) or \
            (outil == "yt_find_replace_descriptions" and entree.get("dry_run")):
        sys.exit(0)
    etat = data.get("session_test")
    if not isinstance(etat, dict):
        try:
            etat = json.load(open(ETAT, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            etat = {}
    vus = etat.get("apercus_lot") or []
    if empreinte(outil, entree) in vus:
        sys.exit(0)
    mode = ("preview_only: true" if outil == "yt_create_bulk_job"
            else "dry_run: true")
    deny(f"{outil} en RÉEL sans aperçu préalable de la même opération dans "
         f"la session. Lancer d'abord le même appel avec {mode}, montrer "
         "l'aperçu à l'humain, puis relancer en réel sur accord — un "
         "paramètre posé par le modèle ne vaut pas confirmation.")


if __name__ == "__main__":
    main()
