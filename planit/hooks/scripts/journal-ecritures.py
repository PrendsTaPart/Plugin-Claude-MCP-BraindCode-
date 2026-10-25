#!/usr/bin/env python3
"""Journal local des écritures Plan'It (PostToolUse) — jamais bloquant.

- Une ligne JSONL par ÉCRITURE dans .claude/logs/planit-<date>.jsonl
  (horodatage, outil, arguments masqués, extrait de réponse). Les lectures
  ne sont pas journalisées.
- Tient .claude/state/planit-session.json, relu par garde-cout-annonce :
  `couts_annonces` (identifiants/noms vus dans estimate_routine_cost et ids
  de proposition renvoyés par propose_routine) et `kpi_catalog`
  (list_kpi_catalog lu).

Secrets masqués (token/secret/key/authorization), e-mails et téléphones
tronqués. Exit 0 quoi qu'il arrive.
"""
import datetime
import json
import os
import re
import sys

DOSSIER_LOGS = os.path.join(".claude", "logs")
ETAT = os.path.join(".claude", "state", "planit-session.json")
RX_MCP = re.compile(r"^mcp__[Pp]lan[_-]?[Ii]t__([A-Za-z0-9_]+)$")
LECTURES = re.compile(r"^(list|get|recommend|estimate|evaluate|preview|"
                      r"route|select|test)_")
CLES_SECRETES = re.compile(r"token|secret|password|api[_-]?key|authorization",
                           re.I)
RX_EMAIL = re.compile(r"([A-Za-z0-9._%+-])[A-Za-z0-9._%+-]*(@[A-Za-z0-9.-]+)")
RX_TEL = re.compile(r"(?<!\d)(\+?\d[\d .-]{7,}\d)(?!\d)")
PLAFOND_OCTETS = 5 * 1024 * 1024


def masquer(obj):
    if isinstance(obj, dict):
        return {k: ("***" if CLES_SECRETES.search(k) else masquer(v))
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [masquer(v) for v in obj]
    if isinstance(obj, str):
        s = RX_EMAIL.sub(r"\1***\2", obj)
        return RX_TEL.sub(lambda m: m.group(1)[:3] + "***" + m.group(1)[-2:], s)
    return obj


def valeurs(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from valeurs(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from valeurs(v)
    elif isinstance(obj, (str, int)):
        yield str(obj)


def maj_session(mutation):
    try:
        with open(ETAT, encoding="utf-8") as f:
            etat = json.load(f)
    except Exception:  # noqa: BLE001
        etat = {}
    jour = datetime.date.today().isoformat()
    etat.setdefault(jour, {"couts_annonces": [], "kpi_catalog": False})
    mutation(etat[jour])
    os.makedirs(os.path.dirname(ETAT), exist_ok=True)
    with open(ETAT, "w", encoding="utf-8") as f:
        json.dump(etat, f, ensure_ascii=False)


def main():
    try:
        payload = json.load(sys.stdin)
        m = RX_MCP.match(payload.get("tool_name", ""))
        if not m:
            return
        outil = m.group(1)
        reponse = payload.get("tool_response")

        if outil == "list_kpi_catalog":
            maj_session(lambda j: j.update(kpi_catalog=True))
        if outil == "estimate_routine_cost":
            vals = [v for v in valeurs(payload.get("tool_input", {}))]
            maj_session(lambda j: j["couts_annonces"].extend(
                v for v in vals if v not in j["couts_annonces"]))
        if outil == "propose_routine" and reponse is not None:
            ids = re.findall(r'"(?:proposal_id|id|task_id)"\s*:\s*"?([\w-]+)',
                             json.dumps(reponse))
            maj_session(lambda j: j["couts_annonces"].extend(
                i for i in ids if i not in j["couts_annonces"]))

        if LECTURES.match(outil):
            return
        jour = datetime.date.today().isoformat()
        ligne = {
            "quand": datetime.datetime.now(datetime.timezone.utc)
            .isoformat(timespec="seconds"),
            "outil": outil,
            "arguments": masquer(payload.get("tool_input", {})),
            "reponse_extrait": masquer(
                json.dumps(reponse, ensure_ascii=False)[:400]
                if reponse is not None else ""),
        }
        os.makedirs(DOSSIER_LOGS, exist_ok=True)
        chemin = os.path.join(DOSSIER_LOGS, f"planit-{jour}.jsonl")
        if os.path.exists(chemin) and os.path.getsize(chemin) > PLAFOND_OCTETS:
            os.replace(chemin, chemin + ".1")
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except Exception:  # noqa: BLE001 — le journal n'est JAMAIS bloquant
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
