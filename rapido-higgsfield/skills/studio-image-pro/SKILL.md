---
name: studio-image-pro
description: Utiliser quand l'utilisateur veut une « image 4K », un « packshot », une « photo produit », un « visuel pub », une « image avec texte parfait » ou une « affiche photoréaliste ». Génère des images premium Higgsfield brandées (pont RapidoCMS → Higgsfield → bibliothèque de marque), avec préflight de coût et critique charte avant tout brouillon.
---

# Studio image pro — images premium brandées (Higgsfield)

La voie **premium** du visuel : photo réaliste, 4K, packshot pub, texte incrusté.
Toujours **branché sur la marque** (RapidoCMS) et **chiffré avant** (crédits).

## Étape 0 — Charger & router (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/routage-media.md` — **confirmer que Higgsfield
  est la bonne voie**. Visuel brandé simple (logo + variante) → **renvoyer** à
  `rapidocms:studio-visuel-marque` (CMS `images_to_image`, moins cher). Texte/layout/
  print → `rapido-canva`. Ne rester ici que pour le **premium** (4K, photo, pub, texte complexe).
- `rapidocms:contenu-conforme-marque` : la **charte KB prime** (couleurs, ton, do/don't).
- `gouvernance-credits` : chiffrer AVANT dès que le lot dépasse le seuil KB.

## Pipeline

### 1. Pont de marque (RapidoCMS → Higgsfield)
- `get_brand` (nom) + assets via `list_all_files` (RapidoCMS) → identifier logo,
  couleurs, images de référence.
- Chaque référence utile : URL publique → `media_import_url` (Higgsfield) → **media_id**
  (jamais l'URL directement dans `medias`). Passer les media_id en `medias:[{value, role:"image"}]`.
- Choix du modèle selon le besoin : `nano_banana_pro` (4K / texte / diagrammes),
  DTC Ads (`ms_image`, **`style_id` requis** via `show_marketing_studio` type=`image_style`
  + `brand_kit_id`) pour les visuels publicitaires, `soul_2` (portraits/UGC, 1 réf max).

### 2. brand_kit Higgsfield (kit miroir de la marque)
- Créer/mettre à jour le kit via `show_marketing_studio` type=`brand_kit` : soit
  `action=fetch` (`scrap_url` = site de la marque, auto-remplissage), soit
  `action=create` manuel depuis la marque RapidoCMS (`brand_name`, `business_overview`,
  `logo`, `images`, `colors`, `tone_of_voice`).
- **Logo et images exigent des URLs CDN Higgsfield** (`cdn.higgsfield.ai` /
  `upload.higgsfield.ai`) → **réimporter** les assets RapidoCMS via le flux media
  avant de créer le kit. **Update = remplacement TOTAL** : `action=get` (kit courant)
  → modifier → renvoyer **tout** (piège #6).
- Stocker le **`brand_kit_id`** dans `./rapido-kb/charte-graphique.md`
  (section « Identité Higgsfield ») pour réutilisation.

### 3. Génération (chiffrée puis critiquée)
- **Préflight de coût** (paramètre get_cost) → verdict `gouvernance-credits`
  (BLOQUÉ = pas de génération). Rappel H0 : image 1k ≈ 2 cr, 4k ≈ 4 cr.
- Générer (le job revient `pending` → récupérer le rendu via son id, une fois).
- **Critique charte** : réutiliser la **grille de `rapidocms:studio-visuel-marque`**
  (P4) — conformité couleurs/ton/marque. Si **FAIL** : itération ciblée (prompt/réf),
  **max 2** reprises, chacune re-chiffrée.

### 4. Rapatriement dans la bibliothèque de marque
- `upload_file_tool` (RapidoCMS) avec nommage **`{marque}-{type}-{variante}-vN`** →
  proposer `add_asset` (rattachement à la marque).
- Enchaînement possible (jamais automatique) : brouillon via `rapidocms:pipeline-contenu-social`.

### 5. FoodEatUp — mode « carte en photos »
- Pour un établissement : `list_dishes` (foodeatup) → sélection des plats → **packshot
  DTC Ads (`ms_image`) par plat** (référence photo du plat importée).
- **Confirmer le coût TOTAL du lot** (`gouvernance-credits`) **avant** de lancer :
  N plats × coût unitaire. Puis rapatriement CMS + liaison `foodeatup:carte-vitrine`.

## Brief flou → directeur-prompts
Si le brief est **flou** (moteur/angle indécis, pas de charte claire, besoin de
variantes comparées), **proposer de passer d'abord par l'agent
`rapido-prompteur:directeur-prompts`** : il lit la grammaire des moteurs en direct,
produit 3 variantes cadrées (paramètres + coût + références) et **délègue ici**
l'exécution. Un brief **net** (produit, angle, format connus) va directement à ce skill.

## Garde-fous
Routage vérifié (brandé simple → CMS ; print → Canva) ; **charte KB prime** ;
coût **préflighté**, lot FoodEatUp **confirmé en total** ; `medias` = media_id
(jamais URL) ; brand_kit update = remplacement complet ; rapatriement CMS nommé,
**aucune publication directe** (brouillon seulement).
