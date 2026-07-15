# Changelog — plugin rapido-seo

## 0.1.0 — 2026-07-15 — Fondations + 6 skills (organique)

- Nouveau plugin **rapido-seo** (18e du marketplace) — acquisition **organique**
  pilotée par les données. Serveurs SEO non connectés → skills écrits d'après les
  grammaires documentées (pattern « construire d'abord », comme ElevenLabs E1).
- `.mcp.json` : `dataforseo` (hébergé, `DATAFORSEO_AUTH`), `gsc` (`GSC_MCP_URL`),
  `analytics`/GA4 (`GA4_MCP_URL`) + ponts rapidocms/rapidocrm. Clés en env, jamais
  dans le dépôt.
- `reference/garde-fous-seo.md` : coûts DataForSEO (facturation à l'appel, > ~10
  unités annoncées, volume → n8n), GA4/Google Ads **read-only**, fraîcheur GSC
  (J-2/J-3, requêtes rares anonymisées), contenu publié **modifié après confirmation**.
- `reference/kb-templates/` : `seo-cibles.md`, `netlinking.md`.
- **6 skills** : `audit-seo-technique` (OnPage), `recherche-mots-cles` (Labs/Keywords ;
  anti-collision `geo-optimization`), `netlinking` (Backlinks + outreach délégué),
  `performance-organique` (GSC+GA4, fraîcheur dite), `tendances-marche` (Trends +
  TikTok best-effort → calendrier-editorial), **`pilotage-seo`** (orchestrateur
  Sense→Plan→Act→Feed→Report, ICE `scripts/prioriser_seo.py`, sous-domaine de
  `pilotage-marketing`).
- **Hooks** : `garde-couts-seo` (ask sur familles DataForSEO facturées sans
  `cout_confirme`) + `Stop` (récap coûts + fraîcheur GSC + lecture seule). Tests au testeur.
