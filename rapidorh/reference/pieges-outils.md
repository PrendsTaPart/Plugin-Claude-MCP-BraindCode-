# Pièges des outils MCP (rapidorh) — référence rapide

Consulter ce tableau au moindre doute avant d'appeler un outil.

| Outil | Paramètres pièges | Erreur fréquente | Parade |
|---|---|---|---|
| `create-daily-tool` | 1 daily/jour/utilisateur ; `hours` 0,5–24 ; membres uniquement | 2e daily le même jour ; 30 h sur une tâche ; owner qui déclare | Vérifier `get-dailies-tool` (date du jour) AVANT ; borner les heures ; owners = consultation seulement |
| `create-user-tool` | `role_id` + `department_id` REQUIS ; email/username/phone UNIQUES ; envoie l'invitation immédiatement | Utilisateur créé avant le rôle ; invitation partie avec une faute dans l'email | Ordre strict : permissions → rôle → département → utilisateur ; tout valider avant l'appel |
| `create-role-tool` | `permissions` = IDs valides | IDs de permissions devinés | `get-permissions-list-tool` TOUJOURS avant |
| `create-project-tool` | `price` requis ; `priority` 1=basse/2=moyenne/3=haute ; `size` 0/1/2 ; dates `YYYY-MM-DD` (fin > début) | Budget inventé ; échelle de priorité confondue avec celle des tâches | Demander le budget ; retenir : PROJET 1-3 (1=basse), TÂCHE 0-2 (0=urgent) |
| `create-task-tool` | `priority` 0=Urgent/1=Moyenne/2=Faible ; `tasklist_id` réel | Priorité inversée ; ID de colonne deviné | `get-task-lists-tool` pour les IDs ; défaut priorité = 1 |
| `create-task-list-tool` | Todo/Doing/Done déjà créées | Recréation des 3 colonnes de base | Uniquement pour des colonnes SUPPLÉMENTAIRES |
| `move-task-tool` | `from_list` = colonne RÉELLE actuelle | `from_list` deviné → échec | Lire la colonne actuelle via `get-project-tasks-tool` |
| `get-project-tasks-tool` / `get-dailies-tool` | vue selon droits (owner = tout, membre = ses tâches/dailies) | « Tâche introuvable » conclu à tort | Penser aux droits : la revue peut être partielle, le dire |
| (réassignation) | AUCUN outil pour réassigner une tâche existante | Promettre une réassignation impossible | Recréer la tâche avec le bon `assigned_users` + sortir l'ancienne, ou action manuelle dans l'interface |
| `delete-user-tool` / `delete-project-link-tool` | destructifs | Suppression dans un flux d'onboarding | Confirmation explicite (hook ask) ; jamais en onboarding |
| Dates (partout) | `YYYY-MM-DD` strict | Formats libres | Convertir en ISO avant l'appel |
