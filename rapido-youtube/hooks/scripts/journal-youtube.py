#!/usr/bin/env python3
"""Hook PostToolUse — journal des écritures YouTube + état de session.

- journalise chaque ÉCRITURE (pas les yt_list_/yt_get_ purs) dans
  .claude/logs/youtube-<date>.jsonl, secrets et jetons de liens signés
  MASQUÉS, rotation à 5 Mo ;
- tient .claude/state/youtube-session.json, lu par les gardes :
  - quota {ts, risk, available} à chaque yt_get_quota_status ;
  - chaine_active / chaine_favorite depuis yt_get_channel_status ;
  - grille_lue (ts) sur yt_list_schedule_slots ;
  - face_models [ids] sur yt_list_face_models ;
  - apercus_lot [empreintes] sur yt_create_bulk_job preview_only et
    yt_find_replace_descriptions dry_run (mêmes empreintes que garde-lot) ;
  - credits_estimes (cumul) : +coût barème si la réponse le donne
    (credits_used / cost), sinon +1 par opération payante (prudence) ;
- jamais bloquant : exit 0 quoi qu'il arrive.
"""
import datetime
import hashlib
import json
import os
import re
import sys

RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"([A-Za-z0-9_]+)$")
LECTURES = ("yt_list_", "yt_get_", "yt_compare_", "yt_suggest_",
            "yt_analyze_", "yt_score_", "yt_research_", "yt_find_outliers",
            "yt_audit_channel", "yt_extract_youtube_thumbnail",
            "yt_draft_comment_reply")
PAYANTS = {"yt_generate_thumbnail", "yt_edit_thumbnail",
           "yt_inpaint_thumbnail", "yt_swap_face", "yt_apply_style",
           "yt_auto_optimize_thumbnail", "yt_clone_style_from_url",
           "yt_generate_vertical_variant", "yt_apply_template"}
CLES_SECRETES = re.compile(r"token|secret|password|api[_-]?key|authorization",
                           re.I)
RX_LIEN_SIGNE = re.compile(r"https?://\S*(?:token=|X-Amz-)\S*")
ETAT = os.path.join(".claude", "state", "youtube-session.json")
PLAFOND_OCTETS = 5 * 1024 * 1024


def masquer(obj):
    if isinstance(obj, dict):
        return {k: ("***" if CLES_SECRETES.search(k) else masquer(v))
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [masquer(v) for v in obj]
    if isinstance(obj, str):
        return RX_LIEN_SIGNE.sub("***lien-signé***", obj)
    return obj


def _maj(maj):
    try:
        etat = json.load(open(ETAT, encoding="utf-8"))
    except Exception:  # noqa: BLE001
        etat = {}
    etat = maj(etat)
    os.makedirs(os.path.dirname(ETAT), exist_ok=True)
    json.dump(etat, open(ETAT, "w", encoding="utf-8"), ensure_ascii=False)


def main():
    try:
        data = json.load(sys.stdin)
        m = RX.match(data.get("tool_name", ""))
        if not m:
            return
        outil = m.group(1)
        entree = data.get("tool_input") or {}
        reponse = data.get("tool_response")
        rep = reponse if isinstance(reponse, dict) else {}
        maintenant = datetime.datetime.now().isoformat(timespec="seconds")

        if outil == "yt_get_quota_status":
            _maj(lambda e: {**e, "quota": {
                "ts": maintenant,
                "risk": rep.get("risk") or rep.get("risque"),
                "available": rep.get("available") or rep.get("remaining")}})
        if outil == "yt_get_channel_status":
            _maj(lambda e: {**e,
                            "chaine_active": rep.get("active_channel")
                            or rep.get("active"),
                            "chaine_favorite": rep.get("favorite_channel")
                            or rep.get("favorite")})
        if outil == "yt_list_schedule_slots":
            _maj(lambda e: {**e, "grille_lue": maintenant})
        if outil == "yt_list_face_models":
            ids = [str(x.get("id")) for x in
                   (rep.get("face_models") or rep.get("models") or [])
                   if isinstance(x, dict) and x.get("id")]
            _maj(lambda e: {**e, "face_models": ids})
        if (outil == "yt_create_bulk_job" and entree.get("preview_only")) or \
                (outil == "yt_find_replace_descriptions"
                 and entree.get("dry_run")):
            # même empreinte que garde-lot.py (recopiée : hooks autonomes)
            if outil == "yt_create_bulk_job":
                base = {"type": entree.get("type") or entree.get("job_type"),
                        "videos": sorted(map(str, entree.get("video_ids")
                                             or entree.get("videos") or [])),
                        "channel": entree.get("channel_id")}
            else:
                base = {"find": entree.get("find") or entree.get("search"),
                        "replace": entree.get("replace")
                        or entree.get("replacement"),
                        "channel": entree.get("channel_id"),
                        "filtres": entree.get("filters")}
            emp = hashlib.md5(json.dumps(base, sort_keys=True,
                                         ensure_ascii=False).encode()
                              ).hexdigest()

            def maj(e):
                vus = e.get("apercus_lot") or []
                if emp not in vus:
                    vus.append(emp)
                e["apercus_lot"] = vus
                return e
            _maj(maj)
        if outil in PAYANTS:
            cout = rep.get("credits_used") or rep.get("cost") or 1

            def maj(e):
                e["credits_estimes"] = e.get("credits_estimes", 0) + \
                    (cout if isinstance(cout, (int, float)) else 1)
                return e
            _maj(maj)

        if outil.startswith(LECTURES):
            return
        jour = maintenant[:10]
        ligne = {"ts": maintenant, "outil": outil,
                 "entree": masquer(entree),
                 "erreur": bool(rep.get("isError"))}
        chemin = os.path.join(".claude", "logs", f"youtube-{jour}.jsonl")
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        if os.path.isfile(chemin) and os.path.getsize(chemin) > PLAFOND_OCTETS:
            os.replace(chemin, chemin + ".1")
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except Exception:  # noqa: BLE001
        pass  # un journal ne bloque jamais le travail


if __name__ == "__main__":
    main()
