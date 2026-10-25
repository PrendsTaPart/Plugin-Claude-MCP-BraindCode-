---
name: auditer-mes-routines
description: Utiliser quand les routines se jugent, que l'utilisateur dit « audite mes routines », « lesquelles ne servent à rien », « pourquoi celle-ci échoue », « combien me coûte cette routine ». Évalue, lit les bilans des routines signalées, et porte UNE proposition d'amélioration par routine — le diff est montré, l'utilisateur applique ou refuse.
---

# Auditer mes routines (verdicts, bilans, une amélioration à la fois)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
   `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.
2. `list_pending_routine_actions` : une amélioration déjà en attente ne se
   double pas (la dernière proposition REMPLACE la précédente).

## Workflow

1. **`list_routines`** — santé, échecs consécutifs, coût mensuel, verdict,
   décisions en attente.
2. **`evaluate_routines`** — les verdicts (effective, needs_improvement,
   no_measured_effect, failing, not_enough_data) sont recalculés et
   ENREGISTRÉS à l'historique. Aucun effet annoncé sur not_enough_data.
3. **`get_routine_report`** sur chaque routine signalée `silent`, `failing`,
   `expensive`, `no_effect` ou `no_kpi` — exécutions, taux de réussite,
   crédits, outils réellement appelés, proposition courante.
4. **UNE amélioration par routine** : **`propose_routine_improvement`** —
   résumé, UN changement (consigne, fréquence, outils, autonomie, plafond,
   objectif), KPI à rattacher, effet attendu, risque, coût. Le serveur rend
   le **diff avant/après** : le présenter tel quel (widget
   `diff-amelioration` en option).
5. **La décision appartient à l'utilisateur** : `apply_routine_improvement`
   (qui REFIGE les références des KPI rattachés — le dire) ou
   `decline_routine_improvement`, selon SA décision, jamais la nôtre.

## Garde-fous

- Jamais de pause de notre initiative, même failing ou coûteuse :
  l'amélioration d'abord (règle du serveur, hook garde-planit en filet).
- Un changement par proposition — plusieurs problèmes = plusieurs semaines.
- Un verdict se cite avec sa base (exécutions, période) ; not_enough_data
  se dit « pas assez de données », rien d'autre.
