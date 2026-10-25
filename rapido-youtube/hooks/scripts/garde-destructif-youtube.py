#!/usr/bin/env python3
"""Hook PreToolUse — suppressions et annulations : ask, avec le vrai effet.

Les raisons viennent de reference/outils-sensibles.json (famille
suppressions_annulations) — dont le rappel clé : yt_delete_video supprime
l'entrée et le fichier DANS L'APPLICATION, la vidéo publiée RESTE en ligne
sur YouTube. Un champ confirm posé par le modèle ne vaut jamais
confirmation humaine. Fail-closed : table illisible = ask générique.
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(os.path.dirname(ICI))
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"(yt_delete_[A-Za-z0-9_]+|yt_cancel_[A-Za-z0-9_]+)$")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    m = RX.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil = m.group(1)
    try:
        table = json.load(open(os.path.join(
            PLUGIN, "reference", "outils-sensibles.json"), encoding="utf-8"))
        raison = table["suppressions_annulations"].get(
            outil, "suppression ou annulation (absente de la table — vérifier)")
    except Exception:  # noqa: BLE001
        raison = ("suppression ou annulation — table des effets illisible "
                  "(fail-closed), relire reference/outils-sensibles.json")
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason":
            f"[garde-destructif-youtube] {outil} : {raison}. Confirmer "
            "élément par élément — un champ confirm posé par le modèle ne "
            "vaut jamais confirmation humaine."}}))
    sys.exit(0)


if __name__ == "__main__":
    main()
