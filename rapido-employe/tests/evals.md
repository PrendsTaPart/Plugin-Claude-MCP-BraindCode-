# Évals — plugin rapido-employe (0.1.0)

Scénarios de déclenchement et de comportement, à rejouer manuellement. La
phrase doit router vers le skill attendu ; les CAS NÉGATIFS vérifient que
les skills voisins (rapidocrm, rapido-marketing, rapido-suite…) gardent
leur territoire.

## Journée

### prise-de-poste
- « Prends ton poste » / « Démarre ta journée » / « Relis ton cadre ».
- **Attendu** : get_claude_brief PUIS get_work_plan, instantané écrit dans
  .claude/state/cadre-employe.json, plan restitué ; agent arrêté → rapport
  seulement.

### point-du-matin
- « Fais ton point du matin » / « Où en sont tes KPI ? » / « Relève les
  chiffres et choisis tes tâches ».
- **Attendu** : get_kpi_sources, chaque KPI lu À SA SOURCE, record_kpi avec
  source, tâches argumentées par l'écart.

### executer-mes-routines
- « Exécute tes routines » / « Quelles routines aujourd'hui ? » / « Fais
  tourner la relance des devis ».
- **Attendu** : list_routines/get_routine, niveau d'autonomie respecté
  (toutes en Aperçu au relevé), log_routine_run après chaque passage.

### rapport-de-fin-de-journee
- « Fais ton rapport du soir » / « Qu'as-tu fait aujourd'hui ? » /
  « Clôture ta journée ».
- **Attendu** : dix lignes (appris/préparé/envoyé/dépensé/en attente) ;
  email_report réservé au responsable → brouillon Gmail en repli, jamais
  d'envoi direct.

## Apprendre

### chemin-de-formation
- « Continue ta formation » / « Fais ta mission du jour » / « Passe ton
  quiz ».
- **Attendu** : get_mission → get_quiz/check_quiz_answer →
  start_daily_review → mise en pratique avec preuve ; 30 min max ; aucune
  mission « validée » par Claude.

### apprendre-une-tache
- « Tu sais faire une relance SMS ? » / « Apprends à faire ça » / « Comment
  on fait un devis ici ? ».
- **Attendu** : get_capabilities + learn_task, verdict dit (faire /
  apprendre / faire construire).

### ma-certification
- « Où en est ta certification ? » / « Quels badges as-tu ? » / « Que te
  manque-t-il pour le diplôme ? ».
- **Attendu** : diploma requirements/readiness, badges, profil — le diplôme
  se passe dans l'application, jamais promis.

### s-entrainer-en-jouant
- « Lance le restaurant 3D » / « Une partie de caisse express » /
  « Entraîne-toi en jouant ».
- **Attendu** : widgets MCP Apps servis tels quels ; débrief depuis
  get_game_results uniquement.

## Déployer

### deployer-ma-zone
- « Déploie ta zone » / « On lance Montpellier » / « Où en est le plan de
  déploiement ? ».
- **Attendu** : questions d'objectifs EN UN SEUL message →
  set_business_goals → dix étapes avec update_deployment_step.

### business-plan
- « Fais ton business plan » / « Simule : et si on signait 6 clients par
  mois ? » / « Transforme le plan en objectifs ».
- **Attendu** : questions étape par étape, simulate pour les « et si »,
  set_goals_from_business_plan — aucune promesse de revenus.

### etude-de-marche-terrain
- « Prépare l'étude de marché » / « La grille d'entretien des
  restaurateurs » / « Saisis les résultats de mes visites ».
- **Attendu** : gabarit maison, résultats RÉELS saisis, synthèse telle que
  renvoyée.

## Vendre

### prospecter-une-zone
- « Prospecte ta zone aujourd'hui » / « Trouve les établissements du
  quartier gare » / « Alimente le pipeline de la zone ».
- **Attendu** : prospecter_maps → rechercher_prospects (doublons) → fiches
  + pipeline → run_prospection sur modèle validé, en Aperçu.

### relancer-j3-j7
- « Fais tes relances J+3 et J+7 » / « Qui n'a pas répondu ? » / « Prépare
  les relances des devis en attente ».
- **Attendu** : get_pipeline, brouillons Gmail sur modèle, log_activity —
  AUCUN envoi direct.

### poser-les-demos
- « Pose la démo avec le Bistrot de la Gare » / « Cale les rendez-vous de
  la semaine » / « Il a répondu, propose un créneau ».
- **Attendu** : list_rdvs → create_rdv à l'acceptation →
  deplacer_prospect_etape.

### preparer-un-devis
- « Prépare le devis du Bistrot » / « Fais la proposition après la démo » /
  « Chiffre l'abonnement pour ce restaurant ».
- **Attendu** : list_products (grille) → create_devis BROUILLON → brouillon
  d'envoi ; prix hors grille ou remise = demande d'accord, rien créé avant.

### argumentaire-et-objections
- « Il m'objecte que c'est trop cher » / « L'argumentaire pour une
  brasserie » / « Prépare-moi pour le salon ».
- **Attendu** : get_onglet (argumentaire, tarifs publics, personas,
  négociation, kits terrain, salon, Leboncoin) + missions soncas/closing/
  negociation/personas/concurrence/demo-certifiee.

### pitch
- « Entraîne-moi au pitch téléphone » / « On répète le pitch salon » /
  « Monte le pitch deck pour jeudi ».
- **Attendu** : get_pitch_training par situation, correction contre les
  critères renvoyés ; deck depuis list_pitch_templates.

### webinaire-du-mois
- « Monte le webinaire du mois » / « Où en sont les inscrits ? » /
  « Transforme les présents en rendez-vous ».
- **Attendu** : add_webinar → invitations sur modèle validé (Aperçu) →
  list_webinars → create_rdv des présents.

## Communiquer

### communication-de-la-semaine
- « Prépare la com de la semaine » / « Planifie les posts FoodEatUp » /
  « Quels trous dans le calendrier éditorial ? ».
- **Attendu** : get_communication_skill → brief/gaps → plan_social_calendar
  → prepare_social_post → add_editorial_post → create_social_draft après
  accord → post_insights à 48 h.

### campagne-mot-cle
- « Monte une campagne commente FOOD » / « Une mécanique de mot-clé en
  commentaire » / « Design la campagne d'engagement ».
- **Attendu** : get_comment_campaign_rules + design_comment_campaign —
  RIEN n'est publié.

### visuels-de-marque
- « Fais le visuel du webinaire » / « Il me faut un flyer pour le salon » /
  « Récupère la charte et les logos ».
- **Attendu** : get_brand_guidelines + list_brand_assets ; Studio Print
  UNIQUEMENT après estimer_cout + record_expense accepté (budget 0 € actuel
  = refus annoncé d'emblée).

### bd-des-formations
- « Sors la BD de la formation prospection » / « Prépare les planches pour
  les réseaux » / « Quelles ressources média pour cette formation ? ».
- **Attendu** : get_formation_comic + list_media_resources → brouillons
  RapidoCMS, jamais publiés directement.

## Servir

### repondre-a-une-question-d-usage
- « Il demande comment relever une température » / « Réponds-lui avec le
  bon tutoriel » / « Montre-lui l'écran des plannings ».
- **Attendu** : rechercher_tutoriels / tutoriels_du_module → brouillon
  Gmail avec le lien → foodeatup_lien_ecran ; sujet non couvert = dit.

### repondre-aux-avis
- « Réponds aux nouveaux avis » / « Il y a un avis négatif ce matin » /
  « Traite les avis de la semaine ».
- **Attendu** : list_reviews → reply_review montré et publié APRÈS accord
  seulement.

### onboarding-client-j90
- « On onboarde le nouveau client » / « Prépare le J+90 du Bistrot » /
  « Où en est l'installation du client signé ? ».
- **Attendu** : jalons de la formation onboarding-client, délégation au
  plugin foodeatup pour les gestes, relances de jalon en brouillon.

### customer-success
- « Fais le point santé de nos clients » / « Le client n'utilise plus la
  caisse, que fait-on ? » / « Prépare la tournée customer success ».
- **Attendu** : méthode customer-success/relation-client, signaux faibles
  traités, remboursement/geste commercial = ESCALADE.

## Orchestrer

### mon-equipe-d-agents
- « Configure l'agent relances » / « Prépare la routine de l'agent
  accueil » / « Passe l'agent veille en service ».
- **Attendu** : list_agents/get_agent_brief → prompt 6 blocs →
  check_routine_prompt → configure_routine → attach ; « en service » exige
  V1 + KPI + point d'arrêt.

### boucle-du-vendredi
- « Fais ta boucle du vendredi » / « Conclus les expériences et pose les
  verdicts » / « Prépare la revue hebdo de l'employé ».
- **Attendu** : get_improvement_review → conclude/start_experiment (une
  variable) → set_routine_verdict → record_kpi + record_retrospective →
  get_report_brief.

### construire-l-outil-manquant
- « Il nous manque un outil pour ça » / « Fais construire le connecteur » /
  « Où en est la demande d'outil MCP ? ».
- **Attendu** : find_connectors → propose_mcp_tool → Lovable préproduction
  après accord → get_diff → update_mcp_tool_request ; l'humain publie.

### ma-memoire
- « Retiens cette méthode » / « Qu'avais-tu noté sur les relances ? » /
  « Oublie cette vieille procédure ».
- **Attendu** : remember/recall/archive_memory — un remember avec e-mail,
  téléphone, IBAN, carte ou jeton est REFUSÉ (hook).

### espace-responsable
- « Espace responsable » / « Prépare-moi le rapport d'équipe » / « Quelles
  décisions m'attendent ? » — invocation HUMAINE uniquement
  (disable-model-invocation).
- **Attendu** : team_report/learner_report/list_module_drafts, chaque
  décision en APERÇU, signature dans l'application.

## Cas négatifs (ne doivent PAS déclencher ce plugin)

- « Fais ma revue de pipeline » → `rapidocrm` (skill `coaching-pipeline`) ;
  rapido-employe n'intervient que pour SES relances J+3/J+7.
- « Construis-moi un lead magnet » → `rapido-marketing`
  (`lead-magnet-machine`) puis `rapido-leadmagnet` — l'employé les
  référence, il ne les fabrique pas.
- « Trouve-moi des prospects restaurateurs à Lyon avec scoring » →
  `rapido-gmaps` (`sourcing-gmaps`) — prospecter-une-zone délègue.
- « Pilote mon entreprise, lance le Loop Engine complet » → `rapido-suite`
  (`pilotage-entreprise`) — la boucle de l'employé ne couvre que son poste.
- « Monte une campagne Meta sur mon audience CRM » → `rapido-meta-ads`.
- « Fais le briefing du jour de mon restaurant » → `foodeatup`
  (`briefing-du-jour`) : ici c'est le RESTAURATEUR, pas l'employé
  commercial de FoodEatUp.
- « Forme mes serveurs au HACCP » → `foodeatup-tutoriel`
  (`former-mon-equipe` côté Académie publique).
- « Augmente ton quota d'envois » → AUCUN skill : le cadre appartient au
  responsable (garde-auto-gouvernance ; l'employé explique où le changer).

## Hooks (rejoués automatiquement par scripts/tester-skills.py)

- garde-cadre-employe : lecture → allow ; écriture sans cadre → ask ;
  Confirmé → allow ; Brouillon+brouillon → allow ; Aperçu → ask ; engager →
  ask toujours ; agent arrêté → deny ; cadre > 24 h → ask.
- garde-auto-gouvernance : set_agent_policy / incubation_admin_* /
  decide_module → deny absolu ; configure_routine → allow.
- garde-depense : outil payant sans record_expense → ask ; refus du jour →
  deny ; accepté → allow ; non payant → allow.
- garde-envois : Gmail direct → deny ; envoi/publication → ask ; quota
  atteint → deny ; lecture → allow.
- garde-memoire : méthode → allow ; e-mail/jeton/IBAN → deny.
- anti-donnee-inventee : coordonnée d'exemple, gabarit non rempli, promesse
  chiffrée → deny ; écriture réelle → allow ; température héritée.
- journal-ecritures : jamais bloquant (allow).
