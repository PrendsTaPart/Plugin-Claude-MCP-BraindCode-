# Changelog — plugin rapido-tiktok-ads

## 0.1.0 — 2026-07-15 — Plugin TikTok Ads verrouillé

- Nouveau plugin **rapido-tiktok-ads** (20e du marketplace) — TikTok Ads en
  lecture/écriture, **verrous argent réel plus stricts** que `rapido-meta-ads`.
  Serveur non connecté → skills d'après le cycle campagne documenté.
- `.mcp.json` : `tiktok-ads` (`TIKTOK_ADS_MCP_URL`) + ponts rapidocms/rapidocrm.
- `reference/garde-fous-tiktok.md` : création toujours inactive (sinon lecture
  seulement) ; budget max annoncé ; activation = confirmation écrite séparée ;
  jamais > X €/jour (KB).
- **3 skills** : `pilotage-performance-tiktok` (CPM/CPC/CPA, comparatif vs Meta via
  catalogue-kpi), `lancement-campagne-tiktok` (campagne→ad group→créatif→ad **100 %
  inactif**, activation séparée), `tendances-creatives-tiktok` (formats/hooks ; brief
  → rapidocms/rapido-video ; frontière avec `rapido-seo:tendances-marche`).
- **Hooks** : `garde-argent-reel-tiktok` (**DENY** création active, **ASK**
  activation/budget) + `Stop` (récap IDs/statuts/budgets/coût max). Tests au testeur.
