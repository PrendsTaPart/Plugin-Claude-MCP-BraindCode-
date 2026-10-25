---
name: ma-certification
description: Utiliser quand l'employé fait le point sur sa certification, que l'utilisateur dit « où en est ta certification », « quels badges as-tu », « que te manque-t-il pour le diplôme », « quelles sont tes forces et faiblesses ». Lit les exigences du diplôme, l'état de préparation, les badges et le profil de compétences, et en tire les prochaines formations.
---

# Ma certification (l'état, les preuves, la suite)

Famille engagée : **apprendre** (lectures seules).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`get_diploma_requirements`** — ce que le diplôme exige, noir sur blanc.
2. **`get_diploma_readiness`** — où on en est face à ces exigences ; et
   `get_diploma_evidence` pour les preuves déjà déposées.
3. **`list_my_badges`** et **`get_skill_profile`** — badges acquis, forces
   et points faibles par compétence.
4. **`get_learning_recommendations`** — les formations recommandées pour
   combler l'écart ; les proposer dans l'ordre du gain (ce qui débloque le
   diplôme d'abord), puis passer au skill `chemin-de-formation`.
5. Restituer en une page : acquis / manquant / prochaine étape datée.
   Option : widget `progression-formation-et-badges`.

KPI : `objectifs-atteints`. Formations : celles que la recommandation
renvoie — jamais une liste de tête.

## Garde-fous

- Le diplôme et l'examen se passent DANS L'APPLICATION : aucun outil ne les
  délivre, Claude ne les promet pas et ne « valide » rien.
- Les points faibles se citent tels que le profil les renvoie — sans
  dramatiser ni flatter.
