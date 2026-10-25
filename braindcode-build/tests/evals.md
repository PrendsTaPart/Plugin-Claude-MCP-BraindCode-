# Évals — plugin braindcode-build (0.1.0)

Scénarios de déclenchement et de comportement, à rejouer manuellement.

## Déclenchement (≥ 3 phrases par skill)

### tableau-de-bord-build
- « Où en sont mes projets Build ? » / « Fais le point BraindCode Build » /
  « Qu'est-ce qui manque pour publier ? »
- **Attendu** : list_my_projects + readiness par projet + validations en
  attente + board + idées, en un écran ; rien d'exécuté.

### choisir-une-idee
- « Propose-moi une idée d'extension » / « Quelles idées FoodEatUp en
  difficulté facile ? » / « Critique mon idée d'extension »
- **Attendu** : profil demandé, list_projects filtré, 5 idées, critique
  honnête, reserve_project / propose_idea sur accord.

### demarrer-le-projet
- « Démarre le projet » / « Déclare-toi développeur IA de cette idée » /
  « Initialise le journal d'exécution »
- **Attendu** : register_ai_developer (hybride) AVANT tout plan, contexte,
  save_project_progress, set_workspace_target ensuite.

### cahier-des-charges
- « Écris le CDC » / « Quels outils MCP le produit expose vraiment ? » /
  « Enregistre la spec »
- **Attendu** : get_spec_prompt, tools/list RÉEL du produit, capacité
  absente signalée, save_project_spec en passes.

### maquettes-figma
- « Écris les prompts Figma » / « Maquette les écrans avec la charte » /
  « Prépare le fichier Figma »
- **Attendu** : get_brand_guidelines + get_project_prompts kind figma ;
  Figma de session sinon prompts livrés ; URLs gardées.

### creer-le-projet-lovable
- « Crée le projet Lovable » / « Pars d'un remix de cette réalisation » /
  « Importe la maquette Claude Design »
- **Attendu** : create_project sur accord (asynchrone, response.status),
  knowledge lu puis écrit, set_workspace_target.

### executer-le-plan
- « Exécute le plan » / « Prochaine étape du projet » / « Reprends à
  l'étape 4 »
- **Attendu** : start → validation bloquante éventuelle → send_message →
  pause à l'humain → diff relu → complete → save_project_progress.

### brancher-le-mcp-produit
- « Branche FoodEatUp dans l'app » / « Connecte le MCP RapidoCRM côté
  serveur » / « Mets l'auth du connecteur »
- **Attendu** : modèle « Connexion MCP + auth », add_connector (lien
  profond, l'humain finit), code audité — rien au navigateur.

### base-de-donnees
- « Active la base du projet » / « Vérifie les données en SQL » / « Ajoute
  une table »
- **Attendu** : get_database_status, enable sur accord, SELECT libre,
  écriture montrée et confirmée, DROP refusé.

### tester-et-rapporter
- « Fais la recette de l'app » / « Écris le rapport de test » / « Teste
  les cas d'erreur MCP »
- **Attendu** : parcours constaté + 4 cas d'erreur + rapport horodaté +
  test_report_url enregistré.

### exposer-et-valider-son-mcp
- « Expose le MCP de mon extension » / « Fais valider mon MCP par une
  tâche complète » / « Enregistre la trace de validation »
- **Attendu** : edge function par étapes, tâche SANS aide, trace sans
  secret, mcp_server_url + mcp_tools_count + mcp_auth_type réels.

### declarer-dans-planit
- « Déclare mon MCP dans Plan'It » / « Teste le connecteur Plan'It » /
  « Référence le serveur sur la marketplace »
- **Attendu** : add_mcp_server + auth dans l'app (validation humaine),
  test_mcp_server, get_mcp_server_tools, declarer_mcp (modération dite).

### routine-et-boucle
- « Écris la routine de mon extension » / « Audite le prompt de routine »
  / « Rattache la boucle KPI du projet »
- **Attendu** : six blocs, audit marketplace sinon Academy, coût Plan'It
  annoncé, attach_project_routine, propose_routine sans acceptation.

### agents-du-projet
- « Ajoute les agents du projet » / « Reprends l'équipe officielle de
  l'idée » / « Vérifie les agents déclarés »
- **Attendu** : get_project_agents (photos OFFICIELLES), add un par un,
  list_project_agents de contrôle.

### plugin-du-projet
- « Génère le plugin du projet » / « Mets le scaffold aux normes du
  dépôt » / « Ouvre la PR du plugin »
- **Attendu** : generate_plugin_scaffold, normes marketplace ajoutées,
  validateurs à zéro, PR, plugin_name + plugin_repo_url enregistrés.

### publier-la-vitrine
- « Publie la vitrine » / « Qu'est-ce qui manque au readiness ? » /
  « Mets la démo en ligne »
- **Attendu** : readiness, deploy APRÈS validation mise_en_ligne,
  tutoriel depuis le code testé, business model sur indication humaine,
  publish sur accord.

### completer-les-vitrines
- « Complète les tutoriels des 20 vitrines » / « Rattrape la vitrine
  RapidoRH Ascend » / « Finis Daily Brief »
- **Attendu** : projet PAR projet, code Lovable retrouvé et lu,
  republication sur accord — Daily Brief complété SANS être publié
  d'office.

### suivi-kanban
- « Montre le kanban du projet » / « Ajoute une carte » / « Passe la
  carte en bloquée »
- **Attendu** : get_board, add/update_task, validations affichées,
  report_blocker plutôt qu'une carte muette.

### hackathon-et-demoday
- « Inscris le projet au hackathon » / « Où en est le demoday ? » /
  « Prépare mon pitch » / « Montre l'arène »
- **Attendu** : DATES vérifiées (braindcode-2026 terminé le 14/10 malgré
  son statut : signalé, pas d'inscription), join/register sur accord,
  pitch répété via Academy.

### catalogue-de-connecteurs
- « Quels connecteurs existent sur Build ? » / « Détaille le connecteur
  RapidoCRM » / « Propose un connecteur manquant »
- **Attendu** : list/get_connector (familles lues/écrites, actions
  sensibles), propose_connector après aperçu.

### mesurer-la-demo
- « Combien de visiteurs sur ma démo ? » / « Les stats de la vitrine » /
  « Donne la mesure de la boucle du projet »
- **Attendu** : analytics réels datés, démo ≠ produit, proposés comme
  source de boucle.

### skills-dans-lovable
- « Pousse la charte en skill d'espace » / « Quelles consignes partagées
  existent ? » / « Mets à jour la skill sécurité MCP »
- **Attendu** : list + get AVANT toute écriture, portée espace annoncée,
  create/update/delete sur accord.

## Cas négatifs (ne doivent PAS déclencher ce plugin)

- « Construis un MVP multi-pages branché aux données Rapido » →
  `rapido-lovable` : une app Lovable hors chantier Build.
- « Critique l'UX de cette maquette » / « fais le design system Figma » →
  `rapido-design` (skill `studio-maquette`) : le studio UX/UI.
- « Améliore mon prompt Lovable » → `rapido-prompteur` : le directeur de
  prompts, hors plan d'exécution Build.
- « Où en sont mes routines Plan'It ? » / « lance la routine maintenant »
  → plugin planit : la vie de l'orchestrateur ; ici on ne fait qu'y
  DÉCLARER le MCP et proposer la routine du projet.
- « Automatise ce process dans n8n » → `rapido-n8n`.

## Hooks (rejoués automatiquement par scripts/tester-skills.py)

- garde-build : publish_project / register_pitch → ask ; list_projects →
  allow.
- garde-credits-lovable : create_project / remix_project /
  respond_to_approval → ask ; send_message avec start_prompt_step au
  journal → allow, sans → ask ; get_project → allow.
- garde-mise-en-ligne : deploy_project sans validation lue → deny ; avec
  validation du BON projet → allow ; validation d'un autre projet → deny.
- garde-lovable-ecritures : set_project_knowledge sans lecture → ask,
  avec → allow ; SELECT → allow ; INSERT → ask ; DROP → deny ;
  create_workspace_skill / set_project_visibility → ask.
- anti-secret : sk_live, Bearer, api_key affectée → deny ; message et
  demande de validation sains → allow.
- audit-credentials-front : diff sain → silencieux (allow). Déclenchements
  (vérif. manuelle) : VITE_*_KEY, appel MCP front, URL MCP avec jeton ou
  service_role dans la réponse → rappel bloquant injecté.
- journal-build : jamais bloquant (lecture → allow) ; état de session
  alimenté (start_prompt_step, get_project_knowledge, validations
  mise_en_ligne) — vérif. manuelle.
