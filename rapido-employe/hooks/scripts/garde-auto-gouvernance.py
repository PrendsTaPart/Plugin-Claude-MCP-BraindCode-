#!/usr/bin/env python3
"""Garde d'auto-gouvernance (PreToolUse) — DENY ABSOLU.

Claude employé ne fixe ni ne valide jamais son propre cadre. Les outils de
gouvernance du responsable (liste `gouvernance_deny` de la table versionnée
reference/familles-outils.json : set_agent_policy, review_practice,
review_team_memory, decide_module, set_tunnel_block, incubation_admin_*,
invite_learner, send_reminder) sont refusés quoi qu'il arrive — y compris si
le modèle pose confirm=true, et même cadre en main. Le skill
`espace-responsable` prépare ces décisions en APERÇU pour signature humaine
dans l'application : il n'appelle pas ces outils non plus.

deny = exit 2 + stderr. Aucun appel réseau. Fail-closed : table illisible →
les noms de repli embarqués ci-dessous s'appliquent. Testé en CI.
"""
import json
import os
import re
import sys

RACINE_PLUGIN = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
TABLE = os.path.join(RACINE_PLUGIN, "reference", "familles-outils.json")
RX_MCP = re.compile(r"^mcp__(.+)__([A-Za-z0-9_-]+)$")
REPLI = {
    "set_agent_policy", "review_practice", "review_team_memory",
    "decide_module", "set_tunnel_block", "invite_learner", "send_reminder",
}


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
            interdits = set(json.load(f).get("gouvernance_deny", []))
    except Exception:  # noqa: BLE001
        interdits = set()
    interdits |= REPLI
    if outil in interdits or outil.startswith("incubation_admin_"):
        print(f"garde-auto-gouvernance : « {outil} » est un outil de "
              "gouvernance du responsable — Claude ne fixe ni ne valide "
              "jamais son propre cadre. Décision à prendre dans "
              "l'application, par un humain.", file=sys.stderr)
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
