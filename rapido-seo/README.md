# rapido-seo

**SEO & acquisition organique pilotés par les données** : audit technique, recherche
de mots-clés, netlinking, Search Console, GA4, tendances — **lecture d'abord**, coûts
DataForSEO **gouvernés**. Orchestrateur `pilotage-seo` (sous-domaine organique de
`rapido-marketing:pilotage-marketing`).

> **Serveurs SEO non encore connectés** : les skills sont écrits d'après les
> grammaires **documentées** (GA4, GSC, DataForSEO) ; les noms d'outils exacts se
> confirment à la connexion (checklist ci-dessous). Pattern « construire d'abord »
> déjà validé (ElevenLabs E1).

## Connecteurs (`.mcp.json`) — clés UNIQUEMENT en variables d'env
| Serveur | Nature | Config | Variables d'env |
|---|---|---|---|
| **dataforseo** | hébergé (HTTP) `mcp.dataforseo.com/mcp` | pay-as-you-go | `DATAFORSEO_AUTH` (Basic login:password encodé) |
| **gsc** | communautaire (`AminForou/mcp-gsc`) | via passerelle HTTP | `GSC_MCP_URL` |
| **analytics** (GA4) | officiel Google (`googleanalytics/google-analytics-mcp`) | via passerelle HTTP | `GA4_MCP_URL` |
| rapidocms / rapidocrm | pont contenu / outreach | URL produit | — |

> GA4 et le futur Google Ads MCP sont **read-only by design** — ces skills
> **analysent et recommandent**, ils n'écrivent pas.

## Checklist de mise en route (une fois, côté comptes)
- [ ] **GA4** : projet Google Cloud + APIs Analytics activées + credentials scope `analytics.readonly`.
- [ ] **GSC** : propriété vérifiée + OAuth/service account (serveur communautaire).
- [ ] **DataForSEO** : compte + crédits pay-as-you-go + login/password API (`DATAFORSEO_AUTH`).
- [ ] **Plafonds** dans `./rapido-kb/` : budget DataForSEO max/mois.

## Skills
- **`audit-seo-technique`** — audit OnPage (erreurs, balises, vitesse, maillage), priorisé par impact.
- **`recherche-mots-cles`** — volumes/difficulté/intention (search classique ; ≠ `geo-optimization` génératif).
- **`netlinking`** — profil backlinks, new/lost, gap concurrents ; outreach → `rapidocrm:draft-outreach`.
- **`performance-organique`** — GSC + GA4 (striking distance, CTR, conversions ; fraîcheur dite).
- **`tendances-marche`** — Google Trends (DataForSEO) + TikTok best-effort → `rapidocms:calendrier-editorial`.
- **`pilotage-seo`** — l'orchestrateur (Sense→Plan→Act→Feed→Report), sous-domaine de `pilotage-marketing`.

## Garde-fous
`reference/garde-fous-seo.md` : coûts DataForSEO annoncés (hook `garde-couts-seo`) +
volume → n8n ; GA4/Google Ads lecture seule ; fraîcheur GSC précisée ; contenu publié
modifié **seulement après confirmation** (via RapidoCMS). Calculs via `catalogue-kpi`.
