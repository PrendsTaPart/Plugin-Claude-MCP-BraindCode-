---
name: pilotage-performance-ads
description: Utiliser quand l'utilisateur demande comment performent ses pubs, un bilan pub ou d'optimiser ses campagnes. Lit les métriques réelles (dépense, coût par résultat), les tendances et anomalies, et livre 3 constats + 3 actions classées par opportunité.
---

# Pilotage de performance Ads

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-meta-ads.md`. Skill en LECTURE :
aucune modification sans demande explicite (et alors via les skills dédiés).

## Workflow

1. **Période et champs** — période explicite (défaut : 14 derniers jours).
   `ads_get_field_context` AVANT la requête pour vérifier les champs
   disponibles (spend, results, cost_per_result, roas…).
2. **Métriques** — `ads_get_ad_entities` avec `time_range`/`date_preset`
   OBLIGATOIRE : dépense, résultats, coût par résultat, ROAS par
   campagne/ad set/ad. Le KPI de référence est le COÛT PAR RÉSULTAT (pas le
   CPM ni les clics).
3. **Tendances et anomalies** — `ads_insights_performance_trend` (évolution),
   `ads_insights_anomaly_signal` (décrochages), `ads_get_opportunity_score`
   (points d'opportunité et recommandations).
4. **Comparaison sectorielle** — `ads_insights_industry_benchmark` : situer
   le coût par résultat vs le secteur (préciser la limite : benchmark
   indicatif).
5. **Restitution** :
   ```
   📊 ADS — {période} — dépense totale {devise}
   3 CONSTATS chiffrés (coût/résultat, tendance, anomalie)
   3 ACTIONS classées par points d'opportunité (score)
   ```
   Chaque action pointe le skill d'exécution (`tests-ab-meta` pour tester,
   `creatifs-publicitaires` pour rafraîchir un créatif fatigué,
   `lancement-campagne-meta` pour rebudgéter — modification de budget =
   confirmation).
6. **Boucle business** — rapprocher des données CRM (`get_stats_campagne`,
   leads réellement entrés en pipeline) : le coût par résultat Meta doit se
   lire en coût par CLIENT, pas par clic.

## Garde-fous

- Aucun chiffre sans période explicite ; champs vérifiés avant requête.
- Pas de modification (budget, pause, arrêt) depuis ce skill sans demande
  explicite — et alors avec récap chiffré (hooks actifs).
- Un « mauvais » chiffre sur 2 jours n'est pas une tendance : minimum
  7 jours avant de conclure.
