# Changelog — plugin planit

## 0.1.0 — 2026-10-25 — Plan'It de bout en bout

Première version, bâtie sur le serveur MCP Plan'It
(https://planit.braindcode.com/mcp) relevé en session live : **63 outils**
(docs/inventaires/planit-tools-live.txt), **10 destructifs** confirmés par
`list_destructive_tools` (reference/outils-sensibles.json, trois familles :
destructifs, payants, qui tranchent).

- **22 skills** : accueil-pilotage, mes-taches, agenda-des-routines,
  creer-une-routine (chaîne de l'Architecte), recommander-des-routines,
  installer-une-routine-du-registre, auditer-mes-routines, boucles-kpi,
  widgets-accueil, alertes-kpi, lancer-pause-reprise,
  bibliotheque-de-prompts, connecteurs-mcp, prompts-de-mes-outils,
  routines-sur-evenement, plugin-prive-sur-mesure,
  exporter-un-plugin-vers-planit (invocation humaine),
  comprendre-l-orchestrateur, video-courte, credits-et-autonomie,
  revue-du-vendredi, decouvrir-planit.
- **4 agents** : architecte, ingenieur-des-boucles, controleur-des-credits,
  concierge-des-connecteurs — chacun avec son périmètre d'outils ; ils
  proposent, l'utilisateur décide.
- **13 commandes** : /planit, /routine-nouvelle, /routines, /audit-routines,
  /boucles, /widgets, /calendrier, /credits, /connecteurs, /evenements,
  /catalogue-prive, /video, /vendredi.
- **6 widgets HTML** (thème neutre signalé — aucune charte Plan'It dans le
  dépôt) + scripts/render_widget.py et scripts/credits_autonomie.py
  (stdlib, formules affichées : crédits vidéo = max(5, ⌈s/2⌉), jours
  d'autonomie = solde / (total_mensuel/30)).
- **6 hooks testés en CI** : garde-planit (ask sur destructifs / payants /
  qui tranchent, fail-closed, confirm du modèle ignoré), garde-cout-annonce
  (deny de run/accept/resume sans estimate_routine_cost au journal de
  session, et d'add_kpi_widget sans list_kpi_catalog), garde-autonomie
  (ask sur autonomy_level auto ; deny du subscribe_event auto portant un
  outil destructif), verite-des-donnees (PostToolUse : rappels
  not_enough_data / throttled / flat_price-default), SessionStart
  (get_kpi_home + list_pending_routine_actions d'abord), journal des
  écritures (secrets masqués, alimente .claude/state/planit-session.json).
- **Référence** : directives-outils.md (les 63 rôles et leurs règles
  « utiliser avant » / « ne jamais », issues des descriptions du serveur),
  pieges-verifies.md (tâche ≠ routine, once/custom refusées, référence
  figée, 3 exécutions ET 14 jours, refus définitifs, sélection lente,
  connecteurs en erreur du relevé), guide-widgets.md (quel type pour quel
  KPI), outils-sensibles.json.
- CI : catalogue fail-closed `planit` (63, min 50) + périmètre OUTILS strict
  pour `planit/` (outils Plan'It uniquement), sans toucher les règles
  existantes.
- État des connecteurs au relevé : Gmail, RapidoCMS, RapidoRH et Plan'It
  connectés ; FoodEatUp en erreur de jeton (depuis juillet) ; RapidoCRM
  déconnecté — documenté dans les pièges, re-relevé à chaque séance.
