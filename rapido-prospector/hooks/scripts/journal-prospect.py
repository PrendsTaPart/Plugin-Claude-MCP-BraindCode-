#!/usr/bin/env python3
"""Hook PostToolUse — journal des écritures Prospect + compteurs d'envoi.

- journalise chaque ÉCRITURE (pas les lectures list_/get_/prospection_history/
  stripe_stats, ni prospection_terms sans add_kind) dans
  .claude/logs/prospect-<date>.jsonl — e-mails, téléphones et jetons MASQUÉS,
  rotation à 5 Mo ;
- incrémente les compteurs du jour .claude/state/prospect-envois.json pour
  les 5 envois réels (comptés en nombre de cibles, même si le serveur
  renvoie une erreur : prudence > précision) ;
- pose les marqueurs de session .claude/state/prospect-session.json
  (list_clients, lu par le hook anti-doublon) ;
- jamais bloquant : exit 0 quoi qu'il arrive.
"""
import datetime
import json
import os
import re
import sys

RX_OUTIL = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Pp]rospect__([A-Za-z0-9_]+)$")
LECTURE_PREFIXES = ("list_", "get_")
LECTURES_NOMMEES = {"prospection_history", "stripe_stats"}
ENVOIS = {"send_email": ("email", "recipients"),
          "send_sms": ("sms", "targets"),
          "place_call": ("appels", "targets"),
          "send_linkedin_invite": ("linkedin_invitations", "connectionId"),
          "send_linkedin_message": ("linkedin_messages", "connectionId")}
CLES_SECRETES = re.compile(r"token|secret|password|api[_-]?key|authorization", re.I)
RX_EMAIL = re.compile(r"([A-Za-z0-9._%+-])[A-Za-z0-9._%+-]*(@[A-Za-z0-9.-]+)")
RX_TEL = re.compile(r"(?<!\d)(\+?\d[\d .-]{7,}\d)(?!\d)")
PLAFOND_OCTETS = 5 * 1024 * 1024


def masquer_texte(s):
    s = RX_EMAIL.sub(r"\1***\2", s)
    return RX_TEL.sub(lambda m: m.group(1)[:3] + "***" + m.group(1)[-2:], s)


def masquer(obj):
    if isinstance(obj, dict):
        return {k: ("***" if CLES_SECRETES.search(k) else masquer(v))
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [masquer(v) for v in obj]
    if isinstance(obj, str):
        return masquer_texte(obj)
    return obj


def _maj_json(chemin, maj):
    try:
        etat = json.load(open(chemin, encoding="utf-8"))
    except Exception:  # noqa: BLE001
        etat = {}
    etat = maj(etat)
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    json.dump(etat, open(chemin, "w", encoding="utf-8"), ensure_ascii=False)


def main():
    try:
        data = json.load(sys.stdin)
        m = RX_OUTIL.match(data.get("tool_name", ""))
        if not m:
            return
        outil = m.group(1)
        entree = data.get("tool_input") or {}
        maintenant = datetime.datetime.now()
        jour = maintenant.date().isoformat()

        if outil == "list_clients":
            _maj_json(os.path.join(".claude", "state", "prospect-session.json"),
                      lambda e: {**e, "list_clients":
                                 maintenant.isoformat(timespec="seconds")})

        est_lecture = (outil.startswith(LECTURE_PREFIXES)
                       or outil in LECTURES_NOMMEES
                       or (outil == "prospection_terms"
                           and not entree.get("add_kind")))
        if est_lecture:
            return

        if outil in ENVOIS:
            canal, champ = ENVOIS[outil]
            cibles = entree.get(champ)
            lot = len(cibles) if isinstance(cibles, list) else 1

            def maj(e):
                if e.get("date") != jour:
                    e = {"date": jour}
                e[canal] = e.get(canal, 0) + lot
                return e
            _maj_json(os.path.join(".claude", "state", "prospect-envois.json"),
                      maj)

        reponse = data.get("tool_response")
        ligne = {"ts": maintenant.isoformat(timespec="seconds"), "outil": outil,
                 "entree": masquer(entree),
                 "erreur": bool(isinstance(reponse, dict)
                                and reponse.get("isError"))}
        chemin = os.path.join(".claude", "logs", f"prospect-{jour}.jsonl")
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        if os.path.isfile(chemin) and os.path.getsize(chemin) > PLAFOND_OCTETS:
            os.replace(chemin, chemin + ".1")
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except Exception:  # noqa: BLE001
        pass  # un journal ne bloque jamais le travail


if __name__ == "__main__":
    main()
