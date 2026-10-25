# Directives transverses — serveur Plan'It (63 outils, relevé live du 2026-10-25)

À charger en étape 0 de chaque skill. Les règles « utiliser avant » et « ne
jamais » viennent des descriptions du serveur lui-même
(docs/inventaires/planit-tools-live.txt fait foi pour la liste ;
reference/outils-sensibles.json pour les familles sensibles).

## Les lois du serveur (valent pour tous les skills)

1. **Tâche ≠ routine** : la routine (`is_routine`) est récurrente, pilotée
   par un objectif chiffré, refuse `once` et `custom`, et seule elle accepte
   une boucle KPI.
2. **Trois niveaux d'autonomie** : propose, confirm, auto. Un outil
   destructif force confirm ; un abonnement événement en auto est refusé si
   la routine contient un outil destructif.
3. **Tout coût s'annonce AVANT** : `estimate_routine_cost` avant
   run_routine_now / accept_routine_proposal / changement de fréquence ;
   `list_kpi_catalog` avant add_kpi_widget ; crédits vidéo = max(5, ⌈s/2⌉).
   Une base `flat_price` ou `default` n'est pas une mesure.
4. **Boucles** : référence FIGÉE au rattachement ; verdict de boucle
   improving/flat/degrading, `not_enough_data` sous 3 exécutions ET
   14 jours ; verdict de routine effective/needs_improvement/
   no_measured_effect/failing/not_enough_data. Aucun effet annoncé sur
   not_enough_data ; `throttled: true` = valeur « pas fraîche » avec son âge.
5. **Propositions d'abord** : propose_* enregistre sans créer ; refusé =
   définitif à l'identique ; une amélioration = UN changement, la dernière
   remplace la précédente ; accept/apply seulement sur l'accord explicite
   portant sur CETTE proposition.
6. **Jamais de pause de sa propre initiative** — amélioration d'abord.
7. **Jamais une promotion hors `list_promotions`.**
8. **Une alerte KPI se tranche avec l'accord de l'utilisateur.**
9. **`add_mcp_server` ne connecte rien** (authentification dans l'app) ;
   catalogue public et connecteur natif jamais supprimables.

## Tâches (tasks)

| Outil | Rôle | Utiliser avant / ne jamais |
|---|---|---|
| `list_tasks` | lister (filtres type, statut, fréquence, dates) | pour les routines, préférer `list_routines` |
| `get_task` | détail par nom | — |
| `create_task` | créer tâche / routine (`is_routine`) | `list_task_prompts` avant un create avec `prompt_id` ; routine sans objectif chiffré = incomplète |
| `update_task` | reporter, reprogrammer, corriger | estimation avant un changement de fréquence d'une routine |
| `delete_task` | suppression DÉFINITIVE (+ notifications) | jamais sans confirmation |
| `get_task_executions` | « ça a tourné ? pourquoi échoué ? » | ne jamais déduire une exécution d'un état ≠ done |
| `list_task_prompts` | prompts planifiables (connecteur connecté) | avant tout create_task avec prompt_id ; jamais pour un simple rappel |
| `get_routine_report` | bilan 30 j : exécutions, crédits, outils, signaux | avant de modifier, promouvoir ou arrêter |
| `propose_routine_improvement` | PROPOSITION d'amélioration (diff rendu) | après get_routine_report ; un changement à la fois |
| `apply_routine_improvement` | APPLIQUE (réfige les références) | jamais sans accord explicite |
| `decline_routine_improvement` | refuse la proposition | sur décision de l'utilisateur |

## Routines (routines)

| Outil | Rôle | Utiliser avant / ne jamais |
|---|---|---|
| `get_calendar` | occurrences sur ≤ 62 jours, event_routines à part | avant de proposer un horaire (chevauchements) |
| `list_routines` | santé, pause, prochaine/dernière exécution, coût/mois, verdict, décisions | à la place de list_tasks+reports pour l'audit |
| `recommend_routines` | candidats calculés (reason, evidence, coût) | ne crée rien ; jamais présenté comme actif |
| `propose_routine` | ENREGISTRE une proposition validée + coût | toujours une raison ; jamais accepté dans la foulée |
| `accept_routine_proposal` | CRÉE la routine (destructif) | coût annoncé + accord explicite sur CETTE proposition |
| `decline_routine_proposal` | refus définitif à l'identique | noter la raison donnée |
| `pause_routine` | suspend (destructif) | jamais de sa propre initiative |
| `resume_routine` | reprend (destructif ; connecteurs revérifiés) | vérifier les connecteurs + annoncer le coût avant |
| `run_routine_now` | exécution réelle immédiate (destructif) | `estimate_routine_cost` + accord avant |
| `evaluate_routines` | verdicts ENREGISTRÉS à l'historique | aucun effet annoncé sur not_enough_data |
| `list_pending_routine_actions` | tout ce qui attend une décision | en début de conversation et d'audit |
| `estimate_routine_cost` | coût 30 j (base measured/flat_price/default) | avant run/accept/changement de fréquence |

## Prompts (prompts)

`list_prompts`, `get_prompt`, `create_prompt` (variables {{typées}},
description courte ≠ contenu), `update_prompt`, `delete_prompt` (destructif,
confirmation), `list_my_mcp_tools` (outils de MES connecteurs + prompt lié),
`apply_my_tool_prompt` / `apply_all_my_tool_prompts` (génèrent les prompts
privés d'outils — `preview_my_tool_prompts` TOUJOURS avant).

## KPI (kpi)

`get_kpi_home` (crédits, autonomie, widgets, boucles, alertes — aucun appel
facturé), `list_kpi_catalog` (coût de collecte : AVANT add_kpi_widget),
`add_kpi_widget` (payant ; échoue si déjà posé), `remove_kpi_widget`
(destructif ; l'historique est conservé), `refresh_kpi` (payant ; règle
throttled), `attach_kpi_to_routine` (fige la référence ; collecte possible
facturée ; routine seulement), `detach_kpi_from_routine` (la boucle et son
verdict disparaissent), `evaluate_loops` (verdict à l'instant ; 3 exécutions
ET 14 jours), `list_active_loops` (référence figée, écart orienté),
`decide_kpi_alert` (tranche : accord explicite obligatoire).

## Connecteurs (mcp)

`list_mcp_servers` (état RÉEL : connecté, erreur, jamais branché),
`get_mcp_server_tools` (outils + drapeau destructif), `list_destructive_tools`
(la liste des actions à ne jamais déclencher sans accord),
`test_mcp_server` (distinguer connecteur cassé / erreur d'usage),
`add_mcp_server` (enregistre, ne connecte pas), `remove_mcp_server`
(destructif ; uniquement un connecteur ajouté par l'utilisateur).

## Orchestration, découverte, événements, catalogue, média

`select_routine_tools` (sous-ensemble pertinent, jusqu'à 3 minutes —
prévenir), `route_orchestrator` (expliquer sans exécuter), `get_tools` /
`get_tools_filtered` (catégories : tasks, routines, prompts, kpi, mcp,
orchestration, discovery, events, catalog, media), `list_promotions`
(la seule source des promos), `list_event_sources` (connecteurs Composio
réellement connectés) → `subscribe_event` (gouvernance validation par
défaut ; auto refusé si destructif) → `unsubscribe_event` (destructif),
`list_my_private_catalog` → `open_private_proposal` (consentement requis ;
respecter refusés/acceptés) → `propose_private_item` (un élément, name +
summary suffisants) ; `create_private_plugin` / `create_private_skill`
(demande explicite seulement, idempotents par slug), `compose_video`
(payant : 1 crédit/2 s, min 5 ; 10-60 s) → `get_composed_video` (état, URL).

## KB client

Si `./rapido-kb/` existe : y lire objectifs et seuils de l'entreprise pour
chiffrer les objectifs des routines (jamais un objectif inventé).
