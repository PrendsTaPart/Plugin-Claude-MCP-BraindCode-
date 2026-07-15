# Changelog — plugin rapido-higgsfield

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
