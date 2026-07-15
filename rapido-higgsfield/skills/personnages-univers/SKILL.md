---
name: personnages-univers
description: Utiliser quand l'utilisateur parle de « personnage récurrent », « notre mascotte en vidéo », « univers PronoClip », « entraîne le personnage », ou « même personnage dans une nouvelle scène/vidéo ». Industrialise la cohérence de personnage via Soul (identité entraînée) et Elements (référence réutilisable), en photo réaliste et en vidéo — successeur technique de coherence-personnage pour la voie premium/vidéo.
---

# Personnages & univers — cohérence industrialisée (Soul / Elements)

Successeur **technique** de `rapidocms:coherence-personnage` (qui reste la voie
`images_to_image` côté CMS). Ici : **Soul** (identité entraînée) et **Elements**
(référence réutilisable) pour la **photo réaliste** et la **vidéo** — dont le
pipeline **PronoClip**.

## Source de vérité — `./rapido-kb/personnages.json` (inchangée)
Le registre reste celui de `rapidocms:coherence-personnage`. Ce skill lui **AJOUTE**
deux champs par personnage : **`element_id`** et **`soul_id`** (voir l'exemple
enrichi `personnages.exemple.json`). Les **portraits canoniques restent stockés en
assets RapidoCMS** ; `brand_id`/`asset_id` résolus (`get_brand`/`list_all_files`),
jamais inventés.

## Étape 0 — Charger & router
- `${CLAUDE_PLUGIN_ROOT}/reference/routage-media.md` + `garde-fous-media.md`.
- `gouvernance-credits` : **chiffrer AVANT** tout clip (vidéo = 10-30 cr, H0).
- Registre `./rapido-kb/personnages.json` (créé par `rapidocms:coherence-personnage`
  s'il manque).

## Arbre de décision — Element vs Soul
- **Element** (défaut) : **instantané**, **multi-sujets**, **non-humains OK**,
  fonctionne avec nano_banana, seedream, **Kling 3.0**, Seedance, Cinema. → mascottes,
  personnages **anime PronoClip**, props/décors. Création : portraits canoniques CMS
  → réimport (`media_import_url` / flux media) → `show_reference_elements`
  `action=create` (medias en URL CDN Higgsfield) → **`element_id`** au registre.
- **Soul** (`show_characters` `action=train`) : **entraînement ~10 min, 5-20 photos,
  UNE personne**, utilisable **seulement** avec Soul V2 / Cinema. → un **humain réel
  récurrent** (fondateur, Mika **si droits OK**), **sur demande explicite**.
- Ambiguïté (avatar/visage sans voie choisie) → **demander** Element vs Soul, ne pas
  entraîner en silence.

## Génération d'images
- Placeholder **`<<<element_id>>>` dans le prompt** (jamais dans `medias`) ;
  **plusieurs personnages = plusieurs placeholders**. Avec Soul : **1 seul `soul_id`
  par génération**.

## Pipeline PronoClip (vidéo cohérente — chiffré AVANT)
1. Portrait canonique (registre, `version_active`) → **`start_image`** (réimporté) +
   **`<<<element_id>>>`** dans le prompt.
2. **Préflight coût** → `gouvernance-credits` (**BLOQUÉ = on ne lance pas**).
3. Génération vidéo `kling3_0` (start_image **obligatoire** pour ancrer l'Element —
   piège #3 ; sans start_image → `seedance_2_0`).
4. Post-prod : `reframe` **9:16** si besoin → `upscale_video`.
5. **Gate viral** → `analyse-video-virale` (H6, à venir) avant tout boost.
6. **Assemblage de l'épisode → `rapido-video:montage-express` (0 crédit)** : concat des
   clips, intro/outro (habillage), sous-titres FR burn-in, reframe 9:16. Puis
   `upload_file_tool` (CMS, nommage `{marque}-{personnage}-scene-vN`) → brouillon
   rattaché à la **campagne PronoClip (#20)** via `rapidocms:pipeline-contenu-social`.

## Évolution du canon
Nouveau look → nouveaux portraits **vN+1** → **nouvel Element** (et/ou ré-entraînement
Soul) → registre mis à jour (`element_id`/`soul_id`/`version_active`), **anciens
conservés** (historique traçable).

## Garde-fous
Cohérence **par Soul/Elements**, jamais un personnage récurrent généré **sans
référence** ; Soul = **droits/consentement** (hook `garde-voix` ne couvre que la
voix — ici, confirmation explicite pour un humain réel) ; clip **chiffré avant**
(BLOQUÉ = pas de génération) ; Kling + Element = **start_image obligatoire** ;
`start_image`/portraits = **media_id** (jamais URL brute) ; **aucune publication
directe** ; registre côté `./rapido-kb/`.

## Frontières
- Voie CMS `images_to_image` (image brandée cohérente, sans vidéo/photo réaliste) →
  `rapidocms:coherence-personnage`.
- Chiffrage/plafond → `gouvernance-credits`. Pub produit → `usine-video-marketing`.
