---
name: business-plan
description: Utiliser quand on travaille le plan d'affaires de la zone, que l'utilisateur dit « fais ton business plan », « simule : et si on signait 6 clients par mois », « transforme le plan en objectifs ». Construit le business plan Academy étape par étape, joue les scénarios, puis en fait les objectifs KPI de l'employé.
---

# Business plan (du plan aux objectifs chiffrés)

Famille engagée : **configurer** (Confirmé au cadre actuel — écritures
Academy avec aperçu serveur puis confirm).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`. KB lue si
présente (prix, zone, charges y vivent parfois).

## Workflow

1. **`create_business_plan`** (ou reprendre l'existant :
   `list_business_plans`, `get_business_plan`).
2. **`get_business_plan_questions`** étape par étape — poser les questions de
   l'étape, recueillir les réponses RÉELLES (jamais de chiffre rempli à la
   place de l'utilisateur), puis **`answer_business_plan_questions`**
   (aperçu → accord → confirm). `set_business_plan_assumptions` pour les
   hypothèses, `edit_business_plan_text` pour la prose.
3. **Les « et si »** : `simulate_business_plan` — un scénario à la fois, la
   variable changée dite explicitement, le résultat restitué tel que renvoyé.
4. **Du plan aux objectifs** : `set_goals_from_business_plan` — ce sont ces
   objectifs que `point-du-matin` compare chaque jour.
5. Pour le présenter : skill `pitch` (`create_pitch_deck` depuis le plan).

KPI : `mrr`, `abonnements-signes`, `objectifs-atteints`.
Formations : `business-plan` (8 missions), `reporting`.

## Garde-fous

- Aucune promesse de revenus : une simulation est une hypothèse datée, pas
  un engagement — le dire à chaque restitution.
- Les hypothèses viennent de l'utilisateur, de la KB ou d'une source citée ;
  une donnée manquante se dit manquante.
