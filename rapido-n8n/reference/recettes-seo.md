# Recettes d'acquisition (SEO / SEA / TikTok) — n8n

> Le **rank-tracking récurrent et toute requête DataForSEO en volume DOIVENT vivre en
> n8n** (coût DataForSEO gouverné), **jamais en conversationnel**. Format maison :
> déclencheur, pseudo-nœuds, table mémoire, garde-fous. Identifiants au registre
> unifié (`SEO-*`, `SEA-*`, `TIKTOK-*`). Installation **sur confirmation**, recette
> par recette, via `usine-automatisations` — **aucun workflow créé d'office**.

## SEO-HEBDO — positions & striking distance (lundi)
- **Déclencheur** : Schedule cron `0 7 * * 1`.
- **Workflow (pseudo-nœuds)** : Schedule → **GSC** (search analytics : positions,
  impressions, CTR) → détecter **striking distance** (position 8-20, fortes
  impressions) → **3 actions contenu** priorisées → **email interne** (brouillon).
  Requêtes DataForSEO éventuelles **bornées** (budget mensuel KB).
- **Table mémoire** : `seo_positions_journal` (`date`, `requete`, `position`,
  `impressions`, `action`) — série des positions, anti-double-alerte.
- **Garde-fous** : coût DataForSEO **plafonné** (KB) ; alerte **interne** ; écriture
  CMS **confirmée** ; fraîcheur GSC (J-3) rappelée.

## SEO-MENSUEL — backlinks & audit delta (1er du mois)
- **Déclencheur** : Schedule cron `0 7 1 * *`.
- **Workflow** : Schedule → **DataForSEO Backlinks** (new/lost, referring domains) →
  **delta d'audit OnPage** vs mois précédent → **rapport interne** (brouillon).
  **Coût DataForSEO annoncé/plafonné.**
- **Table mémoire** : `seo_backlinks_journal` (`mois`, `refdomains`, `new`, `lost`,
  `audit_delta`).
- **Garde-fous** : requête backlinks **facturée** → dans le budget KB ; jamais en
  conversationnel.

## SEA-HEBDO — gaspillage & synergie SEO/SEA (hebdo)
- **Déclencheur** : Schedule hebdomadaire.
- **Workflow** : Schedule → **Google Ads** (lecture : gaspillage, requêtes non
  pertinentes) → croisement **GSC** (mots-clés payés déjà rankés top 3) → **email
  interne** : économies + opportunités paid. **Lecture seule** → actions **manuelles**.
- **Table mémoire** : `sea_synergie_journal` (`date`, `economie_estimee`,
  `opportunites`, `traite`).
- **Garde-fous** : **aucune écriture** Google Ads (read-only) ; recommandations
  **sourcées** ; budgets **plafonds KB**.

## TIKTOK-HEBDO — performance & arbitrage (si compte actif)
- **Déclencheur** : Schedule hebdomadaire.
- **Workflow** : Schedule → **TikTok Ads** (lecture : CPM/CPC/CPA, créatifs) →
  comparatif **vs Meta** (mêmes KPIs) → **email interne** (brouillon).
- **Table mémoire** : `tiktok_perf_journal` (`date`, `cpa`, `cpm`, `arbitrage`).
- **Garde-fous** : lecture pour le reporting ; toute **écriture** TikTok reste
  **verrouillée** (création inactive + confirmation, hors recette).

## Installation
Proposer chaque recette avec sa cadence, son périmètre et sa table mémoire ;
**installer seulement celles confirmées**. Un workflow sans table mémoire n'est pas
installé. Le coût DataForSEO récurrent est **gouverné** (plafond mensuel KB).
