#!/usr/bin/env python3
"""Garde des dépenses (PreToolUse) — rien ne se paie sans record_expense.

Tout outil PAYANT (liste `outils_payants` de reference/familles-outils.json :
Studio Print, génération média, appels vocaux…) exige un `record_expense`
ACCEPTÉ dans la session : le journal (hook journal-ecritures) tient
.claude/state/depenses-session.json à jour à chaque réponse de record_expense.

- aucune trace de record_expense accepté aujourd'hui → ask (la dépense
  s'annonce d'abord : montant, objet, budget restant) ;
- dernier record_expense du jour REFUSÉ (budget dépassé) → deny : un refus
  arrête la dépense — on ne « retente » pas ;
- outil non payant → allow (exit 0).

Le budget lui-même n'est jamais codé ici : il vit dans get_work_plan.
La clé racine `depenses_test` du payload sert aux tests CI (le modèle ne
contrôle que tool_input). Aucun appel réseau.
"""
import datetime
import json
import os
import re
import sys

RACINE_PLUGIN = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
TABLE = os.path.join(RACINE_PLUGIN, "reference", "familles-outils.json")
ETAT = os.path.join(".claude", "state", "depenses-session.json")
RX_MCP = re.compile(r"^mcp__(.+)__([A-Za-z0-9_-]+)$")


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": raison,
    }}, ensure_ascii=False))
    sys.exit(0)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    m = RX_MCP.match(payload.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil = m.group(2)
    try:
        with open(TABLE, encoding="utf-8") as f:
            payants = set(json.load(f).get("outils_payants", []))
    except Exception:  # noqa: BLE001
        payants = set()
    if outil not in payants:
        sys.exit(0)

    etat = payload.get("depenses_test")
    if etat is None:
        try:
            with open(ETAT, encoding="utf-8") as f:
                etat = json.load(f)
        except Exception:  # noqa: BLE001
            etat = {}
    jour = datetime.date.today().isoformat()
    entree = etat.get(jour) if isinstance(etat, dict) else None
    if entree and entree.get("refuse"):
        print(f"garde-depense : la dernière dépense du jour a été REFUSÉE "
              f"(record_expense) — « {outil} » n'est pas lancé. Un refus "
              "arrête la dépense ; relire le budget avec get_work_plan.",
              file=sys.stderr)
        sys.exit(2)
    if entree and entree.get("accepte"):
        sys.exit(0)
    ask(f"« {outil} » est un outil payant : inscrire d'abord la dépense avec "
        "record_expense (montant, objet) et obtenir son acceptation — le "
        "budget du jour vient de get_work_plan, jamais de tête.")


if __name__ == "__main__":
    main()
