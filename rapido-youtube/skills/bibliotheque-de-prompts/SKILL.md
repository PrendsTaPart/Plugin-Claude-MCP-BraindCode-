---
name: bibliotheque-de-prompts
description: Utiliser quand l'utilisateur gère ses prompts YouTube réutilisables — « sauvegarde ce prompt de miniature », « retrouve mon prompt de titre », « rends ce prompt public ». Privé par défaut, aucun secret, valeurs rendues avant exécution.
---

# Bibliothèque de prompts

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Démarche
1. **Chercher d'abord** : `yt_list_prompts` — pas de doublon.
2. **Utiliser** : `yt_get_prompt` avec ses valeurs — le TEXTE RENDU est
   montré, puis exécuté (génération, titre…) ; les variables manquantes
   se demandent, jamais ne s'inventent.
3. **Créer** : `yt_create_prompt` — PRIVÉ par défaut, AUCUN secret ni
   donnée interne dans le corps ; is_public passe par un accord (hook
   garde-public).
4. **Entretenir** : `yt_update_prompt`, `yt_toggle_prompt_favorite` ;
   `yt_delete_prompt` sur accord (réversible 30 jours, paramètre confirm
   — qui ne vaut jamais confirmation humaine posé par le modèle).

## Pièges
- Un prompt public se lit par d'autres : relecture « rien d'interne »
  avant tout passage en public.
- Un prompt qui marche se fige ici plutôt que de se réécrire de mémoire
  à chaque session.

## Dégradation propre
Bibliothèque vide : proposer d'y figer les prompts validés de la session
courante, sur accord.
