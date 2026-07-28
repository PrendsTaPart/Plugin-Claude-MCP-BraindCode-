#!/usr/bin/env python3
"""Garde-fou PreToolUse du plugin foodeatup-boucles. Stdlib uniquement, aucun réseau.

Principe (audit Académie) : un garde-fou que l'appelant peut désactiver n'est pas
un garde-fou. Ce script ne lit JAMAIS les champs `confirm`/`confirmed` du
tool_input — le modèle peut les avoir remplis lui-même. La confirmation vient de
l'utilisateur, via la décision `ask` du harnais, hors du flux du modèle.

Décisions :
- outil de lecture (list_/get_/check_ + lectures nommées)      → allow (exit 0)
- liste outils-destructifs.txt absente/illisible + écriture    → deny  (mode fermé)
- écriture présente dans la liste                              → ask   (toujours)
- écriture absente de la liste                                 → allow
Toute tentative interceptée est journalisée dans .claude/logs/.
"""
import datetime
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
LISTE = os.path.join(ICI, "outils-destructifs.txt")

LECTURE_PREFIXES = ("list_", "get_", "check_")
LECTURE_NOMMEES = {
    "finance_summary", "floor_plan_status", "reservation_availability",
    "search_entities",
}

# Effet réel des outils les plus sensibles, pour un message de blocage parlant.
EFFETS = {
    "launch_campaign": "lance un envoi réel de campagne aux destinataires du segment",
    "publish_site": "publie le site vitrine en ligne, visible du public",
    "apply_site_template": "remplace la mise en page du site publié",
    "close_pos_session": "clôture de caisse (Z) irréversible",
    "record_pos_payment": "enregistre un encaissement d'argent réel",
    "submit_whatsapp_template": "soumet le template WhatsApp à la validation Meta",
    "import_storefront_menu": "réécrit toute la carte vitrine en un appel",
    "update_loyalty_program": "modifie le programme de fidélité de TOUS les clients",
    "adjust_points": "modifie le solde de points d'un client",
    "create_employee_contract": "crée un contrat de travail (acte juridique)",
    "update_employee_schedule": "modifie le planning contractuel d'un employé",
    "moderate_review": "modère un avis client public",
    "reply_review": "publie une réponse publique à un avis",
}


def journaliser(entree):
    try:
        d = os.path.join(os.getcwd(), ".claude", "logs")
        os.makedirs(d, exist_ok=True)
        chemin = os.path.join(d, f"garde-boucles-{datetime.date.today().isoformat()}.jsonl")
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(entree, ensure_ascii=False) + "\n")
    except Exception:
        pass  # la journalisation ne doit jamais changer la décision


def decision_ask(serveur, outil):
    effet = EFFETS.get(outil, "action destructrice ou irréversible")
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                f"« {outil} » ({serveur}) : {effet}. Confirmation humaine requise "
                "— ce garde-fou ignore volontairement tout champ confirm/confirmed "
                "du tool_input, que le modèle peut remplir lui-même "
                "(plugin foodeatup-boucles)."
            ),
        }
    }, ensure_ascii=False))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    tool_name = str(data.get("tool_name", ""))

    # mcp__<serveur>__<outil> ; hors MCP → hors périmètre → allow
    parts = tool_name.split("__")
    if len(parts) < 3 or parts[0] != "mcp":
        sys.exit(0)
    serveur, outil = parts[1].lower(), "__".join(parts[2:])

    # 1. La lecture n'est JAMAIS bloquée, même en mode fermé.
    if outil.startswith(LECTURE_PREFIXES) or outil in LECTURE_NOMMEES:
        sys.exit(0)

    # 2. Charger la liste ; échec → mode fermé : on bloque l'écriture.
    try:
        with open(LISTE, encoding="utf-8") as f:
            destructifs = {l.strip() for l in f
                           if l.strip() and not l.startswith("#")}
        if not destructifs:
            raise ValueError("liste vide")
    except Exception as e:
        journaliser({"ts": datetime.datetime.now().isoformat(timespec="seconds"),
                     "outil": tool_name, "decision": "deny",
                     "motif": f"liste illisible ({e.__class__.__name__})"})
        print("Garde-fou foodeatup-boucles en mode fermé : la liste des outils "
              "destructifs (outils-destructifs.txt) est absente ou illisible — "
              f"écriture « {outil} » bloquée par précaution.", file=sys.stderr)
        sys.exit(2)

    # 3. Écriture destructrice → ask, quoi que contienne tool_input.
    if f"{serveur}:{outil}" in destructifs:
        journaliser({"ts": datetime.datetime.now().isoformat(timespec="seconds"),
                     "outil": tool_name, "decision": "ask",
                     "effet": EFFETS.get(outil, "")})
        decision_ask(serveur, outil)

    # 4. Écriture ordinaire : laisser passer (les gardes du plugin foodeatup
    #    de base restent actifs par ailleurs).
    sys.exit(0)


if __name__ == "__main__":
    main()
