# Changelog — plugin rapido-higgsfield

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
