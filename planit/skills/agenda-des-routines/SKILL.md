---
name: agenda-des-routines
description: Utiliser quand on regarde le planning Plan'It, que l'utilisateur dit « qu'est-ce qui tourne cette semaine », « qu'est-ce qui a raté hier », « trouve un créneau pour une nouvelle routine ». Lit le calendrier par plages de 62 jours au plus, détecte les chevauchements avant de proposer un horaire, et liste à part les routines événementielles.
---

# Agenda des routines (le calendrier, sans surinterprétation)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **`get_calendar`** sur la plage demandée — **62 jours au plus par appel**
   (au-delà : plusieurs appels enchaînés). Chaque occurrence porte son heure
   locale, sa cadence lisible, son état (`done`, `failed`, `missed`,
   `scheduled`), la santé de la routine et son dernier verdict.
2. **Restituer par jour** : fait / raté / manqué / à venir — un état autre
   que `done` ne veut JAMAIS dire « exécuté » (règle du serveur). Les
   échecs renvoient vers `get_task_executions` (skill `mes-taches`) pour le
   pourquoi.
3. **Routines événementielles** : listées À PART (`event_routines`) — elles
   n'ont pas d'horaire, leur déclencheur se gère au skill
   `routines-sur-evenement`.
4. **Proposer un horaire** (nouvelle routine ou déplacement) : détecter les
   chevauchements sur la plage AVANT de proposer — deux routines lourdes au
   même créneau se signalent ; fuseau Europe/Paris par défaut.
5. Mise en page : widget `calendrier-des-routines` (semaine ou mois).

## Garde-fous

- Jamais plus de 62 jours par appel ; jamais une exécution déduite d'un
  `scheduled`.
- Le calendrier est en lecture : tout déplacement passe par `update_task`
  (tâche) ou une proposition d'amélioration (routine — skill
  `auditer-mes-routines`).
