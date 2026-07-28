# Inventaire des plugins de la marketplace `rapido`

> Généré depuis l'état réel du dépôt (P0.1). Régénérable : les données
> proviennent des fichiers, jamais de mémoire. « non déclaré » = info absente des fichiers.

## 1. Plugins présents

| Chemin | Nom | Version | Skills | Commands | Agents | Hooks (entrées) |
|---|---|---|---|---|---|---|
| ./foodeatup | foodeatup | 1.7.0 | 18 | 0 | 4 | 3 |
| ./rapido-canva | rapido-canva | 1.0.2 | 7 | 0 | 1 | 2 |
| ./rapido-copywriter | rapido-copywriter | 0.6.0 | 4 | 0 | 1 | 2 |
| ./rapido-design | rapido-design | 0.5.0 | 4 | 0 | 1 | 2 |
| ./rapido-direction | rapido-direction | 1.1.0 | 5 | 0 | 1 | 2 |
| ./rapido-elevenlabs | rapido-elevenlabs | 0.1.1 | 0 | 0 | 0 | 4 |
| ./rapido-forge | rapido-forge | 1.1.3 | 181 | 0 | 4 | 2 |
| ./rapido-gmaps | rapido-gmaps | 0.5.0 | 4 | 0 | 1 | 3 |
| ./rapido-google-ads | rapido-google-ads | 0.1.0 | 4 | 0 | 0 | 2 |
| ./rapido-higgsfield | rapido-higgsfield | 1.0.4 | 9 | 0 | 1 | 3 |
| ./rapido-leadmagnet | rapido-leadmagnet | 0.5.0 | 4 | 0 | 1 | 2 |
| ./rapido-lovable | rapido-lovable | 1.5.2 | 10 | 0 | 2 | 2 |
| ./rapido-marketing | rapido-marketing | 0.18.3 | 17 | 0 | 5 | 4 |
| ./rapido-meta-ads | rapido-meta-ads | 1.0.5 | 13 | 0 | 1 | 3 |
| ./rapido-n8n | rapido-n8n | 1.6.2 | 4 | 0 | 1 | 3 |
| ./rapido-prompteur | rapido-prompteur | 1.0.0 | 4 | 0 | 1 | 2 |
| ./rapido-relation-client | rapido-relation-client | 0.2.0 | 6 | 0 | 0 | 2 |
| ./rapido-seo | rapido-seo | 0.1.0 | 6 | 0 | 0 | 2 |
| ./rapido-startup | rapido-startup | 1.10.0 | 6 | 0 | 2 | 3 |
| ./rapido-suite | rapido-suite | 1.4.2 | 13 | 0 | 1 | 7 |
| ./rapido-tiktok-ads | rapido-tiktok-ads | 0.1.0 | 3 | 0 | 0 | 2 |
| ./rapido-video | rapido-video | 1.0.1 | 2 | 0 | 0 | 2 |
| ./rapidocms | rapidocms | 1.11.8 | 22 | 0 | 6 | 3 |
| ./rapidocrm | rapidocrm | 1.7.0 | 29 | 0 | 2 | 2 |
| ./rapidorh | rapidorh | 1.1.0 | 12 | 0 | 2 | 2 |

Total : **25 plugins**, **387 skills**, 38 agents.

## 2. Skills par plugin (name + description frontmatter)

### foodeatup

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `analyse-rentabilite-carte` | Utiliser quand l'utilisateur veut analyser sa carte, savoir quels plats garder ou parle d'ingénierie de menu. Applique la matrice popularité × marge (Stars, Plow-horses, Puzzles… |
| `briefing-du-jour` | Utiliser quand l'utilisateur demande le briefing du jour, « ma journée » ou un point du matin. Routine du directeur de restaurant — HACCP, réservations, salle, staffing, product… |
| `caisse-du-jour` | Utiliser quand l'utilisateur parle de caisse, de POS, d'ouvrir la caisse, d'encaisser une note, de rendu monnaie, de clôture Z, de rapport de caisse ou d'ardoises clients — « ou… |
| `carte-vitrine` | Utiliser quand l'utilisateur veut construire ou mettre à jour sa carte en ligne (vitrine web), ses catégories de carte ou ses formules. Bâtit toute la carte vitrine en un appel … |
| `coordination-cuisine` | Utiliser quand, pendant le service, l'utilisateur parle du pass, de l'écran cuisine (KDS), d'un plat prêt, en préparation ou à lancer, ou de coordonner cuisine et salle. Fait av… |
| `fidelite-restaurant` | Utiliser quand l'utilisateur parle de fidélité, de points, de récompenses, de cartes cadeaux, de bons à valider ou d'un geste commercial — « mon programme de fidélité », « ajout… |
| `gestion-commandes` | Utiliser quand l'utilisateur veut créer une commande, suivre les commandes en cours ou changer le statut d'une commande (confirmée, en préparation, prête, livrée) dans son resta… |
| `haccp-conformite-quotidienne` | Utiliser quand l'utilisateur parle de relevé de température, HACCP, contrôle réception, étiquette DLC, checklist hygiène, plan de nettoyage ou conformité du jour. Couvre la rout… |
| `handle-complaint` | Utiliser quand un client se plaint (email, avis, ticket) et qu'il faut traiter la réclamation de bout en bout : contexte récupéré, réponse rédigée, correctif opérationnel propos… |
| `margin-analyzer` | Utiliser quand l'utilisateur parle d'augmenter ses prix, de marges, de coûts qui grignotent le profit, ou demande « est-ce que je gagne assez ? », « je devrais facturer plus ? »… |
| `onboarding-restaurateur` | Utiliser quand un nouveau client restaurateur démarre sur FoodEatUp, ou quand l'utilisateur dit « installe mon restaurant », « configure mon établissement », « on démarre de zér… |
| `planning-equipe` | Utiliser quand l'utilisateur parle de planning, de shifts, d'horaires d'équipe, de demandes de congé, de pointages, de contrat de travail ou de documents d'un employé dans son r… |
| `price-check` | Utiliser quand l'utilisateur veut vérifier ses prix ou voir ses marges par produit avant une décision tarifaire. Produit un tableau marge par produit et trois scénarios de prix … |
| `production-stock` | Utiliser quand l'utilisateur veut planifier une production, consulter les alertes de production ou valider une production réalisée. Enchaîne planification → vérification des ing… |
| `reappro-fournisseurs` | Utiliser quand l'utilisateur parle de stock bas, de commande fournisseur ou de réapprovisionnement. Enchaîne détection des stocks bas → commande fournisseur → réception (contrôl… |
| `recette-cout-marge` | Utiliser quand l'utilisateur veut créer une recette, calculer le coût d'une recette, une marge, ou fixer un prix de vente. Encode les règles de TVA restauration et le calcul de … |
| `service-salle` | Utiliser quand l'utilisateur parle de réservation, d'installer un client, de plan de salle, de file d'attente ou de table libre. Gère le cycle réservation → installation → suivi… |
| `site-vitrine-foodeatup` | Utiliser quand l'utilisateur veut gérer son site vitrine FoodEatUp — « mon site », « publie ma page », « change le thème du site », « applique un template », « mes leads du site… |

### rapido-canva

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `brand-guidelines-anthropic` | Utiliser quand l'utilisateur demande explicitement le look Anthropic (couleurs et typographies officielles) pour un artefact. Avant d'appliquer ces couleurs Anthropic, lire d'ab… |
| `canvas-design` | Utiliser quand l'utilisateur demande un poster, une œuvre visuelle ou un design statique original en .png ou .pdf. Philosophie de design pour créations originales — ne jamais co… |
| `menu-restaurant-design` | Utiliser quand l'utilisateur veut créer son menu, un menu imprimable ou une carte à imprimer pour son restaurant. Compose le contenu depuis FoodEatUp puis génère le design dans … |
| `presentation-codir` | Utiliser quand l'utilisateur veut la présentation du CODIR ou des slides pour le comité de direction. Collecte les données des 4 serveurs Rapido, construit l'outline (1 slide pa… |
| `supports-commerciaux` | Utiliser quand l'utilisateur veut une proposition commerciale, une présentation de vente ou une carte de visite. Croise les données du deal (RapidoCRM) et les arguments de la KB… |
| `theme-factory` | Utiliser quand l'utilisateur veut appliquer un thème (couleurs, typographies) à un artefact — slides, docs, rapports, pages HTML. 10 thèmes prédéfinis, ou génération d'un thème … |
| `visuels-sociaux-canva` | Utiliser quand l'utilisateur veut un visuel Canva, un design pour Instagram/LinkedIn/Facebook ou un template de post. Génère le design au format natif du réseau, l'exporte en PN… |

### rapido-copywriter

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `copy-linkedin` | Utiliser quand l'utilisateur veut de la copy LinkedIn pour une PAGE de marque — « post LinkedIn pour la page », « carrousel LinkedIn », « copy LinkedIn de [marque/produit] ». Pr… |
| `copy-meta` | Utiliser quand l'utilisateur veut de la copy Facebook ou Instagram pour une page de marque — « post Facebook », « post Instagram », « caption », « carrousel Insta », « copy du R… |
| `copy-tiktok` | Utiliser quand l'utilisateur veut un script TikTok pour une page de marque — « script TikTok », « vidéo TikTok pour [marque] », « hook TikTok », « contenu TikTok ». Le livrable … |
| `declinaison-multi-reseaux` | Utiliser quand l'utilisateur veut adapter un contenu à plusieurs réseaux — « décline sur les 4 réseaux », « adapte ce post pour Instagram/TikTok », « repurpose ce contenu ». Une… |

### rapido-design

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `animations-web` | Utiliser quand l'utilisateur veut animer un site — « anime le site », « micro-interactions », « animations au scroll », « transitions », « rends-le vivant ». Plan de motion sobr… |
| `architecture-info` | Utiliser quand l'utilisateur veut structurer un site avant le design — « sitemap », « user flow », « parcours utilisateur », « arborescence du site », « wireframes ». Produit si… |
| `direction-artistique` | Utiliser quand l'utilisateur veut définir l'identité visuelle d'un projet — « direction artistique », « moodboard », « quel style pour [projet] », « définis l'identité visuelle … |
| `studio-maquette` | Utiliser quand l'utilisateur veut les maquettes hi-fi et le design system — « maquette », « design du site », « écrans hi-fi », « design system », « maquette Figma de [projet] »… |

### rapido-direction

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `coffre-documents` | Utiliser quand l'utilisateur veut classer un document ou retrouver un contrat, une facture, un fichier. Gère le Drive du compte connecté comme coffre officiel — arborescence Cli… |
| `delegation-recurrence` | Utiliser quand une demande de direction est récurrente — « tous les lundis… », « à chaque fois que… », ou une tâche refaite à la main pour la énième fois. Transforme la routine … |
| `journee-du-dirigeant` | Utiliser quand l'utilisateur demande sa journée, un briefing complet ou « par quoi je commence ». Fusionne emails, agenda triple (Calendar + CRM + FoodEatUp), business et alerte… |
| `secretariat-commercial` | Utiliser quand un prospect a écrit, ou pour organiser un RDV avec un contact. Lit le fil email, crée/retrouve l'entreprise au CRM, propose des créneaux réels, prépare le brouill… |
| `tri-boite-mail` | Utiliser quand l'utilisateur veut trier ses mails, viser l'inbox zero ou répondre à un mail. Classe la boîte du compte connecté par étiquettes, reconnaît les clients CRM et prép… |

### rapido-forge

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `bootcamp-bmc-complete` | "Utiliser quand l'utilisateur veut compléter son Business Model Canvas (bootcamp 5 jours StartupsForge — Jour 3)." |
| `bootcamp-brand-platform` | "Utiliser quand l'utilisateur veut définir l'ADN de sa marque (bootcamp 5 jours StartupsForge — Jour 4)." |
| `bootcamp-brand-storytelling` | "Utiliser quand l'utilisateur veut construis l'histoire de sa marque (bootcamp 5 jours StartupsForge — Jour 4)." |
| `bootcamp-cash-flow-plan` | "Utiliser quand l'utilisateur veut prévois ses flux de trésorerie (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-certification-b5` | "Utiliser quand l'utilisateur veut obtiens sa certification Bootcamp et célèbre ! (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-competitive-advantage` | "Utiliser quand l'utilisateur veut identifie et formule son avantage défendable (bootcamp 5 jours StartupsForge — Jour 2)." |
| `bootcamp-competitive-deep` | "Utiliser quand l'utilisateur veut analyse détaillée des forces et faiblesses concurrents (bootcamp 5 jours StartupsForge — Jour 2)." |
| `bootcamp-content-strategy-b5` | "Utiliser quand l'utilisateur veut planifie sa stratégie de contenu (bootcamp 5 jours StartupsForge — Jour 4)." |
| `bootcamp-conversion-funnel` | "Utiliser quand l'utilisateur veut construis son funnel de conversion (bootcamp 5 jours StartupsForge — Jour 4)." |
| `bootcamp-editorial-calendar` | "Utiliser quand l'utilisateur veut organise ses publications sur 30 jours (bootcamp 5 jours StartupsForge — Jour 4)." |
| `bootcamp-email-setup` | "Utiliser quand l'utilisateur veut configure ses séquences email (bootcamp 5 jours StartupsForge — Jour 4)." |
| `bootcamp-feature-benchmark` | "Utiliser quand l'utilisateur veut compare les fonctionnalités clés du marché (bootcamp 5 jours StartupsForge — Jour 2)." |
| `bootcamp-financial-projections` | "Utiliser quand l'utilisateur veut créer ses projections sur 3 ans (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-funding-strategy` | "Utiliser quand l'utilisateur veut définir sa stratégie de levée de fonds (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-growth-strategy` | "Utiliser quand l'utilisateur veut planifie sa stratégie de croissance (bootcamp 5 jours StartupsForge — Jour 3)." |
| `bootcamp-investor-faq` | "Utiliser quand l'utilisateur veut prépare les réponses aux questions fréquentes (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-ip-protection` | "Utiliser quand l'utilisateur veut protège sa marque et ses innovations (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-landing-copy-b5` | "Utiliser quand l'utilisateur veut rédiger le contenu de sa landing page (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-launch-budget` | "Utiliser quand l'utilisateur veut estime le budget nécessaire au lancement (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-launch-plan` | "Utiliser quand l'utilisateur veut planifie son lancement step-by-step (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-legal-documents` | "Utiliser quand l'utilisateur veut génère ses documents légaux obligatoires (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-legal-status` | "Utiliser quand l'utilisateur veut choisir la forme juridique adaptée (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-market-segmentation` | "Utiliser quand l'utilisateur veut identifie et priorise ses segments de marché cibles (bootcamp 5 jours StartupsForge — Jour 1)." |
| `bootcamp-market-sizing-b5` | "Utiliser quand l'utilisateur veut calcule la taille de son marché avec précision (bootcamp 5 jours StartupsForge — Jour 1)." |
| `bootcamp-mvp-wireframes` | "Utiliser quand l'utilisateur veut créer les maquettes de son MVP (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-naming-tagline` | "Utiliser quand l'utilisateur veut trouve le nom parfait et son slogan (bootcamp 5 jours StartupsForge — Jour 4)." |
| `bootcamp-okr-kpi-setup` | "Utiliser quand l'utilisateur veut définir ses objectifs et indicateurs clés (bootcamp 5 jours StartupsForge — Jour 3)." |
| `bootcamp-pain-mapping` | "Utiliser quand l'utilisateur veut analyse en profondeur les frustrations utilisateurs (bootcamp 5 jours StartupsForge — Jour 2)." |
| `bootcamp-persona-deep` | "Utiliser quand l'utilisateur veut créer des personas détaillés avec jobs-to-be-done (bootcamp 5 jours StartupsForge — Jour 2)." |
| `bootcamp-pestel-analysis` | "Utiliser quand l'utilisateur veut évalue l'environnement macro-économique (bootcamp 5 jours StartupsForge — Jour 2)." |
| `bootcamp-pitch-deck-b5` | "Utiliser quand l'utilisateur veut créer son pitch deck investisseur (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-pitch-script-b5` | "Utiliser quand l'utilisateur veut prépare son pitch oral de 3 minutes (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-porter-forces` | "Utiliser quand l'utilisateur veut analyse les 5 forces concurrentielles (bootcamp 5 jours StartupsForge — Jour 2)." |
| `bootcamp-positioning-map` | "Utiliser quand l'utilisateur veut définir son positionnement unique sur le marché (bootcamp 5 jours StartupsForge — Jour 2)." |
| `bootcamp-press-release-b5` | "Utiliser quand l'utilisateur veut rédiger son communiqué de lancement (bootcamp 5 jours StartupsForge — Jour 5)." |
| `bootcamp-problem-validation` | "Utiliser quand l'utilisateur veut valide que le problème est réel et fréquent (bootcamp 5 jours StartupsForge — Jour 2)." |
| `bootcamp-qualitative-study` | "Utiliser quand l'utilisateur veut mène des interviews utilisateurs approfondies avec la méthode The Mom Test (bootcamp 5 jours StartupsForge — Jour 1)." |
| `bootcamp-quantitative-study` | "Utiliser quand l'utilisateur veut conçois un questionnaire de validation avec scoring et analyse (bootcamp 5 jours StartupsForge — Jour 1)." |
| `bootcamp-revenue-model-b5` | "Utiliser quand l'utilisateur veut définir ses sources de revenus et pricing (bootcamp 5 jours StartupsForge — Jour 3)." |
| `bootcamp-social-media-strategy` | "Utiliser quand l'utilisateur veut définir sa présence sur les réseaux (bootcamp 5 jours StartupsForge — Jour 4)." |
| `bootcamp-stakeholder-mapping` | "Utiliser quand l'utilisateur veut cartographie tous les acteurs de son écosystème (bootcamp 5 jours StartupsForge — Jour 1)." |
| `bootcamp-tone-of-voice` | "Utiliser quand l'utilisateur veut définir la personnalité de sa communication (bootcamp 5 jours StartupsForge — Jour 4)." |
| `bootcamp-trend-analysis` | "Utiliser quand l'utilisateur veut identifie les tendances émergentes et signaux faibles du marché (bootcamp 5 jours StartupsForge — Jour 1)." |
| `bootcamp-uvp-builder` | "Utiliser quand l'utilisateur veut formule sa proposition de valeur irrésistible (bootcamp 5 jours StartupsForge — Jour 3)." |
| `bootcamp-vision-mission` | "Utiliser quand l'utilisateur veut définir sa vision long terme et sa mission (bootcamp 5 jours StartupsForge — Jour 3)." |
| `bootcamp-visual-identity` | "Utiliser quand l'utilisateur veut créer son logo et charte graphique (bootcamp 5 jours StartupsForge — Jour 4)." |
| `ideation-about-page` | "Utiliser quand l'utilisateur veut raconter l'histoire de sa startup et créer une connexion émotionnelle (parcours idéation StartupsForge)." |
| `ideation-advisory-board` | "Utiliser quand l'utilisateur veut identifier et approcher des advisors potentiels (parcours idéation StartupsForge)." |
| `ideation-analytics-setup` | "Utiliser quand l'utilisateur veut configurer GA4, Mixpanel ou équivalent (parcours idéation StartupsForge)." |
| `ideation-automation-workflow` | "Utiliser quand l'utilisateur veut créer un workflow complet de traitement des nouveaux leads (parcours idéation StartupsForge)." |
| `ideation-avatar-video` | "Utiliser quand l'utilisateur veut créer une vidéo avec un présentateur IA réaliste (parcours idéation StartupsForge)." |
| `ideation-blog-outline` | "Utiliser quand l'utilisateur veut rédiger un article de blog complet et optimisé SEO (parcours idéation StartupsForge)." |
| `ideation-business-model-canvas` | "Utiliser quand l'utilisateur veut remplir un Business Model Canvas complet avec les 9 blocs (parcours idéation StartupsForge)." |
| `ideation-cash-flow` | "Utiliser quand l'utilisateur veut créer un plan de trésorerie mensuel sur 12 mois (parcours idéation StartupsForge)." |
| `ideation-certification` | "Utiliser quand l'utilisateur veut célébrer la fin du hackathon et obtenir sa certification (parcours idéation StartupsForge)." |
| `ideation-changelog-setup` | "Utiliser quand l'utilisateur veut créer et maintenir un changelog public (parcours idéation StartupsForge)." |
| `ideation-cold-email` | "Utiliser quand l'utilisateur veut identifier et préparer le contact de 10 prospects qualifiés (parcours idéation StartupsForge)." |
| `ideation-color-palette` | "Utiliser quand l'utilisateur veut définir une palette de couleurs cohérente et professionnelle (parcours idéation StartupsForge)." |
| `ideation-competitive-analysis` | "Utiliser quand l'utilisateur veut cartographier le paysage concurrentiel avec forces, faiblesses et opportunités de différenciation (parcours idéation StartupsForge)." |
| `ideation-contact-form` | "Utiliser quand l'utilisateur veut créer un formulaire de contact optimisé pour la conversion (parcours idéation StartupsForge)." |
| `ideation-course-outline` | "Utiliser quand l'utilisateur veut structurer le contenu pédagogique de son produit/service (parcours idéation StartupsForge)." |
| `ideation-demo-script` | "Utiliser quand l'utilisateur veut enregistrer une démo produit professionnelle (parcours idéation StartupsForge)." |
| `ideation-email-marketing-setup` | "Utiliser quand l'utilisateur veut configurer son système d'email marketing complet avec automation (parcours idéation StartupsForge)." |
| `ideation-email-sequence` | "Utiliser quand l'utilisateur veut rédiger un email de bienvenue engageant (parcours idéation StartupsForge)." |
| `ideation-export-pdf` | "Utiliser quand l'utilisateur veut compiler tous les documents clés dans un dossier PDF (parcours idéation StartupsForge)." |
| `ideation-feedback-analysis` | "Utiliser quand l'utilisateur veut analyser et synthétiser les premiers retours utilisateurs (parcours idéation StartupsForge)." |
| `ideation-financial-forecast` | "Utiliser quand l'utilisateur veut créer des projections financières à 3 ans (parcours idéation StartupsForge)." |
| `ideation-first-ad-campaign` | "Utiliser quand l'utilisateur veut lancer sa première campagne publicitaire (parcours idéation StartupsForge)." |
| `ideation-gamification` | "Utiliser quand l'utilisateur veut ajouter un élément interactif engageant à son site (parcours idéation StartupsForge)." |
| `ideation-growth-experiments` | "Utiliser quand l'utilisateur veut planifier 3 expériences de croissance (parcours idéation StartupsForge)." |
| `ideation-hero-image` | "Utiliser quand l'utilisateur veut générer des visuels professionnels pour son site web (parcours idéation StartupsForge)." |
| `ideation-hunter-outreach` | "Utiliser quand l'utilisateur veut contacter et sécuriser un hunter pour le lancement (parcours idéation StartupsForge)." |
| `ideation-investor-faq` | "Utiliser quand l'utilisateur veut préparer les réponses aux questions investisseurs (parcours idéation StartupsForge)." |
| `ideation-iteration-planning` | "Utiliser quand l'utilisateur veut planifier le sprint pour la V2 (parcours idéation StartupsForge)." |
| `ideation-kpi-dashboard` | "Utiliser quand l'utilisateur veut créer un dashboard avec les KPIs essentiels (parcours idéation StartupsForge)." |
| `ideation-landing-copy` | "Utiliser quand l'utilisateur veut finaliser le texte de sa landing page (parcours idéation StartupsForge)." |
| `ideation-landing-page` | "Utiliser quand l'utilisateur veut rédiger un titre et sous-titre Hero accrocheurs qui convertissent (parcours idéation StartupsForge)." |
| `ideation-launch-checklist` | "Utiliser quand l'utilisateur veut créer et valider la checklist finale de lancement (parcours idéation StartupsForge)." |
| `ideation-launch-plan` | "Utiliser quand l'utilisateur veut créer un plan de lancement détaillé (parcours idéation StartupsForge)." |
| `ideation-launch-post` | "Utiliser quand l'utilisateur veut rédiger le post de lancement parfait pour ses réseaux (parcours idéation StartupsForge)." |
| `ideation-lead-magnet` | "Utiliser quand l'utilisateur veut créer un ebook ou guide PDF à forte valeur ajoutée (parcours idéation StartupsForge)." |
| `ideation-lean-canvas` | "Utiliser quand l'utilisateur veut remplir un Lean Canvas complet pour visualiser son modèle d'affaires et identifier les hypothèses à valider (parcours idéation StartupsForge)." |
| `ideation-legal-docs` | "Utiliser quand l'utilisateur veut générer des CGV et mentions légales conformes (parcours idéation StartupsForge)." |
| `ideation-legal-structure` | "Utiliser quand l'utilisateur veut choisir le statut juridique adapté à son projet (parcours idéation StartupsForge)." |
| `ideation-lessons-learned` | "Utiliser quand l'utilisateur veut documenter les apprentissages du lancement (parcours idéation StartupsForge)." |
| `ideation-linkedin-posts` | "Utiliser quand l'utilisateur veut rédiger 5 posts LinkedIn prêts à publier (parcours idéation StartupsForge)." |
| `ideation-logo-prompt` | "Utiliser quand l'utilisateur veut créer un logo professionnel représentant l'identité de sa marque (parcours idéation StartupsForge)." |
| `ideation-lovable-prompt` | "Utiliser quand l'utilisateur veut générer le code de son site web avec Lovable.dev (parcours idéation StartupsForge)." |
| `ideation-mvp-wireframes` | "Utiliser quand l'utilisateur veut créer les wireframes de son MVP (parcours idéation StartupsForge)." |
| `ideation-naming-generator` | "Utiliser quand l'utilisateur veut générer et sélectionner un nom de marque mémorable et disponible (parcours idéation StartupsForge)." |
| `ideation-north-star-metric` | "Utiliser quand l'utilisateur veut définir et documenter sa North Star Metric (parcours idéation StartupsForge)." |
| `ideation-paid-acquisition` | "Utiliser quand l'utilisateur veut élaborer une stratégie d'acquisition payante (parcours idéation StartupsForge)." |
| `ideation-persona-maker` | "Utiliser quand l'utilisateur veut créer 2-3 personas détaillés représentant ses clients idéaux avec leurs motivations, frustrations et comportements (parcours idéation Startups… |
| `ideation-ph-page-copy` | "Utiliser quand l'utilisateur veut créer la page Product Hunt parfaite (parcours idéation StartupsForge)." |
| `ideation-pitch-deck` | "Utiliser quand l'utilisateur veut structurer son pitch deck avec les 10-12 slides essentielles (parcours idéation StartupsForge)." |
| `ideation-pitch-script` | "Utiliser quand l'utilisateur veut pratiquer et perfectionner sa présentation orale (parcours idéation StartupsForge)." |
| `ideation-pre-launch-campaign` | "Utiliser quand l'utilisateur veut créer une campagne email de pré-lancement (parcours idéation StartupsForge)." |
| `ideation-press-release` | "Utiliser quand l'utilisateur veut rédiger un communiqué de presse professionnel (parcours idéation StartupsForge)." |
| `ideation-pricing-page` | "Utiliser quand l'utilisateur veut présenter ses tarifs de façon claire et convaincante (parcours idéation StartupsForge)." |
| `ideation-product-hunt-strategy` | "Utiliser quand l'utilisateur veut élaborer une stratégie complète pour Product Hunt (parcours idéation StartupsForge)." |
| `ideation-qa-checklist` | "Utiliser quand l'utilisateur veut tester exhaustivement son site avant le lancement (parcours idéation StartupsForge)." |
| `ideation-quiz-generator` | "Utiliser quand l'utilisateur veut créer un quiz interactif pour engager et qualifier les visiteurs (parcours idéation StartupsForge)." |
| `ideation-referral-program` | "Utiliser quand l'utilisateur veut créer un programme de parrainage efficace (parcours idéation StartupsForge)." |
| `ideation-retargeting-setup` | "Utiliser quand l'utilisateur veut configurer le retargeting pour récupérer les visiteurs (parcours idéation StartupsForge)." |
| `ideation-roadmap-product` | "Utiliser quand l'utilisateur veut définir les fonctionnalités essentielles du MVP à développer en premier (parcours idéation StartupsForge)." |
| `ideation-seo-meta` | "Utiliser quand l'utilisateur veut optimiser le SEO de base de son site pour les moteurs de recherche (parcours idéation StartupsForge)." |
| `ideation-sitemap-generator` | "Utiliser quand l'utilisateur veut planifier la structure de pages de son site web (parcours idéation StartupsForge)." |
| `ideation-social-strategy` | "Utiliser quand l'utilisateur veut planifier 30 jours de contenu social media (parcours idéation StartupsForge)." |
| `ideation-specs-generator` | "Utiliser quand l'utilisateur veut créer un cahier des charges technique complet avec wireframes pour faire développer son MVP (parcours idéation StartupsForge)." |
| `ideation-swot` | "Utiliser quand l'utilisateur veut réaliser une analyse SWOT complète pour guider sa stratégie de développement (parcours idéation StartupsForge)." |
| `ideation-testimonial-request` | "Utiliser quand l'utilisateur veut créer des témoignages crédibles pour renforcer la confiance (parcours idéation StartupsForge)." |
| `ideation-ui-guidelines` | "Utiliser quand l'utilisateur veut sélectionner une combinaison de fonts harmonieuse et lisible (parcours idéation StartupsForge)." |
| `ideation-usp-statement` | "Utiliser quand l'utilisateur veut créer un pitch d'une phrase percutante et mémorable (parcours idéation StartupsForge)." |
| `ideation-value-proposition` | "Utiliser quand l'utilisateur veut identifier et articuler le problème précis que sa solution résout, avec son intensité et sa fréquence (parcours idéation StartupsForge)." |
| `ideation-video-edit` | "Utiliser quand l'utilisateur veut créer une vidéo teaser courte et percutante (parcours idéation StartupsForge)." |
| `ideation-video-script` | "Utiliser quand l'utilisateur veut scripter une vidéo tutoriel ou explicative (parcours idéation StartupsForge)." |
| `ideation-voiceover` | "Utiliser quand l'utilisateur veut générer une voix-off IA pour sa vidéo (parcours idéation StartupsForge)." |
| `ideation-webhook-setup` | "Utiliser quand l'utilisateur veut configurer un webhook pour capturer les leads de son formulaire (parcours idéation StartupsForge)." |
| `scale-ab-testing` | "Utiliser quand l'utilisateur veut définir un plan de 5 tests A/B prioritaires avec hypothèses et métriques (parcours scale StartupsForge)." |
| `scale-adoption-curve` | "Utiliser quand l'utilisateur veut identifier son segment d'adoption actuel et adapter sa stratégie en conséquence (parcours scale StartupsForge)." |
| `scale-ansoff-matrix` | "Utiliser quand l'utilisateur veut définir sa stratégie de croissance principale parmi les 4 options d'Ansoff (parcours scale StartupsForge)." |
| `scale-bant-qualification` | "Utiliser quand l'utilisateur veut créer une grille de qualification BANT pour prioriser ses opportunités (parcours scale StartupsForge)." |
| `scale-bcg-matrix` | "Utiliser quand l'utilisateur veut analyser son portefeuille produits/services pour identifier les Stars à développer, les Vaches à lait à optimiser, les Dilemmes à arbitrer et … |
| `scale-blue-ocean` | "Utiliser quand l'utilisateur veut identifier des espaces de marché inexploités où la concurrence est inexistante (parcours scale StartupsForge)." |
| `scale-break-even` | "Utiliser quand l'utilisateur veut calculer son point mort et définir la trajectoire pour l'atteindre (parcours scale StartupsForge)." |
| `scale-burn-rate` | "Utiliser quand l'utilisateur veut calculer son burn rate actuel et projeter son runway (parcours scale StartupsForge)." |
| `scale-cap-table` | "Utiliser quand l'utilisateur veut créer et simuler sa table de capitalisation avant/après levée (parcours scale StartupsForge)." |
| `scale-cold-email-prospection` | "Utiliser quand l'utilisateur veut rédiger une séquence de cold emails avec personnalisation et follow-ups (parcours scale StartupsForge)." |
| `scale-commercial-proposal` | "Utiliser quand l'utilisateur veut créer un template de proposition commerciale B2B convaincant et professionnel (parcours scale StartupsForge)." |
| `scale-community-building` | "Utiliser quand l'utilisateur veut lancer et structurer une communauté autour de sa marque/produit (parcours scale StartupsForge)." |
| `scale-content-pillar` | "Utiliser quand l'utilisateur veut créer une stratégie de contenu SEO avec articles piliers et clusters (parcours scale StartupsForge)." |
| `scale-cost-waterfall` | "Utiliser quand l'utilisateur veut cartographier et catégoriser tous ses coûts fixes et variables (parcours scale StartupsForge)." |
| `scale-customer-journey` | "Utiliser quand l'utilisateur veut mapper les 7 étapes du parcours client de la découverte à l'advocacy (parcours scale StartupsForge)." |
| `scale-customer-success` | "Utiliser quand l'utilisateur veut définir son playbook Customer Success avec onboarding, check-ins et expansion (parcours scale StartupsForge)." |
| `scale-design-system` | "Utiliser quand l'utilisateur veut créer un Design System V1 avec les composants essentiels (parcours scale StartupsForge)." |
| `scale-eisenhower-matrix` | "Utiliser quand l'utilisateur veut organiser ses tâches selon l'urgence et l'importance pour maximiser son impact (parcours scale StartupsForge)." |
| `scale-financial-projections` | "Utiliser quand l'utilisateur veut créer un P&L prévisionnel sur 3 ans avec hypothèses détaillées (parcours scale StartupsForge)." |
| `scale-fundraising-plan` | "Utiliser quand l'utilisateur veut définir sa stratégie de financement sur les 24 prochains mois (parcours scale StartupsForge)." |
| `scale-funnel-aarrr` | "Utiliser quand l'utilisateur veut analyser et optimiser chaque étape de son funnel AARRR (parcours scale StartupsForge)." |
| `scale-golden-circle` | "Utiliser quand l'utilisateur veut définir clairement son WHY (raison d'être), HOW (différenciation) et WHAT (produit) (parcours scale StartupsForge)." |
| `scale-google-ads-setup` | "Utiliser quand l'utilisateur veut lancer sa première campagne Google Ads Search rentable (parcours scale StartupsForge)." |
| `scale-google-analytics-4` | "Utiliser quand l'utilisateur veut installer et configurer GA4 pour tracker son site web avec les événements clés (parcours scale StartupsForge)." |
| `scale-google-search-console` | "Utiliser quand l'utilisateur veut configurer GSC et analyser les premières données de performance SEO (parcours scale StartupsForge)." |
| `scale-google-trends` | "Utiliser quand l'utilisateur veut identifier les tendances de sa niche et créer du contenu aligné (parcours scale StartupsForge)." |
| `scale-heatmaps` | "Utiliser quand l'utilisateur veut installer et analyser les heatmaps et session recordings sur son site (parcours scale StartupsForge)." |
| `scale-impact-effort` | "Utiliser quand l'utilisateur veut placer toutes ses idées sur la matrice et identifier les Quick Wins (parcours scale StartupsForge)." |
| `scale-influencer-marketing` | "Utiliser quand l'utilisateur veut identifier 20 micro-influenceurs pertinents et créer un plan d'approche (parcours scale StartupsForge)." |
| `scale-jtbd` | "Utiliser quand l'utilisateur veut identifier les 'jobs' fonctionnels, émotionnels et sociaux que ses clients veulent accomplir (parcours scale StartupsForge)." |
| `scale-kpi-dashboard` | "Utiliser quand l'utilisateur veut créer un dashboard des 10 métriques essentielles à suivre chaque semaine (parcours scale StartupsForge)." |
| `scale-linkedin-ads-b2b` | "Utiliser quand l'utilisateur veut lancer une campagne LinkedIn Ads ciblant les décideurs B2B (parcours scale StartupsForge)." |
| `scale-linkedin-pixel` | "Utiliser quand l'utilisateur veut installer le Insight Tag et configurer le tracking B2B (parcours scale StartupsForge)." |
| `scale-marketing-4c` | "Utiliser quand l'utilisateur veut transformer son approche marketing en adoptant la perspective client (parcours scale StartupsForge)." |
| `scale-marketing-4p` | "Utiliser quand l'utilisateur veut optimiser chaque P de son Marketing Mix pour maximiser l'impact (parcours scale StartupsForge)." |
| `scale-meta-ads-campaign` | "Utiliser quand l'utilisateur veut créer et lancer une campagne Meta Ads complète (parcours scale StartupsForge)." |
| `scale-meta-pixel` | "Utiliser quand l'utilisateur veut installer le Meta Pixel avec les événements de conversion clés (parcours scale StartupsForge)." |
| `scale-negotiation-batna` | "Utiliser quand l'utilisateur veut préparer une négociation commerciale avec BATNA, ZOPA et tactiques (parcours scale StartupsForge)." |
| `scale-north-star-metric` | "Utiliser quand l'utilisateur veut identifier et définir LA métrique unique qui guide toutes ses décisions (parcours scale StartupsForge)." |
| `scale-nps-survey` | "Utiliser quand l'utilisateur veut mettre en place une mesure régulière du NPS avec actions correctives (parcours scale StartupsForge)." |
| `scale-objections-playbook` | "Utiliser quand l'utilisateur veut anticiper et préparer des réponses structurées aux 10 objections les plus fréquentes (parcours scale StartupsForge)." |
| `scale-okrs-q1` | "Utiliser quand l'utilisateur veut définir 3-5 objectifs ambitieux avec résultats clés mesurables pour son premier trimestre Scale (parcours scale StartupsForge)." |
| `scale-porter-5-forces` | "Utiliser quand l'utilisateur veut évaluer les 5 forces qui déterminent la rentabilité potentielle de son marché (parcours scale StartupsForge)." |
| `scale-pr-media-kit` | "Utiliser quand l'utilisateur veut créer un Media Kit complet prêt à envoyer aux journalistes et partenaires (parcours scale StartupsForge)." |
| `scale-pricing-strategy` | "Utiliser quand l'utilisateur veut tester et optimiser sa stratégie de pricing pour maximiser le revenu (parcours scale StartupsForge)." |
| `scale-prototype` | "Utiliser quand l'utilisateur veut créer un prototype interactif navigable de son MVP (parcours scale StartupsForge)." |
| `scale-public-roadmap` | "Utiliser quand l'utilisateur veut créer une roadmap produit transparente et engageante pour ses utilisateurs (parcours scale StartupsForge)." |
| `scale-referral-program` | "Utiliser quand l'utilisateur veut concevoir un programme de parrainage viral avec incentives optimisés (parcours scale StartupsForge)." |
| `scale-rice-prioritization` | "Utiliser quand l'utilisateur veut scorer et prioriser ses features avec la méthode RICE (parcours scale StartupsForge)." |
| `scale-sales-call-script` | "Utiliser quand l'utilisateur veut créer un script d'appel de vente structuré en 7 étapes avec transitions naturelles (parcours scale StartupsForge)." |
| `scale-scenarios-planning` | "Utiliser quand l'utilisateur veut créer 3 scénarios de croissance : pessimiste, réaliste, optimiste (parcours scale StartupsForge)." |
| `scale-semrush-audit` | "Utiliser quand l'utilisateur veut réaliser un audit SEO complet et créer un plan d'action priorisé (parcours scale StartupsForge)." |
| `scale-seo-meta` | "Utiliser quand l'utilisateur veut optimiser les balises meta de toutes ses pages clés pour maximiser le CTR (parcours scale StartupsForge)." |
| `scale-soncas` | "Utiliser quand l'utilisateur veut identifier le profil SONCAS de ses clients types et adapter ses argumentaires (parcours scale StartupsForge)." |
| `scale-spin-selling` | "Utiliser quand l'utilisateur veut maîtriser les 4 types de questions SPIN pour qualifier et convertir efficacement (parcours scale StartupsForge)." |
| `scale-tiktok-ads-creator` | "Utiliser quand l'utilisateur veut créer des publicités TikTok natives qui ne ressemblent pas à des pubs (parcours scale StartupsForge)." |
| `scale-tiktok-pixel` | "Utiliser quand l'utilisateur veut préparer son tracking TikTok pour de futures campagnes (parcours scale StartupsForge)." |
| `scale-unit-economics` | "Utiliser quand l'utilisateur veut calculer et optimiser ses métriques unitaires : CAC, LTV, ratio LTV/CAC (parcours scale StartupsForge)." |
| `scale-upsell-crosssell` | "Utiliser quand l'utilisateur veut cartographier les opportunités d'upsell et cross-sell par segment client (parcours scale StartupsForge)." |
| `scale-user-story-mapping` | "Utiliser quand l'utilisateur veut cartographier les parcours utilisateurs en user stories prioritisées (parcours scale StartupsForge)." |
| `scale-user-tests` | "Utiliser quand l'utilisateur veut recruter et observer 5 personnes utilisant son produit/prototype (parcours scale StartupsForge)." |
| `scale-wireframes` | "Utiliser quand l'utilisateur veut esquisser les 5 écrans clés de son application (parcours scale StartupsForge)." |
| `selecteur-framework` | Utiliser quand l'utilisateur décrit un besoin sans nommer de framework (« comment je valide mon idée », « aide-moi à structurer mes prix ») ou demande quel exercice/framework ut… |

### rapido-gmaps

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `detection-opportunites` | Utiliser quand l'utilisateur cherche des prospects FoodEatUp — « restaurants sans système numérique », « prospects FoodEatUp », « trouve des leads pour FoodEatUp », « business s… |
| `enrichissement-fiches` | Utiliser quand l'utilisateur veut compléter/rafraîchir une fiche CRM existante depuis Google Maps — « complète la fiche de [entreprise] », « mets à jour les coordonnées CRM », «… |
| `sourcing-gmaps` | Utiliser quand l'utilisateur veut trouver/prospecter des établissements d'une zone depuis Google Maps — « trouve-moi des restaurants à [ville] », « prospecte les [type] de [zone… |
| `veille-concurrents-gmaps` | Utiliser quand l'utilisateur veut analyser la concurrence d'une zone depuis Google Maps — « scrape les concurrents de [client] », « veille concurrentielle zone », « que proposen… |

### rapido-google-ads

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `audit-compte-google-ads` | Utiliser quand l'utilisateur veut un audit de son compte Google Ads, repérer le gaspillage publicitaire, vérifier son Quality Score, les chevauchements de campagnes, les extensi… |
| `pilotage-performance-google-ads` | Utiliser quand l'utilisateur demande la performance de ses campagnes Google Ads, « comment vont mes pubs Google », son CPA/ROAS Google Ads, ou un point SEA. Analyse dépense, con… |
| `recherche-mots-cles-sea` | Utiliser quand l'utilisateur veut des mots-clés payants Google Ads, des CPC estimés, une structure de campagne SEA, des mots-clés négatifs, ou « sur quels mots-clés enchérir ». … |
| `synergie-seo-sea` | Utiliser quand l'utilisateur veut arbitrer entre SEO et SEA, savoir où il paie alors qu'il ranke déjà, quels mots-clés organiques faibles méritent du paid, ou aligner ses messag… |

### rapido-higgsfield

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `analyse-video-virale` | Utiliser quand l'utilisateur demande « cette vidéo peut-elle percer », « analyse cette vidéo », « gate viral », ou en invocation par les skills vidéo avant un boost payant. Anal… |
| `clips-et-shorts` | Utiliser quand l'utilisateur veut « transformer en short », « des clips depuis cette vidéo YouTube », « décliner en 9:16 », ou « restyler cette vidéo ». Trois chaînes de post-pr… |
| `gouvernance-credits` | Utiliser quand l'utilisateur parle de « combien de crédits », « budget média », « coût de cette vidéo », « consommation Higgsfield », ou en préflight par les autres skills du pl… |
| `personnages-univers` | Utiliser quand l'utilisateur parle de « personnage récurrent », « notre mascotte en vidéo », « univers PronoClip », « entraîne le personnage », ou « même personnage dans une nou… |
| `sites-et-jeux-express` | Utiliser quand l'utilisateur veut un « microsite de campagne », une « page concours », un « jeu concours jouable », un « mini-jeu » ou un « site express ». Crée des microsites j… |
| `studio-image-pro` | Utiliser quand l'utilisateur veut une « image 4K », un « packshot », une « photo produit », un « visuel pub », une « image avec texte parfait » ou une « affiche photoréaliste ».… |
| `usine-video-marketing` | Utiliser quand l'utilisateur veut une « pub vidéo », une « vidéo produit », une « vidéo UGC », « refais cette pub », ou une « vidéo TikTok/Reel pour [produit] ». Chaîne Marketin… |
| `videos-explicatives` | Utiliser quand l'utilisateur veut une « vidéo explicative », un « tuto vidéo », une « vidéo d'onboarding » ou un « épisode Academy ». Assemble une vidéo pédagogique par blocs (s… |
| `voix-et-doublage` | Utiliser quand l'utilisateur veut une « voix off », « doubler cette vidéo en anglais », « cloner ma voix », ou « changer la voix ». Voix off TTS, doublage 18 langues (dont la sé… |

### rapido-leadmagnet

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `campagne-lead-magnet` | Utiliser quand l'utilisateur veut diffuser un lead magnet déjà en ligne — « lance la campagne du lead magnet », « fais connaître le guide », « diffuse le lead magnet », « campag… |
| `fabrication-lead-magnet` | Utiliser quand l'utilisateur veut fabriquer un lead magnet déjà conçu — « fabrique le lead magnet », « rédige le guide/la checklist », « produis l'ebook », « crée le PDF du lead… |
| `page-et-capture` | Utiliser quand l'utilisateur veut mettre un lead magnet en ligne — « page du lead magnet », « landing de capture », « formulaire pour le guide », « mets le lead magnet en ligne … |
| `projet-rh-lead-magnet` | Utiliser quand l'utilisateur veut organiser la campagne lead magnet dans RapidoRH — « crée les tâches du lead magnet », « projet RH de la campagne », « organise la campagne dans… |

### rapido-lovable

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `agent-ia-produit` | Utiliser quand l'utilisateur veut créer un agent IA, un chatbot pour ses clients ou un assistant connecté à ses données. Construit dans Lovable une app de chat dont l'agent emba… |
| `connecteur-mcp-lovable` | Utiliser quand l'utilisateur veut brancher un serveur MCP Rapido (FoodEatUp, CRM, CMS, RH) sur un site Lovable via un agent embarqué — « connecte le MCP FoodEatUp au site », « p… |
| `frontend-design` | Utiliser quand l'utilisateur construit ou refond une interface et veut une direction visuelle distinctive et intentionnelle — esthétique, typographie, des choix qui ne ressemble… |
| `mvp-lovable` | Utiliser quand l'utilisateur veut un site/MVP multi-pages complet sur Lovable — « crée le MVP sur Lovable », « site complet pour [client] », « série de prompts Lovable pour l'ap… |
| `site-restaurant` | Utiliser quand l'utilisateur veut un site pour son restaurant, un site de réservation ou son menu en ligne. Construit une app Lovable avec les données réelles FoodEatUp, un form… |
| `sync-marque-lovable` | Utiliser quand l'utilisateur veut synchroniser sa marque sur Lovable ou appliquer sa charte à toutes ses apps. Pousse la charte, le ton et les offres de la KB dans le knowledge … |
| `ui-styling` | Utiliser quand l'utilisateur construit une interface avec shadcn/ui (Radix UI + Tailwind), implémente un design system, des layouts responsives, des composants accessibles (dial… |
| `ui-ux-pro-max` | Utiliser quand l'utilisateur veut planifier, construire, revoir ou améliorer une UI/UX web ou mobile — site, landing, dashboard, admin, e-commerce, SaaS, portfolio, app mobile —… |
| `usine-a-landing` | Utiliser quand l'utilisateur veut une landing page, une page de campagne ou une page de capture. Construit la page depuis la campagne CRM et les arguments de la KB, le formulair… |
| `web-artifacts-builder` | Utiliser quand l'utilisateur veut un artefact HTML claude.ai complexe et multi-composants (React, Tailwind CSS, shadcn/ui) — gestion d'état, routing, composants shadcn/ui. Pas p… |

### rapido-marketing

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `attribution-kpi-marketing` | Utiliser quand l'utilisateur demande d'où viennent ses clients, une attribution, le ROI par canal, ou ses CAC/LTV. Collecte les métriques multi-sources (CRM, CMS, Meta), appliqu… |
| `core-four-strategie` | Utiliser quand l'utilisateur se demande par où commencer pour trouver des clients, quel canal d'acquisition choisir, combien de prospection faire par jour, ou comment scaler un … |
| `delivrabilite-email` | Utiliser quand l'utilisateur parle de « délivrabilité », dit « mes emails tombent en spam », « vérifie la liste avant envoi », « warmup », « on peut envoyer ? ». Gate OBLIGATOIR… |
| `geo-optimization` | Utiliser quand l'utilisateur parle de GEO, veut être cité par ChatGPT/Claude/Perplexity/AI Overviews, ou d'optimisation pour les moteurs génératifs. Audite un contenu contre une… |
| `growth-experiments` | Utiliser quand l'utilisateur veut des expériences de croissance, un A/B test, un backlog growth, ou faire du CRO. Priorise les hypothèses par score ICE, définit un protocole d'e… |
| `icp-generator` | Utiliser quand l'utilisateur veut définir son ICP, son client idéal, ou savoir quelles entreprises cibler. Construit le profil d'ENTREPRISE cible (secteur, taille, signaux, tech… |
| `lead-getters-systeme` | Utiliser quand l'utilisateur veut mettre en place un programme de parrainage, faire générer des leads par ses clients, employés, agences ou affiliés, ou déléguer son acquisition… |
| `lead-magnet-machine` | Utiliser quand l'utilisateur veut créer un aimant à prospects, un lead magnet, une ressource ou un cadeau gratuit pour capter des emails, ou améliorer le nom d'une offre gratuit… |
| `lead-scoring` | Utiliser quand l'utilisateur veut scorer ses leads, savoir quels prospects prioriser aujourd'hui, ou mettre en place un lead scoring. Applique un modèle transparent à 3 facteurs… |
| `machine-inbound` | Utiliser quand l'utilisateur veut mettre en place l'inbound, une machine à leads entrants, une stratégie de contenu qui convertit, ou un lead magnet de bout en bout. Orchestre l… |
| `machine-outbound` | Utiliser quand l'utilisateur veut lancer la prospection, monter une machine outbound, remplir son pipeline, ou construire une séquence de cold email. Orchestre la chaîne outboun… |
| `money-math-acquisition` | Utiliser quand l'utilisateur veut savoir combien il peut dépenser pour acquérir un client, si ses publicités sont rentables, son ratio LTGP:CAC, ou comment financer son acquisit… |
| `operations-influenceurs` | Utiliser quand l'utilisateur veut lancer une campagne d'influence, trouver des influenceurs, calculer le ROI de ses influenceurs, ou opérer des collaborations (micro-influenceur… |
| `pilotage-marketing` | Utiliser quand l'utilisateur dit « pilote mon marketing », « fais le point marketing », veut une boucle de pilotage marketing (Sense → Plan → Act → Feed → Report) ou un rapport … |
| `sales-intelligence-fireflies` | Utiliser quand l'utilisateur veut « analyser mes calls », savoir « quelles objections reviennent », capter la « voix du client », « miner mes transcripts » ou comprendre « ce qu… |
| `social-selling-linkedin` | Utiliser quand l'utilisateur parle de social selling, veut prospecter sur LinkedIn, optimiser son profil LinkedIn de fondateur, ou construire une séquence LinkedIn. Produit une … |
| `tunnel-de-vente-360` | Utiliser quand l'utilisateur veut construire son tunnel de vente, un funnel complet pour un produit, un tunnel parfait pour [produit], ou aller de la pub au client. Conçoit ET c… |

### rapido-meta-ads

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `audiences-crm` | Utiliser quand l'utilisateur veut une audience de ses clients, un lookalike ou du retargeting clients. Construit une audience personnalisée depuis le CRM (consentement RGPD véri… |
| `boost-post-instagram` | Utiliser quand l'utilisateur veut booster un post ou sponsoriser son meilleur post Instagram. Identifie le top post via les insights CMS puis boost en deux temps — plan (confirm… |
| `campaign-plan-methodo` | Utiliser quand l'utilisateur planifie un lancement produit, une campagne de génération de leads ou de notoriété et veut un brief complet : objectifs, audience, message, stratégi… |
| `creatifs-publicitaires` | Utiliser quand l'utilisateur veut un créatif pour la pub ou un visuel publicitaire. Génère le visuel (Canva ou image IA CMS) aux couleurs de la charte, crée le créatif Meta avec… |
| `hundred-million-offers` | Utiliser quand l'utilisateur veut rendre son offre irrésistible, ajouter des bonus, structurer une garantie, nommer son offre ou répondre à « c'est trop cher ». Value Equation, … |
| `influence-psychology` | Utiliser quand l'utilisateur parle de preuve sociale, de copy persuasive, de « pourquoi les gens ne convertissent pas », de rareté, de réciprocité, de confiance ou de signaux de… |
| `lancement-campagne-meta` | Utiliser quand l'utilisateur veut lancer une pub, une campagne Facebook/Instagram ou sponsoriser son activité. Construit campagne → ad set → créatif → ad (tout en PAUSED), récap… |
| `one-page-marketing` | Utiliser quand l'utilisateur veut un plan marketing complet, une stratégie marketing, choisir ses canaux d'acquisition, parle de cible ou d'USP, ou dit « je ne sais pas par où c… |
| `performance-report-methodo` | Utiliser quand l'utilisateur clôture une campagne ou prépare un bilan marketing hebdomadaire, mensuel ou trimestriel pour des décideurs : métriques clés, tendances, réussites et… |
| `pilotage-performance-ads` | Utiliser quand l'utilisateur demande comment performent ses pubs, un bilan pub ou d'optimiser ses campagnes. Lit les métriques réelles (dépense, coût par résultat), les tendance… |
| `pixel-et-retargeting` | Utiliser quand l'utilisateur veut poser le pixel, tracker les conversions ou faire du retargeting. Installe et active les événements pixel sur les landings Lovable, vérifie en T… |
| `tests-ab-meta` | Utiliser quand l'utilisateur veut tester deux versions ou un A/B test de pub. Vérifie l'éligibilité, crée les variantes, passe par un dry run, puis crée le test réel et lit les … |
| `veille-ads-concurrents` | Utiliser quand l'utilisateur demande ce que font ses concurrents en pub ou une veille publicitaire. Recherche leurs pubs actives dans l'Ad Library, synthétise les angles et offr… |

### rapido-n8n

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `memoire-operationnelle` | Utiliser quand un workflow a besoin d'une mémoire entre exécutions — ne pas relancer deux fois le même devis, se souvenir de ce qui a été traité. Gère les tables de données n8n … |
| `recettes-metier` | Utiliser quand un besoin d'automatisation correspond à une recette métier Rapido connue — relances de devis, alertes de stock, rappels HACCP, leads entrants, récap hebdo, annive… |
| `surveillance-automatisations` | Utiliser quand l'utilisateur demande si ses automatisations tournent ou parle d'erreurs de workflows. Contrôle les workflows actifs, chasse les exécutions en échec sur 7 jours, … |
| `usine-automatisations` | Utiliser quand l'utilisateur veut automatiser quelque chose, créer un workflow, ou dit « tous les jours / à chaque fois, fais… ». Fabrique un workflow n8n complet (cycle SDK, va… |

### rapido-prompteur

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `prompt-image` | Utiliser quand l'utilisateur veut un PROMPT d'image (pas l'image elle-même) — « prompt image », « prompt pour une photo de… », « prompt packshot », « prompt portrait », « prompt… |
| `prompt-lovable` | Utiliser quand l'utilisateur demande un « prompt Lovable », un « brief pour le site », un « prompt pour l'app / la landing », ou veut faire construire un site / une app par Lova… |
| `prompt-personnage` | Utiliser quand l'utilisateur veut des prompts de scène COHÉRENTS pour un personnage / une mascotte de marque récurrent(e) (« garde le même personnage », « décline ma mascotte da… |
| `prompt-video` | Utiliser quand l'utilisateur veut un PROMPT vidéo (pas la vidéo elle-même) — « prompt vidéo », « prompt pour une pub produit », « prompt explainer », « prompt scène personnage »… |

### rapido-relation-client

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `boucle-nps` | Utiliser quand l'utilisateur veut mesurer la satisfaction, lancer/lire un NPS, segmenter promoteurs/passifs/détracteurs, ou agir sur la fidélité. Lance/lit les sondages NPS via … |
| `cent-premiers-jours` | Utiliser quand l'utilisateur veut piloter l'onboarding d'un nouveau client, ses 100 premiers jours, un plan d'accueil, ou réduire le churn précoce. Traduit les 8 phases de l'exp… |
| `coach-relation-client` | Utiliser quand l'utilisateur demande comment fidéliser, améliorer l'expérience client, réduire le churn, activer ses utilisateurs SaaS, ou transformer des clients en ambassadeur… |
| `pilotage-service-client` | Utiliser quand l'utilisateur dit « pilote mon service client », « fais le point support », veut une boucle de pilotage du support (Sense → Plan → Act → Feed → Report) ou un rapp… |
| `sante-client` | Utiliser quand l'utilisateur veut un health score, savoir quels clients sont à risque, la santé de son portefeuille, ou qui va churner. Health score composite calculé sur donnée… |
| `segmentation-rfm` | Utiliser quand l'utilisateur veut segmenter ses clients, une analyse RFM, identifier ses champions/clients à risque/endormis, ou cibler par valeur. Récence × Fréquence × Montant… |

### rapido-seo

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `audit-seo-technique` | Utiliser quand l'utilisateur veut un « audit SEO », demande « pourquoi mon site ne ranke pas », « erreurs techniques du site », un audit OnPage ou un diagnostic de crawl. Audite… |
| `netlinking` | Utiliser quand l'utilisateur parle de « backlinks », « liens entrants », « netlinking », « profil de liens de mes concurrents », ou veut des opportunités de liens. Analyse les p… |
| `performance-organique` | Utiliser quand l'utilisateur demande « ma performance SEO », « mes positions Google », « quelles pages convertissent en organique », ses requêtes en striking distance ou ses pag… |
| `pilotage-seo` | Utiliser quand l'utilisateur dit « pilote mon SEO », « fais le point SEO », veut une boucle de pilotage organique (Sense → Plan → Act → Feed → Report) ou un rapport SEO une page… |
| `recherche-mots-cles` | Utiliser quand l'utilisateur veut une « recherche de mots-clés », demande « sur quoi me positionner », « volumes de recherche », des questions/longue traîne, ou l'intention de r… |
| `tendances-marche` | Utiliser quand l'utilisateur demande « tendances », « qu'est-ce qui monte », « saisonnalité de mes mots-clés », « TikTok trends », ou des idées de contenu d'actualité. Google Tr… |

### rapido-startup

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `amelioration-des-routines` | Utiliser quand l'utilisateur veut améliorer une routine sur la base de ses résultats, mesurer si ses routines servent encore, ou arbitrer lesquelles garder — « améliore la routi… |
| `catalogue-kpi` | Utiliser quand l'utilisateur demande un KPI, une métrique, une formule (MRR, CAC, LTV, churn, runway, burn, NRR, Rule of 40, DSO, point mort, vélocité pipeline, food cost…), « c… |
| `interview-business-plan` | Utiliser quand l'utilisateur veut créer un business plan, structurer son projet de startup, préparer une levée de fonds, un dossier banque/BPI, ou dit « aide-moi à créer mon ent… |
| `loop-engine-v2` | Utiliser quand l'utilisateur dit « lance R4/R5/R6/R7/R8/R9 », « routine du lundi », « board mensuel », « sentinelle cash », « épisode du jour », ou veut installer/planifier ses … |
| `plan-execution-startup` | Utiliser quand l'utilisateur veut passer du business plan à l'action - créer le projet de sa startup, planifier toutes les tâches de création et de gestion d'entreprise, ou dit … |
| `plan-financier-previsionnel` | Utiliser quand l'utilisateur veut un prévisionnel financier, un plan de trésorerie, un compte de résultat prévisionnel 3 ans, un point mort, des scénarios, ou finaliser la parti… |

### rapido-suite

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `business-pulse` | Utiliser quand l'utilisateur demande comment va la boîte, un snapshot, un résumé rapide, ou dit « qu'est-ce que je rate ? », « remets-moi dans le bain ». Photo une-page transver… |
| `cash-flow-snapshot` | Utiliser quand l'utilisateur demande une prévision de trésorerie, dit « est-ce que je pourrai payer les salaires ? », parle de runway ou de trou de trésorerie. Projection 30/60/… |
| `comite-de-direction` | Utiliser quand l'utilisateur demande un comité de direction, une vision globale ou « où en est l'entreprise ». Orchestre la revue business multi-domaines et la restitue en forma… |
| `dossier-startup-360` | Utiliser quand l'utilisateur veut structurer les données de sa startup, créer son dossier fondateur (vision, persona, marché, offre, pitch), ou donner aux agents IA le contexte … |
| `invoice-chase` | Utiliser quand l'utilisateur demande qui lui doit de l'argent, parle de factures en retard ou veut relancer des impayés avec un ton adapté à chaque client (courtois pour les bon… |
| `lancement-projet-360` | Utiliser quand l'utilisateur veut lancer un nouveau projet/produit/SaaS de A à Z, ou dit « accompagne-moi sur tout le cycle », « on part de zéro sur [idée] ». Orchestre méthodol… |
| `mise-a-jour-kb` | Utiliser quand l'utilisateur veut mettre à jour la base de connaissance, signale un changement de prix, une nouvelle offre, un nouveau concurrent ou toute évolution de l'entrepr… |
| `monday-brief` | Utiliser quand l'utilisateur demande son brief du lundi matin : une page — trésorerie, ventes, pipeline, semaine à venir, top 3 des choses à faire. S'appuie sur les MCP foodeatu… |
| `onboarding-client-360` | Utiliser quand l'utilisateur veut onboarder un nouveau client, annonce un client gagné ou un nouveau contrat signé. Orchestre CRM, CMS et RH pour mettre en place le client de bo… |
| `onboarding-entreprise` | Utiliser quand l'utilisateur parle d'onboarding, de configurer le plugin, de setup initial, ou demande d'apprendre à connaître son entreprise. Interviewe l'utilisateur et constr… |
| `pilotage-entreprise` | Utiliser quand l'utilisateur dit « pilote mon entreprise », « lance le Loop Engine complet », « fais le tour de toute la boîte » ou veut une session de pilotage transverse (fina… |
| `revue-hebdo-business` | Utiliser quand l'utilisateur demande une revue hebdo, un point business ou un tableau de bord global. Agrège en LECTURE SEULE les indicateurs des 4 serveurs (CRM, CMS, RH, FoodE… |
| `skill-creator` | Utiliser quand l'utilisateur veut créer un skill, améliorer ou modifier un skill existant, lancer des évals pour tester un skill, mesurer sa performance (avec analyse de varianc… |

### rapido-tiktok-ads

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `lancement-campagne-tiktok` | Utiliser quand l'utilisateur veut lancer/créer une campagne TikTok Ads, monter un ad group, une pub TikTok. Construit la campagne → ad group → créatif → ad TOUT EN ÉTAT INACTIF,… |
| `pilotage-performance-tiktok` | Utiliser quand l'utilisateur demande la performance de ses pubs TikTok, « comment vont mes TikTok Ads », son CPM/CPC/CPA TikTok, la performance par créatif, ou veut arbitrer le … |
| `tendances-creatives-tiktok` | Utiliser quand l'utilisateur demande les tendances créatives TikTok, quels formats/hooks de pub marchent, des idées de créatifs TikTok, ou un brief créatif TikTok. Analyse les f… |

### rapido-video

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `montage-express` | Utiliser quand l'utilisateur veut « monter ces clips », « couper cette vidéo », « assembler », « sous-titrer cette vidéo », « passer en 9:16 », « ajouter l'intro/le logo » ou « … |
| `motion-design-remotion` | Utiliser quand l'utilisateur veut une « intro animée », une « outro », un « lower third », un « générique », du « motion design », une « animation de logo » ou une « vidéo expli… |

### rapidocms

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `analyse-performance-contenu` | Utiliser quand l'utilisateur demande quels posts marchent, une analyse de ses stats ou un bilan du mois. Lit les insights réels, identifie les patterns gagnants et livre 3 recom… |
| `bibliotheque-assets` | Utiliser quand l'utilisateur veut ajouter/importer un fichier ou un asset, gérer sa bibliothèque de fichiers, rattacher un logo ou un visuel à une marque, savoir quels visuels o… |
| `bibliotheque-prompts` | Utiliser quand l'utilisateur veut sauvegarder un prompt qui a bien fonctionné, réutiliser un prompt gagnant, ou gérer sa bibliothèque de prompts (visuels, copy, vidéo). |
| `brand-review` | Utiliser quand l'utilisateur veut vérifier un contenu contre la voix de marque, le style guide et les piliers de message avant publication : écarts signalés par sévérité avec co… |
| `calendrier-editorial` | Utiliser quand l'utilisateur veut un calendrier éditorial, planifier ses posts du mois ou un plan de contenu. Méthode piliers → répartition par réseau → formats variés → brouill… |
| `carte-digitale` | Utiliser quand l'utilisateur parle de carte de visite digitale, de carte NFC, de page de carte ou d'ajouter un lien à une carte. Crée la carte, lui assigne un template avec QR c… |
| `coherence-personnage` | Utiliser quand l'utilisateur veut réutiliser le même personnage ou la même mascotte, garder le style d'un personnage récurrent, une nouvelle scène avec un personnage nommé, ou p… |
| `contagious` | Utiliser quand l'utilisateur veut du bouche-à-oreille, du contenu partageable, un programme de parrainage, ou dit « personne ne partage », « comment devenir viral ». Framework S… |
| `content-creation-methodo` | Utiliser quand l'utilisateur rédige du contenu marketing multi-canaux — article de blog, posts sociaux, newsletter, landing page, communiqué de presse, étude de cas — et veut un… |
| `contenu-conforme-marque` | Utiliser quand l'utilisateur demande de respecter la charte, le ton de la marque ou les couleurs de la marque — et en amont de toute génération de contenu ou de template. Charge… |
| `email-sequence` | Utiliser quand l'utilisateur construit une séquence d'emails — onboarding, nurture, réengagement, win-back, lancement produit — avec copy complet, timing, embranchements, condit… |
| `funnel-tofu-mofu-bofu` | Utiliser quand l'utilisateur veut des posts par étape du funnel (TOFU, MOFU, BOFU), un équilibre découverte/considération/vente, une stratégie de contenu par niveau de maturité,… |
| `generation-article-blog` | Utiliser quand l'utilisateur veut écrire un article de blog, un article SEO, un contenu long pour son site, un brief d'article, réécrire/optimiser un article existant, ou dit « … |
| `gestion-marques` | Utiliser quand l'utilisateur veut créer ou modifier une marque, gérer plusieurs marques (multi-enseignes), ajouter un logo ou un asset de marque, ou parle de la charte d'une de … |
| `made-to-stick` | Utiliser quand l'utilisateur veut un message mémorable — tagline, proposition de valeur, pitch deck, vulgariser un produit complexe — ou dit « personne ne retient notre pitch ».… |
| `orchestration-campagne` | Utiliser quand l'utilisateur parle de campagne de contenu, de série de posts ou d'insights de campagne sur les réseaux sociaux. Regroupe des posts dans une campagne et en analys… |
| `pipeline-contenu-social` | Utiliser quand l'utilisateur veut créer un post, un brouillon, programmer une publication ou du contenu réseaux sociaux (Facebook, Instagram, LinkedIn, TikTok). Enchaîne compte … |
| `prompt-engineering-visuel` | Utiliser quand l'utilisateur veut générer une image, créer un visuel ou améliorer un prompt image. Méthode de construction de prompts pour generate_image, avec variantes, critiq… |
| `prompts-visuels-pro` | Utiliser quand l'utilisateur veut un prompt de génération d'image professionnel, un prompt négatif, un visuel contenant du texte sans aucune faute, ou corriger une faute de text… |
| `storybrand-messaging` | Utiliser quand l'utilisateur parle de message de marque, de copy de site web, d'elevator pitch, de one-liner ou dit « mon message ne porte pas ». Structure narrative qui positio… |
| `studio-visuel-marque` | Utiliser quand l'utilisateur veut un visuel avec son logo, une image aux couleurs de la marque, un visuel brandé, intégrer le logo ou la mascotte dans une image, ou décliner un … |
| `video-marketing` | Utiliser quand l'utilisateur veut une vidéo, un teaser, une vidéo de campagne ou une vidéo du menu. Compose une vidéo HyperFrames (HeyGen) alignée sur la marque, la fait valider… |

### rapidocrm

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `account-research` | Utiliser quand l'utilisateur veut des renseignements commerciaux sur une entreprise ou une personne — « recherche [entreprise] », « qui est [nom] chez [société] », « dis-m'en pl… |
| `agenda-rdv` | Utiliser quand l'utilisateur veut prendre un rendez-vous client, voir son agenda du jour ou de la semaine, ou créer un événement commercial. Gère les RDV (visio, téléphone, prés… |
| `animation-client` | Utiliser quand l'utilisateur veut lancer un sondage, un jeu concours, consulter des résultats de sondage, animer ou fidéliser ses clients, ou parle de points de fidélité. |
| `campagne-marketing` | Utiliser quand l'utilisateur parle de campagne, de segment, d'envoi de masse ou de newsletter marketing. Construit le segment cible, crée la campagne, la lance et suit ses résul… |
| `coach-de-vente` | Utiliser quand l'utilisateur demande comment vendre à un prospect, quelle approche de vente adopter, « il ne répond plus je fais quoi », ou un coach de vente. Diagnostic de la s… |
| `coaching-pipeline` | Utiliser quand l'utilisateur demande une revue de pipeline, « où en sont mes deals » ou quoi relancer. Méthode de revue — deals dormants, devis expirants, étapes engorgées — ave… |
| `communication-client` | Utiliser quand l'utilisateur veut envoyer un email ou un SMS, planifier un envoi, ou contacter une entreprise. Part de la fiche entreprise, choisit la cible et le canal, avec te… |
| `contrats-clients` | Utiliser quand l'utilisateur parle de contrat client, de template de contrat, de faire signer un contrat ou de relancer un contrat non signé. Gère le cycle template → contrat en… |
| `devis-facture-relance` | Utiliser quand l'utilisateur parle de devis, de facture, de relancer un impayé ou de changer le statut d'une facture. Gère le cycle devis → facture → suivi des statuts → relances. |
| `draft-outreach` | Utiliser quand l'utilisateur veut un premier message de prospection personnalisé — « écris un cold email à X », « contacte ce prospect » : recherche sur le prospect puis rédacti… |
| `draft-response` | Utiliser quand l'utilisateur doit répondre à un client dans une situation délicate — question produit, escalade ou incident, annonce d'un retard ou d'un refus, demande de foncti… |
| `expansion-clients` | Utiliser quand l'utilisateur veut faire monter ses clients en gamme, détecter les opportunités d'upsell, ou piloter le tunnel Studio → Agence → SaaS de BraindCode. Détecte 3 tra… |
| `forecast` | Utiliser quand l'utilisateur prépare un forecast de ventes — scénarios pessimiste/probable/optimiste, commit vs upside, écart à l'objectif, couverture de pipeline — pour un poin… |
| `funnel-aarrr-reel` | Utiliser quand l'utilisateur veut son funnel AARRR, ses métriques pirates, ou savoir où fuit son funnel. Calcule Acquisition/Activation/Rétention/Referral/Revenue sur les donnée… |
| `gestion-depenses` | Utiliser quand l'utilisateur veut saisir une dépense, enregistrer un achat ou un abonnement, consulter ses dépenses, suivre ses coûts ou vérifier un montant TTC/HT/TVA côté CRM.… |
| `mom-test` | Utiliser quand l'utilisateur prépare des entretiens clients ou veut valider une idée sans se faire raconter ce qu'il veut entendre — « les utilisateurs disent qu'ils achèteraien… |
| `negotiation` | Utiliser quand l'utilisateur prépare ou mène une négociation — conditions de contrat, objections, négociation salariale, différend de prix, conversation à enjeu, « ils ne bougen… |
| `performance-commerciale` | Utiliser quand l'utilisateur demande la performance de l'équipe, les objectifs, les KPIs ou un tableau de bord commercial. Agrège commerciaux, performances individuelles et indi… |
| `pilotage-commercial` | Utiliser quand l'utilisateur dit « pilote mon commercial », « fais le point ventes », veut une boucle de pilotage commercial (Sense → Plan → Act → Feed → Report) : hygiène des d… |
| `pipeline-review-methodo` | Utiliser quand l'utilisateur mène une revue de pipeline hebdomadaire formelle : prioriser les deals, repérer les risques et les opportunités bloquées, auditer l'hygiène (dates d… |
| `playbook-objections-vivant` | Utiliser quand l'utilisateur veut un playbook d'objections, savoir quelles objections reviennent, ou comment répondre à une objection (« c'est trop cher », « je réfléchis »). Ag… |
| `predictable-revenue` | Utiliser quand l'utilisateur veut monter une machine de vente outbound B2B — rôles spécialisés SDR/AE/CSM, séquences de cold email, Cold Calling 2.0, qualification ANUM, maths d… |
| `preparation-rdv` | Utiliser quand l'utilisateur dit « prépare mon RDV », « je vois [client] demain », veut un profil SONCAS d'un contact, ou une fiche de préparation d'entretien commercial. Charge… |
| `programme-ambassadeurs` | Utiliser quand l'utilisateur veut opérer le programme ambassadeurs BraindCode (10 % client / 20 % apporteur pro), identifier les clients éligibles au parrainage, suivre les comm… |
| `prospection-pipeline` | Utiliser quand l'utilisateur veut prospecter, trouver des entreprises, ajouter au pipeline ou traiter un nouveau prospect. Choisit la bonne source de prospection, dédoublonne, p… |
| `qualification-deals` | Utiliser quand l'utilisateur veut qualifier son pipeline, savoir si un deal est solide, un score BANT/MEDDIC, ou repérer les deals fragiles. Score de qualification par deal réel… |
| `redaction-commerciale` | Utiliser quand l'utilisateur veut écrire un email de prospection, un message de relance ou une proposition commerciale. Frameworks AIDA/PAS, règles d'objet et de CTA, personnali… |
| `studio-templates` | Utiliser quand l'utilisateur veut créer un template dans l'éditeur RapidoCRM — newsletter, landing page, site web, carte de visite, email marketing ou brochure — à partir d'un d… |
| `ticket-triage` | Utiliser quand un ticket support ou un problème client arrive et doit être trié : catégorisation, priorité P1-P4, équipe destinataire, détection de doublon ou de problème connu … |

### rapidorh

| Skill | Description (frontmatter, tronquée à 180 c.) |
|---|---|
| `daily-report` | Utiliser quand l'utilisateur parle de daily, de rapport journalier ou de ses heures du jour dans RapidoRh. Crée le daily du jour avec les tâches travaillées et les heures, en ap… |
| `detection-surcharge` | Utiliser quand l'utilisateur demande qui est surchargé, la répartition de la charge ou la capacité de l'équipe. Croise heures des dailies et heures contractuelles, compte les tâ… |
| `flux-kanban` | Utiliser quand l'utilisateur veut créer une tâche, assigner une tâche, déplacer une tâche ou parle du Kanban d'un projet RapidoRh. Gère la création et le déplacement des tâches … |
| `interview-prep` | Utiliser quand l'utilisateur prépare des entretiens d'embauche : plan d'entretien structuré, questions par compétence, grilles d'évaluation (scorecards). S'appuie sur le MCP rap… |
| `job-post-builder` | Utiliser quand l'utilisateur recrute pour un poste — « aide-moi à embaucher », fiche de poste, annonce, questions d'entretien, grille de notation, lettre d'offre — et veut le ki… |
| `onboarding-equipe` | Utiliser quand l'utilisateur veut ajouter un employé, créer un rôle ou parle d'onboarding dans RapidoRh. Suit l'ordre obligatoire permissions → rôle → département → utilisateur … |
| `onboarding-rh-methodo` | Utiliser quand une prise de poste approche et qu'il faut le plan d'accueil : checklist pré-arrivée (comptes, matériel, parrain), programme du jour 1 et de la semaine 1, objectif… |
| `people-report` | Utiliser quand l'utilisateur veut un rapport RH — effectifs, turnover/attrition, diversité, santé de l'organisation (span of control, risques de départ) — pour la direction ou u… |
| `recruiting-pipeline` | Utiliser quand l'utilisateur demande un point recrutement — pipeline de candidats, combien de candidatures, statut des embauches — ou parle de sourcing, présélection, entretiens… |
| `revue-projet-hebdo` | Utiliser quand l'utilisateur demande où en est le projet, une revue hebdo projet ou l'avancement. Mesure l'avancement par colonne, détecte blocages et retards, lit les dailies d… |
| `setup-projet` | Utiliser quand l'utilisateur veut créer un projet ou parle d'un nouveau projet dans RapidoRh. Récupère les IDs valides, crée le projet avec ses paramètres, puis ajoute colonnes … |
| `tournee-des-agents` | Utiliser quand l'utilisateur veut exécuter les tâches du jour confiées aux agents sur le Kanban RapidoRh — « fais la tournée des agents », « réalise les tâches du jour », « exéc… |

## 3. Croisé skills × serveurs MCP appelés

Détection : outils MCP en `backticks` dans le corps du SKILL.md, rapprochés des
catalogues serveur connus (ceux de `scripts/tester-skills.py` + liste live FoodEatUp).
Un skill sans outil détecté = « aucun (skill de méthode) ».

| Plugin | Skill | Serveurs MCP appelés |
|---|---|---|
| foodeatup | `analyse-rentabilite-carte` | foodeatup |
| foodeatup | `briefing-du-jour` | foodeatup |
| foodeatup | `caisse-du-jour` | foodeatup |
| foodeatup | `carte-vitrine` | foodeatup |
| foodeatup | `coordination-cuisine` | foodeatup |
| foodeatup | `fidelite-restaurant` | foodeatup |
| foodeatup | `gestion-commandes` | foodeatup, foodeatup/rapidocrm |
| foodeatup | `haccp-conformite-quotidienne` | foodeatup |
| foodeatup | `handle-complaint` | foodeatup, rapidocrm |
| foodeatup | `margin-analyzer` | foodeatup, rapidocrm |
| foodeatup | `onboarding-restaurateur` | foodeatup |
| foodeatup | `planning-equipe` | foodeatup |
| foodeatup | `price-check` | foodeatup, foodeatup/rapidocrm, rapidocrm |
| foodeatup | `production-stock` | foodeatup |
| foodeatup | `reappro-fournisseurs` | foodeatup, foodeatup/rapidocrm |
| foodeatup | `recette-cout-marge` | foodeatup |
| foodeatup | `service-salle` | foodeatup |
| foodeatup | `site-vitrine-foodeatup` | foodeatup, rapidocrm |
| rapido-canva | `brand-guidelines-anthropic` | aucun (skill de méthode) |
| rapido-canva | `canvas-design` | aucun (skill de méthode) |
| rapido-canva | `menu-restaurant-design` | foodeatup, rapidocms |
| rapido-canva | `presentation-codir` | foodeatup, rapidocms, rapidocrm |
| rapido-canva | `supports-commerciaux` | rapidocrm |
| rapido-canva | `theme-factory` | aucun (skill de méthode) |
| rapido-canva | `visuels-sociaux-canva` | rapidocms |
| rapido-copywriter | `copy-linkedin` | rapidocms |
| rapido-copywriter | `copy-meta` | rapidocms |
| rapido-copywriter | `copy-tiktok` | rapidocms |
| rapido-copywriter | `declinaison-multi-reseaux` | rapidocms |
| rapido-design | `animations-web` | aucun (skill de méthode) |
| rapido-design | `architecture-info` | aucun (skill de méthode) |
| rapido-design | `direction-artistique` | rapidocms |
| rapido-design | `studio-maquette` | rapidocms |
| rapido-direction | `coffre-documents` | google-drive, rapidocrm |
| rapido-direction | `delegation-recurrence` | aucun (skill de méthode) |
| rapido-direction | `journee-du-dirigeant` | foodeatup, gmail, google-calendar, n8n, rapidocrm |
| rapido-direction | `secretariat-commercial` | gmail, google-calendar, rapidocrm |
| rapido-direction | `tri-boite-mail` | gmail, rapidocrm |
| rapido-forge | `bootcamp-bmc-complete` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-brand-platform` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-brand-storytelling` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-cash-flow-plan` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-certification-b5` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-competitive-advantage` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-competitive-deep` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-content-strategy-b5` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-conversion-funnel` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-editorial-calendar` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-email-setup` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-feature-benchmark` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-financial-projections` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-funding-strategy` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-growth-strategy` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-investor-faq` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-ip-protection` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-landing-copy-b5` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-launch-budget` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-launch-plan` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-legal-documents` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-legal-status` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-market-segmentation` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-market-sizing-b5` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-mvp-wireframes` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-naming-tagline` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-okr-kpi-setup` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-pain-mapping` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-persona-deep` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-pestel-analysis` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-pitch-deck-b5` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-pitch-script-b5` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-porter-forces` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-positioning-map` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-press-release-b5` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-problem-validation` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-qualitative-study` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-quantitative-study` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-revenue-model-b5` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-social-media-strategy` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-stakeholder-mapping` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-tone-of-voice` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-trend-analysis` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-uvp-builder` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-vision-mission` | aucun (skill de méthode) |
| rapido-forge | `bootcamp-visual-identity` | aucun (skill de méthode) |
| rapido-forge | `ideation-about-page` | aucun (skill de méthode) |
| rapido-forge | `ideation-advisory-board` | aucun (skill de méthode) |
| rapido-forge | `ideation-analytics-setup` | aucun (skill de méthode) |
| rapido-forge | `ideation-automation-workflow` | aucun (skill de méthode) |
| rapido-forge | `ideation-avatar-video` | aucun (skill de méthode) |
| rapido-forge | `ideation-blog-outline` | aucun (skill de méthode) |
| rapido-forge | `ideation-business-model-canvas` | aucun (skill de méthode) |
| rapido-forge | `ideation-cash-flow` | aucun (skill de méthode) |
| rapido-forge | `ideation-certification` | aucun (skill de méthode) |
| rapido-forge | `ideation-changelog-setup` | aucun (skill de méthode) |
| rapido-forge | `ideation-cold-email` | aucun (skill de méthode) |
| rapido-forge | `ideation-color-palette` | aucun (skill de méthode) |
| rapido-forge | `ideation-competitive-analysis` | aucun (skill de méthode) |
| rapido-forge | `ideation-contact-form` | aucun (skill de méthode) |
| rapido-forge | `ideation-course-outline` | aucun (skill de méthode) |
| rapido-forge | `ideation-demo-script` | aucun (skill de méthode) |
| rapido-forge | `ideation-email-marketing-setup` | aucun (skill de méthode) |
| rapido-forge | `ideation-email-sequence` | aucun (skill de méthode) |
| rapido-forge | `ideation-export-pdf` | aucun (skill de méthode) |
| rapido-forge | `ideation-feedback-analysis` | aucun (skill de méthode) |
| rapido-forge | `ideation-financial-forecast` | aucun (skill de méthode) |
| rapido-forge | `ideation-first-ad-campaign` | aucun (skill de méthode) |
| rapido-forge | `ideation-gamification` | aucun (skill de méthode) |
| rapido-forge | `ideation-growth-experiments` | aucun (skill de méthode) |
| rapido-forge | `ideation-hero-image` | aucun (skill de méthode) |
| rapido-forge | `ideation-hunter-outreach` | aucun (skill de méthode) |
| rapido-forge | `ideation-investor-faq` | aucun (skill de méthode) |
| rapido-forge | `ideation-iteration-planning` | aucun (skill de méthode) |
| rapido-forge | `ideation-kpi-dashboard` | aucun (skill de méthode) |
| rapido-forge | `ideation-landing-copy` | aucun (skill de méthode) |
| rapido-forge | `ideation-landing-page` | aucun (skill de méthode) |
| rapido-forge | `ideation-launch-checklist` | aucun (skill de méthode) |
| rapido-forge | `ideation-launch-plan` | aucun (skill de méthode) |
| rapido-forge | `ideation-launch-post` | aucun (skill de méthode) |
| rapido-forge | `ideation-lead-magnet` | aucun (skill de méthode) |
| rapido-forge | `ideation-lean-canvas` | aucun (skill de méthode) |
| rapido-forge | `ideation-legal-docs` | aucun (skill de méthode) |
| rapido-forge | `ideation-legal-structure` | aucun (skill de méthode) |
| rapido-forge | `ideation-lessons-learned` | aucun (skill de méthode) |
| rapido-forge | `ideation-linkedin-posts` | aucun (skill de méthode) |
| rapido-forge | `ideation-logo-prompt` | aucun (skill de méthode) |
| rapido-forge | `ideation-lovable-prompt` | rapidocms |
| rapido-forge | `ideation-mvp-wireframes` | aucun (skill de méthode) |
| rapido-forge | `ideation-naming-generator` | aucun (skill de méthode) |
| rapido-forge | `ideation-north-star-metric` | aucun (skill de méthode) |
| rapido-forge | `ideation-paid-acquisition` | aucun (skill de méthode) |
| rapido-forge | `ideation-persona-maker` | aucun (skill de méthode) |
| rapido-forge | `ideation-ph-page-copy` | aucun (skill de méthode) |
| rapido-forge | `ideation-pitch-deck` | aucun (skill de méthode) |
| rapido-forge | `ideation-pitch-script` | aucun (skill de méthode) |
| rapido-forge | `ideation-pre-launch-campaign` | aucun (skill de méthode) |
| rapido-forge | `ideation-press-release` | aucun (skill de méthode) |
| rapido-forge | `ideation-pricing-page` | aucun (skill de méthode) |
| rapido-forge | `ideation-product-hunt-strategy` | aucun (skill de méthode) |
| rapido-forge | `ideation-qa-checklist` | aucun (skill de méthode) |
| rapido-forge | `ideation-quiz-generator` | aucun (skill de méthode) |
| rapido-forge | `ideation-referral-program` | aucun (skill de méthode) |
| rapido-forge | `ideation-retargeting-setup` | aucun (skill de méthode) |
| rapido-forge | `ideation-roadmap-product` | aucun (skill de méthode) |
| rapido-forge | `ideation-seo-meta` | aucun (skill de méthode) |
| rapido-forge | `ideation-sitemap-generator` | aucun (skill de méthode) |
| rapido-forge | `ideation-social-strategy` | aucun (skill de méthode) |
| rapido-forge | `ideation-specs-generator` | aucun (skill de méthode) |
| rapido-forge | `ideation-swot` | aucun (skill de méthode) |
| rapido-forge | `ideation-testimonial-request` | aucun (skill de méthode) |
| rapido-forge | `ideation-ui-guidelines` | aucun (skill de méthode) |
| rapido-forge | `ideation-usp-statement` | aucun (skill de méthode) |
| rapido-forge | `ideation-value-proposition` | aucun (skill de méthode) |
| rapido-forge | `ideation-video-edit` | aucun (skill de méthode) |
| rapido-forge | `ideation-video-script` | aucun (skill de méthode) |
| rapido-forge | `ideation-voiceover` | aucun (skill de méthode) |
| rapido-forge | `ideation-webhook-setup` | aucun (skill de méthode) |
| rapido-forge | `scale-ab-testing` | aucun (skill de méthode) |
| rapido-forge | `scale-adoption-curve` | aucun (skill de méthode) |
| rapido-forge | `scale-ansoff-matrix` | aucun (skill de méthode) |
| rapido-forge | `scale-bant-qualification` | aucun (skill de méthode) |
| rapido-forge | `scale-bcg-matrix` | aucun (skill de méthode) |
| rapido-forge | `scale-blue-ocean` | aucun (skill de méthode) |
| rapido-forge | `scale-break-even` | aucun (skill de méthode) |
| rapido-forge | `scale-burn-rate` | aucun (skill de méthode) |
| rapido-forge | `scale-cap-table` | aucun (skill de méthode) |
| rapido-forge | `scale-cold-email-prospection` | aucun (skill de méthode) |
| rapido-forge | `scale-commercial-proposal` | aucun (skill de méthode) |
| rapido-forge | `scale-community-building` | aucun (skill de méthode) |
| rapido-forge | `scale-content-pillar` | aucun (skill de méthode) |
| rapido-forge | `scale-cost-waterfall` | aucun (skill de méthode) |
| rapido-forge | `scale-customer-journey` | aucun (skill de méthode) |
| rapido-forge | `scale-customer-success` | aucun (skill de méthode) |
| rapido-forge | `scale-design-system` | aucun (skill de méthode) |
| rapido-forge | `scale-eisenhower-matrix` | aucun (skill de méthode) |
| rapido-forge | `scale-financial-projections` | aucun (skill de méthode) |
| rapido-forge | `scale-fundraising-plan` | aucun (skill de méthode) |
| rapido-forge | `scale-funnel-aarrr` | aucun (skill de méthode) |
| rapido-forge | `scale-golden-circle` | aucun (skill de méthode) |
| rapido-forge | `scale-google-ads-setup` | aucun (skill de méthode) |
| rapido-forge | `scale-google-analytics-4` | aucun (skill de méthode) |
| rapido-forge | `scale-google-search-console` | aucun (skill de méthode) |
| rapido-forge | `scale-google-trends` | aucun (skill de méthode) |
| rapido-forge | `scale-heatmaps` | aucun (skill de méthode) |
| rapido-forge | `scale-impact-effort` | aucun (skill de méthode) |
| rapido-forge | `scale-influencer-marketing` | aucun (skill de méthode) |
| rapido-forge | `scale-jtbd` | aucun (skill de méthode) |
| rapido-forge | `scale-kpi-dashboard` | aucun (skill de méthode) |
| rapido-forge | `scale-linkedin-ads-b2b` | aucun (skill de méthode) |
| rapido-forge | `scale-linkedin-pixel` | aucun (skill de méthode) |
| rapido-forge | `scale-marketing-4c` | aucun (skill de méthode) |
| rapido-forge | `scale-marketing-4p` | aucun (skill de méthode) |
| rapido-forge | `scale-meta-ads-campaign` | aucun (skill de méthode) |
| rapido-forge | `scale-meta-pixel` | aucun (skill de méthode) |
| rapido-forge | `scale-negotiation-batna` | aucun (skill de méthode) |
| rapido-forge | `scale-north-star-metric` | aucun (skill de méthode) |
| rapido-forge | `scale-nps-survey` | aucun (skill de méthode) |
| rapido-forge | `scale-objections-playbook` | aucun (skill de méthode) |
| rapido-forge | `scale-okrs-q1` | aucun (skill de méthode) |
| rapido-forge | `scale-porter-5-forces` | aucun (skill de méthode) |
| rapido-forge | `scale-pr-media-kit` | aucun (skill de méthode) |
| rapido-forge | `scale-pricing-strategy` | aucun (skill de méthode) |
| rapido-forge | `scale-prototype` | aucun (skill de méthode) |
| rapido-forge | `scale-public-roadmap` | aucun (skill de méthode) |
| rapido-forge | `scale-referral-program` | aucun (skill de méthode) |
| rapido-forge | `scale-rice-prioritization` | aucun (skill de méthode) |
| rapido-forge | `scale-sales-call-script` | aucun (skill de méthode) |
| rapido-forge | `scale-scenarios-planning` | aucun (skill de méthode) |
| rapido-forge | `scale-semrush-audit` | aucun (skill de méthode) |
| rapido-forge | `scale-seo-meta` | aucun (skill de méthode) |
| rapido-forge | `scale-soncas` | aucun (skill de méthode) |
| rapido-forge | `scale-spin-selling` | aucun (skill de méthode) |
| rapido-forge | `scale-tiktok-ads-creator` | aucun (skill de méthode) |
| rapido-forge | `scale-tiktok-pixel` | aucun (skill de méthode) |
| rapido-forge | `scale-unit-economics` | aucun (skill de méthode) |
| rapido-forge | `scale-upsell-crosssell` | aucun (skill de méthode) |
| rapido-forge | `scale-user-story-mapping` | aucun (skill de méthode) |
| rapido-forge | `scale-user-tests` | aucun (skill de méthode) |
| rapido-forge | `scale-wireframes` | aucun (skill de méthode) |
| rapido-forge | `selecteur-framework` | aucun (skill de méthode) |
| rapido-gmaps | `detection-opportunites` | rapidocrm |
| rapido-gmaps | `enrichissement-fiches` | rapidocrm |
| rapido-gmaps | `sourcing-gmaps` | rapidocrm |
| rapido-gmaps | `veille-concurrents-gmaps` | foodeatup |
| rapido-google-ads | `audit-compte-google-ads` | aucun (skill de méthode) |
| rapido-google-ads | `pilotage-performance-google-ads` | aucun (skill de méthode) |
| rapido-google-ads | `recherche-mots-cles-sea` | aucun (skill de méthode) |
| rapido-google-ads | `synergie-seo-sea` | aucun (skill de méthode) |
| rapido-higgsfield | `analyse-video-virale` | aucun (skill de méthode) |
| rapido-higgsfield | `clips-et-shorts` | rapidocms |
| rapido-higgsfield | `gouvernance-credits` | aucun (skill de méthode) |
| rapido-higgsfield | `personnages-univers` | rapidocms |
| rapido-higgsfield | `sites-et-jeux-express` | rapidocrm |
| rapido-higgsfield | `studio-image-pro` | foodeatup, rapidocms |
| rapido-higgsfield | `usine-video-marketing` | rapidocms |
| rapido-higgsfield | `videos-explicatives` | rapidocms |
| rapido-higgsfield | `voix-et-doublage` | rapidocms |
| rapido-leadmagnet | `campagne-lead-magnet` | rapidocms/rapidocrm, rapidocrm |
| rapido-leadmagnet | `fabrication-lead-magnet` | rapidocms |
| rapido-leadmagnet | `page-et-capture` | rapidocrm |
| rapido-leadmagnet | `projet-rh-lead-magnet` | aucun (skill de méthode) |
| rapido-lovable | `agent-ia-produit` | foodeatup, lovable, rapidocrm |
| rapido-lovable | `connecteur-mcp-lovable` | gmail/lovable, lovable, rapidocms |
| rapido-lovable | `frontend-design` | aucun (skill de méthode) |
| rapido-lovable | `mvp-lovable` | lovable, rapidocms, rapidocrm |
| rapido-lovable | `site-restaurant` | foodeatup, lovable, rapidocms |
| rapido-lovable | `sync-marque-lovable` | lovable |
| rapido-lovable | `ui-styling` | aucun (skill de méthode) |
| rapido-lovable | `ui-ux-pro-max` | aucun (skill de méthode) |
| rapido-lovable | `usine-a-landing` | lovable, rapidocms/rapidocrm, rapidocrm |
| rapido-lovable | `web-artifacts-builder` | aucun (skill de méthode) |
| rapido-marketing | `attribution-kpi-marketing` | rapidocms, rapidocrm |
| rapido-marketing | `core-four-strategie` | aucun (skill de méthode) |
| rapido-marketing | `delivrabilite-email` | rapidocms/rapidocrm, rapidocrm |
| rapido-marketing | `geo-optimization` | rapidocms |
| rapido-marketing | `growth-experiments` | rapidocrm |
| rapido-marketing | `icp-generator` | rapidocrm |
| rapido-marketing | `lead-getters-systeme` | rapidocrm |
| rapido-marketing | `lead-magnet-machine` | rapidocrm |
| rapido-marketing | `lead-scoring` | rapidocrm |
| rapido-marketing | `machine-inbound` | rapidocms, rapidocms/rapidocrm, rapidocrm |
| rapido-marketing | `machine-outbound` | rapidocrm |
| rapido-marketing | `money-math-acquisition` | rapidocrm |
| rapido-marketing | `operations-influenceurs` | rapidocrm |
| rapido-marketing | `pilotage-marketing` | aucun (skill de méthode) |
| rapido-marketing | `sales-intelligence-fireflies` | rapidocrm |
| rapido-marketing | `social-selling-linkedin` | rapidocms, rapidocrm |
| rapido-marketing | `tunnel-de-vente-360` | rapidocrm |
| rapido-meta-ads | `audiences-crm` | facebook-ads, foodeatup, rapidocrm |
| rapido-meta-ads | `boost-post-instagram` | facebook-ads, rapidocms |
| rapido-meta-ads | `campaign-plan-methodo` | aucun (skill de méthode) |
| rapido-meta-ads | `creatifs-publicitaires` | facebook-ads, rapidocms |
| rapido-meta-ads | `hundred-million-offers` | aucun (skill de méthode) |
| rapido-meta-ads | `influence-psychology` | aucun (skill de méthode) |
| rapido-meta-ads | `lancement-campagne-meta` | facebook-ads, rapidocms/rapidocrm |
| rapido-meta-ads | `one-page-marketing` | aucun (skill de méthode) |
| rapido-meta-ads | `performance-report-methodo` | aucun (skill de méthode) |
| rapido-meta-ads | `pilotage-performance-ads` | facebook-ads, rapidocrm |
| rapido-meta-ads | `pixel-et-retargeting` | facebook-ads, lovable |
| rapido-meta-ads | `tests-ab-meta` | facebook-ads |
| rapido-meta-ads | `veille-ads-concurrents` | facebook-ads |
| rapido-n8n | `memoire-operationnelle` | n8n |
| rapido-n8n | `recettes-metier` | aucun (skill de méthode) |
| rapido-n8n | `surveillance-automatisations` | n8n |
| rapido-n8n | `usine-automatisations` | n8n |
| rapido-prompteur | `prompt-image` | rapidocms |
| rapido-prompteur | `prompt-lovable` | lovable, rapidocms, rapidocrm |
| rapido-prompteur | `prompt-personnage` | rapidocms |
| rapido-prompteur | `prompt-video` | rapidocms |
| rapido-relation-client | `boucle-nps` | rapidocrm |
| rapido-relation-client | `cent-premiers-jours` | aucun (skill de méthode) |
| rapido-relation-client | `coach-relation-client` | aucun (skill de méthode) |
| rapido-relation-client | `pilotage-service-client` | aucun (skill de méthode) |
| rapido-relation-client | `sante-client` | rapidocrm |
| rapido-relation-client | `segmentation-rfm` | rapidocrm |
| rapido-seo | `audit-seo-technique` | rapidocms |
| rapido-seo | `netlinking` | aucun (skill de méthode) |
| rapido-seo | `performance-organique` | aucun (skill de méthode) |
| rapido-seo | `pilotage-seo` | rapidocms |
| rapido-seo | `recherche-mots-cles` | aucun (skill de méthode) |
| rapido-seo | `tendances-marche` | aucun (skill de méthode) |
| rapido-startup | `amelioration-des-routines` | aucun (skill de méthode) |
| rapido-startup | `catalogue-kpi` | aucun (skill de méthode) |
| rapido-startup | `interview-business-plan` | foodeatup, foodeatup/rapidocrm, rapidocms, rapidocrm, stripe |
| rapido-startup | `loop-engine-v2` | aucun (skill de méthode) |
| rapido-startup | `plan-execution-startup` | google-calendar, rapidocrm |
| rapido-startup | `plan-financier-previsionnel` | rapidocrm, stripe |
| rapido-suite | `business-pulse` | foodeatup, rapidocrm |
| rapido-suite | `cash-flow-snapshot` | foodeatup, rapidocrm |
| rapido-suite | `comite-de-direction` | facebook-ads, foodeatup, lovable, n8n, rapidocms, rapidocrm |
| rapido-suite | `dossier-startup-360` | foodeatup/rapidocrm, rapidocms, rapidocrm |
| rapido-suite | `invoice-chase` | foodeatup, rapidocrm |
| rapido-suite | `lancement-projet-360` | aucun (skill de méthode) |
| rapido-suite | `mise-a-jour-kb` | foodeatup/rapidocrm, rapidocms |
| rapido-suite | `monday-brief` | foodeatup, rapidocrm |
| rapido-suite | `onboarding-client-360` | rapidocms, rapidocms/rapidocrm, rapidocrm |
| rapido-suite | `onboarding-entreprise` | foodeatup, foodeatup/rapidocrm, rapidocms, rapidocrm |
| rapido-suite | `pilotage-entreprise` | aucun (skill de méthode) |
| rapido-suite | `revue-hebdo-business` | facebook-ads, foodeatup, lovable, n8n, rapidocms, rapidocrm |
| rapido-suite | `skill-creator` | aucun (skill de méthode) |
| rapido-tiktok-ads | `lancement-campagne-tiktok` | aucun (skill de méthode) |
| rapido-tiktok-ads | `pilotage-performance-tiktok` | aucun (skill de méthode) |
| rapido-tiktok-ads | `tendances-creatives-tiktok` | aucun (skill de méthode) |
| rapido-video | `montage-express` | rapidocms |
| rapido-video | `motion-design-remotion` | rapidocms |
| rapidocms | `analyse-performance-contenu` | rapidocms, rapidocms/rapidocrm |
| rapidocms | `bibliotheque-assets` | rapidocms |
| rapidocms | `bibliotheque-prompts` | rapidocms |
| rapidocms | `brand-review` | aucun (skill de méthode) |
| rapidocms | `calendrier-editorial` | rapidocms, rapidocms/rapidocrm |
| rapidocms | `carte-digitale` | rapidocms |
| rapidocms | `coherence-personnage` | rapidocms |
| rapidocms | `contagious` | aucun (skill de méthode) |
| rapidocms | `content-creation-methodo` | aucun (skill de méthode) |
| rapidocms | `contenu-conforme-marque` | rapidocms |
| rapidocms | `email-sequence` | aucun (skill de méthode) |
| rapidocms | `funnel-tofu-mofu-bofu` | rapidocms |
| rapidocms | `generation-article-blog` | rapidocms |
| rapidocms | `gestion-marques` | rapidocms |
| rapidocms | `made-to-stick` | aucun (skill de méthode) |
| rapidocms | `orchestration-campagne` | rapidocms, rapidocms/rapidocrm |
| rapidocms | `pipeline-contenu-social` | rapidocms |
| rapidocms | `prompt-engineering-visuel` | rapidocms |
| rapidocms | `prompts-visuels-pro` | rapidocms |
| rapidocms | `storybrand-messaging` | aucun (skill de méthode) |
| rapidocms | `studio-visuel-marque` | rapidocms |
| rapidocms | `video-marketing` | lovable, rapidocms |
| rapidocrm | `account-research` | aucun (skill de méthode) |
| rapidocrm | `agenda-rdv` | rapidocrm |
| rapidocrm | `animation-client` | rapidocrm |
| rapidocrm | `campagne-marketing` | rapidocms/rapidocrm, rapidocrm |
| rapidocrm | `coach-de-vente` | rapidocrm |
| rapidocrm | `coaching-pipeline` | rapidocrm |
| rapidocrm | `communication-client` | rapidocrm |
| rapidocrm | `contrats-clients` | rapidocrm |
| rapidocrm | `devis-facture-relance` | rapidocrm |
| rapidocrm | `draft-outreach` | aucun (skill de méthode) |
| rapidocrm | `draft-response` | aucun (skill de méthode) |
| rapidocrm | `expansion-clients` | rapidocms/rapidocrm, rapidocrm |
| rapidocrm | `forecast` | aucun (skill de méthode) |
| rapidocrm | `funnel-aarrr-reel` | rapidocms/rapidocrm, rapidocrm |
| rapidocrm | `gestion-depenses` | rapidocrm |
| rapidocrm | `mom-test` | aucun (skill de méthode) |
| rapidocrm | `negotiation` | aucun (skill de méthode) |
| rapidocrm | `performance-commerciale` | rapidocrm |
| rapidocrm | `pilotage-commercial` | rapidocrm |
| rapidocrm | `pipeline-review-methodo` | aucun (skill de méthode) |
| rapidocrm | `playbook-objections-vivant` | rapidocrm |
| rapidocrm | `predictable-revenue` | aucun (skill de méthode) |
| rapidocrm | `preparation-rdv` | rapidocrm |
| rapidocrm | `programme-ambassadeurs` | rapidocrm |
| rapidocrm | `prospection-pipeline` | rapidocrm |
| rapidocrm | `qualification-deals` | rapidocrm |
| rapidocrm | `redaction-commerciale` | rapidocrm |
| rapidocrm | `studio-templates` | rapidocrm |
| rapidocrm | `ticket-triage` | aucun (skill de méthode) |
| rapidorh | `daily-report` | aucun (skill de méthode) |
| rapidorh | `detection-surcharge` | aucun (skill de méthode) |
| rapidorh | `flux-kanban` | aucun (skill de méthode) |
| rapidorh | `interview-prep` | aucun (skill de méthode) |
| rapidorh | `job-post-builder` | aucun (skill de méthode) |
| rapidorh | `onboarding-equipe` | aucun (skill de méthode) |
| rapidorh | `onboarding-rh-methodo` | aucun (skill de méthode) |
| rapidorh | `people-report` | aucun (skill de méthode) |
| rapidorh | `recruiting-pipeline` | aucun (skill de méthode) |
| rapidorh | `revue-projet-hebdo` | aucun (skill de méthode) |
| rapidorh | `setup-projet` | aucun (skill de méthode) |
| rapidorh | `tournee-des-agents` | aucun (skill de méthode) |

## 4. Descriptions se recouvrant à plus de 50 % (risque de déclenchement ambigu)

Mesure : recouvrement Jaccard des **mots significatifs** des descriptions
frontmatter (minuscules, mots de 4 lettres et plus, hors mots-outils français et
hors gabarit « Utiliser quand l'utilisateur… » commun à tous les skills).
Un ratio brut type `difflib` est inutilisable ici : le gabarit partagé fait
dépasser 0,50 à presque toutes les paires. Seuil retenu : Jaccard > 0,50.
Les 181 exercices de `rapido-forge` partagent volontairement un gabarit :
les paires internes à forge sont comptées à part.

| Skill A | Skill B | Jaccard |
|---|---|---|
| _aucune paire au-dessus du seuil_ | | |

0 paire(s) hors forge au-dessus du seuil ; 26 paire(s) internes aux exercices forge (gabarit assumé).

Pour situer la marge de sécurité, les 10 paires les plus proches (sous le seuil) :

| Skill A | Skill B | Jaccard |
|---|---|---|
| rapido-copywriter:`copy-linkedin` | rapido-copywriter:`copy-meta` | 0.47 |
| rapido-marketing:`pilotage-marketing` | rapidocrm:`pilotage-commercial` | 0.45 |
| rapido-marketing:`pilotage-marketing` | rapido-seo:`pilotage-seo` | 0.40 |
| rapido-seo:`pilotage-seo` | rapidocrm:`pilotage-commercial` | 0.31 |
| rapido-relation-client:`pilotage-service-client` | rapido-seo:`pilotage-seo` | 0.30 |
| rapido-marketing:`pilotage-marketing` | rapido-relation-client:`pilotage-service-client` | 0.30 |
| rapido-canva:`visuels-sociaux-canva` | rapidocms:`pipeline-contenu-social` | 0.30 |
| rapidorh:`interview-prep` | rapidorh:`job-post-builder` | 0.29 |
| rapidorh:`interview-prep` | rapidorh:`recruiting-pipeline` | 0.27 |
| rapido-relation-client:`pilotage-service-client` | rapidocrm:`pilotage-commercial` | 0.26 |

## 5. Plugins sans AUCUN hook et sans AUCUN agent

| Plugin | Skills | Remarque |
|---|---|---|
| _aucun_ | | |

