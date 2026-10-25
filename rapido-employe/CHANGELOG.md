# Changelog — plugin rapido-employe

## 0.1.0 — 2026-10-25 — Claude employé commercial FoodEatUp

Première version, bâtie sur le cadre « Claude employé » du serveur Academy
« FoodEatUp formation » (`https://formation.foodeatup.fr/mcp`, 191 outils
relevés en session live via describe_server — liste versionnée
docs/inventaires/academy-tools-live.txt). Le principe : **le cadre se relit
(get_claude_brief puis get_work_plan), il ne se code jamais** — familles
d'autonomie, quotas et budget vivent dans l'Academy.

- **31 skills** en six groupes : journée (prise-de-poste, point-du-matin,
  executer-mes-routines, rapport-de-fin-de-journee), apprendre
  (chemin-de-formation, apprendre-une-tache, ma-certification,
  s-entrainer-en-jouant), déployer (deployer-ma-zone, business-plan,
  etude-de-marche-terrain), vendre (prospecter-une-zone, relancer-j3-j7,
  poser-les-demos, preparer-un-devis, argumentaire-et-objections, pitch,
  webinaire-du-mois), communiquer (communication-de-la-semaine,
  campagne-mot-cle, visuels-de-marque, bd-des-formations), servir
  (repondre-a-une-question-d-usage, repondre-aux-avis, onboarding-client-j90,
  customer-success), orchestrer (mon-equipe-d-agents, boucle-du-vendredi,
  construire-l-outil-manquant, ma-memoire, espace-responsable — réservé à
  l'invocation humaine).
- **9 agents** : claude-employe (chef d'orchestre), coach-academy,
  responsable (prépare les décisions, n'en prend aucune), et les six agents
  préparés dans l'Academy (accueil-demandes, relance-devis, prescripteurs,
  contenus, veille, pilotage) — leur prompt de production vient de
  get_agent_brief, les fichiers ne fixent que rôle, périmètre et garde-fous.
- **15 commandes** : /prise-de-poste, /point-du-matin, /routines,
  /apprendre, /deployer, /prospecter, /relances, /demo, /devis, /pitch,
  /semaine-com, /vendredi, /rapport, /outil-manquant, /cadre.
- **6 widgets HTML** (palette Academy du gabarit get_report_brief) +
  scripts/render_widget.py (stdlib, formules affichées) :
  plan-de-travail-du-jour, tableau-de-bord-kpi, pipeline-de-la-zone,
  progression-formation-et-badges, calendrier-editorial-semaine,
  avancement-du-deploiement. Les widgets MCP Apps du serveur
  (restaurant_3d, jeu_caisse_express) sont servis tels quels.
- **8 hooks testés en CI** : garde-cadre-employe (familles → niveaux relus
  dans .claude/state/cadre-employe.json, fail-closed, périmé > 24 h, deny si
  agent arrêté, « engager » toujours ask), garde-depense (record_expense
  accepté requis, refus = deny), garde-auto-gouvernance (deny absolu sur
  set_agent_policy, review_*, decide_module, incubation_admin_*,
  invite_learner, send_reminder), garde-envois (deny de l'envoi Gmail
  direct, ask sur tout envoi/publication, quotas du jour en deny),
  garde-memoire (e-mail/téléphone/IBAN/carte/jeton refusés dans remember),
  anti-donnee-inventee (coordonnées d'exemple, gabarits non remplis,
  promesses chiffrées — + héritage du contrôle température), SessionStart
  contexte, journal des écritures (PostToolUse, secrets masqués, compteurs
  de quotas, état des dépenses).
- **Table versionnée** reference/familles-outils.json : les écritures de
  tous les serveurs classées dans les 8 familles (clé serveur:outil, outil,
  préfixe — fail-closed : non classé = ask) ; source unique des 4 gardes.
- **Inventaires** : academy-tools-live.txt (191), planit-tools-live.txt
  (63), foodeatup-tutoriel-tools-live.txt (36) — relevés en session live du
  2026-10-25.
- `.mcp.json` : 9 serveurs requis (academy — porte à jeton
  `${ACADEMY_MCP_TOKEN}` —, foodeatup, foodeatup-tutoriel, site, social,
  rapidocrm, rapidocms, rapidorh, planit) + 6 optionnels (studio-print et
  prospector-hub en `${..._MCP_URL}` faute d'adresse publiée, build,
  lovable, gmail, google-drive). Un optionnel absent = volet sauté en le
  disant.
- CI : catalogues fail-closed academy/planit/foodeatup-tutoriel, périmètre
  OUTILS propre à rapido-employe/ (union des catalogues déclarés + table du
  plugin) sans toucher les périmètres foodeatup*/, serveurs annoncés
  (site, social, prospector-hub, studio-print, build) en catalogue distant.
