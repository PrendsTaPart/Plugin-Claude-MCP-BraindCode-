# Pièges des outils Higgsfield (à encoder dans les skills)

Règles relevées sur les schémas du MCP (session du 15/07/2026). **À confirmer et
compléter par l'audit H0** (`docs/AUDIT-MCP-HIGGSFIELD.md`, `docs/GRILLE-COUTS-HIGGSFIELD.md`).

> **Nom du serveur** : les outils sont exposés sous le namespace `mcp__huggsfield__*`
> (id serveur = `huggsfield`), même si la marque est « Higgsfield ». Les matchers de
> hooks et `.mcp.json` utilisent `huggsfield`.

1. **`medias[].value` = media_id ou job_id (UUID), JAMAIS une URL.** Une URL web →
   `media_import_url` d'abord ; un fichier local → widget d'upload ou
   `media_upload` + `media_confirm`.
2. **Pont RapidoCMS → Higgsfield** : les assets CMS sont des URLs publiques →
   `media_import_url` pour les rendre utilisables. **Pont inverse** : les rendus
   Higgsfield (URLs) → `upload_file_tool` RapidoCMS pour entrer dans la bibliothèque
   de marque.
3. **Kling 3.0 + Elements : `start_image` obligatoire** dans `params.medias`, sinon
   le placeholder `<<<UUID>>>` est ignoré. Sans start_image → choisir `seedance_2_0`.
4. **1 seul `soul_id` par génération** (Soul V2 / Cinema uniquement). Plusieurs
   personnages dans un plan → **Elements** (`<<<UUID>>>` multiples dans le prompt).
5. **Marketing Studio** : `aspect_ratio: "9:16"` EXPLICITE pour TikTok/Reels (défaut
   = 16:9) ; `hook_id`/`setting_id` **XOR** `ad_reference_id` (jamais les deux) ;
   après un fetch produit, enchaîner `generate_video` model `marketing_studio_video`.
   Lier explicitement `avatars`/`product_ids` au `generate_video` (le lien sur
   l'`ad_reference` ne se propage pas seul).
6. **`brand_kit` Higgsfield** : logo et images exigent des URLs CDN Higgsfield →
   **réimporter** les assets RapidoCMS via `media_upload` avant création ; update =
   **remplacement TOTAL** (get → modifier → renvoyer tout).
7. **`get_cost: true`** en préflight partout où c'est supporté ; un `recovery_tool`
   retourné = l'appeler immédiatement ; **ne pas poller** (les widgets s'auto-actualisent).
8. **`select_workspace` = facturation** : toujours vérifier le workspace actif avant
   une session de production (`list_workspaces`).
9. **Où vit le plugin** : en claude.ai ces outils sont des apps partenaires (opt-in
   utilisateur) ; dans **Claude Code avec le connecteur branché**, les skills du
   plugin les appellent directement. Le connecteur Higgsfield est **requis** (voir
   README / `.mcp.json` `${HIGGSFIELD_MCP_URL}`).

> H0 figera : catalogue exact des modèles (image/vidéo/audio/3d) et leurs
> `aspect_ratios`/paramètres, limites d'images de référence par modèle, et la
> **grille de coûts** par livrable type. Tant que H0 n'a pas tourné, aucun skill de
> production n'est livré (H2+).
