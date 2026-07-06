---
name: onboarding-equipe
description: Utiliser quand l'utilisateur veut ajouter un employé, créer un rôle ou parle d'onboarding dans RapidoRh. Suit l'ordre obligatoire permissions → rôle → département → utilisateur → affectation projets.
---

# Onboarding équipe

## Ordre OBLIGATOIRE du workflow

Le rôle doit exister AVANT de créer l'utilisateur (`role_id` est requis par
`create-user-tool`). Ne jamais inverser les étapes 1-2 et 4.

1. **Permissions disponibles** — `get-permissions-list-tool` (sans paramètre) :
   obtenir les IDs de permissions valides. Toujours l'appeler AVANT de créer un
   rôle.
2. **Rôle** — vérifier d'abord si un rôle adapté existe (`get-roles-list-tool`) ;
   sinon `create-role-tool` (`name` requis, `permissions` = liste d'IDs de
   l'étape 1). Faire valider la liste des permissions par l'utilisateur (elle
   définit les droits d'accès).
3. **Département** — `get-departments-list-tool` : récupérer le `department_id`
   cible. Si aucun département ne convient, demander à l'utilisateur.
4. **Créer l'employé** — `create-user-tool`. Champs TOUS requis :
   `first_name`, `last_name`, `email` (unique), `username` (unique), `phone`
   (unique), `hours_worked`, `salary`, `leave_days`, `role_id` (étape 2),
   `department_id` (étape 3).
   - ATTENTION : la création déclenche AUTOMATIQUEMENT l'email d'invitation à
     l'employé (définition du mot de passe). Vérifier l'adresse email et faire
     valider l'ensemble des informations (dont salaire) par l'utilisateur AVANT
     l'appel — l'invitation part immédiatement.
5. **Affecter aux projets** — identifier les projets concernés via
   `get-projects-list-tool`, puis assigner le nouvel employé à ses premières
   tâches via `create-task-tool` / `assigned_users` (voir skill flux-kanban).

## Garde-fous

- Jamais de `create-user-tool` sans validation explicite (email, salaire, rôle,
  département) : l'email d'invitation part sans retour possible.
- Données sensibles (salaire) : ne les mentionner que si nécessaire et ne jamais
  les inventer.
- `delete-user-tool` (suppression d'un employé) : action destructrice —
  confirmation explicite obligatoire, jamais dans un flux d'onboarding.
