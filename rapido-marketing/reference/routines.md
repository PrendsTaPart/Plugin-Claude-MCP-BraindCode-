# Routines marketing récurrentes (n8n)

> **Identifiants canoniques** (registre unifié `reference/registre-routines.md`,
> racine du monorepo, fait foi) : `MKT-HEBDO`, `MKT-QUOTIDIEN`, `MKT-MENSUEL`. Les
> noms `R-MKT-*` ci-dessous restent des **alias reconnus** (rétrocompatibilité).

Trois routines pilotées par `pilotage-marketing`, **proposées puis installées sur
confirmation** via `rapido-n8n:usine-automatisations`. Chacune a son workflow n8n
et sa **table mémoire** (mémoire d'exécution = tables n8n, cf. `reference/memoire.md`) ;
aucune n'envoie ni ne publie sans le garde-fou `garde-envois`.

> Règle : le récurrent et le volume vivent en n8n (`reference/cout-ia.md`), pas en
> appels modèle un par un. Une routine ne **prépare** et **alerte** ; toute action
> visible reste confirmée par un humain.

## R-MKT-HEBDO — rapport de pilotage (lundi)
- **Objectif** : produire le rapport une page de `pilotage-marketing` (KPI vs
  objectifs, actions, décisions à prendre) en début de semaine.
- **Déclencheur** : Schedule Trigger cron `0 7 * * 1` (lundi 07:00, fuseau KB).
- **Workflow n8n** : Schedule → collecte lecture (HTTP RapidoCRM/CMS/Meta :
  attribution, pipeline, contenus, pubs) → calcul KPI (node Code = script) →
  composition du rapport → notification (email interne **en brouillon**, jamais
  envoi client).
- **Table mémoire** : `mkt_pilotage_journal` (`date`, `resume`, `kpi_json`,
  `decisions`, `ids`) — historise chaque rapport, sert de base au FEED.

## R-MKT-QUOTIDIEN — sentinelle (tous les jours)
- **Objectif** : détecter deux fuites : **leads non traités > 24 h** et
  **soumissions de formulaires orphelines** (non rattachées à un prospect).
- **Déclencheur** : Schedule Trigger cron `0 8 * * *` (08:00).
- **Workflow n8n** : Schedule → RapidoCRM (leads du pipeline + `get_formulaire_soumissions`)
  → filtre âge > 24 h / soumission sans prospect lié → si trouvés, alerte interne
  avec la liste → proposition d'action (relance / rattachement), **jamais exécutée
  d'office**.
- **Table mémoire** : `mkt_sentinelle_leads` (`date`, `lead_id`, `type_alerte`,
  `signale_le`, `resolu`) — anti-double-alerte (ne pas re-signaler un lead déjà
  ouvert non résolu).

## R-MKT-MENSUEL — board marketing (1er du mois)
- **Objectif** : board mensuel = **attribution par canal + benchmarks + décisions**
  (arbitrage budget/canaux).
- **Déclencheur** : Schedule Trigger cron `0 7 1 * *` (1er du mois, 07:00).
- **Workflow n8n** : Schedule → collecte mensuelle (attribution multi-source,
  dépenses, funnel) → calcul (node Code = script, formules) → comparaison à
  `benchmarks.md` → board une page → notification interne en brouillon.
- **Table mémoire** : `mkt_board_mensuel` (`mois`, `attribution_json`,
  `benchmarks_json`, `decisions`, `ids`) — série mensuelle pour les tendances.

## Installation
Proposer les 3 routines avec leur cron et leur périmètre ; **installer seulement
celles confirmées** via `rapido-n8n:usine-automatisations`. Un workflow qui n'a
pas sa table mémoire n'est pas installé (anti-doublon impossible sinon).
