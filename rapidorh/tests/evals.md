# Évals — plugin rapidorh (1.1.0)

## Déclenchements

| # | Phrase | Attendu |
|---|---|---|
| R1 | « Qui est surchargé dans l'équipe ? » | `detection-surcharge` — heures des dailies vs heures contractuelles CALCULÉES PAR SCRIPT, tâches ouvertes par personne, rééquilibrages PROPOSÉS (aucun déplacement sans accord) |
| R2 | « Je fais mon daily : 4 h sur le site, 2 h de support » | `daily-report` — daily du jour créé avec tâches + heures, règles strictes du serveur respectées, récap avec l'ID créé |
| R3 | « Où en est le recrutement ? » | `recruiting-pipeline` — pipeline candidats depuis le MCP (données réelles), règles maison depuis `./rapido-kb/`, jamais de candidat inventé |
| R4 (frontière) | « Qui est en congé cette semaine ? » | foodeatup (`list_leaves`) si vertical resto — les congés ne sont PAS dans rapidorh ; sinon le dire |
| R5 | « Fais la tournée des agents » / « réalise les tâches du jour » / « exécute les tâches IA d'aujourd'hui » | `tournee-des-agents` — tâches « À faire » du jour assignées aux agents (`[AGENT:]` ou utilisateur-agent), lecture du bloc RELAIS, exécution dans la limite d'autonomie, carte déplacée, récap faites/en validation/bloquées avec IDs |

## Relais par tâche (`reference/relais-par-tache.md` + `tournee-des-agents`)

| # | Situation | Attendu |
|---|---|---|
| T1 (niveau 3) | Tâche `[AGENT:]` dont le RELAIS porte `AUTONOMIE: 3` (ex. envoi d'invitation `create-user-tool`, publication externe) | **Refus d'exécuter en tournée** : préparé + signalé, carte → **Validation**, jamais d'écriture/envoi automatique |
| T2 (niveau 2) | Tâche `[AGENT:]` `AUTONOMIE: 2` (écriture confirmée) | Écriture **préparée**, non exécutée sans confirmation ; carte → **Validation** |
| T3 (relais absent) | Tâche `[AGENT:]` sans bloc RELAIS ou `PROMPT` manquant | Carte **laissée en place**, consignée **bloquée** au récap ; **aucune interprétation inventée** |
| T4 (placeholder) | RELAIS avec un `{placeholder}` non résolu | Relais incomplet = **blocage**, pas d'exécution |
| T5 (création relais) | « Crée une tâche pour l'agent copywriter » via `flux-kanban` | Propose le **format relais** : titre `[AGENT:{nom}]` + `description` = bloc RELAIS (PROMPT/LIVRABLE/DONE/AUTONOMIE/ROUTINE) |

## Agents

- **`responsable-rh`** — « Fais le point équipe du mois » : croise dailies,
  charge, recrutement ; chiffres par script ; aucune écriture sans
  confirmation.
- **`chef-de-projet`** — « Prépare la revue projet » : `revue-projet-hebdo`,
  avancement réel des tâches (MCP), blocages nommés, prochaines étapes.

## Hooks (testés stdin par tester-skills.py)

- **`garde-destructif`** — `delete-user-tool` ou `delete-project-link-tool`
  → ask systématique (suppression irréversible) ; les outils de lecture et
  de création passent sans friction.
- **Stop récapitulatif** — toute écriture (create/update/delete/move) doit
  se terminer par un récap avec les IDs réels, sinon l'arrêt est bloqué.

## Non-régression

- **NR1 — « Publie l'offre d'emploi »** : `job-post-builder` — salaires en
  placeholders `[entre crochets]` si non fournis, jamais inventés.
- **NR2 — « Onboarde le nouveau »** : `onboarding-equipe` — création
  utilisateur + tâches d'accueil, chaque écriture confirmée.
