---
name: lancement-campagne-meta
description: Utiliser quand l'utilisateur veut lancer une pub, une campagne Facebook/Instagram ou sponsoriser son activité. Construit campagne → ad set → créatif → ad (tout en PAUSED), récapitule le coût maximum et n'active qu'après accord explicite.
---

# Lancement de campagne Meta

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-meta-ads.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md`. `advertiser_request` = mots
exacts de l'utilisateur à chaque appel.

## Workflow

1. **Brief** — traduire l'objectif BUSINESS en objectif ODAX : venir manger /
   visiter le site → OUTCOME_TRAFFIC ; réserver/acheter → OUTCOME_SALES ;
   laisser ses coordonnées → OUTCOME_LEADS ; notoriété locale →
   OUTCOME_AWARENESS ; engagement → OUTCOME_ENGAGEMENT. Cible (zone), budget/
   jour, durée. Catégorie spéciale (crédit/emploi/logement/politique) ?
   Demander si le secteur est concerné.
2. **Compte et devise** — `ads_get_ad_accounts` : `currency`,
   `min_daily_budget_cents`, `is_ads_mcp_enabled` ; `ads_get_ad_account_pages`
   pour le `page_id`. Budget converti en CENTIMES de la devise du compte —
   vérifier le plafond maison (`processus-internes.md`, défaut 50 €/jour).
3. **Campagne (CBO)** — `ads_create_campaign` (objectif ODAX, budget au niveau
   campagne, PAUSED d'office). Noter le `recommended_optimization_goal` du
   retour.
4. **Ad set** — `ads_create_ad_set` (optimization_goal = celui recommandé,
   ciblage LARGE `geo_locations` — ville + rayon pour un restaurant, jamais
   d'IDs d'intérêts inventés, DSA auto en UE). PAS de `daily_budget` ici
   (CBO → rejet « Must Use Campaign Bid Strategy »).
5. **Créatif** — skill `creatifs-publicitaires` (visuel + texte + CTA adapté à
   l'objectif) → `ads_create_ad` (PAUSED) → `ads_get_ad_preview` : montrer
   l'aperçu par placement.
6. **RÉCAP COMPLET avant activation** — campagne/ad set/ad (IDs, statuts
   PAUSED), cible, budget/jour en devise réelle, durée, **COÛT MAXIMUM
   estimé** (budget × jours). Attendre l'accord explicite.
7. **Activation TOP-DOWN** — uniquement après accord : `ads_activate_entity`
   campagne → ad set → ad (le hook demandera confirmation — c'est normal).
8. **Lier au CRM** — `create_campagne` (RapidoCRM : nom, canal, budget,
   dates) pour suivre la campagne dans le pipeline marketing.
9. **Suivi** — à J+2/J+3 : `ads_get_opportunity_score` + skill
   `pilotage-performance-ads`.

## Garde-fous

- Rien n'est activé sans le récap de l'étape 6 validé ; tout reste PAUSED
  sinon (et on le dit).
- Budget sous `min_daily_budget_cents` = rejet : proposer le minimum du compte.
- Petit budget test d'abord (voir agent `media-buyer`) : 10 €/j × 5 j avant
  de scaler.
