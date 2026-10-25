#!/usr/bin/env python3
"""Hook PostToolUse — journal des écritures Build/Lovable + état de session.

- journalise chaque ÉCRITURE (pas les list_/get_/check_/render_) dans
  .claude/logs/build-<date>.jsonl, secrets MASQUÉS, rotation à 5 Mo ;
- tient .claude/state/build-session.json :
  - start_prompt_step : horodatage de la dernière étape démarrée (lu par
    garde-credits-lovable) ;
  - get_project_knowledge : horodatage de la dernière lecture (lu par
    garde-lovable-ecritures) ;
  - validations_mise_en_ligne : {project_id: true} dès qu'une lecture de
    get_pending_validations montre une validation de kind mise_en_ligne
    au statut validé (lu par garde-mise-en-ligne) ;
- jamais bloquant : exit 0 quoi qu'il arrive.
"""
import datetime
import json
import os
import re
import sys

RX_OUTIL = re.compile(
    r"^mcp__(?:plugin_[\w-]+_)?(?:[Ll]ovable|[Bb]raindcode[-_][Bb]uild)__"
    r"([A-Za-z0-9_-]+)$")
LECTURE_PREFIXES = ("list_", "get_", "check_", "render_")
CLES_SECRETES = re.compile(
    r"token|secret|password|api[_-]?key|authorization|service_role", re.I)
RX_JWT = re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{6,}[A-Za-z0-9_.-]*")
PLAFOND_OCTETS = 5 * 1024 * 1024
ETAT = os.path.join(".claude", "state", "build-session.json")
RX_VALIDEE = re.compile(
    r'"kind"\s*:\s*"mise_en_ligne"[^}]{0,200}?"status"\s*:\s*"(valid|approuv|accord)[^"]*"',
    re.I | re.S)
RX_PROJET = re.compile(r'"project_id"\s*:\s*"?([\w-]+)')


def masquer(obj):
    if isinstance(obj, dict):
        return {k: ("***" if CLES_SECRETES.search(k) else masquer(v))
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [masquer(v) for v in obj]
    if isinstance(obj, str):
        return RX_JWT.sub("***jwt***", obj)
    return obj


def _maj_etat(maj):
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
        m = RX_OUTIL.match(data.get("tool_name", ""))
        if not m:
            return
        outil = m.group(1)
        maintenant = datetime.datetime.now().isoformat(timespec="seconds")
        if outil in ("start_prompt_step", "get_project_knowledge"):
            _maj_etat(lambda e: {**e, outil: maintenant})
        if outil == "get_pending_validations":
            brut = json.dumps(data.get("tool_response") or {},
                              ensure_ascii=False)
            if RX_VALIDEE.search(brut):
                projets = RX_PROJET.findall(brut) or ["?"]

                def maj(e):
                    v = e.get("validations_mise_en_ligne") or {}
                    for p in projets:
                        v[p] = True
                    e["validations_mise_en_ligne"] = v
                    return e
                _maj_etat(maj)
        if outil.startswith(LECTURE_PREFIXES):
            return
        jour = maintenant[:10]
        ligne = {"ts": maintenant, "outil": outil,
                 "entree": masquer(data.get("tool_input") or {})}
        chemin = os.path.join(".claude", "logs", f"build-{jour}.jsonl")
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        if os.path.isfile(chemin) and os.path.getsize(chemin) > PLAFOND_OCTETS:
            os.replace(chemin, chemin + ".1")
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except Exception:  # noqa: BLE001
        pass  # un journal ne bloque jamais le travail


if __name__ == "__main__":
    main()
