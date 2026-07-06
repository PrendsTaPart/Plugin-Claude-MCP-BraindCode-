---
name: detection-surcharge
description: Utiliser quand l'utilisateur demande qui est surchargé, la répartition de la charge ou la capacité de l'équipe. Croise heures des dailies et heures contractuelles, compte les tâches ouvertes par personne et propose des rééquilibrages.
---

# Détection de surcharge

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).

## Workflow (lecture seule jusqu'aux réaffectations validées)

1. **Périmètre** — période analysée (défaut : 2 dernières semaines) et équipe
   (tout le monde ou un projet : `get-users-list-tool`, filtres possibles).
2. **Heures déclarées vs contractuelles** — pour chaque personne :
   - heures des dailies sur la période : `get-dailies-tool` (par `date` /
     `user_id`, vue owner) ;
   - référence contractuelle : `hours_worked` (via `get-users-list-tool`) ;
   - ratio charge = heures déclarées / heures contractuelles attendues sur la
     période. Seuils indicatifs : > 110 % répété = surcharge ; < 60 % =
     sous-affectation OU dailies non remplis — TOUJOURS distinguer les deux
     avant de conclure (un daily manquant n'est pas du temps libre).
3. **Tâches ouvertes par personne** — `get-projects-list-tool` (projets en
   cours) puis `get-project-tasks-tool` par projet : compter par personne les
   tâches non-Done, en pondérant par priorité (0 urgent pèse plus) et en
   signalant les échéances rapprochées.
4. **Signaler les déséquilibres** :
   ```
   ⚖️ CHARGE ÉQUIPE — {période}
   personne | h déclarées / h attendues | tâches ouvertes (dont urgentes) | signal
   ```
   Signaux : 🔴 surcharge (heures ET tâches au-dessus), 🟡 à surveiller,
   🟢 ok, ⚪ données incomplètes (dailies manquants — le dire).
5. **Proposer des rééquilibrages** — du plus chargé vers le moins chargé, en
   respectant les compétences (demander si inconnu) :
   - reporter/déprioriser : `move-task-tool` (retour en Todo, avec accord) ;
   - réaffecter : le serveur n'a PAS d'outil de réassignation d'une tâche
     existante → recréer la tâche avec `create-task-tool` (bon
     `assigned_users`) et faire sortir l'ancienne (déplacement de colonne +
     note), OU signaler l'action manuelle dans l'interface RapidoRh ;
   - si la surcharge est structurelle (toujours la même personne) : le
     remonter comme sujet RH, pas comme un problème de Kanban.

## Garde-fous

- Aucune réaffectation sans validation explicite de l'utilisateur, tâche par
  tâche.
- Formulation factuelle et bienveillante : on parle de charge et de capacité,
  jamais de « productivité » individuelle ; pas de classement public de
  l'équipe.
- Ne jamais afficher les salaires dans cette analyse.
