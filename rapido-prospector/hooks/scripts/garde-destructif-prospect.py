#!/usr/bin/env python3
"""Hook PreToolUse — les 12 suppressions définitives du serveur Prospect.

Toujours ask, avec la CASCADE rappelée depuis reference/outils-sensibles.json
(connexion LinkedIn → modèles + historique + messages programmés ;
webinaire → inscriptions + rappels ; lead magnet → fichier stocké ;
client → définitif). Confirmation fiche par fiche : un champ `confirm` posé
par le modèle ne vaut jamais confirmation humaine. Fail-closed : table
illisible = ask avec avertissement générique.
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(os.path.dirname(ICI))
RX_OUTIL = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Pp]rospect__(delete_[A-Za-z0-9_]+)$")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    m = RX_OUTIL.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil = m.group(1)
    try:
        table = json.load(open(os.path.join(
            PLUGIN, "reference", "outils-sensibles.json"), encoding="utf-8"))
        cascade = table["suppressions"].get(
            outil, "suppression définitive (outil absent de la table — vérifier)")
    except Exception:  # noqa: BLE001
        cascade = ("suppression définitive — table des cascades illisible "
                   "(fail-closed), relire reference/outils-sensibles.json")
    ident = (data.get("tool_input") or {}).get("id", "?")
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason":
            f"[garde-destructif-prospect] {outil} sur id={ident} : {cascade}. "
            "Confirmer fiche par fiche — aucune récupération possible."}}))
    sys.exit(0)


if __name__ == "__main__":
    main()
