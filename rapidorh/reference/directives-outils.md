# Directives communes d'utilisation des outils (rapidorh)

Règles applicables à TOUTE exécution de skill de ce plugin.

## 1. Résolution d'ID d'abord

- Ne JAMAIS deviner un ID : IDs d'utilisateurs, de projets, de colonnes Kanban
  (`tasklist_id`), de tâches, de rôles, de permissions, de départements.
- Récupérer chaque ID via l'outil de liste correspondant
  (`get-users-list-tool`, `get-projects-list-tool`, `get-task-lists-tool`,
  `get-project-tasks-tool`, `get-roles-list-tool`, `get-permissions-list-tool`,
  `get-departments-list-tool`) ou le demander à l'utilisateur, AVANT d'agir.
- Le contexte company/utilisateur est déduit de la session authentifiée ; les
  droits diffèrent entre owner et membre (ex. `get-project-tasks-tool`,
  `get-dailies-tool`).

## 2. Confirmation avant action destructrice ou irréversible

Récapituler l'action et obtenir un accord explicite de l'utilisateur avant :
- `delete-user-tool` (suppression d'employé), `delete-project-link-tool` ;
- `create-user-tool` — la création envoie IMMÉDIATEMENT l'email d'invitation :
  valider email, rôle, département et salaire avant l'appel ;
- un déplacement de tâche en arrière (ex. Done → Doing).

## 3. Ne jamais inventer de données

Salaires, heures travaillées, jours de congé, budgets (`price`), dates : toujours
fournis par l'utilisateur. Valeur manquante → la demander, jamais de défaut
inventé.

## 4. Locale et formats

- Monnaie : euros. Dates ISO `YYYY-MM-DD`.
- Échelles distinctes (ne pas confondre) : priorité PROJET 1 = basse, 2 = moyenne,
  3 = haute ; priorité TÂCHE 0 = urgent, 1 = moyenne, 2 = faible ; taille projet
  0 = petit, 1 = moyen, 2 = grand.
- Dailies : un seul par jour par utilisateur, 0,5 à 24 h par tâche, réservés aux
  membres (pas aux owners), toujours datés d'aujourd'hui.

## 5. Gestion d'erreur

Si un outil échoue : expliquer clairement la cause probable (droits owner/membre,
doublon de daily, unicité email/username/téléphone…), ne PAS boucler ni réessayer
aveuglément, proposer l'alternative manuelle (ex. action dans l'interface
RapidoRh).

## 6. Récapitulatif de fin de séquence

Terminer chaque séquence par la liste des objets créés/modifiés avec leurs IDs
(projets, colonnes, tâches, dailies, rôles, utilisateurs, liens).
