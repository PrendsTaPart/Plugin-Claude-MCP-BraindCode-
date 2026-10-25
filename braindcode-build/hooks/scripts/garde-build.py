#!/usr/bin/env python3
"""Hook PreToolUse — écritures visibles côté BraindCode Build.

Ask systématique sur publish_project, unpublish_project, propose_idea,
propose_connector, join_hackathon et register_pitch : chacun rend quelque
chose public ou engage le projet vis-à-vis des équipes Build. La raison de
chaque outil vient de reference/outils-sensibles.json (fail-closed : table
illisible = ask générique). Un champ confirm posé par le modèle ne vaut
jamais confirmation humaine.
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(os.path.dirname(ICI))
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Bb]raindcode[-_][Bb]uild__([A-Za-z0-9_]+)$")


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
        publication = table["publication_build"]
    except Exception:  # noqa: BLE001
        publication = {}
        raison = ("table des outils sensibles illisible (fail-closed) — "
                  "confirmer cette écriture Build")
    if outil in publication or not publication:
        raison = publication.get(outil, "écriture visible côté Build")
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse", "permissionDecision": "ask",
            "permissionDecisionReason":
                f"[garde-build] {outil} : {raison}. Montrer l'aperçu complet "
                "et obtenir l'accord explicite — un champ posé par le modèle "
                "ne vaut jamais confirmation."}}))
    sys.exit(0)


if __name__ == "__main__":
    main()
