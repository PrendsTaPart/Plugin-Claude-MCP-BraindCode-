#!/usr/bin/env python3
"""Hook PreToolUse — l'image des personnes est verrouillée.

- yt_swap_face, et yt_generate_thumbnail avec face_model_id :
  deny si AUCUN yt_list_face_models n'a été lu dans la session (journal),
  deny si le face_model_id demandé est ABSENT de la liste relevée ;
  ask sinon (famille « image des personnes » : l'humain confirme l'usage
  de SON modèle de visage sur CETTE miniature).
Fail-closed par construction : sans liste, rien ne passe. Un visage
d'autrui n'a pas de chemin ici. Clé de test CI : session_test.
"""
import json
import os
import re
import sys

ETAT = os.path.join(".claude", "state", "youtube-session.json")
RX = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Rr]apido[-_][Yy]ou[Tt]ube__"
                r"(yt_swap_face|yt_generate_thumbnail)$")


def deny(raison):
    print(f"[garde-visage] REFUS : {raison}", file=sys.stderr)
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
    face_id = entree.get("face_model_id")
    if outil == "yt_generate_thumbnail" and not face_id:
        sys.exit(0)  # génération sans visage : garde-credits s'en occupe
    etat = data.get("session_test")
    if not isinstance(etat, dict):
        try:
            etat = json.load(open(ETAT, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            etat = {}
    modeles = etat.get("face_models")
    if not isinstance(modeles, list) or not modeles:
        deny(f"{outil} sans relevé des modèles de visage dans la session : "
             "lire yt_list_face_models d'abord — seuls les modèles de "
             "visage de l'utilisateur sont utilisables, jamais un visage "
             "d'autrui.")
    if face_id and str(face_id) not in [str(x) for x in modeles]:
        deny(f"face_model_id « {face_id} » ABSENT des modèles relevés par "
             "yt_list_face_models dans cette session — aucun visage hors "
             "des modèles de l'utilisateur.")
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason":
            f"[garde-visage] {outil} avec le modèle de visage "
            f"« {face_id or '?'} » (relevé dans la session) : confirmer "
            "l'usage de ce visage sur CETTE miniature."}}))
    sys.exit(0)


if __name__ == "__main__":
    main()
