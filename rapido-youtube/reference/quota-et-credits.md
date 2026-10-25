# Quota YouTube et crédits — ce que chaque geste coûte

Source : familles de reference/outils-sensibles.json (manifeste du
2026-10-25) et lectures live `yt_get_quota_status` /
`yt_get_credit_balance`. Les scripts quota.py et credits.py appliquent ces
règles, formules affichées.

## Le quota (unités API YouTube, remis à zéro chaque jour)

- **Un envoi complet** par appel : yt_publish_video, yt_schedule_video,
  yt_register_uploaded_video, yt_bulk_schedule (par vidéo),
  yt_publish_clip, yt_retry_video, yt_retry_videos (par vidéo),
  yt_retry_failed_items, yt_queue_autopilot (par envoi mis en file).
- **50 unités** : yt_attach_thumbnail_to_video avec push_to_youtube ;
  yt_reply_to_comment.
- **Consomment aussi** : yt_research_keywords avec with_competition,
  yt_list_comments avec sync, yt_get_video_momentum avec refresh,
  yt_get_slot_scores avec recompute, les jobs en lot.
- `yt_get_quota_status` est la SEULE vérité : quota du jour, part réservée
  aux publications planifiées sous 24 h, **disponible réel**, risque
  (ok / tight / will_fail). Le disponible réel peut être à zéro alors que
  le quota brut ne l'est pas — c'est le cas du relevé du 2026-10-25.
- Règle des hooks : pas d'envoi sans lecture < 30 min ; will_fail = deny ;
  tight = ask. Une campagne s'estime AVANT (scripts/quota.py) et se
  découpe si elle ne tient pas — jamais de fractionnement pour « passer ».

## Les crédits (atelier visuel)

- Outils payants : yt_generate_thumbnail, yt_edit_thumbnail,
  yt_inpaint_thumbnail, yt_swap_face, yt_apply_style,
  yt_auto_optimize_thumbnail (2 passes), yt_clone_style_from_url,
  yt_generate_vertical_variant, yt_apply_template.
- Le barème est SERVI par `yt_get_credit_balance` — jamais codé en dur :
  scripts/credits.py le lit et affiche le coût d'un plan de travail avant
  l'accord.
- `yt_analyze_thumbnail` et `yt_compare_thumbnails` sont GRATUITS : on
  analyse largement, on génère sobrement (variations limitées — le hook
  garde-credits demande au-delà de 1).
- Le seuil de dépense par session vit dans ./rapido-kb/youtube.md ; sans
  KB, seuil prudent par défaut (25 crédits).
- Relevé du 2026-10-25 : 9 981 crédits restants.
