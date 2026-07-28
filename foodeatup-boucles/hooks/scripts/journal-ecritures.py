#!/usr/bin/env python3
"""Hook PostToolUse du plugin foodeatup-boucles : journal des écritures MCP.

Sans journal, aucune reconstitution possible après une écriture non voulue.
Écrit une ligne JSONL par écriture dans .claude/logs/ecritures-<date>.jsonl :
horodatage, outil, établissement, paramètres (secrets masqués), succès/échec.

Contrat P2.3 :
- les lectures (list_/get_/check_ + lectures nommées) ne sont PAS journalisées ;
- aucun token, email complet ou numéro de téléphone en clair ;
- plafond de taille par fichier (rotation .1) ;
- jamais bloquant : exit 0 quoi qu'il arrive.
"""
import datetime
import json
import os
import re
import sys

PLAFOND_OCTETS = 5 * 1024 * 1024  # 5 Mo par fichier de journal
LECTURE_PREFIXES = ("list_", "get_", "check_")
LECTURE_NOMMEES = {
    "finance_summary", "floor_plan_status", "reservation_availability",
    "search_entities", "rechercher_prospects", "rechercher_entreprise_siret",
    "search_entreprises",
}
CLES_SECRETES = re.compile(r"token|secret|password|api[_-]?key|authorization", re.I)
RX_EMAIL = re.compile(r"([A-Za-z0-9._%+-])[A-Za-z0-9._%+-]*(@[A-Za-z0-9.-]+)")
RX_TEL = re.compile(r"(?<!\d)(\+?\d[\d .-]{7,}\d)(?!\d)")


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


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    tool_name = str(data.get("tool_name", ""))
    parts = tool_name.split("__")
    if len(parts) < 3 or parts[0] != "mcp":
        return  # hors MCP : pas notre périmètre
    outil = "__".join(parts[2:])
    if outil.startswith(LECTURE_PREFIXES) or outil in LECTURE_NOMMEES:
        return  # les lectures ne sont pas journalisées (bruit)

    tool_input = data.get("tool_input") or {}
    reponse = data.get("tool_response")
    succes = True
    if isinstance(reponse, dict) and (reponse.get("is_error") or reponse.get("error")):
        succes = False
    resume_reponse = masquer_texte(json.dumps(reponse, ensure_ascii=False,
                                              default=str)[:400]) if reponse is not None else None

    entree = {
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        "outil": tool_name,
        "etablissement": tool_input.get("establishment_id")
        if isinstance(tool_input, dict) else None,
        "parametres": masquer(tool_input),
        "succes": succes,
        "reponse_tronquee": resume_reponse,
    }

    d = os.path.join(os.getcwd(), ".claude", "logs")
    os.makedirs(d, exist_ok=True)
    chemin = os.path.join(d, f"ecritures-{datetime.date.today().isoformat()}.jsonl")
    try:
        if os.path.exists(chemin) and os.path.getsize(chemin) > PLAFOND_OCTETS:
            os.replace(chemin, chemin + ".1")  # rotation simple : une génération
    except Exception:
        pass
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(json.dumps(entree, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # le journal ne doit jamais faire échouer l'outil journalisé
    sys.exit(0)
