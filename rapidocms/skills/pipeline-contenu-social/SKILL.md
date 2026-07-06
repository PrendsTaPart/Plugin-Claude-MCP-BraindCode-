---
name: pipeline-contenu-social
description: Utiliser quand l'utilisateur veut créer un post, un brouillon, programmer une publication ou du contenu réseaux sociaux (Facebook, Instagram, LinkedIn, TikTok). Enchaîne compte → visuel → brouillon → planification → insights.
---

# Pipeline de contenu social

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` — ce skill produit du
contenu visible. Priorité aux valeurs live `get_brand`/`get_company`/`get_profile` ;
la charte sert de repli et pour les règles non exposées par l'API.

## Workflow

1. **Comptes connectés** — `list_connected_accounts` (filtre `networks` ∈ facebook |
   instagram | linkedin | linkedin_profile | tiktok). Récupérer l'identifiant du
   compte cible : `page_id` (pages), `profile_id` ou `open_id` selon le réseau —
   c'est lui qui sert d'`account_id` à l'étape 3. Si plusieurs comptes correspondent,
   demander lequel utiliser.
2. **Visuel (optionnel)** — générer avec `generate_image` (`prompt`, `size` = hd |
   standard), puis uploader dans la bibliothèque avec `upload_file_tool` (`type` =
   image | video | doc, `name`, `file_url` = URL publique). Appliquer la charte de
   marque (voir skill contenu-conforme-marque : `get_brand`).
3. **Brouillon** — `create_draft_tool`, un appel PAR réseau ciblé :
   - `post_name`, `social_type` ∈ linkedin | facebook | instagram | tiktok,
     `account_id` (étape 1), `post_type` ∈ media | text | mediatext ;
   - `media_type` (image | video), `media_url` (URL du fichier uploadé),
     `media_caption`, `media_source` = toujours `"biblio"` ;
   - tous ces champs sont requis par l'API, y compris pour un post texte.
   - **Adapter le format et le ton au réseau** : LinkedIn = professionnel,
     paragraphes courts + hashtags sobres ; Instagram = visuel obligatoire, caption
     incisive + hashtags ; Facebook = conversationnel ; TikTok = vidéo, accroche
     immédiate. Ne JAMAIS copier-coller le même texte sur tous les réseaux.
4. **Planifier** — `schedule_draft_tool` (`draft_id`, `post_date` format STRICT
   `Y-m-d`, `post_heure` format STRICT `H-i-s`, ex. `2026-07-10` / `18-30-00`).
   Confirmer date et heure avec l'utilisateur avant l'appel. Retrouver un brouillon
   avec `list_drafts_tool` (`name`, `social`), vérifier avec `list_scheduled_posts`.
5. **Insights** — après publication, `post_insights` (`post_ids`, **10 posts
   maximum par appel** — découper au-delà).

## Garde-fous

- Confirmation utilisateur avant toute planification (contenu + date/heure + compte).
- Annuler une publication programmée : `cancel_schedules_post` (`post_id`) —
  action destructrice, confirmation explicite obligatoire.
- Ne jamais publier/planifier un visuel généré sans l'avoir montré ou décrit à
  l'utilisateur pour validation.
