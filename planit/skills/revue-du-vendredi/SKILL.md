---
name: revue-du-vendredi
description: Utiliser quand la semaine Plan'It se juge, que l'utilisateur dit « fais la revue du vendredi de Plan'It », « quelles routines progressent », « le point hebdo des boucles et des décisions ». Évalue boucles et routines, propose une amélioration par routine qui stagne, et rend un rapport qui distingue progrès, stagnation, manque de données et décisions en attente.
---

# Revue du vendredi (le rituel Plan'It de fin de semaine)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
   `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.
2. Ce rituel est l'EXÉCUTANT Plan'It des revues hebdo des autres plugins
   (rapido-suite, rapido-startup, rapido-employe) : il juge les routines
   PLAN'IT, il ne refait pas leurs revues métier.

## Workflow

1. **`evaluate_loops`** — verdicts des boucles à l'instant (improving /
   flat / degrading / not_enough_data — « pas assez de données » dit tel
   quel).
2. **`evaluate_routines`** — verdicts des routines, enregistrés à
   l'historique.
3. **`list_pending_routine_actions`** — ce qui attend déjà une décision :
   présenté, jamais doublé.
4. **Une proposition d'amélioration PAR routine qui stagne** (flat,
   no_measured_effect, needs_improvement) : `get_routine_report` puis
   `propose_routine_improvement` — UN changement, diff montré (skill
   `auditer-mes-routines` pour la mécanique). Les routines
   not_enough_data ne se touchent PAS : elles n'ont pas fini de mesurer.
5. **Le rapport**, en quatre blocs nets : CE QUI PROGRESSE (verdicts
   improving/effective, chiffres à l'appui), CE QUI STAGNE (+ la
   proposition déposée), CE QUI MANQUE DE DONNÉES (et quand le verdict
   tombera : 3 exécutions ET 14 jours), LES DÉCISIONS EN ATTENTE (liste
   datée). Widgets `boucles-kpi` et `credits-par-routine` en option.

## Garde-fous

- Aucune application ni pause pendant la revue : on évalue, on propose, on
  liste — l'utilisateur décide après.
- Chaque affirmation du rapport cite son verdict serveur ; rien au ressenti.
