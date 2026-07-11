---
name: people-report
description: Utiliser quand l'utilisateur veut un rapport RH — effectifs, turnover/attrition, diversité, santé de l'organisation (span of control, risques de départ) — pour la direction ou une analyse par équipe. S'appuie sur le MCP rapidorh pour les données réelles et sur ./rapido-kb/ pour les règles maison.
source: anthropics/knowledge-work-plugins (commit 564d560c), Apache 2.0
argument-hint: "<report type — headcount, attrition, diversity, org health>"
---

# /people-report

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


Generate people analytics reports from your HR data. Analyze workforce data to surface trends, risks, and opportunities.

## Usage

```
/people-report $ARGUMENTS
```

## Report Types

**Headcount**: Current org snapshot — by team, location, level, tenure
**Attrition**: Turnover analysis — voluntary/involuntary, by team, trends
**Diversity**: Representation metrics — by level, team, pipeline
**Org Health**: Span of control, management layers, team sizes, flight risk

## Key Metrics

### Retention
- Overall attrition rate (voluntary + involuntary)
- Regrettable attrition rate
- Average tenure
- Flight risk indicators

### Diversity
- Representation by level, team, and function
- Pipeline diversity (hiring funnel by demographic)
- Promotion rates by group
- Pay equity analysis

### Engagement
- Survey scores and trends
- eNPS (Employee Net Promoter Score)
- Participation rates
- Open-ended feedback themes

### Productivity
- Revenue per employee
- Span of control efficiency
- Time to productivity for new hires

## Approach

1. Understand what question they're trying to answer
2. Identify the right data (upload, paste, or pull from ~~HRIS)
3. Analyze with appropriate statistical methods
4. Present findings with context and caveats
5. Recommend specific actions based on data

## What I Need From You

Upload a CSV or describe your data. Helpful fields:
- Employee name/ID, department, team
- Title, level, location
- Start date, end date (if applicable)
- Manager, compensation (if relevant)
- Demographics (for diversity reports, if available)

## Output

```markdown
## People Report: [Type] — [Date]

### Executive Summary
[2-3 key takeaways]

### Key Metrics
| Metric | Value | Trend |
|--------|-------|-------|
| [Metric] | [Value] | [up/down/flat] |

### Detailed Analysis
[Charts, tables, and narrative for the specific report type]

### Recommendations
- [Data-driven recommendation]
- [Action item]

### Methodology
[How the numbers were calculated, any caveats]
```

## If Connectors Available

If **~~HRIS** is connected:
- Pull live employee data — headcount, tenure, department, level
- Generate reports without needing a CSV upload

If **~~chat** is connected:
- Offer to share the report summary in a relevant channel
