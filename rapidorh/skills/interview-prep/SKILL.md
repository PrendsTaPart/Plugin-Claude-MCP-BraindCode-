---
name: interview-prep
description: Create structured interview plans with competency-based questions and scorecards. Trigger with "interview plan for", "interview questions for", "how should we interview", "scorecard for", or when the user is preparing to interview candidates. S'appuie sur le MCP rapidorh pour les données réelles (équipe, départements, rôles, dailies, projets) et sur ./rapido-kb/ pour les règles maison.
---

# Interview Prep

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


Create structured interview plans to evaluate candidates consistently and fairly.

## Interview Design Principles

1. **Structured**: Same questions for all candidates in the role
2. **Competency-based**: Map questions to specific skills and behaviors
3. **Evidence-based**: Use behavioral and situational questions
4. **Diverse panel**: Multiple perspectives reduce bias
5. **Scored**: Use rubrics, not gut feelings

## Interview Plan Components

### Role Competencies
Define 4-6 key competencies for the role (e.g., technical skills, communication, leadership, problem-solving).

### Question Bank
For each competency, provide:
- 2-3 behavioral questions ("Tell me about a time...")
- 1-2 situational questions ("How would you handle...")
- Follow-up probes

### Scorecard
Rate each competency on a consistent scale (1-4) with clear descriptions of what each level looks like.

### Debrief Template
Structured format for interviewers to share findings and make a decision.

## Output

Produce a complete interview kit: panel assignment (who interviews for what), question bank by competency, scoring rubric, and debrief template.
