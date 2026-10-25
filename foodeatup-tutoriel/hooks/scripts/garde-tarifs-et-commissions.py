#!/usr/bin/env python3
"""Garde tarifs & commissions (double événement).

1. PreToolUse sur Write|Edit : écrire un montant en euros à propos de
   FoodEatUp (pack, abonnement, commission, essai) sans date de vérification
   (« vérifié le … » / verifieLe) → ask. La règle du serveur : jamais un
   montant absent de la réponse de `tarifs_et_essai` ou de
   `reseau_partenaires_foodeatup`, et toujours la date de vérification.

2. UserPromptSubmit : une question de prix/commission → injection d'un
   rappel de la règle en contexte (additionalContext), sans jamais bloquer
   le prompt.

Aucun appel réseau. Comportement Write/Edit testé par scripts/tester-skills.py.
"""
import json
import re
import sys

RX_MONTANT = re.compile(r"\d[\d\s]*(?:,\d+)?\s*(?:€|euros?\b|EUR\b)", re.I)
RX_SUJET = re.compile(
    r"foodeatup|académie|academie|stockvision|premiers\s+pas|commission|"
    r"abonnement|pack", re.I)
RX_DATE_VERIF = re.compile(r"v[ée]rifi[ée]e?s?\s+le|verifieLe|date de "
                           r"v[ée]rification", re.I)
RX_PROMPT_PRIX = re.compile(
    r"\bprix\b|\btarif|combien\s+(ça\s+)?co[ûu]te|commission|essai\s+gratuit|"
    r"c'est\s+gratuit|abonnement", re.I)

REGLE = ("Règle du plugin foodeatup-tutoriel : tout montant (tarif, essai, "
         "commission) vient d'un appel du jour à tarifs_et_essai ou "
         "reseau_partenaires_foodeatup, cité avec sa date de vérification "
         "(verifieLe). Jamais de montant absent de la réponse du serveur ; "
         "pour le reste, renvoyer vers la page tarifs.")


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": raison,
    }}))
    sys.exit(0)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)

    if payload.get("hook_event_name") == "UserPromptSubmit" \
            and "tool_name" not in payload:
        if RX_PROMPT_PRIX.search(payload.get("prompt", "") or ""):
            print(json.dumps({"hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": REGLE,
            }}, ensure_ascii=False))
        sys.exit(0)

    if payload.get("tool_name") in ("Write", "Edit"):
        entree = payload.get("tool_input", {}) or {}
        texte = " ".join(str(entree.get(k, "")) for k in
                         ("content", "new_string", "new_str"))
        if RX_MONTANT.search(texte) and RX_SUJET.search(texte) \
                and not RX_DATE_VERIF.search(texte):
            ask("garde-tarifs-et-commissions : montant en euros à propos de "
                "FoodEatUp sans date de vérification. " + REGLE)
    sys.exit(0)


if __name__ == "__main__":
    main()
