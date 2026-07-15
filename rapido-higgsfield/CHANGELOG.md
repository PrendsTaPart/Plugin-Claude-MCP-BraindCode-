# Changelog — plugin rapido-higgsfield

## 1.0.2 — 2026-07-15 — croisements rapido-video

- **Croisements montage local** (patch V5) : la voie **0 crédit** de `rapido-video`
  prime dès que des médias réels existent.
  - `clips-et-shorts` : rushes existants → `rapido-video:montage-express` ;
    `shorts_studio` réservé au **restyle génératif**.
  - `videos-explicatives` : **assemblage local par défaut** (`rapido-video:montage-express`
    + habillage `motion-design-remotion` en mode aperçu) ; `explainer_video` seulement
    si tout est génératif.
  - `personnages-univers` : le pipeline PronoClip **assemble l'épisode via
    `rapido-video:montage-express`** (concat + intro/outro + sous-titres + 9:16).

## 1.0.1 — 2026-07-15 — DELTA V1 montage

- **README** : « Prérequis utilisateur : AUCUN » (marketplace add + install + MCP ;
  dépendances de montage auto-installées et confirmées à la 1re utilisation).
- **`reference/pieges-montage.md`** (nouveau) : une section par OS (conteneur Linux
  = mesuré ; Windows/macOS = théorique) ; chemins lus dans `rapido-kb/outils-locaux.md`,
  via `pathlib`, **aucun antislash Windows en dur**.
- **`reference/garde-fous-media.md`** : §(e) montage local — « temps de rendu selon
  l'environnement » (à mesurer localement, plus de « CPU Windows »), dépendances
  auto-installées annoncées/confirmées, chemins via KB.
- **Hook `Stop`** : le récapitulatif inclut désormais les **téléchargements
  effectués** (nom, taille, emplacement) en plus des IDs/coûts.
- `scripts/bootstrap_video.py` : écrit la section « Téléchargements effectués »
  (nom · taille · emplacement) dans `rapido-kb/outils-locaux.md`.

## 1.0.0 — 2026-07-15 — RELEASE usine média IA

Première version stable : **9 skills + 1 agent**, audit live H0, garde-fous et
hooks coûts/voix, 7 croisements dans l'écosystème (rapidocms, meta-ads,
rapido-marketing, foodeatup, rapidorh).

- **Clôture H10** : évals consolidées (par skill + **3 anti-déclenchements** de
  routage + tests hooks) ; `docs/RECETTE-HIGGSFIELD.md` — la **preuve de bout en
  bout** est le test de plomberie H0 (réel) ; la **recette vidéo est différée**
  (solde 80 cr < recette complète, le short 30s ≈ 90 cr) et documentée pour
  exécution ultérieure sous `gouvernance-credits`.
- README du plugin finalisé (table des 9 skills + agent).
- ⚠️ **Tag & Release** : le push de tag est fait **côté utilisateur** (le proxy de
  session refuse les tags) — `git tag rapido-higgsfield-v1.0.0` + GitHub Release.

## 0.9.0 — 2026-07-15

- Agent **`producteur-studio`** (H9) : l'exécutant média — route, **chiffre avant**
  (`gouvernance-credits`), produit via H3-H8, critique charte, rapatrie CMS,
  **récapitule job_ids/asset_ids/coûts**. Interdits : publier, booster (sans PASS au
  gate), cloner une voix sans consentement, dépasser le plafond. Briefs de
  `rapidocms:directeur-artistique` + managers M11 ; écarts → `rapidocms:gardien-de-marque`.

## 0.8.0 — 2026-07-15

- Skill **`sites-et-jeux-express`** (H8) : microsites jetables + jeux jouables.
  - **Routage en tête** : landing/app connectée CRM → `rapido-lovable:usine-a-landing`
    (prioritaire) ; microsite jetable / jeu → ici.
  - Sites : instructions officielles d'abord → create → repo → `deploy_website`
    (ship = live, **OG complètes avant**) ; `website_secrets` ; `website_db` lecture
    seule. Jeux : instructions d'abord → build → zip → `media_upload`/`media_confirm`
    → `deploy_game` (thumbnail 16:9 + favicon 1:1) ; **update = `game_id` exact**
    (jamais inventé, sinon nouveau jeu silencieux).
  - Croisement CRM : `lancer_jeu_concours_entreprise` (mécanique officielle) + URL
    du jeu injectée en campagne. Registre `tunnels.md`. Schémas vérifiés live.
  - `tests/evals.md` : 3 scénarios (dont SJ2 routage → Lovable).

## 0.7.0 — 2026-07-15

- Skills **`voix-et-doublage`** + **`videos-explicatives`** (H7).
  - `voix-et-doublage` : TTS (`seed_audio`/`text2speech_v2`), **doublage 18 langues**
    (`dubbing` — cas FoodEatUp V1-V6 fra→eng/ara/spa), `voice_change`, clonage
    **encadré droits/consentement** (hook `garde-voix`, clone asynchrone). Routage
    Mika→HeyGen. Coûts non préflightables (dubbing/clone) signalés comme estimation.
  - `videos-explicatives` : pipeline par blocs — script (`rapidocms:content-creation-methodo`)
    → clips → voix (`voix-et-doublage`) → assemblage `explainer_video` (sous-titres
    burn-in), **coût total confirmé avant assemblage** ; croisements onboarding RH,
    FoodEatUp Academy, synthèse webinar Fireflies. Brouillon CMS.
  - Schémas vérifiés live (voice_change, create_voice, dubbing). `tests/evals.md` :
    5 scénarios (dont VD2 refus clonage sans droits).

## 0.6.0 — 2026-07-15

- Skills **`clips-et-shorts`** + **`analyse-video-virale`** (H6).
  - `clips-et-shorts` : 3 chaînes — Personal Clipper (`personal_clipper_create`,
    YouTube → clips, long-running prévenu), Shorts Studio (`shorts_studio_list_presets`
    + `shorts_studio_create`, préflight coût), reframe/upscale à l'unité ; rapatriement
    CMS + brouillons confirmés ; routine n8n lundi (top post → short).
  - `analyse-video-virale` : `video_analysis_create` (scène par scène) +
    `virality_predictor` → **verdict PASS / RETRAVAILLER + 3 corrections** ; scores →
    `benchmarks.md`. **Gate : aucun boost payant Meta sans PASS** (règle appliquée
    aussi côté rapido-meta-ads — patch séparé).
  - Schémas vérifiés live (virality_predictor, video_analysis, reframe, shorts,
    personal_clipper). `tests/evals.md` : 5 scénarios (dont AV2 gate boost).

## 0.5.0 — 2026-07-15

- Skill **`personnages-univers`** ⭐ (H5) — cohérence de personnage industrialisée
  (Soul + Elements), successeur technique de `rapidocms:coherence-personnage` pour
  la voie premium/vidéo. **Débloque le pipeline PronoClip.**
  - Registre `personnages.json` inchangé, **enrichi** de `element_id` / `soul_id`
    (portraits canoniques toujours en assets CMS).
  - Arbre **Element** (défaut : instantané, multi-sujets, non-humains, Kling/Seedance ;
    `<<<element_id>>>` dans le prompt) vs **Soul** (humain réel, 5-20 photos, 1 soul_id/gen,
    droits/consentement, sur demande explicite).
  - **Pipeline PronoClip** : portrait → `start_image` + `<<<element_id>>>` →
    **préflight coût** (`gouvernance-credits`, BLOQUÉ = pas de génération) → `kling3_0`
    (start_image obligatoire, sinon `seedance_2_0`) → `reframe` 9:16 → `upscale_video`
    → gate viral (H6) → brouillon CMS rattaché à la campagne PronoClip (#20).
  - Schémas vérifiés live : `show_reference_elements` (Elements), `show_characters` (Soul).
  - `tests/evals.md` : 4 scénarios (dont PU3 PronoClip dry-run get_cost, PU4 frontière CMS).
  - 🎯 Clôt le pending « character consistency PronoClip ».

## 0.4.0 — 2026-07-15

- Skill **`usine-video-marketing`** (H4) : chaîne Marketing Studio (pub vidéo/UGC).
  - Produit via `show_marketing_studio` fetch (URL réelle : site Rapido, carte
    FoodEatUp, landing CRM) ou create manuel ; `product` vs `webproduct`.
  - Composition **hooks/settings XOR `ad_reference`** (« refais cette pub » :
    `video_analysis` → blueprint) ; **avatar_ids/product_ids liés explicitement**
    (ne se propagent pas depuis l'ad_reference — piège H0).
  - Génération `marketing_studio_video` **9:16 par défaut**, **préflight coût**
    (`gouvernance-credits`, BLOQUÉ = pas de génération) ; post-prod `reframe`/`upscale_video`.
  - Sorties (jamais automatiques) : brouillon CMS (`pipeline-contenu-social`) et/ou
    créatif Meta (`rapido-meta-ads:creatifs-publicitaires`, **self_ai_disclosure
    OPT_IN**, PAUSED, budget confirmé) ; **gate viral avant tout boost** (H6).
  - `tests/evals.md` : 4 scénarios (dont UVM2 ad_reference, UVM3 sortie Meta, UVM4 blocage).

## 0.3.0 — 2026-07-15

- Skill **`studio-image-pro`** (H3) : images premium brandées (Higgsfield).
  - **Pont de marque** RapidoCMS → Higgsfield (`get_brand`/`list_all_files` →
    `media_import_url` → `medias` par media_id) ; modèles `nano_banana_pro` (4K/texte),
    DTC Ads (`ms_image` + `style_id` + `brand_kit`), `soul_2` (portraits).
  - **brand_kit miroir** via `show_marketing_studio` type=brand_kit (fetch site OU
    create depuis la marque CMS ; logo/images en CDN Higgsfield ; update = remplacement
    total) ; `brand_kit_id` stocké dans `charte-graphique.md`.
  - Génération **chiffrée** (préflight → `gouvernance-credits`) → critique charte
    (grille `rapidocms:studio-visuel-marque`, max 2 itérations) → rapatriement CMS
    `{marque}-{type}-{variante}-vN` + `add_asset`.
  - Mode **carte-en-photos FoodEatUp** : `list_dishes` → packshot par plat, **coût
    total du lot confirmé** avant lancement, liaison `foodeatup:carte-vitrine`.
  - Schémas vérifiés live (H0/H3) : `get_brand`, `show_marketing_studio` (brand_kit
    create/get/update/fetch), `media_import_url`, `upload_file_tool`, `add_asset`.
  - `tests/evals.md` : 4 scénarios (dont SIP2 routage refusé, SIP4 lot FoodEatUp).

## 0.2.0 — 2026-07-15

- Skill **`gouvernance-credits`** (H2) : gardien budgétaire du plugin.
  - `scripts/verifie_budget.py` (stdlib) : verdict **OK / CONFIRMATION REQUISE /
    BLOQUÉ** — BLOQUÉ si coût > solde ou coût > (plafond − déjà consommé) ;
    CONFIRMATION si coût > seuil ; formule affichée, somme des `transactions`
    spend/deduct pour le compteur.
  - Workflow : `balance` (solde), `transactions` (consommation), **préflight
    get_cost** (jamais de tête ; cas non préflightables — dubbing/upscale — estimés
    via la grille H0 et signalés), verdict par script, compteur mensuel tenu à jour.
  - **Règle transverse** : tout skill du plugin invoque `gouvernance-credits` en
    préflight dès que la production dépasse le seuil KB (hook `garde-couts` en filet).
  - `tests/evals.md` : 3 scénarios (dont GC3 blocage pub 15 s sur solde gratuit).

## 0.1.1 — 2026-07-15

- **Audit live H0** (`docs/AUDIT-MCP-HIGGSFIELD.md` + `docs/GRILLE-COUTS-HIGGSFIELD.md`) :
  catalogue des modèles (image/vidéo/audio/3d) relevé via `models_explore`, grille de
  coûts via `get_cost` (préflight) + 1 image réelle, **test de plomberie CMS↔Higgsfield
  réussi dans les deux sens** (media_import_url → generate_image → upload_file_tool).
- `reference/pieges-outils.md` : section **Confirmations H0** (params-nesting, `get_cost`
  supporté/non supporté, génération asynchrone via `job_display`, alias `nano_banana_pro`
  →`nano_banana_2`, **budget réel = plan gratuit 10 crédits**).
- GO/NO-GO figé : H2→H9 **GO** (coût nul à construire) ; **H4/H5/H6/H10 bloqués budget**
  (vidéos/shorts = 10-90 crédits, top-up requis) — détail dans l'audit.

## 0.1.0 — 2026-07-15

- **Squelette du plugin** (routage média, garde-fous, hooks) — les skills de
  production arrivent en H2+, après l'audit live H0.
- `.claude-plugin/plugin.json` + entrée `marketplace.json` (14e plugin).
- `.mcp.json` : `huggsfield` via `${HIGGSFIELD_MCP_URL}` (URL/transport à figer en
  H0) + ponts RapidoCMS/CRM/RH/FoodEatUp (URLs réelles).
- `reference/routage-media.md` : arbre de décision unique du média dans
  l'écosystème (Canva / CMS `images_to_image` / Higgsfield / HyperFrames / Lovable),
  référencé par tous les skills média.
- `reference/pieges-outils.md` : 9 règles relevées sur les schémas (medias = UUID
  jamais URL ; ponts CMS↔Higgsfield ; Kling 3.0 + `start_image` ; 1 soul_id/gen ;
  Marketing Studio 9:16 + XOR hook/ad_reference ; brand_kit remplacement total ;
  `get_cost` préflight ; `select_workspace` = facturation ; namespace `huggsfield`)
  — à compléter en H0.
- `reference/garde-fous-media.md` : coûts, voix (droits), marque (charte avant
  publication), publication (jamais directe, OPT_IN Meta, gate viral avant boost).
- `hooks/` : `garde-couts` (PreToolUse — refus des générations payantes sans coût
  confirmé, marqueur `get_cost:true` ou `cout_confirme:true` ; lit le plafond
  `rapido-kb/budget-media.md`), `garde-voix` (PreToolUse — `ask` forcé sur
  create_voice/voice_change/dubbing avec mention des droits), `Stop` (récap
  job_ids/asset_ids + coûts).
- `reference/kb-templates/budget-media.md` : plafond mensuel, seuil de
  confirmation, compteur.
