#!/usr/bin/env python3
"""Anti-lien-inventé (PreToolUse sur les outils Académie).

Toute URL et tout slug passés au serveur doivent ressembler à ce que le
serveur sert réellement :

- un paramètre « slug » (slug, moduleSlug, metierSlug, secteurSlug,
  categorieSlug, journeeSlug, et les listes slugsVus/dejaVus) doit être un
  slug kebab-case — pas une URL, pas une phrase, pas de majuscule : un slug
  ne s'invente pas, il vient d'une réponse précédente → deny sinon ;
- toute URL présente dans un argument doit appartenir aux domaines servis
  par l'Académie (tutoriel.foodeatup.com, foodeatup.com, youtube.com,
  youtu.be, rapido-software.s3.eu-west-3.amazonaws.com) → deny sinon.

deny = exit 2 + stderr (bloquant). Aucun appel réseau. Testé en CI.
"""
import json
import re
import sys

RX_SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
RX_URL = re.compile(r"https?://([^/\s\"']+)", re.I)
DOMAINES = ("tutoriel.foodeatup.com", "foodeatup.com", "www.youtube.com",
            "youtube.com", "youtu.be",
            "rapido-software.s3.eu-west-3.amazonaws.com")
CLES_SLUG = re.compile(r"slug", re.I)


def deny(raison):
    print(f"anti-lien-invente : {raison}", file=sys.stderr)
    sys.exit(2)


def verifier(cle, valeur):
    if isinstance(valeur, str):
        for dom in RX_URL.findall(valeur):
            d = dom.lower().split(":")[0]
            if d not in DOMAINES and not d.endswith(
                    (".foodeatup.com", ".youtube.com")):
                deny(f"URL hors domaines de l'Académie dans « {cle} » "
                     f"({d}) — un lien vient d'une réponse du serveur, "
                     "jamais de mémoire.")
        if CLES_SLUG.search(cle) and not RX_SLUG.match(valeur):
            deny(f"« {cle} » n'est pas un slug (reçu : {valeur[:60]!r}) — "
                 "un slug est en kebab-case et vient d'une réponse du "
                 "serveur (rechercher_tutoriels, lister_tutoriels…).")
    elif isinstance(valeur, list):
        for v in valeur:
            verifier(cle, v)
    elif isinstance(valeur, dict):
        for k, v in valeur.items():
            verifier(k, v)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    entree = payload.get("tool_input", {})
    if isinstance(entree, dict):
        for cle, valeur in entree.items():
            verifier(cle, valeur)
    sys.exit(0)


if __name__ == "__main__":
    main()
