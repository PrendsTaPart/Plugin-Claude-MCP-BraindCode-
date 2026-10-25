---
name: videos
description: Utiliser quand l'utilisateur prépare ses vidéos Prospector Hub — « planifie la vidéo de la semaine », « renseigne les prompts des séquences », « la vidéo est montée, mets les liens ». Fiches vidéo complètes ; la génération se délègue aux plugins vidéo.
---

# Vidéos (fiches, prompts, liens)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Démarche
1. **Lire** : `list_video_posts` (période, statut) — avec leurs prompts de
   séquence 1 et 2.
2. **Créer la fiche** : `add_video_post` (title, description,
   prompt_sequence_1, prompt_sequence_2, prompt_montage, script_voix_off,
   scheduled_at, status brouillon) — les prompts se travaillent avec les
   plugins dédiés quand ils sont installés : génération via
   rapido-higgsfield ou rapido-video, voix off via rapido-elevenlabs.
   Ce skill TIENT LA FICHE, il ne génère pas.
3. **Après production** : `update_video_post` — renseigner `video_url` et
   `thumbnail_url` RÉELS (fournis par l'utilisateur ou l'outil de
   production ; jamais d'URL inventée).
4. **Publier** : statut « publie » sur accord (hook garde-publication).
5. **Supprimer** : `delete_video_post` sur confirmation (définitif).

## Pièges
- Une fiche sans video_url n'est pas « prête » : le statut le reflète.
- Le coût de génération (crédits Higgsfield, etc.) s'annonce côté plugin
  de génération, AVANT de lancer — pas après.

## Dégradation propre
Plugins vidéo absents : livrer la fiche complète (prompts, script) prête à
produire, et le dire.
