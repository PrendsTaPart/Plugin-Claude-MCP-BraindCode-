# Changelog — plugin rapido-google-ads

## 0.1.0 — 2026-07-15 — Plugin SEA lecture (pilotage, audit, synergie SEO/SEA)

- Nouveau plugin **rapido-google-ads** (19e du marketplace) — SEA Google Ads en
  **LECTURE SEULE** (MCP officiel read-only). Analyse et recommande ; exécution
  **manuelle** guidée. Calqué sur `rapido-meta-ads`. Serveur non connecté → skills
  d'après la grammaire documentée.
- `.mcp.json` : `google-ads` (`GOOGLE_ADS_MCP_URL`), `dataforseo` (CPC), `analytics`/GA4
  (croisement conversions) + pont rapidocrm. Clés en env.
- `reference/garde-fous-sea.md` : lecture seule assumée, recommandations sourcées,
  budgets plafonds KB, jamais de promesse d'exécution.
- **4 skills** : `pilotage-performance-google-ads` (3 constats + 3 actions manuelles ;
  anti-collision Meta homonyme), `recherche-mots-cles-sea` (CPC/SKAG-STAG/négatifs ;
  frontière avec `rapido-seo:recherche-mots-cles`), `audit-compte-google-ads`
  (gaspillage, QS, écarts conversions Google Ads/GA4), `synergie-seo-sea` (croise
  GSC + Google Ads : économies + opportunités paid).
- **Hooks** : `garde-ecriture-google-ads` (ask sur `mutate`/`create` — filet si le
  serveur évolue vers l'écriture) + `Stop` (recommandations sourcées, actions manuelles).
