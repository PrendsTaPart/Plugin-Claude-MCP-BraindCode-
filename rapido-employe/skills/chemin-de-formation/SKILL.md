---
name: chemin-de-formation
description: Utiliser quand l'employé suit sa formation Academy, que l'utilisateur dit « continue ta formation », « fais ta mission du jour », « passe ton quiz », « révise ». Déroule la prochaine mission du chemin (Se brancher, S'outiller, Prospecter et vendre, Communiquer, Servir et fidéliser, Orchestrer et mesurer), son quiz, la révision et la mise en pratique — 30 minutes par jour au plus.
---

# Chemin de formation (30 minutes par jour, pas plus)

Famille engagée : **apprendre** (Confirmé au cadre actuel — Claude agit seul
et le note au journal).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. La prochaine mission vient du cadre (`get_work_plan`, champ
   `prochaine_mission`) — skill `prise-de-poste` d'abord si besoin.

## Workflow

1. **La leçon** : `get_mission` (clé de la prochaine mission) — diapositives
   et narrations, restituées à l'oral, une idée à la fois.
2. **Le quiz** : `get_quiz` puis `check_quiz_answer` question par question —
   corriger sans modifier la progression ; une erreur renvoie à la
   diapositive concernée.
3. **La révision** : `start_daily_review` puis `answer_daily_review` — la
   répétition espacée du serveur, pas un résumé improvisé.
4. **La mise en pratique réelle** : `start_practical_exercise`,
   `get_exercise_instructions`, exécution RÉELLE dans l'outil concerné (via
   le skill métier, dans son niveau d'autonomie), puis `submit_practice_proof`
   avec la preuve (`confirm=true` après accord). `get_practical_feedback`
   pour le retour.
5. **S'arrêter à 30 minutes** : le reste de la mission attend demain — la
   régularité bat le marathon. Noter où on en est.

KPI : `objectifs-atteints` (progression du chemin).
Formations : celles du chemin — l'ordre vient de `get_work_plan`, jamais
d'une préférence.

## Garde-fous

- AUCUN outil ne valide une mission, ne passe l'examen ni n'émet de
  certificat : les points se gagnent dans l'application, en faisant la
  mission jusqu'au bout. Claude ne le promet jamais.
- Les réponses du quiz ne se montrent qu'après la tentative.
- La mise en pratique est un geste réel soumis aux gardes (famille de
  l'outil utilisé) — jamais une simulation racontée.
