#!/usr/bin/env python3
"""Journal local des écritures MCP (PostToolUse) — plugin rapido-employe.

Une ligne JSONL par ÉCRITURE dans .claude/logs/employe-<date>.jsonl :
horodatage, serveur, outil, famille, arguments (secrets masqués, e-mails et
téléphones tronqués), succès/échec apparent. Les lectures ne sont pas
journalisées. Jamais bloquant : exit 0 quoi qu'il arrive.

Tient aussi les deux états que les gardes relisent :
- .claude/state/compteurs-envois.json : compteurs du jour (envois,
  publications, réponses) pour les quotas du cadre ;
- .claude/state/depenses-session.json : le dernier record_expense du jour
  (accepté ou refusé, d'après la réponse du serveur).
"""
import datetime
import json
import os
import re
import sys

RACINE_PLUGIN = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
TABLE = os.path.join(RACINE_PLUGIN, "reference", "familles-outils.json")
DOSSIER_LOGS = os.path.join(".claude", "logs")
DOSSIER_ETAT = os.path.join(".claude", "state")
RX_MCP = re.compile(r"^mcp__(.+)__([A-Za-z0-9_-]+)$")
RX_LECTURE = re.compile(r"^(list|get|search|check|describe|rechercher|lister|"
                        r"obtenir|preview|read)[_-]")
CLES_SECRETES = re.compile(r"token|secret|password|api[_-]?key|authorization|"
                           r"client_secret|bearer", re.I)
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


def maj_etat(chemin, mutation):
    try:
        with open(chemin, encoding="utf-8") as f:
            etat = json.load(f)
    except Exception:  # noqa: BLE001
        etat = {}
    mutation(etat)
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(etat, f, ensure_ascii=False)


def main():
    try:
        payload = json.load(sys.stdin)
        m = RX_MCP.match(payload.get("tool_name", ""))
        if not m or RX_LECTURE.match(m.group(2)):
            return
        serveur, outil = m.group(1), m.group(2)
        try:
            with open(TABLE, encoding="utf-8") as f:
                table = json.load(f)
        except Exception:  # noqa: BLE001
            table = {}
        entree = (table.get("outils", {}).get(outil) or {})
        reponse = payload.get("tool_response")
        reponse_txt = json.dumps(reponse, ensure_ascii=False)[:400] \
            if reponse is not None else ""
        jour = datetime.date.today().isoformat()

        ligne = {
            "quand": datetime.datetime.now(datetime.timezone.utc)
            .isoformat(timespec="seconds"),
            "serveur": serveur, "outil": outil,
            "famille": entree.get("famille"),
            "arguments": masquer(payload.get("tool_input", {})),
            "reponse_extrait": masquer(reponse_txt),
        }
        os.makedirs(DOSSIER_LOGS, exist_ok=True)
        chemin = os.path.join(DOSSIER_LOGS, f"employe-{jour}.jsonl")
        if os.path.exists(chemin) and os.path.getsize(chemin) > PLAFOND_OCTETS:
            os.replace(chemin, chemin + ".1")
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")

        # Compteurs de quotas du jour (relus par garde-envois).
        for liste, compteur in (("quota_envois", "envois"),
                                ("quota_publications", "publications"),
                                ("quota_reponses", "reponses")):
            noms = {c.split(":", 1)[-1] for c in table.get(liste, [])}
            if outil in noms:
                def inc(etat, c=compteur, j=jour):
                    etat.setdefault(j, {})
                    etat[j][c] = int(etat[j].get(c, 0)) + 1
                maj_etat(os.path.join(DOSSIER_ETAT, "compteurs-envois.json"), inc)

        # Dernier record_expense du jour (relu par garde-depense).
        if outil == "record_expense":
            refus = bool(re.search(r"refus|budget\s+d[ée]pass|rejet",
                                   reponse_txt, re.I))
            accepte = (not refus) and bool(
                re.search(r"accept|enregistr|inscrit|ok", reponse_txt, re.I))
            def pose(etat, j=jour, r=refus, a=accepte):
                etat[j] = {"refuse": r, "accepte": a}
            maj_etat(os.path.join(DOSSIER_ETAT, "depenses-session.json"), pose)
    except Exception:  # noqa: BLE001 — le journal n'est JAMAIS bloquant
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
