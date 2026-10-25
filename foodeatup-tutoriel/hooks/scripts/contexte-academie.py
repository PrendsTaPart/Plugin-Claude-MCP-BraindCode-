#!/usr/bin/env python3
"""Contexte de session (SessionStart) du plugin foodeatup-tutoriel.

Au démarrage d'une session, rappelle en une poignée de lignes le contrat du
plugin. Sur tout autre événement (payload portant un tool_name, comme dans
les tests CI), reste silencieux et n'interfère jamais (exit 0).
Aucun appel réseau.
"""
import json
import sys

CONTEXTE = """Plugin foodeatup-tutoriel actif — contrat de session :
- Le serveur « FoodEatUp tutoriel » ENSEIGNE (public, lecture seule, 36
  outils vérifiés) : il n'agit sur aucun compte.
- Agir pour de vrai = connecteur produit https://foodeatup.com/api/mcp,
  installé par l'utilisateur ; ce plugin ne l'appelle jamais.
- Méthode : diagnostic_demarrage d'abord (secteur avant métier), une leçon à
  la fois, vignette en bloc image, quiz puis exercice après chaque leçon,
  code de reprise en fin de séance.
- Rien d'inventé : sujet non couvert → le dire (audit_formation) ; chiffre →
  outil + date de vérification ; lien → réponse du serveur ; convive → pas
  de lien vidéo (non tournées)."""


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        payload = {}
    if payload.get("hook_event_name") == "SessionStart" \
            and "tool_name" not in payload:
        print(CONTEXTE)
    sys.exit(0)


if __name__ == "__main__":
    main()
