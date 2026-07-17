# Convention « relais par tâche » — passer un ordre à un agent (ou un employé) via le Kanban

Une routine, un chef de projet ou un agent qui **délègue un travail** ne se contente
pas d'un titre : la tâche Kanban doit porter **tout ce qu'il faut pour l'exécuter sans
retour en arrière**. C'est le contrat que lit `tournee-des-agents`.

> **Réalité outils (vérifiée)** : RapidoRh n'expose **ni outil de commentaire, ni
> mise à jour de tâche, ni réassignation**. Le seul champ texte libre d'une tâche est sa
> **`description`** (créée avec `create-task-tool`). Donc « le commentaire de la carte »
> = la **`description`**, écrite **à la création**. Quand RH V2 exposera des commentaires
> de tâche ou une mise à jour, le résultat de tournée s'y ajoutera ; aujourd'hui il vit
> dans le **récap de tournée** et se reflète par le **déplacement de colonne**.

## (a) Assignation — à qui

1. **Si RH V2 le permet** (utilisateur-agent réel dans `get-users-list-tool`) :
   assigner via `assigned_users` = l'ID de l'utilisateur-agent.
2. **Sinon (aujourd'hui)** : préfixer le **titre** de `[AGENT:{nom}]` — c'est ce préfixe
   qui rend la tâche **découvrable** par la tournée. Le mettre **dans tous les cas** où
   aucun utilisateur-agent n'existe.

Exemple de titre : `[AGENT:copywriter-social] Rédiger les 3 posts LinkedIn de la semaine`.

## (b) Le brief, dans la `description` de la tâche

La `description` contient un **bloc RELAIS** structuré et **variables résolues**
(aucun `{placeholder}` non résolu, aucune donnée inventée — cf. `directives-outils.md`) :

```
--- RELAIS ---
PROMPT: <le prompt EXACT à exécuter, toutes variables déjà résolues>
LIVRABLE: <ce qui doit être produit, format compris>
DONE: <critère de done vérifiable — comment on sait que c'est fini>
AUTONOMIE: <0 | 1 | 2 | 3>   # cf. reference/autonomie.md
ROUTINE: <étiquette de la routine d'origine — ex. STARTUP-BUILDER, GROWTH-LOOP, ou "manuel">
```

- **PROMPT** : ce que l'exécutant (skill/agent) doit faire, écrit comme un ordre
  auto-suffisant. Pas « voir la campagne » : le texte complet, valeurs incluses.
- **AUTONOMIE** : le plafond d'action autorisé pour CETTE tâche. La tournée ne dépasse
  jamais ce niveau (niveau 3 = jamais exécuté en tournée).
- **ROUTINE** : trace d'origine, pour le journal et la mémoire des boucles.

## (c) Tâches employés — même format

Une tâche destinée à un **employé** (humain) suit le **même bloc RELAIS** : le
**PROMPT devient son brief** (ce qu'on attend, le livrable, le critère de done). La
différence : `assigned_users` = l'ID de l'employé, pas de préfixe `[AGENT:]`, et
`AUTONOMIE` cadre ce que l'assistant pourra préparer **pour** lui, pas décider **à sa
place**.

## Modèle à copier (création via `create-task-tool`)

- `title` : `[AGENT:{nom}] <titre actionnable>`  *(ou titre simple si assigné à un employé/agent-user)*
- `assigned_users` : `[<id>]` (ID réel via `get-users-list-tool`) quand un agent-user/employé existe
- `priority` : 0 urgent / 1 moyenne (défaut) / 2 faible
- `due_date` : `YYYY-MM-DD`
- `description` : le **bloc RELAIS** ci-dessus

## Garde-fous

- **Pas de brief, pas d'exécution** : une tâche `[AGENT:]` sans bloc RELAIS lisible
  (PROMPT + AUTONOMIE au minimum) est **bloquée** par la tournée, jamais interprétée.
- **Variables résolues à la création** : la tournée exécute le PROMPT **tel quel** ;
  un `{placeholder}` restant = relais incomplet = blocage.
- **Rien d'inventé** : si une valeur manque pour résoudre le PROMPT, la demander avant
  de créer la tâche (jamais de défaut inventé — `directives-outils.md` §3).
