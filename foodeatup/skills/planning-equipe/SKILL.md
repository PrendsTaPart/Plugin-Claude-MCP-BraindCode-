---
name: planning-equipe
description: Utiliser quand l'utilisateur parle de planning, de shifts, d'horaires d'équipe, de demandes de congé ou de pointages dans son restaurant. Gère les créneaux de travail, les congés et le suivi du coût.
---

# Planning équipe (restaurant)

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.

## Workflow

1. **Vue de la semaine** — `list_plannings` (`establishment_id`, `week` = une
   date dans la semaine voulue, défaut aujourd'hui) : shifts, heures et **coût
   estimé — TOUJOURS l'afficher** à l'utilisateur après toute création ou
   modification (règle : masse salariale ≤ 35 % du CA, seuil maison de
   `./rapido-kb/processus-internes.md` prioritaire).
2. **Congés AVANT les shifts** — `list_leaves` : demandes en attente et congés
   approuvés de la période.
   - RÈGLE DURE : ne JAMAIS créer un shift pour un employé sur un congé
     APPROUVÉ — vérifier avant chaque `create_shift`.
   - Traiter les demandes en attente : `approve_leave` / `reject_leave`
     (`establishment_id`, `leave_id`, `comments`) — décision de l'utilisateur,
     jamais la vôtre ; un refus mérite un commentaire.
3. **Créer les shifts** — `create_shift` (`establishment_id`,
   `professional_id` via `list_employees`, `day` YYYY-MM-DD, `start`/`end`
   HH:MM, `role_label` ∈ cuisine, salle, plonge, bar, management, livraison ;
   `break_minutes`, `note`). Le shift est publié immédiatement : valider le
   récapitulatif (qui, quand, quel poste) avant l'appel.
4. **Contrôler les pointages** — `list_attendances` (`establishment_id`,
   `date_from`/`date_to`, défaut mois en cours) : croiser pointages vs shifts
   planifiés et signaler les écarts (retards récurrents, heures sup non
   planifiées) — factuellement, sans jugement de personne.

## Garde-fous

- Congé approuvé = intouchable : pas de shift dessus, pas d'annulation de
  congé sans demande explicite de l'utilisateur.
- Afficher le coût estimé de la semaine (via `list_plannings`) après chaque
  session de planification ; alerter si la tendance dépasse le seuil maison.
- Cohérence salle/cuisine : rappeler le briefing du jour (`briefing-du-jour`)
  qui croise couverts attendus et staffing.
