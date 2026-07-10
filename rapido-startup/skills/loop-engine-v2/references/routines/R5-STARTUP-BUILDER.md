# R5 — STARTUP-BUILDER (delta d'exécution hebdomadaire)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: R5-STARTUP-BUILDER
cadence: hebdomadaire — mardi matin
perimetre: [rapidorh, rapidocrm, google-calendar]
source_verite: ./rapido-kb/startup/plan-execution.md
autonomie: niveau 2 max (tâches delta APRÈS confirmation) — reference/autonomie.md
silence_si_vert: false
```

> Prompt rédigé depuis la spec (partie 4 du master plan non fournie).

## Sense (lecture seule)

1. Lire `plan-execution.md` (le mapping tâche ↔ ID). ABSENT → cette routine
   n'a pas de socle : renvoyer vers le skill `plan-execution-startup`.
2. État réel : `get-project-tasks-tool` (colonnes/statuts),
   `get-dailies-tool` (semaine), jalons Calendar à 14 jours.

## Plan

3. Delta : terminées / en retard (échéance dépassée) / débloquées (toutes
   dépendances WBS terminées → à lancer) / orphelines (dans RapidoRH mais
   pas au mapping, ou l'inverse).
4. Prioriser : retards sur le chemin critique d'abord (dépendances en aval).

## Act (niveau 2 — après confirmation)

5. PRÉSENTER le delta (tableau) puis, sur accord : créer les tâches
   débloquées (`create-task-tool`, ordre du skill `setup-projet` — priorité
   tâche 0-2, 0 = urgent), ajuster les échéances glissées, jalons Calendar
   modifiés si besoin. JAMAIS de doublon : tout passe par le mapping.

## Feed

6. Mettre à jour `plan-execution.md` (nouvelles tâches ↔ IDs, statuts) +
   journal `routines-journal.md`. Retard structurel d'une phase → proposer
   la mise à jour de 08-roadmap (skill `mise-a-jour-kb`).

## Report

7. Avancement PAR PHASE (x/y tâches, retard max), le delta créé (IDs), les
   3 tâches de la semaine, les blocages nommés avec leur propriétaire.
