---
name: setup-projet
description: Utiliser quand l'utilisateur veut créer un projet ou parle d'un nouveau projet dans RapidoRh. Récupère les IDs valides, crée le projet avec ses paramètres, puis ajoute colonnes et liens si demandé.
---

# Setup d'un projet

## Workflow

1. **Récupérer les IDs valides** — `get-users-list-tool` (filtres `search`,
   `status` = 1 actif, `role_id`, `department_id`) pour identifier le chef de
   projet et les employés. Ne JAMAIS inventer un ID utilisateur.
2. **Créer le projet** — `create-project-tool`. Champs TOUS requis :
   - `name`, `start_date` / `end_date` au format YYYY-MM-DD (fin strictement
     après début) ;
   - `price` : budget numérique (ex. 15000) — le demander s'il n'est pas donné ;
   - `priority` PROJET : 1 = basse, 2 = moyenne, 3 = haute (≠ priorité des
     tâches) ;
   - `size` : 0 = Petit, 1 = Moyen, 2 = Grand ;
   - `project_manager_id` + `employees` (liste d'IDs, étape 1).
   Pas de logo via MCP — le signaler si demandé.
3. **Colonnes Kanban** — Todo, Doing et Done sont créées AUTOMATIQUEMENT avec le
   projet : ne pas les recréer. Ajouter des colonnes supplémentaires UNIQUEMENT si
   l'utilisateur le demande : `create-task-list-tool` (`project_id`, `name` —
   ex. « Review », « En validation », « Bloqué »).
4. **Liens externes** — `create-project-link-tool` (`project_id`, `url` valide et
   complète, ex. `https://figma.com/file/xxx`). Retrouver le `project_id` via
   `get-projects-list-tool` (`search`, `statuses` : 0 en cours, 1 terminé,
   2 archivé) si besoin.

## Garde-fous

- Récapituler les paramètres (dates, budget, priorité, taille, équipe) et faire
  valider par l'utilisateur AVANT `create-project-tool`.
- Demander les informations manquantes (budget, dates) plutôt que d'inventer des
  valeurs par défaut.
- Ne pas confondre les échelles : priorité projet 1-3 (1=basse) vs priorité tâche
  0-2 (0=urgent) — voir skill flux-kanban.
