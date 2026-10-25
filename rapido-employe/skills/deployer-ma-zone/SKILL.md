---
name: deployer-ma-zone
description: Utiliser quand on installe la machine de vente d'une zone, que l'utilisateur dit « déploie ta zone », « on lance Montpellier », « où en est le plan de déploiement ». Déroule le plan Academy « vendre FoodEatUp dans ma zone » — questions d'objectifs en un seul message, puis les dix étapes, chacune cochée au fur et à mesure.
---

# Déployer ma zone (le plan en dix étapes)

Familles engagées : **configurer** (`set_business_goals`,
`update_deployment_step`, routines) — les actions d'étape ont leur propre
famille (préparer, prospecter, publier).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Cadre du jour en main (skill `prise-de-poste`). KB `./rapido-kb/` lue si
   présente (zone et cibles y sont souvent déjà).

## Workflow

1. **`get_deployment_plan`** — les questions encore sans réponse, l'étape en
   cours, ses connecteurs, ses outils, ses routines, ses KPI.
2. **Les questions d'objectifs, EN UN SEUL message** : zone, cible, objectif
   (rendez-vous et signatures par mois), budget mensuel, canaux autorisés,
   disponibilités de démonstration — puis **`set_business_goals`** (aperçu,
   accord, `confirm=true`), et `remember` pour les préférences durables.
3. **Dérouler les dix étapes, dans l'ordre** (objectifs, agents IA, équipe
   RapidoRH, tâches, tunnels RapidoCRM, calendrier RapidoCMS, lead magnets,
   prospection, webinaires, mesure) :
   - vérifier les connecteurs de l'étape — un manquant se demande avec son
     adresse, et on attend ;
   - configurer avec les outils listés par le plan, dans le niveau de chaque
     famille (aperçu puis confirm) ;
   - créer les routines de l'étape (`configure_routine` après
     `check_routine_prompt` — skill `mon-equipe-d-agents`), choisir les KPI ;
   - **`update_deployment_step`** pour cocher, avec la note de ce qui a été
     fait.
4. Les étapes métier s'exécutent par les skills dédiés : lead magnets →
   plugin `rapido-leadmagnet` ; prospection → skill `prospecter-une-zone` ;
   webinaires → skill `webinaire-du-mois` ; mesure → skill `point-du-matin`.
5. Le vendredi, mesurer avant de passer à l'étape suivante (skill
   `boucle-du-vendredi`). Option : widget `avancement-du-deploiement`.

KPI : ceux du plan (rdv, signatures, pipeline). Formations : `premiers-pas`,
`prospection`, `calendrier`, `orchestration`.

## Garde-fous

- Une étape ne se coche que faite et vérifiée — `update_deployment_step`
  porte la preuve dans sa note.
- Le budget répondu à l'étape objectifs ne crée AUCUN droit de dépense : le
  cadre (get_work_plan) et record_expense gouvernent, à chaque fois.
