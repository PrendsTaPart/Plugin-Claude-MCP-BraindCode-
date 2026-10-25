#!/usr/bin/env python3
"""Hook PreToolUse — les crédits de l'atelier visuel sous contrôle.

Sur les outils payants (reference/outils-sensibles.json, famille
cout_credits) :
- ask quand `variations` > 1 (une génération à la fois, l'analyse est
  gratuite) ;
- ask quand le cumul estimé de la session dépasse le seuil de
  ./rapido-kb/youtube.md (bloc machine, seuil_credits_session) — sans KB,
  seuil PRUDENT de 25 crédits. Le cumul vient du journal de session
  (credits_estimes, alimenté en PostToolUse).
Fail-closed : table des outils sensibles illisible = ask sur tout outil
matché. Clé de test réservée au harnais CI : session_test, kb_test.
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(os.path.dirname(ICI))
ETAT = os.path.join(".claude", "state", "youtube-session.json")
KB = os.path.join("rapido-kb", "youtube.md")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"(yt_[A-Za-z0-9_]+)$")
SEUIL_DEFAUT = 25


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": f"[garde-credits] {raison}"}}))
    sys.exit(0)


def seuil_kb(data):
    kb = data.get("kb_test")
    if isinstance(kb, dict):
        return kb.get("seuil_credits_session", SEUIL_DEFAUT)
    try:
        texte = open(KB, encoding="utf-8").read()
        bloc = re.search(r"```json\s*(\{.*?\})\s*```", texte, re.S).group(1)
        return json.loads(bloc).get("seuil_credits_session", SEUIL_DEFAUT)
    except Exception:  # noqa: BLE001
        return SEUIL_DEFAUT


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    m = RX.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil, entree = m.group(1), data.get("tool_input") or {}
    try:
        table = json.load(open(os.path.join(
            PLUGIN, "reference", "outils-sensibles.json"), encoding="utf-8"))
        payants = set(table["cout_credits"]["outils"])
    except Exception:  # noqa: BLE001
        ask("table des outils sensibles illisible (fail-closed) — annoncer "
            "le coût en crédits et confirmer cette génération.")
    if outil not in payants:
        sys.exit(0)
    variations = entree.get("variations")
    if isinstance(variations, (int, float)) and variations > 1:
        ask(f"{outil} avec variations={variations} : chaque variation coûte "
            "des crédits (barème de yt_get_credit_balance) et l'analyse est "
            "gratuite — confirmer ce nombre, ou générer une variation puis "
            "analyser.")
    etat = data.get("session_test")
    if not isinstance(etat, dict):
        try:
            etat = json.load(open(ETAT, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            etat = {}
    cumul = etat.get("credits_estimes", 0)
    seuil = seuil_kb(data)
    if isinstance(cumul, (int, float)) and cumul >= seuil:
        ask(f"cumul estimé de la session : {cumul} crédit(s) ≥ seuil "
            f"{seuil} (./rapido-kb/youtube.md, défaut {SEUIL_DEFAUT}). "
            f"Confirmer {outil} en annonçant son coût au barème.")
    sys.exit(0)


if __name__ == "__main__":
    main()
