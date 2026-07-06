---
name: recruiting-pipeline
description: Track and manage recruiting pipeline stages. Trigger with "recruiting update", "candidate pipeline", "how many candidates", "hiring status", or when the user discusses sourcing, screening, interviewing, or extending offers. S'appuie sur le MCP rapidorh pour les données réelles (équipe, départements, rôles, dailies, projets) et sur ./rapido-kb/ pour les règles maison.
---

# Recruiting Pipeline

## Adaptation Rapido (lire d'abord)

Ce skill vient d'un contexte US générique. Dans cette marketplace, remplacer
systématiquement ses outils par les équivalents Rapido :

| Outil cité dans ce skill | Équivalent à utiliser ici |
|---|---|
| SIRH / HRIS (Workday, BambooHR, Gusto…) | RapidoRh : `get-users-list-tool`, `get-departments-list-tool`, `get-roles-list-tool`, `get-dailies-tool` |
| ATS (Greenhouse, Lever, Ashby) | pas d'ATS — matérialiser le pipeline de recrutement en PROJET Kanban RapidoRh : `create-project-tool` + colonnes par étape (`create-task-list-tool` : Sourcés, Screening, Entretien, Offre) + une tâche par candidat (`create-task-tool`, `move-task-tool`) |
| Slack (notifications) | pas d'équivalent — restituer dans la conversation, ou notification via un workflow n8n (plugin rapido-n8n) |
| Gmail / Google Docs / Drive | brouillons et documents via le plugin rapido-direction (`tri-boite-mail`, `coffre-documents`) s'il est installé, sinon restituer le texte à copier |
| LinkedIn / Indeed (diffusion d'annonces) | pas d'équivalent — livrer l'annonce prête à publier, la diffusion reste manuelle |

Règles locales : l'embauche effective passe par le skill maison
`onboarding-equipe` (ordre OBLIGATOIRE permissions → rôle → département →
`create-user-tool`, qui envoie l'invitation immédiatement). Les seuils et
politiques maison de `./rapido-kb/processus-internes.md` priment sur les
défauts US. Données non exposées par le MCP (diversité, salaires agrégés,
ancienneté fine) : le DIRE et demander la source — ne jamais inventer.


Help manage the recruiting pipeline from sourcing through offer acceptance.

## Pipeline Stages

| Stage | Description | Key Actions |
|-------|-------------|-------------|
| Sourced | Identified and reached out | Personalized outreach |
| Screen | Phone/video screen | Evaluate basic fit |
| Interview | On-site or panel interviews | Structured evaluation |
| Debrief | Team decision | Calibrate feedback |
| Offer | Extending offer | Comp package, negotiation |
| Accepted | Offer accepted | Transition to onboarding |

## Metrics to Track

- **Pipeline velocity**: Days per stage
- **Conversion rates**: Stage-to-stage drop-off
- **Source effectiveness**: Which channels produce hires
- **Offer acceptance rate**: Offers extended vs. accepted
- **Time to fill**: Days from req open to offer accepted

## If ATS Connected

Pull candidate data automatically, update statuses, and track pipeline metrics in real time.
