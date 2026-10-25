---
name: espace-responsable
description: Utiliser quand Michael, le responsable, pilote son équipe et son employé IA — uniquement sur son invocation explicite (« espace responsable », « prépare-moi le rapport d'équipe », « quelles décisions m'attendent »). Prépare les rapports et chaque décision en APERÇU pour signature humaine — l'employé n'y entre jamais de lui-même.
disable-model-invocation: true
---

# Espace responsable (préparer les décisions, jamais les prendre)

Famille engagée : lectures réservées au rôle responsable + préparation
d'APERÇUS. Les outils de décision eux-mêmes (`set_agent_policy`,
`review_practice`, `review_team_memory`, `decide_module`) restent refusés
par le hook garde-auto-gouvernance : la signature se fait DANS L'APPLICATION.

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Ce skill ne se déclenche QUE sur invocation humaine explicite — jamais
   proposé spontanément par l'employé (frontmatter
   `disable-model-invocation`).

## Workflow

1. **L'état de l'équipe** : `team_report`, `learner_report` (par apprenant),
   `get_challenge_ranking` — restitués tels quels, forces et retards
   nommés ; `list_module_drafts` pour les modules en attente de publication.
2. **Les décisions en attente**, préparées UNE PAR UNE en aperçu :
   - pratiques à valider : lire la preuve, proposer un avis motivé —
     la validation (`review_practice`) se signe dans l'application ;
   - mémoire d'équipe proposée : lire, proposer garder/corriger/refuser —
     `review_team_memory` se signe dans l'application ;
   - modules proposés : lire le brouillon, proposer publier/retravailler —
     `decide_module` se signe dans l'application ;
   - cadre de l'employé (niveaux, quotas, budget, arrêt/marche) : montrer
     l'état actuel (`get_work_plan`) et l'effet de chaque changement —
     `set_agent_policy` se signe dans l'application.
3. **Livrer la feuille de décisions** : une ligne par décision (objet, avis
   proposé, où signer), rien d'exécuté.

KPI : `objectifs-atteints` (équipe). Formations : `orchestration`,
`reporting`.

## Garde-fous

- Tout est APERÇU : ce skill ne signe rien, n'exécute rien — le hook
  garde-auto-gouvernance refuse de toute façon les outils de décision.
- Les données d'apprenants servent le responsable seul : rien n'en sort
  (pas de partage, pas de mémoire).
- Si l'appelant n'a pas le rôle responsable, les outils échoueront : le
  dire et s'arrêter — pas de contournement.
