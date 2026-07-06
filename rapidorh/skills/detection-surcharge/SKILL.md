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
2. **Collecter les données** — pour chaque personne :
   - heures des dailies sur la période : `get-dailies-tool` (par `date` /
     `user_id`, vue owner), avec le compte de dailies remplis vs attendus ;
   - référence contractuelle : `hours_worked` (via `get-users-list-tool`) ;
   - tâches ouvertes : `get-projects-list-tool` (projets en cours) puis
     `get-project-tasks-tool` par projet — compter les non-Done et les
     urgentes (priorité 0) par personne.
3. **Calculer avec le SCRIPT — jamais de tête.** Utiliser le script pour tout
   calcul ; ne jamais calculer de tête. Construire le JSON d'entrée
   `{periode_jours_ouvres, personnes: [{nom, hours_worked, heures_declarees,
   dailies_remplis, dailies_attendus, taches_ouvertes, taches_urgentes}]}` et
   exécuter :
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/detection-surcharge/scripts/charge_equipe.py" <fichier.json>`
   Le script renvoie le taux de charge % (déclaré / attendu), un signal par
   personne (rouge > 110 %, vert 90-110 %, jaune 60-90 % ou sous-affectation,
   BLANC = dailies incomplets — jamais conclu en sous-charge) et les
   déséquilibres de tâches vs moyenne d'équipe — reprendre ces chiffres tels
   quels.
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
