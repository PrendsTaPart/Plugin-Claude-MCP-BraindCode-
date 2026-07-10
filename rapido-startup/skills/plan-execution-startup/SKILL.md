---
name: plan-execution-startup
description: Utiliser quand l'utilisateur veut passer du business plan à l'action - créer le projet de sa startup, planifier toutes les tâches de création et de gestion d'entreprise, ou dit « lance l'exécution », « crée les tâches de mon BP ».
---

# Plan d'exécution startup — du business plan aux tâches (routine R5 STARTUP-BUILDER)

Transforme le business plan en projet exécutable : WBS adapté, projet RapidoRH
avec Kanban, jalons Google Calendar, tâches commerciales CRM, mapping tracé.
**Réutilise les skills existants par référence — ne duplique jamais leur
logique** : ce skill orchestre, les skills spécialisés exécutent.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`references/wbs-startup.md` (le référentiel : ~120 tâches en 6 phases avec
dépendances et durées types). Rappels : confirmation PAR SYSTÈME avant
écriture, récapitulatif des IDs en fin de tour (hook récap-actions),
`google-calendar` optionnel (dégrader proprement s'il n'est pas connecté :
jalons listés dans plan-execution.md seulement).

## Workflow (= routine R5 STARTUP-BUILDER)

1. **Prérequis — le business plan existe.** Vérifier
   `./rapido-kb/startup/business-plan/` (BUSINESS-PLAN.md ou fichiers de
   phase). ABSENT → s'arrêter et renvoyer vers le skill
   `interview-business-plan` (« le plan d'exécution se déduit du BP, pas
   l'inverse »). Lire aussi `./rapido-kb/startup/08-roadmap.md` s'il existe
   (skill `dossier-startup-360`) pour ne pas contredire la roadmap validée.

2. **Adapter le WBS au BP — puis PRÉSENTER, AVANT toute écriture.**
   Partir de `references/wbs-startup.md` et l'adapter :
   - **vertical** : restaurant → garder les volets FoodEatUp/HACCP ; SaaS →
     volets produit/beta ; services → volets staffing ;
   - **équipe** : assigner selon les fondateurs/recrues réels
     (`get-users-list-tool`) — pas de tâche assignée à un rôle qui n'existe
     pas encore (elle dépend alors de la tâche de recrutement) ;
   - **budget/stade** : supprimer les tâches sans objet (pas de levée → pas
     de dossier BPI…), ajuster les durées ;
   - marquer chaque tâche : phase, dépendances, durée type, échéance
     proposée, outil/skill d'exécution.
   Présenter LE PLAN COMPLET (tableau par phase) et attendre la validation
   explicite. Aucun outil d'écriture avant l'accord.

3. **Créer, après accord — dans cet ordre, par système :**
   - **RapidoRH** : suivre l'ordre obligatoire du skill `setup-projet`
     (IDs valides d'abord, jamais devinés) — `create-project-tool` (le
     projet startup), colonnes via `create-task-list-tool` (une par phase du
     WBS), puis `create-task-tool` pour chaque tâche validée (titre,
     description avec dépendances, échéance, assigné, priorité — échelle
     tâche 0-2, 0 = urgent) ;
   - **Google Calendar** (si connecté) : `create_event` pour les JALONS
     seulement (fins de phase, échéances légales, board mensuel) — pas une
     tâche = un événement ;
   - **RapidoCRM** : les tâches COMMERCIALES du WBS (prospection, relances)
     via `create_task`, rattachées aux entités CRM concernées.
   En cas d'échec en cours de route : STOP + liste de ce qui est déjà créé.

4. **Tracer le mapping** dans `./rapido-kb/startup/plan-execution.md` :
   date, projet (ID), puis une ligne par tâche « tâche WBS ↔ ID RapidoRH
   (ou ID event Calendar / ID task CRM) ↔ échéance ↔ assigné ». C'est le
   fichier que les revues liront pour suivre l'avancement.

5. **Récapitulatif final** (exigé par le hook récap-actions) : par système,
   tous les IDs créés (projet, colonnes, tâches, événements), le lien vers
   plan-execution.md, et les 3 prochaines actions (généralement : phase 1
   juridique en tête, routines de pilotage à armer en dernier).

## Réutilisation des skills existants (référence, pas duplication)

Les tâches du WBS qui correspondent à un skill l'indiquent — l'exécution de
CETTE tâche se fait en invoquant le skill, jamais en réimplémentant :
`usine-a-landing` (site/landing), `calendrier-editorial` (contenus),
`prospection-pipeline` (prospection), `lancement-campagne-meta` (pub),
`job-post-builder` (fiches de poste), `onboarding-equipe` (arrivées),
`plan-financier-previsionnel` (prévisionnel), `catalogue-kpi` (tableau de
bord), `revue-hebdo-business` et `comite-de-direction` (routines de
pilotage), `mise-a-jour-kb` (KB), `recettes-metier` (automatisations n8n).

## Garde-fous

- JAMAIS d'écriture avant la validation explicite du plan complet (étape 2).
- Les échéances légales (immatriculation, DPAE, assurances) ne sont pas des
  conseils juridiques : recommander la validation par un professionnel.
- Le WBS est un référentiel : tout ajout/suppression du client est notée
  dans plan-execution.md (le document fait foi, pas le template).
- Relance de la routine R5 sur un projet existant : lire plan-execution.md
  d'abord et ne créer QUE le delta (jamais de doublons de tâches).
