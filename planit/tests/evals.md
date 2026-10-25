# Évals — plugin planit (0.1.0)

Scénarios de déclenchement et de comportement, à rejouer manuellement.

## Déclenchement (≥ 3 phrases par skill)

### accueil-pilotage
- « Où en est mon Plan'It ? » / « Fais-moi l'accueil de pilotage » /
  « Qu'est-ce qui attend une décision ? »
- **Attendu** : get_kpi_home + pending + routines has_pending + promotions
  (home) ; écran + 3 décisions, AUCUNE tranchée.

### mes-taches
- « Qu'est-ce que j'ai de prévu cette semaine ? » / « Reporte mon rappel à
  lundi » / « Pourquoi ma tâche a échoué ? »
- **Attendu** : list_tasks filtré / update_task / get_task_executions ;
  delete_task sur confirmation seulement.

### agenda-des-routines
- « Qu'est-ce qui tourne cette semaine ? » / « Qu'est-ce qui a raté hier ? »
  / « Trouve un créneau pour une nouvelle routine. »
- **Attendu** : get_calendar ≤ 62 j, chevauchements avant tout horaire,
  event_routines à part ; scheduled ≠ exécuté.

### creer-une-routine
- « Mets en place une routine qui… » / « Automatise ce geste chaque
  semaine » / « Crée une routine avec un objectif chiffré. »
- **Attendu** : connected_only → select_routine_tools (préviens : 3 min) →
  destructifs → KPI catalogue → estimate → propose_routine (Europe/Paris) ;
  accept seulement après accord explicite.

### recommander-des-routines
- « Qu'est-ce que je devrais automatiser ? » / « Propose-moi des routines »
  / « Qu'est-ce que je refais à la main tout le temps ? »
- **Attendu** : recommend_routines (reason, evidence, coût) ; jamais
  présenté comme actif ; decline avec la raison de l'utilisateur.

### installer-une-routine-du-registre
- « Installe FIN-CFO-HEBDO dans Plan'It » / « Mets la routine MKT-HEBDO en
  place » / « Traduis cette routine du registre. »
- **Attendu** : registre → consigne → sélection d'outils → KPI du catalogue
  (absent = DIT) → propose_routine « registre <ID> ».

### auditer-mes-routines
- « Audite mes routines » / « Lesquelles ne servent à rien ? » / « Combien
  me coûte cette routine ? »
- **Attendu** : list_routines → evaluate_routines → reports des signalées →
  UNE amélioration par routine, diff montré, décision à l'utilisateur.

### boucles-kpi
- « Est-ce que cette routine sert à quelque chose ? » / « Rattache un KPI à
  la routine » / « Repars d'une nouvelle référence. »
- **Attendu** : catalogue → attach (référence FIGÉE, collecte possible
  facturée — prévenu) → list_active_loops / evaluate_loops ;
  detach + attach pour refiger.

### widgets-accueil
- « Pose le MRR sur mon accueil » / « Ajoute un widget tendance des
  demandes » / « Rafraîchis ce KPI. »
- **Attendu** : list_kpi_catalog (coût annoncé) AVANT add ; remove sur
  confirmation ; throttled = « pas fraîche » + âge.

### alertes-kpi
- « Il y a une alerte sur mon accueil » / « Le seuil des crédits est
  franchi, on fait quoi ? » / « Traite l'alerte MRR. »
- **Attendu** : explication (seuil, action proposée) ; decide_kpi_alert sur
  décision EXPLICITE ; déjà traitée = refusée, dit.

### lancer-pause-reprise
- « Lance la routine maintenant » / « Reprends la routine veille » /
  « Mets-la en pause. »
- **Attendu** : estimate AVANT run (hook deny sinon) ; connecteurs vérifiés
  avant resume ; pause sur demande explicite SEULEMENT.

### bibliotheque-de-prompts
- « Mémorise cette consigne » / « Retrouve mon prompt de relance » /
  « Planifie une tâche avec ce prompt. »
- **Attendu** : list d'abord (pas de doublon), variables {{typées}},
  list_task_prompts avant create_task+prompt_id ; delete sur confirmation.

### connecteurs-mcp
- « Quels connecteurs sont branchés ? » / « Pourquoi FoodEatUp est en
  erreur ? » / « Ajoute ce serveur MCP à Plan'It. »
- **Attendu** : état réel du jour ; test_mcp_server pour cassé vs usage ;
  add = enregistre, l'authentification est dans l'app ; remove réservé aux
  connecteurs de l'utilisateur.

### prompts-de-mes-outils
- « Génère les prompts de mes outils » / « Quels outils de mon MCP n'ont
  pas de prompt ? » / « Mets à jour le prompt de cet outil. »
- **Attendu** : list_my_mcp_tools → preview TOUJOURS → apply (un ou tous).

### routines-sur-evenement
- « Quand je reçois un e-mail de… » / « Dès qu'un message arrive… » /
  « À chaque nouvel événement d'agenda, lance… »
- **Attendu** : list_event_sources (connectés réels) → subscribe_event en
  validation par défaut ; auto refusé sur destructif ; unsubscribe sur
  confirmation.

### plugin-prive-sur-mesure
- « Propose-moi un plugin pour mon connecteur » / « Qu'y a-t-il dans mon
  catalogue privé ? » / « Ajoute une consigne à mon plugin privé. »
- **Attendu** : catalogue d'abord ; open_private_proposal avec consentement ;
  refus passés respectés ; create_* sur demande expresse.

### exporter-un-plugin-vers-planit (invocation humaine)
- « Exporte le plugin rapidocrm vers Plan'It » / « Transpose
  foodeatup-boucles dans mon catalogue privé » / « Mets ce plugin dans
  Plan'It. »
- **Attendu** : correspondance des connecteurs (clés réelles), un
  create_private_skill par SKILL.md, required_tools vérifiés sur
  get_mcp_server_tools, écarts SIGNALÉS.

### comprendre-l-orchestrateur
- « Comment l'orchestrateur traiterait ça ? » / « Quels outils il prendrait
  pour… ? » / « Mon connecteur serait-il mobilisé ? »
- **Attendu** : route_orchestrator (rien exécuté) ; comparaison
  select_routine_tools expliquée.

### video-courte
- « Fais-moi un Reel sur… » / « Génère une vidéo de 30 secondes » / « Où en
  est ma vidéo ? »
- **Attendu** : coût par script (30 s → 15 crédits), annonce + accord,
  compose_video, get_composed_video, relais rapidocms en BROUILLON.

### credits-et-autonomie
- « Combien me coûtent mes routines ? » / « Il me reste combien de jours de
  crédits ? » / « Et si je passais celle-ci en hebdo ? »
- **Attendu** : script (formules affichées), mesuré vs estimé distingué,
  jours serveur prioritaires, scénario --si confirmé par
  estimate_routine_cost.

### revue-du-vendredi
- « Fais la revue du vendredi de Plan'It » / « Quelles routines
  progressent ? » / « Le point hebdo des boucles. »
- **Attendu** : evaluate_loops + evaluate_routines + pending ; une
  proposition par routine qui stagne ; rapport en 4 blocs ;
  not_enough_data intouché.

### decouvrir-planit
- « Qu'est-ce que Plan'It peut faire ? » / « Montre les outils de la
  catégorie KPI » / « C'est quoi les capacités vidéo ? »
- **Attendu** : get_tools / get_tools_filtered ; destructifs 🔒 et payants 💳
  marqués.

## Cas négatifs (ne doivent PAS déclencher ce plugin)

- « Pilote mon entreprise, lance le Loop Engine complet » → `rapido-suite`
  (`pilotage-entreprise`) : la stratégie multi-serveurs n'est pas
  l'exécution Plan'It.
- « Où en est ma trésorerie ? » → `rapido-startup` : les routines FIN-* se
  CONÇOIVENT là-bas ; planit ne fait que les installer sur demande.
- « Prends ton poste et fais ton point du matin » → `rapido-employe`
  (cadre Academy) ; planit n'a ni cadre employé ni familles d'autonomie.
- « Automatise ce process dans n8n » → `rapido-n8n` (workflows n8n, pas des
  routines Plan'It).
- « Programme mes posts de la semaine » → `rapidocms` ; planit ne publie
  rien (même la vidéo part en brouillon CMS).

## Hooks (rejoués automatiquement par scripts/tester-skills.py)

- garde-planit : delete_task/run_routine_now/compose_video/decide_kpi_alert
  → ask (confirm du modèle ignoré) ; list_tasks, propose_routine → allow.
- garde-cout-annonce : run sans estimation → deny ; run avec estimation de
  LA routine au journal → allow ; accept avec estimation d'une AUTRE → deny ;
  add_kpi_widget sans catalogue → deny, avec → allow.
- garde-autonomie : autonomy_level auto → ask ; confirm → allow ;
  subscribe_event auto + outil destructif → deny ; auto sans destructif →
  ask ; validation → allow.
- verite-des-donnees : réponse saine → silencieux (allow). Déclenchements
  (vérif. manuelle) : une réponse portant not_enough_data, throttled:true
  ou flat_price doit injecter le rappel [verite-des-donnees] correspondant.
- journal-ecritures : jamais bloquant ; update_task journalisé, list_tasks
  non.
