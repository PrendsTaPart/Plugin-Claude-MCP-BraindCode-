---
name: tests-ab-meta
description: Utiliser quand l'utilisateur veut tester deux versions ou un A/B test de pub. Vérifie l'éligibilité, crée les variantes, passe par un dry run, puis crée le test réel et lit les résultats sur le KPI business.
---

# Tests A/B Meta

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-meta-ads.md`. Règle du media-buyer :
UNE variable testée à la fois (accroche OU visuel OU audience — jamais deux).

## Workflow

1. **Hypothèse** — formuler ce qu'on teste et pourquoi (« l'accroche preuve
   sociale bat l'accroche prix ») ; définir le KPI de décision : COÛT PAR
   RÉSULTAT (jamais le CPM ni le CTR seul).
2. **Éligibilité** — `ads_experiment_check_eligibility` : le compte/les
   entités peuvent-ils être testés ? Sinon expliquer le blocage.
3. **Variantes** — 2 versions ne différant QUE par la variable testée :
   créatifs via le skill `creatifs-publicitaires` (2-3 accroches proposées),
   structure via `lancement-campagne-meta` (tout PAUSED).
4. **DRY RUN d'abord** — `ads_experiment_abtest_create_test` en mode dry run :
   vérifier la configuration (variantes, répartition, durée, budget) sans
   rien créer.
5. **Récap puis création réelle** — présenter : variable testée, variantes,
   budget total du test, durée (minimum 7 jours recommandé), KPI de décision.
   Après accord : création réelle (`ads_experiment_abtest_create_test`).
   L'activation des entités reste soumise aux confirmations habituelles.
6. **Lecture des résultats** — `ads_experiment_abtest_get_test` à
   l'échéance : décision sur le COÛT PAR RÉSULTAT avec le volume atteint ;
   si l'écart n'est pas net (chevauchement), le dire — « pas de gagnant » est
   un résultat valide.
7. **Capitaliser** — noter l'enseignement dans `ton-et-accroches.md` (via
   `mise-a-jour-kb`, avec accord) : les accroches gagnantes nourrissent les
   prochains créatifs.

## Garde-fous

- Pas de test multi-variables ; pas de conclusion avant la fin de la durée
  prévue (pas d'arrêt au bout de 2 jours sur un faux signal).
- Budget du test soumis au plafond maison (hook) ; étude de lift
  (`ads_experiment_lift_create_test`) = payante, confirmation dédiée.
- Un test = une décision documentée (gagnant, perdant, ou non conclusif).
