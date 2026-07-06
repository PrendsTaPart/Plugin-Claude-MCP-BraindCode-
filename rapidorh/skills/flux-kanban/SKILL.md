---
name: flux-kanban
description: Utiliser quand l'utilisateur veut créer une tâche, assigner une tâche, déplacer une tâche ou parle du Kanban d'un projet RapidoRh. Gère la création et le déplacement des tâches entre colonnes.
---

# Flux Kanban

## Workflow

1. **Identifier le projet** — `get-projects-list-tool` (`search` par nom) si le
   `project_id` n'est pas connu.
2. **Récupérer les colonnes** — `get-task-lists-tool` (`project_id`) : obtenir les
   IDs réels des colonnes (Todo, Doing, Done + colonnes personnalisées). Ne JAMAIS
   supposer un ID de colonne.
3. **Créer une tâche** — `create-task-tool` (`project_id`, `tasklist_id` — en
   général l'ID de « Todo » —, `title` requis ; optionnels : `description`,
   `due_date` YYYY-MM-DD, `assigned_users` = IDs via `get-users-list-tool`,
   `priority` TÂCHE : 0 = Urgent, 1 = Moyenne (défaut), 2 = Faible).
   - Attention : échelle inversée par rapport à la priorité projet (1-3, 1=basse).
4. **Déplacer une tâche** — `move-task-tool` (`project_id`, `task_id`,
   `from_list`, `to_list`).
   - Retrouver le `task_id` et sa colonne actuelle via `get-project-tasks-tool`
     (`project_id`, filtre `tasklist_id` optionnel) ;
   - `from_list` doit être la colonne RÉELLE actuelle de la tâche (vérifier, ne
     pas deviner) ;
   - flux nominal : Todo → Doing → Done ; un retour en arrière (ex. Done → Doing)
     est possible mais doit être confirmé par l'utilisateur.

## Garde-fous

- `get-project-tasks-tool` retourne toutes les tâches pour un owner, mais
  uniquement les tâches assignées pour un membre : si une tâche est introuvable,
  c'est peut-être une question de droits — le signaler.
- Ne jamais assigner un utilisateur sans vérifier son ID via `get-users-list-tool`.
- Récapituler après action : tâche, colonne source → destination, assignés.
