#!/usr/bin/env python3
"""Garde Plan'It (PreToolUse) — FAIL-CLOSED sur les trois familles sensibles.

Lit reference/outils-sensibles.json (versionné, relevé du serveur) et impose
ask sur :
- les 10 outils DESTRUCTIFS du serveur (suppriment, créent/retouchent une
  routine réelle, lancent une exécution facturée, retirent un connecteur) ;
- les outils PAYANTS (vidéo, collectes KPI) — la dépense s'annonce, jamais
  ne se décide seule ;
- les outils qui TRANCHENT à la place de l'utilisateur (alerte, refus de
  proposition) — la décision lui appartient.

Les champs de confirmation posés par le modèle (confirm, confirmed,
approved…) ne valent JAMAIS confirmation humaine : ils sont ignorés.
Table illisible = fail-closed : ask sur toute écriture Plan'It en forme
d'écriture. Aucun appel réseau. Testé par scripts/tester-skills.py.
"""
import json
import os
import re
import sys

RACINE_PLUGIN = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
TABLE = os.path.join(RACINE_PLUGIN, "reference", "outils-sensibles.json")
RX_MCP = re.compile(r"^mcp__[Pp]lan[_-]?[Ii]t__([A-Za-z0-9_]+)$")
RX_ECRITURE = re.compile(
    r"^(create|update|delete|add|remove|apply|accept|decline|pause|resume|"
    r"run|subscribe|unsubscribe|attach|detach|decide|compose|refresh|open)_")

RAISONS = {
    "destructifs": ("effet réel et irréversible (liste des 10 destructifs du "
                    "serveur) — confirmation humaine obligatoire."),
    "payants": ("consomme des crédits — le coût s'annonce avant "
                "(estimate_routine_cost / list_kpi_catalog / calcul vidéo) "
                "et l'utilisateur accepte."),
    "tranchent": ("tranche une décision qui appartient à l'utilisateur "
                  "(alerte, refus de proposition) — son accord explicite "
                  "d'abord."),
}


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
    outil = m.group(1)
    try:
        with open(TABLE, encoding="utf-8") as f:
            table = json.load(f)
    except Exception:  # noqa: BLE001
        table = None
    if table is None:
        if RX_ECRITURE.match(outil):
            ask("garde-planit : reference/outils-sensibles.json illisible — "
                f"fail-closed, « {outil} » attend une confirmation humaine.")
        sys.exit(0)
    for famille in ("destructifs", "payants", "tranchent"):
        if outil in set(table.get(famille, [])):
            ask(f"garde-planit : « {outil} » — {RAISONS[famille]}")
    sys.exit(0)


if __name__ == "__main__":
    main()
