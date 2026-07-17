# Backlog — recettes n8n pour la collection « routines »

> Issu de la collection `data/prompts-collections/routines.json` : chaque routine
> badgée 🤖 (mode `n8n` ou `mixte`) suppose un workflow n8n qui la déclenche **sans
> Claude** (planning), via `usine-automatisations`. Ce fichier liste celles **qui
> n'ont pas encore de recette** dans `reference/recettes-*.md`. Une recette = un
> Schedule/Webhook → appels MCP/HTTP → mémoire (table anti-doublon) → rappel/alerte.
>
> **Déjà couverte** : `#33 La sentinelle cash (R7)` → `reference/recette-r7-cash-sentinel.md`.

## À produire (12)

| # | Routine | Fréquence | Mode | Serveurs | Nature du workflow n8n attendu |
|---|---|---|---|---|---|
| 1 | La tournée des agents | quotidien 9h | mixte | rapidorh | **Rappel** : Schedule 9h → notifie « lance la tournée des agents » (le prompt prêt). L'exécution reste en session (niveau 2). |
| 3 | Où en est le projet | hebdo (vendredi 16h) | n8n | rapidorh | **Rapport** : Schedule → lecture Kanban/dailies → synthèse avancement/blocages → envoi interne (lecture seule). |
| 5 | Le people report | mensuel (1er) | n8n | rapidorh | **Rapport** : Schedule mensuel → effectifs/charge/risques → page direction (lecture seule). |
| 8 | Les stats du soir | quotidien 18h30 | mixte | rapidocms | **Relevé** : Schedule → insights des posts publiés → écriture journal/banque de hooks ; l'analyse fine en session. |
| 13 | Les leads de la nuit | quotidien 8h45 | n8n | rapidocrm | **Scoring** : Schedule → nouveaux leads → score fit×engagement×fraîcheur → top du jour (lecture + tri). |
| 14 | Les devis qui expirent | quotidien 9h30 | mixte | rapidocrm | **Détection** : Schedule → devis J-7 → liste (mémoire anti-double-signalement) ; les relances en brouillon restent en session. |
| 20 | Le briefing du patron | quotidien 8h | n8n | foodeatup | **Rapport** : Schedule 8h → `get_daily_brief` (HACCP/résa/staff/prod/stocks) → envoi du brief. |
| 21 | Les températures sans oubli | quotidien 9h et 15h | mixte | foodeatup | **Rappel** : 2 Schedules → équipements à contrôler → notification ; la saisie guidée en session (jamais de valeur inventée). |
| 23 | La caisse propre | quotidien 23h | n8n | foodeatup | **Rapport** : Schedule 23h → rapport X de session + écarts (lecture) ; la clôture Z reste une confirmation humaine. |
| 27 | Les pubs sous contrôle | quotidien 9h15 | n8n | facebook-ads, google-ads, tiktok-ads | **Alerte** : Schedule → dépense/coût par résultat vs seuils KB → alerte si dérive (aucune modification). |
| 30 | La veille concurrents | hebdo (jeudi) | mixte | facebook-ads | **Relevé** : Schedule → pubs actives des concurrents (angles/offres) → journal ; le contre-angle en session. |
| 32 | Le monday brief | hebdo (lundi 8h) | mixte | rapidocrm, rapidocms, rapidorh, foodeatup | **Rappel** : Schedule lundi 8h → notifie « lance le monday brief » (le prompt prêt). Synthèse en session (lecture). |

## Règles communes (à respecter dans chaque recette)

- **Mémoire obligatoire** : une table n8n par routine (`*_journal`) pour éviter les
  doubles envois / re-signalements (cf. recettes existantes).
- **Gouvernance d'autonomie** : les workflows 🤖 se limitent au **niveau de la routine**
  (`autonomie` dans `routines.json`) — lecture/alerte pour aut. 0, brouillon pour aut. 1 ;
  aucune écriture métier ni envoi externe d'office.
- **Seuils depuis `./rapido-kb/`** : jamais de seuil de décision en dur (KB prime).
- **Déploiement** : via `usine-automatisations` (cycle complet : design → validate →
  create → test), pas de workflow créé à la main.

> Priorité suggérée : les 🤖 purs d'abord (#3, #5, #13, #20, #23, #27), qui apportent
> le plus de valeur « sans Claude » ; puis les rappels des mixtes (#1, #8, #14, #21,
> #30, #32).
