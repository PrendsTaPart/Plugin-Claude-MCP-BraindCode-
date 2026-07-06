# Pièges des outils MCP (rapidocms) — référence rapide

Consulter ce tableau au moindre doute avant d'appeler un outil.

| Outil | Paramètres pièges | Erreur fréquente | Parade |
|---|---|---|---|
| `create_draft_tool` | `account_id` = `page_id`, `profile_id` ou `open_id` SELON le réseau | Mauvais identifiant de compte | Toujours le récupérer via `list_connected_accounts` (le `page_id` sert d'identifiant pour les pages) |
| `create_draft_tool` | `media_source` | Autre valeur que `"biblio"` | `media_source` vaut TOUJOURS `"biblio"` |
| `create_draft_tool` | tous les champs requis (même post texte) | `media_type`/`media_url`/`media_caption` omis sur un post texte | Renseigner tous les champs exigés par le schéma, même pour `post_type: "text"` |
| `schedule_draft_tool` | `post_date` = `Y-m-d`, `post_heure` = `H-i-s` | Heure en `HH:MM` ou `18:30:00` | Format à TIRETS pour l'heure : `18-30-00` |
| `post_insights` | `post_ids` max 10 | 15 posts passés d'un coup | Découper en lots de 10 |
| `ingishts_campagne` | orthographe du nom | « Corrigé » en `insights_campagne` → outil introuvable | Utiliser le nom EXACT du serveur : `ingishts_campagne` |
| `add_digital_card` | `owner_phone` chiffres uniquement ; tous champs requis | `+33 6...` avec espaces/`+` | Nombre nu (ex. `33612345678`) ; collecter tous les champs avant l'appel |
| `edit_card_page` | `text` en HTML avec CSS INLINE | Classes CSS ou feuille de style externe | Styles dans les éléments eux-mêmes (couleur, taille, décoration) |
| `upload_file_tool` / `add_card_page_link` | `file_url` / `image_url` publiques | URL locale ou privée | URL http(s) publiquement accessible uniquement |
| `generate_image` | `size` ∈ hd / standard ; palette | Palette laissée au hasard | Couleurs hex de la charte dans le prompt ; pas de texte dans l'image |
| Formats visuels par réseau | dimensions | Recadrage aveugle inter-réseaux | IG post 1080×1350, story/TikTok 1080×1920, LinkedIn 1200×627, Facebook 1200×630 — décliner par destination |
| `cancel_schedules_post` / `delete_*` | irréversibles | Annulation/suppression sans accord | Confirmation utilisateur explicite (hook ask) |
