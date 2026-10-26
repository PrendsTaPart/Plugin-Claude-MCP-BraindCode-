---
name: shorts-depuis-une-video-longue
description: Utiliser quand l'utilisateur tire des Shorts d'une vidéo longue — « découpe cette vidéo en Shorts », « quels clips dans ce tuto ? », « publie les 3 meilleurs clips ». Détection asynchrone suivie, choix humain, rendu dans l'application avant publication.
---

# Shorts depuis une vidéo longue

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (loi n° 5).

## Démarche
1. **Détecter** : `yt_create_clips_from_video` — tourne en
   ARRIÈRE-PLAN ; suivre avec `yt_get_clip` jusqu'au statut final.
2. **Choisir** : les clips détectés sont montrés (widget clips-detectes :
   bornes, accroche, score estimé) — le score viral est une ESTIMATION
   ÉDITORIALE, l'HUMAIN choisit.
3. **Rendre** : le rendu du clip se fait DANS L'APPLICATION — le dire,
   et vérifier le statut rendu via `yt_get_clip` avant toute suite.
4. **Publier** : `yt_publish_clip` (un envoi complet — quota lu avant,
   chaîne explicite), miniature verticale par
   `yt_generate_vertical_variant` si besoin.
5. **Distribuer** : `yt_schedule_cross_post` via le skill
   `distribution-multi-plateformes` (comptes connectés requis).
6. **Montage fin** : recadrage, sous-titres, habillage → délégué à
   rapido-video (ffmpeg/Whisper) quand il est installé.

## Pièges
- Publier un clip non rendu échoue : yt_get_clip fait foi, pas
  l'impatience.
- 5 Shorts = 5 envois complets : l'estimation de campagne les compte
  tous.

## Dégradation propre
Détection vide ou médiocre : le dire — proposer un découpage manuel via
rapido-video plutôt que publier des clips faibles.
