---
name: planning-equipe
description: Utiliser quand l'utilisateur parle de planning, de shifts, d'horaires d'équipe, de demandes de congé, de pointages, de contrat de travail ou de documents d'un employé dans son restaurant. Gère les créneaux, les congés, le suivi du coût et l'administratif des contrats.
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
5. **Planning hebdomadaire type** — `update_employee_schedule`
   (`establishment_id`, `employee_id`, `schedules` =
   `[{day, start_time, end_time, break_duration}]`) : ⚠️ REMPLACE
   ENTIÈREMENT le planning type de l'employé (pas un ajout) — récapituler
   l'ancien et le nouveau, confirmation obligatoire (hook en filet).
6. **Affecter une tâche** — `assign_task` (`establishment_id`,
   `professional_id`, `name` ; `date`, `time` HH:MM, `priority` ∈ basse,
   normale, haute, urgente, `category`) : la consigne du jour rattachée à la
   bonne personne.

## Volet administratif — contrats et documents

1. **Créer un contrat** — `create_employee_contract` (`establishment_id`,
   `employee_id` via `list_employees` ; `type` ∈ CDI, CDD, Extra,
   Apprentissage, Stage — défaut CDI ; `start_date` défaut aujourd'hui,
   `end_date` obligatoire pour un CDD ; `weekly_hours`, `days_per_week`,
   `base_salary`, `job_title`, `manager_name`).
   - **Confirmation niveau 2 obligatoire** (données sensibles — salaire,
     durée) : récapituler employé, type, dates, heures et salaire, attendre le
     OK explicite AVANT l'appel (hook garde-destructif en filet). Chaque
     valeur vient de l'utilisateur — jamais un salaire ou des heures devinés.
2. **Consulter les contrats** — `list_employee_contracts`
   (`establishment_id`, `employee_id` optionnel) : type, dates, heures
   hebdomadaires réelles de chaque employé.
3. **Documents administratifs** — `list_employee_documents`
   (`establishment_id`, `employee_id` optionnel) : pièces du dossier employé ;
   signaler les dossiers incomplets, sans en exposer le contenu inutilement.

> **Croisement `detection-surcharge` (plugin rapidorh)** : les heures
> contractuelles sont désormais lues depuis les CONTRATS RÉELS
> (`list_employee_contracts` → `weekly_hours`), plus supposées — c'est cette
> valeur qui sert de référence « heures attendues » dans l'analyse de charge
> et dans le contrôle pointages vs planning ci-dessus.

## Garde-fous

- Congé approuvé = intouchable : pas de shift dessus, pas d'annulation de
  congé sans demande explicite de l'utilisateur.
- Afficher le coût estimé de la semaine (via `list_plannings`) après chaque
  session de planification ; alerter si la tendance dépasse le seuil maison.
- Cohérence salle/cuisine : rappeler le briefing du jour (`briefing-du-jour`)
  qui croise couverts attendus et staffing.
- Données sensibles : jamais de création de contrat sans confirmation
  explicite ; les salaires ne s'affichent que sur demande directe, jamais
  dans une vue d'équipe ou une analyse de charge.

## Fiche employé (ajout SYNC S1)

Consulter/éditer une fiche : `get_employee`, `update_employee` (prénom, nom, email,
téléphone, rôle). **`delete_employee` = offboarding, confirmation** (hook). Création
(`create_employee`, `create_employee_contract`) déjà couverte.
