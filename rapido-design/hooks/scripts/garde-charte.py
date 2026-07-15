#!/usr/bin/env python3
"""garde-charte — garde-fou déterministe du plugin rapido-design.

Toute **création visuelle** (génération d'un design/fichier Figma, création d'un
projet Lovable) passe par une CONFIRMATION rappelant : la **charte** doit être
chargée d'abord (`get_brand` + charte KB), et la maquette **consomme les tokens**
(jamais de valeur en dur). Le fil rouge des tokens (CMS → Figma → Lovable) ne doit
jamais diverger.

Ne bloque jamais en dur (aucun deny). Contrat : ask = exit 0 + JSON stdout ;
allow = exit 0 sans stdout. Aucune I/O réseau, aucun secret.
"""
import json
import re
import sys

RX_VISUEL = re.compile(
    r"(Figma__(generate_figma_design|create_new_file|use_figma)|"
    r"Lovable__create_project)$",
    re.IGNORECASE,
)


def demander(raison):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": raison,
        }
    }))
    sys.exit(0)


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (ValueError, TypeError):
        sys.exit(0)
    outil = data.get("tool_name") or ""
    if RX_VISUEL.search(outil):
        demander(
            "Création visuelle : la charte a-t-elle été chargée d'abord (get_brand + "
            "charte KB) ? La maquette doit CONSOMMER les tokens (couleurs/typo), jamais "
            "de valeur en dur — fil rouge CMS → Figma → Lovable sans divergence."
        )
    sys.exit(0)


if __name__ == "__main__":
    main()
