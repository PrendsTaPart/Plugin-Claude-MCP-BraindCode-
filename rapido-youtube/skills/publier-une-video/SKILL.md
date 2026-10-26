---
name: publier-une-video
description: Utiliser quand l'utilisateur publie une vidéo YouTube — « publie cette vidéo », « envoie le fichier sur la chaîne », « mets-la en ligne en non répertorié ». Quota lu, chaîne explicite, SEO noté, miniature analysée, privacy prudente, idempotence - dans cet ordre.
---

# Publier une vidéo

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (loi n° 3) et
  `${CLAUDE_PLUGIN_ROOT}/reference/quota-et-credits.md`.

## Démarche
1. **Le quota** : `yt_get_quota_status` — un envoi complet doit tenir
   dans le DISPONIBLE RÉEL (scripts/quota.py) ; will_fail = on s'arrête
   (le hook garde-quota refuse de toute façon).
2. **La chaîne** : channel_id EXPLICITE, nom annoncé (hook garde-chaine).
3. **Le contenu** : SEO noté (`yt_score_video_seo`, skill
   `titre-description-seo`) et miniature analysée (skill
   `atelier-miniatures`) AVANT l'envoi.
4. **La privacy** : private ou unlisted par défaut — PUBLIC uniquement
   sur accord explicite (hook garde-public).
5. **Envoyer** : `yt_publish_video` avec client_request_id (idempotence —
   jamais de double envoi sur erreur réseau) ; GROS fichier :
   `yt_create_upload_url` puis `yt_register_uploaded_video`.
6. **Vérifier** : `yt_get_video_status`, puis
   `yt_attach_thumbnail_to_video` (50 unités avec push_to_youtube —
   annoncées).

## Pièges
- Publier puis attacher la miniature = 1 envoi + 50 unités : les compter
  ENSEMBLE dans l'estimation.
- Une vidéo déjà sur YouTube (upload manuel) s'enregistre par
  `yt_register_uploaded_video`, elle ne se re-publie pas.

## Dégradation propre
Échec d'envoi : lire l'erreur réelle (`yt_get_video_status`), passer par
le skill `reprise-des-echecs` — jamais de ré-émission aveugle.
