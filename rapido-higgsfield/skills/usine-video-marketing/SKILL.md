---
name: usine-video-marketing
description: Utiliser quand l'utilisateur veut une « pub vidéo », une « vidéo produit », une « vidéo UGC », « refais cette pub », ou une « vidéo TikTok/Reel pour [produit] ». Chaîne Marketing Studio Higgsfield : produit (fetch URL ou médias) → composition (hooks/settings ou ad_reference) → vidéo verticale, chiffrée avant, sortie en brouillon CMS et/ou créatif Meta déclaré IA.
---

# Usine vidéo marketing — Marketing Studio (Higgsfield)

Pub vidéo produit/UGC, prête TikTok/Reels. **Chiffrée avant** (les vidéos coûtent
cher — H0 : pub 15s ≈ 75 crédits), **jamais publiée directement**.

## Étape 0 — Charger & router (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/routage-media.md` (vidéo générative/pub → ici ;
  vidéo éditoriale maquettée → HyperFrames ; avatar Mika → HeyGen) +
  `garde-fous-media.md`.
- `gouvernance-credits` : **préflight obligatoire** (une vidéo dépasse le seuil KB).
- `rapidocms:contenu-conforme-marque` (charte).

## Pipeline

### 1. Produit
- `show_marketing_studio` `action=fetch` avec une **URL réelle** (page produit du
  site Rapido, carte vitrine FoodEatUp, landing CRM) → entité produit ; ou
  `action=create` manuel depuis des médias importés.
- **`product`** = un article précis à mettre en avant ; **`webproduct`** = un
  site/app/service promu en tant que tel. Dans le doute → `product`.

### 2. Composition (deux voies, exclusives)
- **Hooks + settings** : `show_marketing_studio` type=`hook` / `setting` (lister,
  faire choisir) → `hook_id` (le « quoi ») + `setting_id` (le « où »). Supportés
  seulement pour les presets UGC, Tutorial, Unboxing, Product Review, Virtual Try On.
- **`ad_reference`** (« refais cette pub ») : l'utilisateur **uploade la vidéo de
  référence** (chat attachment → `video_input_id` ; pas d'URL TikTok/YT) →
  `video_analysis` la dissèque → `show_marketing_studio` type=`ad_reference` en
  extrait le blueprint → passer `ad_reference_id`.
- **`hook_id`/`setting_id` XOR `ad_reference_id`** — jamais les deux (piège #5).
- **Avatars/produits ne se propagent PAS** depuis l'ad_reference : lier
  **explicitement** `avatar_ids` / `product_ids` sur l'appel de génération, même si
  l'ad_reference les référençait (piège documenté H0).

### 3. Génération (chiffrée)
- **Préflight de coût** (paramètre get_cost) → verdict `gouvernance-credits`
  (**BLOQUÉ = pas de génération** ; rappel : plan gratuit ~10 cr < une pub 15s).
- Générer avec le modèle `marketing_studio_video`, **`aspect_ratio: "9:16"` par
  défaut** (16:9 seulement si demandé — piège #5). Job `pending` → rendu via son id.

### 4. Post-production (optionnelle)
- `reframe` (déclinaison 16:9 ↔ 9:16), `upscale_video` (netteté/résolution).

### 5. Sorties (au choix, jamais automatique)
- **Brouillon RapidoCMS** : `upload_file_tool` du rendu → `rapidocms:pipeline-contenu-social`.
- **Créatif Meta** : déléguer à `rapido-meta-ads:creatifs-publicitaires` — créatif
  avec **`self_ai_disclosure: "OPT_IN"`** (créatif IA = déclaration Meta obligatoire),
  campagne en **PAUSED**, **budget confirmé**.
- Les deux, ou aucune (préparation seule).

### 6. Gate viral (avant tout boost payant)
- Avant de booster, passer la vidéo au gate → `analyse-video-virale` (H6, à venir) :
  aucun boost payant Meta sur une vidéo non passée au gate.

## Brief flou → directeur-prompts
Si le brief vidéo est **flou** (hook/format/ton indécis, pas de charte, besoin de
variantes), **proposer de passer d'abord par l'agent
`rapido-prompteur:directeur-prompts`** : il cadre 3 variantes (paramètres lus en
direct + coût + références) puis **délègue ici** l'exécution. Un brief **net** va
directement à ce skill.

## Garde-fous
Coût **préflighté**, **BLOQUÉ = pas de génération** ; `9:16` par défaut ;
hooks/settings **XOR** ad_reference ; avatars/produits **liés explicitement** ;
**aucune publication directe** (brouillon) ; créatif Meta **OPT_IN + PAUSED + budget
confirmé** ; boost **seulement après gate viral**.
