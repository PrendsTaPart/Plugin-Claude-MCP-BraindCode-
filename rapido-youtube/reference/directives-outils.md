# Directives d'usage des 86 outils officiels du serveur Rapido YouTube

Relevé du 2026-10-25 depuis le manifeste MCP publié du projet
(« youtube-publisher-bot » 0.4.0). Point d'entrée :
https://youtube.rapidocms.com/mcp — ressource OAuth (Supabase),
authentification au premier appel, aucun jeton dans le dépôt.

## Règle n° 1 — les noms d'outils

Chaque outil existe en DEUX exemplaires : le nom officiel `yt_…` et un
alias déprécié sans préfixe, **retiré le 2026-12-31**. Ce plugin n'utilise
QUE les noms `yt_` : la CI fait échouer toute citation d'un alias
(docs/inventaires/rapido-youtube-alias-deprecies.txt) et le hook
alias-deprecies refuse leur appel en donnant le nom à utiliser.

## Les lois du serveur (vérifiées, à respecter dans chaque skill)

1. **La cible par défaut** : sans channel_id, les publications partent
   vers la chaîne ACTIVE, sinon la FAVORITE ; `yt_get_channel_status`
   signale toute divergence entre les deux. Règle du plugin : toute
   écriture passe un channel_id EXPLICITE et annonce le nom de la chaîne.
2. **Le quota se lit avant d'agir** : `yt_get_quota_status` donne le quota
   du jour, la part réservée aux publications planifiées sous 24 h, le
   disponible RÉEL et un risque (ok / tight / will_fail). Le hook
   garde-quota refuse tout envoi sans lecture récente ou sur will_fail.
3. **Publier prudent** : privacy `private` par défaut ;
   `yt_schedule_video` en mode upload_now_publish_at est le plus fiable ;
   `client_request_id` rend l'opération idempotente (jamais de double
   envoi) ; gros fichier → `yt_create_upload_url` puis
   `yt_register_uploaded_video` ; `yt_bulk_schedule` accepte 10 vidéos au
   plus.
4. **Les créneaux viennent de l'historique réel**
   (`yt_suggest_publishing_slots`, `yt_get_slot_scores`,
   `yt_set_autopilot`) : sans historique, l'outil le dit — rien n'est
   inventé à sa place.
5. **Les clips sont asynchrones** : `yt_create_clips_from_video` tourne en
   arrière-plan, suivi par `yt_get_clip` ; un clip doit être RENDU dans
   l'application avant `yt_publish_clip` ; son score viral est une
   estimation éditoriale.
6. **Les scores de titres** (`yt_generate_titles`) sont des estimations,
   jamais des mesures.
7. **Tests A/B honnêtes** : `yt_start_ab_test` ne déclare un gagnant
   qu'au-delà de 95 % de confiance ET 100 impressions par phase ; sinon le
   test est non concluant et la miniature A est restaurée. Une donnée
   absente n'est jamais comptée comme zéro.
8. **Analytics coupée = reconnexion** : `yt_compare_videos` et
   `yt_get_video_momentum` renvoient une erreur explicite si l'API
   Analytics est coupée — la réponse est de reconnecter la chaîne, pas de
   réessayer en boucle.
9. **Le lot s'aperçoit d'abord** : `yt_find_replace_descriptions` toujours
   en dry_run d'abord ; `yt_create_bulk_job` toujours en preview_only
   d'abord (le hook garde-lot le force).
10. **Reprise sous conditions** : `yt_retry_videos` refuse une vidéo
    bloquée par uploadLimitExceeded depuis moins de 24 h et donne l'heure
    de réarmement — on la respecte.
11. **Distribution = comptes connectés** : `yt_schedule_cross_post` exige
    des comptes vérifiés par `yt_list_connected_accounts` (au relevé du
    2026-10-25 : AUCUN compte connecté).

## Les chaînes de travail (outils dans l'ordre)

| Chaîne | Enchaînement |
|---|---|
| Veille → idée | `yt_track_channel` → `yt_list_tracked_channels` → `yt_find_outliers` → `yt_analyze_outlier_pattern` → `yt_get_daily_ideas` |
| Mots-clés → titre → description | `yt_research_keywords` (with_competition = quota, sur accord) → `yt_generate_titles` (choix humain) → `yt_generate_description` → `yt_score_video_seo` |
| Miniature | `yt_list_brand_kits` / `yt_list_styles` / `yt_list_face_models` → `yt_generate_thumbnail` (crédits annoncés) → `yt_analyze_thumbnail` (gratuit) → `yt_edit_thumbnail` / `yt_inpaint_thumbnail` / `yt_auto_optimize_thumbnail` (2 crédits) / `yt_apply_style` / `yt_apply_template` / `yt_swap_face` → `yt_compare_thumbnails` → `yt_attach_thumbnail_to_video` (50 unités avec push_to_youtube) |
| Publication | `yt_get_quota_status` → `yt_score_video_seo` → `yt_publish_video` OU `yt_create_upload_url` + `yt_register_uploaded_video` → `yt_get_video_status` → `yt_attach_thumbnail_to_video` |
| Planification | `yt_suggest_publishing_slots` / `yt_get_slot_scores` / `yt_get_publishing_slots` / `yt_suggest_slots` → `yt_list_schedule_slots` → `yt_set_schedule_slots` → `yt_schedule_video` / `yt_bulk_schedule` → `yt_list_schedule` → `yt_reschedule_video` / `yt_cancel_scheduled_video` |
| Autopilote | `yt_set_autopilot` → `yt_queue_autopilot` (coût quota rappelé) |
| Shorts | `yt_create_clips_from_video` → `yt_get_clip` → rendu dans l'app → `yt_publish_clip` → `yt_generate_vertical_variant` (miniature) → `yt_schedule_cross_post` |
| Distribution | `yt_list_connected_accounts` → `yt_schedule_cross_post` (6 posts max) → `yt_list_cross_posts` → `yt_cancel_cross_post` |
| Mesure | `yt_get_channel_analytics` / `yt_get_video_analytics` / `yt_compare_videos` / `yt_get_video_momentum` / `yt_get_channel_health_score` → `yt_generate_report` (lien public, sur accord) |
| Correction en lot | `yt_audit_channel` → `yt_create_bulk_job` (preview_only) → accord → job réel → `yt_get_bulk_job_status` → `yt_retry_failed_items` / `yt_cancel_bulk_job` ; `yt_find_replace_descriptions` (dry_run → réel) |
| Commentaires | `yt_list_comments` (sync = quota, sur accord) → `yt_draft_comment_reply` → relecture humaine → `yt_reply_to_comment` (50 unités, publique) |
| Échecs | `yt_list_videos` (erreurs) → `yt_retry_video` / `yt_retry_videos` (heure de réarmement respectée) |
| Prompts | `yt_list_prompts` → `yt_get_prompt` (valeurs rendues) → `yt_create_prompt` (privé par défaut, aucun secret) / `yt_update_prompt` / `yt_delete_prompt` (confirm) / `yt_toggle_prompt_favorite` |
| Divers | `yt_switch_channel` / `yt_set_favorite_channel` (accord) ; `yt_extract_youtube_thumbnail` (repartir d'une miniature) ; `yt_clone_style_from_url` (ambiance seulement — jamais une marque, un logo, un personnage ni un visage d'autrui) ; `yt_list_recent_uploads` ; `yt_get_thumbnail` / `yt_list_thumbnails` / `yt_get_thumbnail_insights` |

## Serveurs optionnels

foodeatup-tutoriel, academy, rapidocms, rapidocms-tuto, rapidorh-tuto,
planit-tutoriel, planit — absents de la session, le volet est sauté EN LE
DISANT. Les trois serveurs tuto sont déclarés par variables
d'environnement (URL non publiées dans le dépôt).
