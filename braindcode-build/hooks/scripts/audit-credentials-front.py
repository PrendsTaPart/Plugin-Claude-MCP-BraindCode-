#!/usr/bin/env python3
"""Hook PostToolUse — audit des credentials côté navigateur.

Sur get_diff et read_file (Lovable), scanne la RÉPONSE et signale par un
rappel bloquant (additionalContext) :
- toute variable d'environnement exposée au navigateur (VITE_*,
  NEXT_PUBLIC_*, REACT_APP_*, EXPO_PUBLIC_*) qui porte une clé, un secret
  ou un jeton ;
- tout appel MCP depuis le front (URL /mcp ou /api/mcp dans du code
  client) ;
- toute URL MCP accompagnée d'un jeton (token=, Authorization inline).

Critère maison n° 3 : AUCUN credential MCP n'atteint le navigateur — le
correctif passe par une edge function. Silencieux quand rien n'est trouvé ;
jamais bloquant techniquement (PostToolUse), mais le rappel exige le
correctif avant de continuer.
"""
import json
import re
import sys

RX_OUTIL = re.compile(
    r"^mcp__(?:plugin_[\w-]+_)?[Ll]ovable__(get_diff|read_file)$")
MOTIFS = [
    ("variable front porteuse de clé", re.compile(
        r"\b(?:VITE|NEXT_PUBLIC|REACT_APP|EXPO_PUBLIC)_[A-Z0-9_]*"
        r"(?:KEY|SECRET|TOKEN|PASSWORD)[A-Z0-9_]*\b")),
    ("appel MCP depuis le front", re.compile(
        r"(?:fetch|axios|XMLHttpRequest)[^\n]{0,120}/(?:api/)?mcp\b", re.I)),
    ("URL MCP avec jeton", re.compile(
        r"/(?:api/)?mcp[^\s\"']{0,80}(?:token=|Authorization|Bearer)", re.I)),
    ("service_role dans le code livré", re.compile(r"service_role", re.I)),
]


def _texte(obj):
    try:
        return json.dumps(obj, ensure_ascii=False)
    except Exception:  # noqa: BLE001
        return str(obj)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    if not RX_OUTIL.match(data.get("tool_name", "")):
        sys.exit(0)
    texte = _texte(data.get("tool_response"))
    trouves = [nom for nom, rx in MOTIFS if rx.search(texte)]
    if not trouves:
        sys.exit(0)
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext":
            "[audit-credentials-front] RAPPEL BLOQUANT — motifs détectés "
            f"dans le code relu : {', '.join(trouves)}. Critère Build n° 3 : "
            "aucun credential MCP n'atteint le navigateur. Corriger via une "
            "edge function (appel côté serveur, scope verrouillé, journaux "
            "masqués) AVANT de clôturer l'étape ou de déployer."}}))
    sys.exit(0)


if __name__ == "__main__":
    main()
