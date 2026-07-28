#!/usr/bin/env python3
"""Garde-fou PreToolUse du plugin foodeatup-iris. Stdlib uniquement, aucun réseau.

Deux principes du cahier des charges Iris, appliqués hors du flux du modèle :

1. JAMAIS de publication automatique : toute planification/publication passe
   par une confirmation humaine (ask), sans réglage pour la contourner.
2. Les crédits s'annoncent AVANT : une génération vidéo sans coût confirmé
   par l'utilisateur (`cout_confirme: true` posé APRÈS son accord explicite)
   est refusée avec un message pédagogique (deny).
"""
import json
import sys

PUBLICATION = {
    "schedule_draft_tool": "planifie une publication réelle sur les réseaux",
    "cancel_schedules_post": "annule une publication planifiée",
    "tiktok_publish": "publie immédiatement sur TikTok",
    "add_post_campagne": "ajoute un post à une campagne active",
}
GENERATION_PAYANTE = {
    "generate_video": "génération vidéo Higgsfield",
    "upscale_video": "upscale vidéo Higgsfield",
    "motion_control": "animation Higgsfield",
    "dubbing": "doublage Higgsfield",
}


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    tool_name = str(data.get("tool_name", ""))
    parts = tool_name.split("__")
    if len(parts) < 3 or parts[0] != "mcp":
        sys.exit(0)
    outil = "__".join(parts[2:])
    tool_input = data.get("tool_input") or {}

    if outil in PUBLICATION:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": (
                    f"« {outil} » {PUBLICATION[outil]}. Principe Iris : rien ne "
                    "sort sans validation humaine — l'image publique d'un "
                    "restaurant ne se délègue pas à une machine "
                    "(plugin foodeatup-iris)."
                ),
            }
        }, ensure_ascii=False))
        sys.exit(0)

    if outil in GENERATION_PAYANTE:
        if isinstance(tool_input, dict) and tool_input.get("cout_confirme") is True:
            sys.exit(0)  # coût annoncé et accepté par l'utilisateur
        sys.stderr.write(
            f"Refus (garde-iris) : {GENERATION_PAYANTE[outil]} sans coût "
            "confirmé. Annoncer le coût en crédits à l'utilisateur, obtenir son "
            "accord, PUIS rappeler l'outil avec cout_confirme:true. Les crédits "
            "s'annoncent avant, jamais après.")
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
