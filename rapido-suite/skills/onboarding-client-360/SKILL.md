---
name: onboarding-client-360
description: Utiliser quand l'utilisateur veut onboarder un nouveau client, annonce un client gagné ou un nouveau contrat signé. Orchestre CRM, CMS et RH pour mettre en place le client de bout en bout.
---

# Onboarding client 360°

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes,
dont la confirmation PAR SYSTÈME) et `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md`
pour l'étape CMS — ce skill produit du contenu visible.

Workflow transverse sur 3 serveurs MCP : rapidocrm, rapidocms, rapidorh.
RÈGLE CENTRALE : demander une confirmation explicite à l'utilisateur AVANT chaque
création dans un nouveau système (une validation par système, pas une validation
globale au début).

## Étape 1 — CRM : confirmer la fiche client

1. Rechercher l'entreprise : `search_entreprises` (`q`) puis `get_entreprise`
   (`id`). Si absente, proposer `create_entreprise` (avec accord de
   l'utilisateur) ; vérifier le SIRET via `rechercher_entreprise_siret` si fourni.
2. Vérifier l'état commercial : `get_historique_prospect` et, si le deal vient
   d'être gagné, clôturer l'opportunité (`close_opportunity`) et/ou déplacer le
   prospect à l'étape finale (`deplacer_prospect_etape`).
3. Noter l'`entreprise_id` — il sert de référence pour tout le reste.

## Étape 2 — CMS : initialiser la présence sociale (CONFIRMER d'abord)

1. Vérifier les comptes connectés : `list_connected_accounts`.
2. Selon le besoin du client :
   - première campagne de contenu : `create_campagne` (CMS) puis posts via
     `create_draft_tool` / `schedule_draft_tool` ;
   - carte digitale : `add_digital_card` + `assign_card_template`
     (template AVEC QR code) ;
   - respecter la charte : `get_brand` avant tout contenu.

## Étape 3 — RH : créer le projet client (CONFIRMER d'abord)

1. `get-users-list-tool` : identifier chef de projet et équipe (IDs réels).
2. `create-project-tool` : nom = client, `start_date`/`end_date` YYYY-MM-DD,
   `price` = budget du contrat, `priority` (1 basse / 2 moyenne / 3 haute),
   `size` (0 petit / 1 moyen / 2 grand), `project_manager_id`, `employees`.
   Les colonnes Todo/Doing/Done sont créées automatiquement.
3. Premières tâches d'onboarding : `create-task-tool` (priorité tâche :
   0 urgent / 1 moyenne / 2 faible) avec `assigned_users`.
4. Lien vers la fiche CRM ou les ressources client : `create-project-link-tool`.

## Récapitulatif final OBLIGATOIRE

Terminer par un tableau récapitulatif des objets créés dans CHAQUE système avec
leurs IDs : CRM (entreprise_id, opportunité), CMS (campagne_id, card_id,
draft_ids), RH (project_id, task_ids). Mentionner ce qui a été volontairement
sauté et pourquoi.

## Garde-fous

- Jamais deux systèmes modifiés sans confirmation intermédiaire.
- Si une étape échoue, s'arrêter, le signaler, et lister ce qui a déjà été créé
  (pas de retour arrière silencieux).
- Réutiliser les données du CRM (nom, contacts) partout — ne pas redemander ce qui
  est déjà connu.
