---
name: video-virale-plats
description: Utiliser quand l'utilisateur veut une vidéo d'un plat ou de sa carte — « fais une vidéo virale de mon burger », « anime la photo du plat du jour », « une story vidéo pour le menu de la semaine », « ce plat mérite un reel ». Transforme les VRAIES photos de plats en vidéos courtes via Higgsfield, format réseaux, coûts en crédits confirmés avant.
---

# Vidéo virale de plats (photos réelles → Higgsfield → réseaux)

Le trio : FoodEatUp fournit la raison (plat star, plat du jour, surstock à
écouler) et la marge, Higgsfield anime la vraie photo, RapidoCMS porte la
charte et le brouillon de publication.

## 1. La matière première : de VRAIES photos

- Chercher les photos existantes du plat : assets de marque RapidoCMS
  (`list_all_files` → `file_url` publiques) ; sinon demander une photo à
  l'utilisateur (smartphone suffit) et l'héberger via `upload_file_tool`
  (URL http(s) exigée par le hook rapidocms).
- **Règle d'honnêteté : pas de photo → pas de vidéo du plat.** On peut faire
  une vidéo d'ambiance ou typographique, mais on ne génère jamais un faux
  plat photoréaliste présenté comme le vrai.
- Côté Higgsfield, importer la photo par URL (`media_import_url`) avant de
  l'animer.

## 2. Fabrication (coût confirmé AVANT chaque étape payante)

1. `models_explore` (action recommend) avec l'objectif : « animer une photo
   de plat en vidéo courte appétissante » — ne pas deviner le modèle.
2. `generate_video` en image-to-video depuis la photo importée : mouvement
   court (vapeur, zoom lent, nappage), 6-10 s — c'est le format qui retient.
3. `reframe` pour décliner : 9:16 (Reels/TikTok/story), 1:1 (feed), 16:9 si
   besoin. `upscale_video` seulement si la plateforme l'exige.
4. `virality_predictor` sur le résultat : hook des 2 premières secondes,
   rétention, recommandations — régénérer UNE fois si le verdict est faible,
   puis montrer tel quel (pas de boucle infinie de crédits).
5. Habillage aux couleurs de la maison (texte, logo depuis la charte
   `get_brand`) — le gate charte du skill `fabrique-contenu-iris` s'applique.

Chaque étape payante (génération, upscale, reframe) est annoncée avec son coût
en crédits et attend l'accord — le garde-fou du plugin refuse toute génération
vidéo sans coût confirmé.

## 3. Publication (jamais automatique)

- La vidéo finit en **brouillon** RapidoCMS (`upload_file_tool` puis
  `create_draft_tool`) avec sa copy et SA RAISON (« Parce que le burger
  signature dégage X % de marge et sort Y fois par semaine »).
- La planification passe par le skill `calendrier-iris` : validation humaine,
  garde-fou sur la planification.
- La publication TikTok directe côté Higgsfield (`tiktok_publish`) est
  également derrière confirmation — préférer le circuit brouillon CMS.

## Ce que ce skill NE fait PAS

- Les campagnes vidéo lourdes multi-scènes (pubs, explainers, UGC) → plugin
  rapido-higgsfield (skills `usine-video-marketing`, `videos-explicatives`) ;
  l'analyse virale approfondie → son skill `analyse-video-virale`.
- Le montage local sans crédits (concat, sous-titres) → plugin rapido-video.
- Décider quand publier → skill `calendrier-iris`.
