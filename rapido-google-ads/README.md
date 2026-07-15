# rapido-google-ads

**SEA Google Ads en LECTURE SEULE.** Le MCP officiel Google Ads est *read-only by
design* : ce plugin **analyse et recommande** (pilotage, audit, mots-clés payants,
synergie SEO/SEA) — l'**exécution est manuelle** dans l'interface Google Ads, guidée
par des instructions écran par écran. Calqué sur `rapido-meta-ads`.

> **MCP Google Ads non encore connecté** : skills écrits d'après la grammaire
> documentée (lecture seule) ; noms d'outils exacts confirmés à la connexion.

## Connecteurs (`.mcp.json`) — clés en variables d'env
| Serveur | Config | Env |
|---|---|---|
| **google-ads** (officiel, read-only) | passerelle HTTP | `GOOGLE_ADS_MCP_URL` (+ developer token / OAuth côté serveur) |
| **dataforseo** | hébergé | `DATAFORSEO_AUTH` (CPC/volumes payants) |
| **analytics** (GA4) | passerelle HTTP | `GA4_MCP_URL` (croisement conversions) |
| rapidocrm | pont | — |

## Checklist (une fois, côté comptes)
- [ ] **Google Ads** : developer token (validation Google parfois nécessaire) + OAuth.
- [ ] **GA4** : credentials scope `analytics.readonly` (croisement conversions).
- [ ] **Plafonds** `./rapido-kb/` : budget pub max/jour.

## Skills
- **`pilotage-performance-google-ads`** — dépense/conversions/CPA/ROAS, 3 constats + 3 actions manuelles.
- **`recherche-mots-cles-sea`** — CPC/volumes (DataForSEO), structure SKAG/STAG, négatifs (≠ organique).
- **`audit-compte-google-ads`** — gaspillage, Quality Score, chevauchements, extensions, écarts conversions vs GA4.
- **`synergie-seo-sea`** — croise GSC + Google Ads : économies (top 3 organique payé), opportunités paid, cohérence messages.

## Garde-fous
`reference/garde-fous-sea.md` : **lecture seule** (jamais d'exécution promise) ;
recommandations **sourcées** ; budgets **plafonds KB** ; hook `garde-ecriture-google-ads`
(ask si un outil `mutate`/`create` apparaît) ; calculs via `catalogue-kpi`.
