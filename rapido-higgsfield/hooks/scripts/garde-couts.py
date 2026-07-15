#!/usr/bin/env python3
"""PreToolUse — garde-coûts Higgsfield (tout est payant en crédits).

Bloque une génération/rendu/déploiement Higgsfield payant TANT QUE le coût n'a pas
été confirmé dans le tour. La confirmation est matérialisée par un marqueur dans
`tool_input` : `get_cost: true` (préflight = devis, aucune facturation → autorisé)
ou `cout_confirme: true` (le coût a été chiffré et présenté, l'utilisateur a
validé). Sinon → refus pédagogique.

Contrat hook : deny = exit 2 + stderr ; allow = exit 0 sans sortie.
Stdlib uniquement, < 1 s, sans réseau.
"""
import json
import os
import sys

PAYANT = ("generate_", "dubbing", "voice_change", "upscale_", "shorts_studio_create",
          "personal_clipper_create", "explainer_video", "outpaint_image",
          "motion_control", "render_video", "deploy_website", "deploy_game")


def est_payant(tool):
    return any(k in tool for k in PAYANT)


def plafond_kb():
    """Lecture optionnelle du plafond dans ./rapido-kb/budget-media.md (sinon None)."""
    chemin = os.path.join("rapido-kb", "budget-media.md")
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                if "plafond" in ligne.lower():
                    return ligne.strip()
    except OSError:
        return None
    return None


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool = data.get("tool_name", "") or ""
    ti = data.get("tool_input") or {}

    if not est_payant(tool):
        return 0  # allow — non payant
    if ti.get("get_cost"):
        return 0  # allow — préflight devis (pas de facturation)
    if ti.get("cout_confirme") or ti.get("cost_confirmed"):
        return 0  # allow — coût chiffré et validé

    plafond = plafond_kb()
    sys.stderr.write(
        "💳 Génération payante Higgsfield bloquée : coût NON confirmé dans ce tour.\n"
        "→ Chiffrer d'abord (préflight `get_cost: true`, ou skill `gouvernance-credits`), "
        "présenter le coût en crédits, puis relancer l'appel avec le marqueur "
        "`cout_confirme: true`.\n"
        + (f"Plafond média : {plafond}\n" if plafond else
           "Astuce : définir un plafond dans rapido-kb/budget-media.md.\n")
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
