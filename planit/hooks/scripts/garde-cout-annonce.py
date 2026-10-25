#!/usr/bin/env python3
"""Garde du coût annoncé (PreToolUse) — pas d'exécution sans estimation.

Le journal de session (.claude/state/planit-session.json, alimenté par le
hook PostToolUse journal-ecritures) retient, pour la journée :
- `couts_annonces` : les identifiants et noms vus dans les appels
  estimate_routine_cost et les propositions renvoyées par propose_routine ;
- `kpi_catalog` : list_kpi_catalog a été lu.

Ce garde REFUSE (deny) :
- run_routine_now, accept_routine_proposal, resume_routine quand AUCUNE
  estimation de la même routine ou proposition n'apparaît au journal ;
- add_kpi_widget sans list_kpi_catalog préalable dans la session.

La clé racine `session_test` du payload sert aux tests CI (le modèle ne
contrôle que tool_input). Aucun appel réseau.
"""
import datetime
import json
import os
import re
import sys

ETAT = os.path.join(".claude", "state", "planit-session.json")
RX_MCP = re.compile(r"^mcp__[Pp]lan[_-]?[Ii]t__([A-Za-z0-9_]+)$")
CIBLES = {"run_routine_now", "accept_routine_proposal", "resume_routine"}


def deny(raison):
    print(f"garde-cout-annonce : {raison}", file=sys.stderr)
    sys.exit(2)


def valeurs(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from valeurs(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from valeurs(v)
    elif isinstance(obj, (str, int)):
        yield str(obj)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    m = RX_MCP.match(payload.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil = m.group(1)
    if outil not in CIBLES and outil != "add_kpi_widget":
        sys.exit(0)

    etat = payload.get("session_test")
    if etat is None:
        try:
            with open(ETAT, encoding="utf-8") as f:
                etat = json.load(f)
        except Exception:  # noqa: BLE001
            etat = {}
    jour = etat.get(datetime.date.today().isoformat(), {}) \
        if isinstance(etat, dict) else {}

    if outil == "add_kpi_widget":
        if not jour.get("kpi_catalog"):
            deny("add_kpi_widget sans list_kpi_catalog dans la session — le "
                 "coût de collecte s'annonce AVANT de poser un widget.")
        sys.exit(0)

    annonces = {str(a) for a in jour.get("couts_annonces", [])}
    if annonces & set(valeurs(payload.get("tool_input", {}))):
        sys.exit(0)
    deny(f"{outil} sans estimate_routine_cost sur la même routine ou "
         "proposition dans cette session — annoncer le coût d'abord "
         "(estimate_routine_cost), puis demander l'accord.")


if __name__ == "__main__":
    main()
