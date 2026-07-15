# Audit MCP Higgsfield (H0) — live 2026-07-15

> Serveur MCP `huggsfield` (marque « Higgsfield »). Audit **lecture + préflights**
> `get_cost` (gratuits) + **1 génération image réelle** (test de plomberie autorisé).
> Compagnon : `GRILLE-COUTS-HIGGSFIELD.md`. Conditionne le GO/NO-GO de H1→H10.

## 0. Compte & facturation (relevé live)
- `list_workspaces` → **1 workspace privé**, `plan_type: free`, **10 crédits**,
  `is_selected: **false**` (aucun workspace explicitement sélectionné — les
  opérations ciblent le privé par défaut ; la génération test a bien abouti sans
  `select_workspace`).
- `balance` → 10 crédits (avant), **8 crédits (après le test)** → l'image a coûté **2**.
- `show_plans_and_credits` = widget de vente (upgrade/top-up), pas une donnée d'audit.

## 1. Catalogue de modèles (via `models_explore action=list`)
- **Image (30+ modèles)** : `nano_banana_pro`/`nano_banana_2` (1k/2k/4k, texte,
  diagrammes), `soul_2`/`soul_cinematic`/`soul_cast`/`soul_location` (Soul,
  `soul_id`), `marketing_studio_image` & `ms_image` (DTC, `style_id` **requis** +
  `brand_kit_id`, `medias` max 14, `batch_size` 1-20), `gpt_image_2`, `seedream_v4_5`
  (4-6K), `flux_2`, `kling_omni_image`, `recraft_v4_1` (vector/logos), `outpaint`,
  `topaz_image*` & `bytedance_image_upscale` (upscale), `image_background_remover`,
  `autosprite` (sprite sheets de jeu). Résolutions par `params.resolution` ;
  `aspect_ratios` listés par modèle.
- **Vidéo (25+ modèles)** : `kling3_0` (3-15s, mode std/pro/**4k**, `sound` on/off,
  roles `start_image`/`end_image`), `kling3_0_turbo`, `kling2_6`, `seedance_2_0` /
  `_mini` (réf image/vidéo/audio, identité, 4k), `marketing_studio_video` (12-15s,
  hooks/settings **XOR** `ad_reference_id`, `avatar_ids`/`product_ids`),
  `cinematic_studio_3_0` (jusqu'à 4k), `veo3`/`veo3_1`, `minimax_hailuo`, `wan2_*`,
  `clipify` (Personal Clipper YouTube→clips), `explainer_video` (assemblage blocs +
  voix + sous-titres), `topaz_video`/`bytedance_video_upscale`, background removers,
  `sync_so` (lipsync).
- **Audio (5)** : `seed_audio` (TTS ByteDance, voix preset/element, clone via
  `audio_references`), `text2speech_v2` (variant elevenlabs/minimax/seed_speech/
  vibe_voice/cozy_voice). `sonilo_music`/`mirelo_text_to_audio`/`inworld_text_to_speech`
  = **pipeline jeu uniquement** (ne pas utiliser en audio standalone).
- **3D (7)** : `image_to_3d`/`meshy_image_to_3d` (texture, PBR, rigging, animation),
  `multi_image_to_3d` (1-4 vues), `sam_3_3d`, `3d_rigging` (prend `model_url`),
  `tripo_3d` (text-to-3D). Rigging + `animation_action_id` (0-696, 678 clips).
- **Doublage** : `dubbing` (18 langues : eng, fra, ara, spa, deu, por, jpn, kor…).

## 2. Workflows embarqués (`get_workflow_instructions`)
**1 seul** workflow bundlé exposé : **`video-explainer`** (explainer/story animé,
1 narrateur sur blocs 10s, style-key). → à **orchestrer** en H7 (`videos-explicatives`),
pas à recréer. Les autres formats (tv-ad, ugc, podcast…) sont cités mais non listés
comme bundles chargeables ici.

## 3. Signatures & pièges CONFIRMÉS (complètent `pieges-outils.md`)
1. **`model`, `prompt`, `medias`, `get_cost` vont DANS `params`** pour
   `generate_image`/`generate_video`/`generate_audio`/`generate_3d` — **pas** au
   niveau racine (sinon `params.model undefined`). `shorts_studio_create`,
   `dubbing`, `upscale_*` ont leur **propre** forme (souvent `params` plat ou racine).
2. **`get_cost: true`** fonctionne sur image/vidéo/audio/3d et `shorts_studio_create`
   (avec `duration_seconds`). **NE fonctionne PAS** sur `dubbing` ni `upscale_video` ;
   `upscale_image` exige un `image_id` résoluble même pour l'estimation.
3. **Résolution de modèle** : `nano_banana_pro` est accepté mais **exécuté comme
   `nano_banana_2`** (alias interne) — ne pas s'alarmer du renommage en réponse.
4. **`medias[].value` = UUID** (media_id / job_id), jamais une URL — confirmé
   (l'URL S3 a dû passer par `media_import_url` d'abord).
5. **Limites de références** (par `models_explore`) : `soul_2`/`soul_cinematic` =
   **1 image** ; `ms_image` = **14** ; Kling/Seedance = roles `start_image`/`end_image`.
6. **Kling 3.0 + Elements sans `start_image`** : **non exécuté** (une vidéo = 10-30 cr,
   hors périmètre « 1 image test »). Inféré du schéma : `kling3_0.medias.roles =
   [start_image, end_image]` → un Element (`<<<UUID>>>` dans le prompt) a besoin d'un
   `start_image` pour s'ancrer (piège #3 de `pieges-outils.md`). **À confirmer par
   exécution** quand le budget le permettra (H5).
7. **Génération = asynchrone** : `generate_image` renvoie `status: pending` + un
   `id` (job). Résultat via `job_display(id)` (une fois) → `results.rawUrl`. Ne pas
   marteler le poll (piège #7).

## 4. Test de plomberie inter-MCP (RÉEL, réussi — les deux ponts)
| Étape | Appel | Résultat |
|---|---|---|
| 1. Source CMS | `list_all_files` (RapidoCMS) | asset `braind_robot_ai` **id 166**, URL S3 publique. `search` **ne filtre pas** (305 fichiers renvoyés — piège CMS connu). |
| 2. Pont → Higgsfield | `media_import_url` | **media_id `b6e9d941-85b1-4bde-81a7-932e5df77199`** (image/png). |
| 3. Génération | `generate_image` `nano_banana_pro` 1k, `medias:[{value:b6e9d941, role:image}]` | job **`640c63cc-…`** → `completed`, **2 crédits** (10→8). Rendu CloudFront. |
| 4. Pont ← CMS | `upload_file_tool` (RapidoCMS) | fichier **`TEST-H0-braind-render`** enregistré (company_id 321, URL S3). |

**Conclusion** : le pont **CMS ↔ Higgsfield fonctionne dans les deux sens**
(URL publique → `media_import_url` ; rendu → `upload_file_tool`). C'est la base
technique de H3/H4/H5.

## 5. GO / NO-GO H1 → H10
| Prompt | Verdict | Note |
|---|---|---|
| H1 squelette | ✅ **fait** | plugin `rapido-higgsfield` v0.1.0 mergé. |
| H2 gouvernance-credits | ✅ **GO** | `balance`/`transactions`/`get_cost` OK ; gérer les cas **non préflightables** (dubbing/upscale) = estimer via grille + confirmer. |
| H3 studio-image-pro | ✅ **GO** | pont image + référence **prouvé de bout en bout** ; `brand_kit` à valider en H3. |
| H4 usine-video-marketing | ⚠️ **GO capacité / BLOQUÉ budget** | pub 15s = **75 cr** > solde. Skill constructible ; exécution réelle = **après top-up**. |
| H5 personnages-univers | ⚠️ **GO Elements / clip BLOQUÉ budget** | cohérence via Elements OK à câbler ; clip Kling = 10-30 cr → top-up. |
| H6 clips/shorts + analyse-virale | ⚠️ **GO / short BLOQUÉ budget** | short = **90 cr** ; `virality_predictor`/`video_analysis` à valider en H6. |
| H7 voix/doublage + explainer | ✅ **GO** | TTS **0.4 cr** (bon marché) ; `dubbing` coût **à mesurer** (1er réel) ; `explainer_video` + workflow `video-explainer` dispo. |
| H8 sites/jeux | ✅ **GO** | via bundles `get_*_creation_instructions` ; coût de déploiement à mesurer. |
| H9 agent + patchs | ✅ **GO** | aucune dépendance de coût. |
| H10 recette réelle | ⛔ **BLOQUÉ** | packshot + clip PronoClip + short + dubbing ≫ 8 crédits. **Top-up / plan payant requis** avant H10. |

### Blocage transverse = BUDGET
Le plan actif est **gratuit (10 crédits)**. **Images (≤4 cr) et audio (≤1 cr)** sont
faisables ; **toute vidéo (10-75 cr) ou short (90 cr) est hors budget**. Recommandation :
construire H2→H9 (skills + garde-fous, coût nul), et **réserver toute recette vidéo
(H10) à un workspace rechargé**. `gouvernance-credits` (H2) doit refléter ce solde réel.

## 6. Récapitulatif des IDs créés (traçabilité / nettoyage)
- Higgsfield media importé : `b6e9d941-85b1-4bde-81a7-932e5df77199` (historique média).
- Higgsfield job image : `640c63cc-ee51-4115-8640-fc3932a665a3` (historique génération).
- **RapidoCMS — donnée test à nettoyer** : fichier bibliothèque **`TEST-H0-braind-render`**
  (aucun outil `delete_file` côté CMS — cf. audit P0 ; suppression manuelle, comme
  le fichier 624 de P0).
- Crédits consommés : **2** (10 → 8). Aucune autre génération payante.
