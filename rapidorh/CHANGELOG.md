# Changelog — plugin rapidorh

## 0.7.1 — 2026-07-06

- Correctif `job-post-builder` : dossier `reference/` renommé en `references/`
  (les chemins du SKILL.md source étaient cassés en amont — 5 fichiers).

## 0.7.0 — 2026-07-06

- Intégration de 5 skills Apache 2.0 d'anthropics/knowledge-work-plugins
  (packs human-resources + small-business ; LICENSE dans chaque dossier,
  provenance dans ATTRIBUTIONS.md) : `onboarding-rh-methodo` (renommé depuis
  onboarding — checklist et plan 30/60/90 j d'un nouvel arrivant),
  `recruiting-pipeline` (suivi du pipeline de recrutement),
  `interview-prep` (plans d'entretien structurés + scorecards),
  `job-post-builder` (annonce + guide d'entretien + lettre d'offre),
  `people-report` (headcount, turnover, santé d'organisation).
- Adaptation : mention MCP rapidorh/KB en description + section « Adaptation
  Rapido » (SIRH → get-users/departments/roles/dailies ; ATS → pipeline de
  recrutement en projet Kanban RapidoRh ; Slack/Gmail/LinkedIn signalés sans
  équivalent ; embauche effective via onboarding-equipe ; données non
  exposées par le MCP jamais inventées).

## 0.6.0 — 2026-07-06

- Passe de portabilité : devise (salaires, budgets) lue depuis la KB (défaut euros signalé).

## 0.5.0 — 2026-07-06

- Utilisation de la base de connaissance `./rapido-kb/` : règle de chargement
  dans les directives (seuils de charge et horaires maison de
  processus-internes.md prioritaires) ; agent `chef-de-projet` cite ses seuils
  maison (ex. seuil de blocage) sinon défauts signalés.

## 0.4.0 — 2026-07-06

- Script de calcul `skills/detection-surcharge/scripts/charge_equipe.py`
  (stdlib) : taux de charge %, signaux rouge/jaune/vert/blanc, déséquilibres
  de tâches — le skill impose « utiliser le script pour tout calcul ; ne
  jamais calculer de tête ».
- `reference/pieges-outils.md` : tableau des pièges (1 daily/jour et 0,5-24 h,
  owners sans dailies, rôle avant utilisateur, échelles de priorité, pas de
  réassignation de tâche…), référencé par les directives.

## 0.3.0 — 2026-07-06

- Hooks déterministes (`hooks/hooks.json` + `hooks/scripts/`) :
  - PreToolUse `garde-destructif` : confirmation forcée (ask) sur
    `delete-user-tool` et `delete-project-link-tool` ;
  - Stop `récap-actions` (hook prompt) : bloque la fin de tour si des écritures
    MCP ont eu lieu sans récapitulatif des IDs dans la réponse.

## 0.2.0 — 2026-07-06

- Ajout de la couche métier :
  - Agents : `chef-de-projet` (décomposition en tâches assignées/datées,
    signaux faibles, rythme daily/revue, escalade tôt) et `responsable-rh`
    (onboarding structuré, suivi de charge dailies vs heures contractuelles,
    équité d'affectation, confidentialité).
  - Skills d'expertise : `revue-projet-hebdo` (% d'avancement par colonne,
    tâches bloquées et en retard, dailies de la semaine, 3 actions) et
    `detection-surcharge` (heures déclarées vs hours_worked, tâches ouvertes
    par personne, propositions de rééquilibrage).
- Limite serveur documentée : pas d'outil de réassignation d'une tâche
  existante (contournement : recréer la tâche ou action manuelle).

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (serveur rapidorh), référence
  `directives-outils.md`, skills workflow `setup-projet`, `flux-kanban`,
  `daily-report`, `onboarding-equipe`.
