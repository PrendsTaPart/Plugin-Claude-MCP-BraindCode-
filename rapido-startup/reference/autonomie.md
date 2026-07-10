# Gouvernance des routines (rapido-startup / Loop Engine)

> Rédigée depuis la spécification du propriétaire (la section « Gouvernance »
> de la partie 4 du master plan n'ayant pas été fournie, ce fichier fait
> foi — à réconcilier si le master plan diverge).

## Niveaux d'autonomie

- **Niveau 0 — Lecture seule (DÉFAUT de toute routine)** : appels MCP de
  lecture, calculs par script, écriture des journaux dans
  `./rapido-kb/startup/` uniquement. Aucune confirmation requise.
- **Niveau 1 — Préparation** : brouillons et plans (email non envoyé, plan
  de campagne PAUSED, tâches proposées) — présentés, jamais exécutés seuls.
- **Niveau 2 — Écriture confirmée** : création/modification dans les
  systèmes (tâches RapidoRH, événements Calendar, tâches CRM) — UNE
  confirmation PAR SYSTÈME, récapitulatif des IDs exigé (hook récap-actions).
- **Niveau 3 — Externe (JAMAIS automatique)** : tout ce qui sort de
  l'entreprise ou engage de l'argent — envoi d'email/SMS, publication,
  activation de pub, écriture Stripe. Demande explicite de l'utilisateur au
  moment T, confirmation dédiée, hooks en filet (garde-stripe-write,
  garde-argent-reel, garde-production).

## Par routine

| Routine | Sense | Act maximum autorisé |
|---|---|---|
| R4 CFO-WEEKLY | lecture | Niveau 1 : relances d'impayés PRÉPARÉES (non envoyées) + notification d'alerte FoodEatUp (règle 7) |
| R5 STARTUP-BUILDER | lecture | Niveau 2 : tâches delta après confirmation |
| R6 GROWTH-LOOP | lecture | Niveau 1 : expérience préparée (campagne PAUSED, brouillons) |
| R7 CASH-SENTINEL | lecture | Niveau 0 : ALERTE SEULEMENT — aucune écriture métier (seule exception : notification d'alerte FoodEatUp, règle 7) |
| R8 MONTHLY-BOARD | lecture | Niveau 2 : board écrit dans la KB + jalon Calendar confirmé |
| R9 VIDEO-FACTORY | lecture | Niveau 1 : épisode PRÉPARÉ (brief, composition committée dans le dépôt de production, preview) — RENDU payant et PUBLICATION = niveau 3, jamais automatiques |

## Règles absolues

1. Écriture **Stripe** en routine : INTERDITE (même confirmée — elle relève
   d'une demande explicite hors routine).
2. Un montant, un KPI → script `calcul_kpi.py`, formule affichée (hook
   « KPI sans script »).
3. Échec en cours d'Act multi-systèmes : STOP + liste de ce qui est créé.
4. Donnée manquante = annoncée, jamais estimée ; seuil absent de la KB =
   défaut secteur CITÉ comme tel.
5. Toute exécution se journalise (date, routine, verdicts, IDs) dans
   `./rapido-kb/startup/routines-journal.md` — c'est la mémoire des boucles.
6. Silence configurable : une sentinelle au vert peut ne rien poster
   (CONFIG `silence_si_vert: true`) — mais elle journalise quand même.
7. Notification FoodEatUp (`create_notification`) : c'est un CANAL D'ALERTE,
   pas une action métier. Autorisée en routine (R4, R7) UNIQUEMENT pour
   diffuser un verdict 🔴/🟡 quand le vertical resto est actif — `type`
   `danger` ou `warning`, jamais au vert, jamais pour autre chose, ID
   récapitulé. Elle ne remplace pas le rapport : elle le double côté
   FoodEatUp (lue par `briefing-du-jour`).
