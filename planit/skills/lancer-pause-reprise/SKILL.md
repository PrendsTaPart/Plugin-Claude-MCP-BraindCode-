---
name: lancer-pause-reprise
description: Utiliser quand une routine se pilote à la main, que l'utilisateur dit « lance la routine maintenant », « mets-la en pause », « reprends la routine veille ». Lance après coût annoncé et accord, reprend après vérification des connecteurs, et ne met en pause QUE sur demande explicite.
---

# Lancer, pause, reprise (les trois gestes qui engagent)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow — lancer maintenant

1. **`estimate_routine_cost`** sur la routine — annoncer le coût d'une
   exécution (base dite si flat_price/default). Le hook garde-cout-annonce
   REFUSE un lancement sans estimation dans la session.
2. **`run_routine_now`** sur l'accord explicite — l'exécution appelle
   réellement les outils (envois, publications…) et consomme des crédits.
3. Suivre le résultat : `get_task_executions`.

## Workflow — reprise

1. **`list_mcp_servers`** — les connecteurs de la routine sont-ils tous
   connectés ? `resume_routine` est REFUSÉ par le serveur si l'un est
   débranché (relevé du 2026-10-25 : FoodEatUp en erreur, RapidoCRM
   déconnecté) → renvoyer vers l'écran Connecteurs de l'app d'abord.
2. **`estimate_routine_cost`** — la reprise relance la consommation :
   l'annoncer.
3. **`resume_routine`** sur l'accord explicite — compteur d'échecs remis à
   zéro, prochaine exécution recalculée.

## Workflow — pause

- **UNIQUEMENT sur demande explicite de l'utilisateur.** Une routine qui
  échoue ou coûte cher ne se met JAMAIS en pause de notre initiative : on
  propose d'abord une amélioration (skill `auditer-mes-routines`).
- `pause_routine` sur sa demande ; sans effet si déjà en pause (le dire).

## Garde-fous

- Trois outils destructifs : confirmation humaine à chaque fois (hook).
- Après un lancement raté : diagnostic (exécutions, connecteurs) avant
  toute relance — on ne « re-lance pour voir » pas.
