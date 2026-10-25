---
name: apprendre-une-tache
description: Utiliser quand une tâche demandée n'est pas sue, que l'utilisateur dit « apprends à faire ça », « tu sais faire une relance SMS ? », « comment on fait un devis ici ». Interroge l'Academy sur la tâche (learn_task) et rend le verdict — la faire, l'apprendre d'abord, ou faire construire l'outil manquant.
---

# Apprendre une tâche (faire, apprendre, ou faire construire)

Famille engagée : **apprendre** (Confirmé).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`get_capabilities`** avec le `besoin` dans les mots de l'utilisateur :
   la tâche outillée existe-t-elle (étapes, serveurs, KPI, formations) ?
   Vérifier dans sa propre liste d'outils que chaque connecteur requis est
   branché.
2. **`learn_task`** sur la tâche : la formation qui l'enseigne, le tutoriel
   du logiciel, la procédure déjà retenue en mémoire (`recall`).
3. **Le verdict**, dit explicitement :
   - **FAIRE** : la tâche est connue, les connecteurs sont là → dérouler le
     skill métier correspondant, dans le niveau de sa famille ;
   - **APPRENDRE** : une mission l'enseigne → la suivre d'abord (skill
     `chemin-de-formation`), puis faire une première fois en Aperçu ou en
     Brouillon, mesurer, et retenir la procédure (`remember`, type méthode) ;
   - **FAIRE CONSTRUIRE** : aucun outil ne la couvre → skill
     `construire-l-outil-manquant` (`propose_mcp_tool`), et continuer avec
     le reste de la journée sans bloquer.
4. Une procédure qui a marché se retient avec `remember` (méthode) — jamais
   une coordonnée, jamais un secret (hook garde-memoire).

KPI : `routines-en-service` (chaque semaine, une tâche de plus sait se faire
seule). Formations : celle que `learn_task` désigne.

## Garde-fous

- On n'improvise pas une tâche inconnue « pour voir » : le verdict précède
  le geste.
- Un connecteur manquant se demande à l'humain avec son adresse — jamais
  d'URL inventée.
