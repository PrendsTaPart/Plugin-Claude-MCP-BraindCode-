---
name: mes-taches
description: Utiliser quand on gère les tâches simples Plan'It, que l'utilisateur dit « qu'est-ce que j'ai de prévu cette semaine », « reporte mon rappel à lundi », « est-ce que ma tâche a tourné », « pourquoi elle a échoué ». Liste, crée, reprogramme et diagnostique les tâches — la suppression seulement après confirmation.
---

# Mes tâches (rappels et actions ponctuelles)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. **Tâche ≠ routine** : si la demande est récurrente avec un objectif
   chiffré, c'est le skill `creer-une-routine` — pas celui-ci.

## Workflow

1. **`list_tasks`** avec les filtres utiles (type tâche simple, statut,
   fréquence, plage de dates d'échéance) — « mes tâches en retard », « la
   semaine » se répondent ici. Pour la santé des ROUTINES :
   `list_routines` (skill `auditer-mes-routines`).
2. **`get_task`** pour le détail d'une tâche nommée (description, fréquence,
   prochaine échéance, statut, prompt associé).
3. **Créer** : `create_task` — un rappel ou une action ponctuelle (fréquence
   `custom` autorisée ici). Pour une tâche qui EXÉCUTE un outil :
   `list_task_prompts` d'abord (connecteurs réellement connectés), puis
   `create_task` avec `prompt_id` — jamais pour un simple rappel.
4. **Reporter / reprogrammer / corriger** : `update_task` (titre,
   description, fréquence, échéance, statut).
5. **« Ça a tourné ? Pourquoi échoué ? »** : `get_task_executions` — dates,
   statut par exécution, résultat, message d'erreur. Un état ≠ done ne veut
   jamais dire « exécuté ».
6. **Supprimer** : `delete_task` UNIQUEMENT après confirmation explicite —
   l'action est irréversible et emporte les notifications (le hook
   garde-planit demande de toute façon).

## Garde-fous

- Ne jamais transformer silencieusement une tâche en routine (ou l'inverse) :
  la qualification se dit et se valide.
- Un échec d'exécution se diagnostique (message d'erreur, connecteur —
  `test_mcp_server` au besoin via le skill `connecteurs-mcp`) avant toute
  reprogrammation.
