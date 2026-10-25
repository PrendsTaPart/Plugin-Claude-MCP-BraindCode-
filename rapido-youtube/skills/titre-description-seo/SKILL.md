---
name: titre-description-seo
description: Utiliser quand l'utilisateur travaille titre, description ou SEO d'une vidéo — « propose des titres », « écris la description chaptée », « note le SEO avant publication ». Titres en estimations assumées, choix humain, chapitres depuis la transcription, score avant chaque publication.
---

# Titre, description, SEO

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (loi n° 6 : les
  scores de titres sont des ESTIMATIONS).

## Démarche
1. **Titres** : `yt_generate_titles` avec le mot-clé retenu — les scores
   sont des estimations, présentées comme telles ; L'HUMAIN choisit.
2. **Description** : `yt_generate_description` sur le titre choisi ; les
   CHAPITRES viennent de la transcription quand elle existe
   (`python3 ${CLAUDE_PLUGIN_ROOT}/scripts/chapitres.py transcription.txt`
   — 0:00 en premier, ≥ 3, ≥ 10 s), sinon pas de chapitres artificiels.
3. **Checklist locale** :
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/seo_checklist.py titre.txt
   description.txt mot-cle` — gratuit, mécanique.
4. **Score serveur** : `yt_score_video_seo` AVANT chaque publication —
   les corrections suggérées s'appliquent, puis on re-note.
5. **Transmettre** : titre + description validés vers
   `publier-une-video` ; le mot-clé vers l'atelier miniatures.

## Pièges
- Un titre > 70 caractères se coupe à l'affichage : le dire même si le
  serveur accepte jusqu'à 100.
- Jamais de lien signé temporaire (aperçu de miniature) dans une
  description : la checklist le refuse.

## Dégradation propre
Pas de transcription : description sans chapitres, en le disant — le
montage/transcription se délègue à rapido-video.
