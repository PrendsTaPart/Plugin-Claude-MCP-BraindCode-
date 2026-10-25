#!/usr/bin/env python3
"""Hook PreToolUse — écritures risquées Lovable.

- set_project_knowledge : REMPLACE tout le knowledge → ask si aucun
  get_project_knowledge n'apparaît au journal de session ; allow sinon ;
- query_database : SELECT → allow ; DROP / TRUNCATE → deny ; toute autre
  écriture SQL → ask, la requête montrée ;
- enable_database, set_project_visibility, set_folder_visibility,
  move_projects_to_folder, create/update/delete_workspace_skill → ask.

Fail-closed : une requête SQL illisible est traitée comme écriture (ask).
Clé de test réservée au harnais CI : session_test.
"""
import json
import os
import re
import sys

ETAT = os.path.join(".claude", "state", "build-session.json")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Ll]ovable__([A-Za-z0-9_]+)$")
ASK_SIMPLE = {
    "enable_database": "provisionne la base du projet",
    "set_project_visibility": "change la visibilité du projet",
    "set_folder_visibility": "change la visibilité d'un dossier",
    "move_projects_to_folder": "déplace des projets",
    "create_workspace_skill": "pousse une consigne à TOUT l'espace Lovable",
    "update_workspace_skill": "modifie une consigne d'espace (la lire d'abord)",
    "delete_workspace_skill": "supprime une consigne d'espace",
}


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": f"[garde-lovable-ecritures] {raison}"}}))
    sys.exit(0)


def deny(raison):
    print(f"[garde-lovable-ecritures] REFUS : {raison}", file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    m = RX.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil, entree = m.group(1), data.get("tool_input") or {}

    if outil in ASK_SIMPLE:
        ask(f"{outil} : {ASK_SIMPLE[outil]}. Confirmer.")

    if outil == "set_project_knowledge":
        etat = data.get("session_test")
        if not isinstance(etat, dict):
            try:
                etat = json.load(open(ETAT, encoding="utf-8"))
            except Exception:  # noqa: BLE001
                etat = {}
        if etat.get("get_project_knowledge"):
            sys.exit(0)
        ask("set_project_knowledge REMPLACE tout le knowledge et aucun "
            "get_project_knowledge n'apparaît dans la session : lire "
            "l'existant d'abord, fusionner, puis confirmer l'écriture.")

    if outil == "query_database":
        sql = str(entree.get("query") or entree.get("sql") or "").strip()
        premier = sql.split(None, 1)[0].upper() if sql else ""
        if re.search(r"\b(DROP|TRUNCATE)\b", sql, re.I):
            deny("DROP / TRUNCATE sur la base du projet — destruction "
                 "irréversible, ce hook ne le laisse jamais passer.")
        if premier in ("SELECT", "EXPLAIN", "WITH") and \
                not re.search(r"\b(INSERT|UPDATE|DELETE|ALTER|CREATE|GRANT)\b",
                              sql, re.I):
            sys.exit(0)
        ask("query_database hors SELECT — écriture SQL directe. Montrer la "
            f"requête exacte et confirmer : {sql[:120] or '(requête vide)'}")
    sys.exit(0)


if __name__ == "__main__":
    main()
