# Changelog — plugin rapidorh

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
