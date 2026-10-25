---
name: point-du-matin
description: Utiliser quand l'employé fait ses chiffres du matin, que l'utilisateur dit « fais ton point du matin », « où en sont tes KPI », « relève les chiffres et choisis tes tâches ». Lit chaque KPI dans l'outil que l'Academy indique, l'enregistre avec sa source, compare aux objectifs et choisit les tâches du jour qui rapprochent le plus de l'objectif.
---

# Point du matin (les chiffres d'abord)

Familles engagées : **apprendre** (lectures) + **configurer**
(`record_kpi`, niveau Confirmé au cadre actuel).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Cadre du jour absent ou périmé → skill `prise-de-poste` d'abord.

## Workflow

1. **`get_kpi_sources`** (Academy) — pour chaque KPI suivi : l'outil et le
   serveur où le lire. C'est la carte, on ne lit pas ailleurs.
2. **Lire chaque KPI à sa source**, serveur par serveur, par exemple :
   - RapidoCRM : `get_dashboard_kpis`, `get_stats_pipeline`,
     `get_conversion_par_canal` ;
   - Site FoodEatUp (inbound) : `get_inbound_stats` ;
   - Prospector Hub : `stripe_stats` (clients, MRR estimé) ;
   - RapidoCMS : `post_insights` / `ingishts_campagne` ;
   - FoodEatUp : `get_daily_brief` si la source le désigne.
   Serveur absent → la ligne KPI est marquée « source indisponible », jamais
   estimée.
3. **`record_kpi`** pour chaque valeur lue, AVEC la source — une mesure par
   KPI et par jour, l'horodatage métier fait foi.
4. **Comparer aux objectifs** (ceux posés par `set_goals_from_business_plan`,
   relus via `get_my_kpis` / `get_kpi_dashboard`) : écart par KPI, tendance.
5. **Choisir les tâches du jour** : celles qui rapprochent le plus de
   l'objectif le plus en retard (`get_capabilities` avec le besoin pour
   retrouver la tâche outillée). Les proposer dans l'ordre, avec la famille
   d'autonomie de chacune, puis dérouler via les skills du groupe vendre /
   communiquer / servir.
6. Option : widget `tableau-de-bord-kpi` pour l'affichage.

KPI que ce skill fait bouger : tous (c'est lui qui les mesure) — en
particulier `rdv-tenus`, `pipeline`, `demandes-entrantes`, `mrr`.
Formations : `reporting` (8 missions), `business-plan`.

## Garde-fous

- Un chiffre absent se dit absent ; aucune moyenne « de tête » (tout calcul
  passe par un script stdlib, formule affichée).
- `record_kpi` sans source relevée = interdit — la source fait partie de la
  mesure.
- Le choix des tâches s'explique en une phrase par tâche (« parce que le KPI
  X est à Y contre Z visé »), jamais « au feeling ».
