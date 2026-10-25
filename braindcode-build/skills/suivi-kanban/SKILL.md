---
name: suivi-kanban
description: Utiliser quand le tableau Build se consulte ou se tient — « montre le kanban du projet », « ajoute une carte », « passe la carte en bloquée ». get_board, cartes ajoutées et mises à jour, validations et blocages visibles.
---

# Suivi kanban du projet

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` (le journal
  d'exécution).

## Démarche
1. **Lire** : `get_board` (include_prompts pour voir les prompts des
   cartes) — colonnes, cartes en cours, à valider, bloquées.
2. **Ajouter** : `add_task` — une carte par travail réel, avec son
   livrable ; pas de cartes décoratives.
3. **Mettre à jour** : `update_task` — statut, résultat, lien ; les
   cartes d'étapes du plan restent pilotées par start/complete_prompt_step
   (skill `executer-le-plan`), on ne les double pas.
4. **Ce qui attend** : `get_pending_validations` affiché avec le board —
   une carte « à valider » sans validation ouverte est une incohérence à
   corriger.
5. **Bloquer proprement** : `report_blocker` (sans secret) plutôt qu'une
   carte qui stagne sans explication.

## Pièges
- Deux sources de vérité (board + notes locales) divergent vite : le
  board Build fait foi.

## Dégradation propre
Board vide : proposer d'initialiser par `get_prompt_execution_plan`
(skill `executer-le-plan`), pas de colonnes inventées.
