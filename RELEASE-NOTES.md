# Notes de release

## Le chef de chantier Build — braindcode-build (2026-10-25)

Nouveau plugin **`braindcode-build`** (29e) — Claude Code **développeur IA
déclaré** d'une extension BraindCode Build, de l'idée à la routine : cahier
des charges sur outils réels, maquettes, **construction Lovable pas à pas**
(pauses à l'humain, diffs relus), MCP produit branché **côté serveur**,
tests et rapport obligatoire, **MCP de l'extension exposé et validé par une
tâche tracée**, déclaration Plan'It + marketplace, routine auditée, plugin
publié sur ce dépôt, vitrine, hackathon.

- **22 skills**, **6 agents**, **17 commandes**, **8 widgets** charte
  BraindCode (vérifiée dans le design system du projet Build).
- **8 hooks fail-closed, 33 cas CI** : deploy_project REFUSÉ sans
  validation humaine de mise en ligne lue, anti-secret (deny sur clés,
  jetons, mots de passe dans 7 outils), audit des credentials front
  (critère n° 3), crédits Lovable sous accord, knowledge lu avant d'être
  remplacé, DROP/TRUNCATE refusés.
- **6 catalogues CI** branchés : Build 44 (manifeste MCP publié du
  projet), **Lovable 42 en liste versionnée** (remplace le relevé embarqué
  périmé : 5 outils disparus, 3 nouveaux), marketplace 53, + academy,
  planit et tutoriel repris des branches sœurs.
- Référence : méthode en dix étapes + cinq critères + trois parcours,
  règles Lovable, carte des interconnexions (8 serveurs), pièges vérifiés
  (hackathon aux dates périmées, 20 vitrines sans tutoriel, Daily Brief en
  brouillon).
  **Validation : TOUT VALIDE (29 plugins) ; tester 0 FAIL / 0 WARN.**
## Le prospecteur Prospector Hub — rapido-prospector (2026-10-25)

Nouveau plugin **`rapido-prospector`** (29e) — **toute la prospection
commerciale** au-dessus du serveur MCP Prospect (« Prospector Hub »,
66 outils relevés, OAuth au premier appel) : zones et spécialités, base
dédoublonnée, campagnes **e-mail / SMS / LinkedIn sous contrôle humain**,
calendrier éditorial, blog, vidéos, webinaires, lead magnets, journal et
**MRR Stripe (présenté en estimation)**.

- **19 skills**, **4 agents** (chasseur, rédacteur de séquences,
  programmateur de contenus, contrôleur conformité et mesure),
  **12 commandes**, **8 widgets** à la charte FoodEatUp.
- **7 scripts stdlib** (dédoublonnage 5 critères, E.164/mobiles, segments
  GSM-7/UCS-2, quotas min(KB, cadre Academy), entonnoir, MRR, conformité)
  — formules affichées.
- **7 hooks fail-closed, 30 cas CI** : ask systématique sur les 5 envois
  réels, deny quota/lot/fenêtre, deny sans désinscription/STOP/identité,
  **appels automatisés désactivés par défaut** (activation = KB + base
  légale validée), cascades des 12 delete rappelées, anti-doublon sur
  add_clients, journal masqué.
- **KB de prospection** (gabarit rapido-kb-template/prospection.md) :
  quotas, fenêtre horaire, identité d'expéditeur, désinscription/STOP,
  **liste d'opposition** ; reference/conformite-prospection.md marqué
  « à faire valider par un juriste ».
- CI : catalogue fail-closed 66 outils + périmètre OUTILS strict.
  **Validation : TOUT VALIDE (29 plugins) ; tester 0 FAIL / 0 WARN.**
## Le pilote Plan'It — planit 0.1.0 (2026-10-25)

Nouveau plugin **`planit`** (29e) : Claude Code pilote **Plan'It**
(`https://planit.braindcode.com/mcp`) de bout en bout — tâches, routines,
calendrier, **boucles routine ↔ KPI** (loop engineering), widgets de
l'accueil, alertes, crédits, connecteurs MCP, routines sur événement,
prompts, catalogue privé et vidéos courtes.

- **Le contrat** : tout coût s'annonce AVANT (estimation obligatoire,
  vérifiée par hook) ; propositions d'abord (rien ne se crée sans l'accord
  explicite sur CETTE proposition, un refus est définitif à l'identique) ;
  les 10 outils destructifs du serveur + les payants + ceux qui tranchent
  passent en confirmation ; aucun effet annoncé sur `not_enough_data`
  (3 exécutions ET 14 jours) ; jamais de pause de notre initiative.
- **22 skills** (de l'accueil de pilotage à la revue du vendredi, chaîne de
  l'Architecte, export de plugins vers le catalogue privé Plan'It),
  **4 agents** (architecte, ingénieur des boucles, contrôleur des crédits,
  concierge des connecteurs), **13 commandes**, **6 widgets** + scripts
  stdlib (crédits vidéo = max(5, ⌈s/2⌉) ; jours d'autonomie =
  solde / (total/30), formules affichées).
- **6 hooks fail-closed testés** (26 cas) : garde-planit (trois familles
  sensibles versionnées dans reference/outils-sensibles.json),
  garde-cout-annonce (deny sans estimation au journal de session),
  garde-autonomie (auto = ask ; auto + destructif = deny),
  verite-des-donnees (PostToolUse : not_enough_data / throttled /
  flat_price), contexte de session, journal masqué.
- Inventaire live docs/inventaires/planit-tools-live.txt (63 outils) branché
  au contrôle CI + périmètre OUTILS strict pour `planit/`.
- Position assumée : **l'exécutant Plan'It** des routines conçues par
  rapido-suite, rapido-startup et rapido-employe (registre traduit par
  `installer-une-routine-du-registre`) — zéro skill doublonné.
## Claude employé — rapido-employe 0.1.0 (2026-10-25)

Nouveau plugin **`rapido-employe`** (29e) : Claude Code devient **l'employé
commercial de FoodEatUp** — il se forme avec l'Academy (serveur « FoodEatUp
formation », `https://formation.foodeatup.fr/mcp`, 191 outils relevés en
live), puis prospecte, relance, prépare démos et devis, communique, sert et
s'améliore chaque vendredi, à travers 15 serveurs déclarés.

- **Le modèle** : le cadre se RELIT à chaque prise de poste
  (`get_claude_brief` → `get_work_plan`) — 8 familles d'actions à 3 niveaux
  (Aperçu/Brouillon/Confirmé), quotas du jour, budget `record_expense` —
  rien n'est codé en dur, instantané dans `.claude/state/cadre-employe.json`.
- **31 skills** (journée, apprendre, déployer, vendre, communiquer, servir,
  orchestrer), **9 agents** (dont les six de l'équipe Academy, prompt de
  production via `get_agent_brief`), **15 commandes** (/prise-de-poste …
  /cadre), **6 widgets** à la palette Academy + `render_widget.py`.
- **8 hooks fail-closed testés** : garde-cadre (familles → niveaux relus,
  périmé > 24 h, agent arrêté = deny, « engager » toujours humain),
  garde-depense (un refus arrête), garde-auto-gouvernance (deny absolu :
  Claude ne fixe jamais son propre cadre), garde-envois (Gmail direct
  interdit, quotas en deny), garde-memoire, anti-donnee-inventee, contexte
  de session, journal des écritures (secrets masqués, compteurs).
- Table versionnée `reference/familles-outils.json` (écritures de tous les
  serveurs → familles, source unique des gardes, égalité d'intention avec
  les inventaires `academy-tools-live.txt` 191 / `planit-tools-live.txt`
  63 / `foodeatup-tutoriel-tools-live.txt` 36).
- Orchestrateur assumé : délègue à rapidocrm, rapido-gmaps,
  rapido-leadmagnet, rapido-copywriter, rapido-direction, rapido-suite —
  zéro skill doublonné (contrôle de similarité CI).
## L'Académie FoodEatUp, version serveur réel — foodeatup-tutoriel 0.2.0 (2026-10-25)

Le plugin **`foodeatup-tutoriel`** est reconstruit sous le même slug sur le
**vrai serveur public « FoodEatUp tutoriel »** (36 outils vérifiés en session
live, v0.7.0, endpoint `https://tutoriel.foodeatup.com/mcp` — lecture seule,
sans compte), en remplacement de la surface Academy de juillet (26 outils,
serveur resté injoignable).

- **16 skills** couvrant tout le serveur : cadrage (`demarrer-academie`,
  secteur avant métier), parcours (`parcours-sur-mesure`), rituel de leçon
  vidéo → quiz → exercice (`lecon-guidee`), recherche et exploration, équipe
  (`former-mon-equipe`, rien n'est « envoyé »), carnet de reprise, prompts,
  pont vers le connecteur produit (`passer-a-l-action` — jamais appelé par le
  plugin), offre et partenaires aux **chiffres exclusivement sourcés et
  datés**, parcours convive (**vidéos non tournées : aucun lien annoncé**),
  API développeur, studio de production des tutos manquants.
- **4 agents** (chef-formateur, responsable-formation, conseiller-academie,
  producteur-tutos) + **7 commandes** (/academie, /lecon, /quiz, /parcours,
  /former-equipe, /carnet, /tutos-manquants).
- **5 widgets HTML** rendus par `render_widget.py` (stdlib, formules
  affichées) — le serveur n'expose aucune ressource MCP Apps (vérifié), les
  gabarits locaux sont le repli officiel.
- **4 hooks testés en CI** : périmètre Académie **fail-closed** (inventaire
  embarqué = liste versionnée, égalité contrôlée), anti-lien-inventé (deny),
  garde tarifs/commissions (montant sans date de vérification → ask),
  contexte de session.
- CI étendue **sans assouplir les autres règles** : catalogue fail-closed 36
  outils + périmètre OUTILS « Académie seule » pour `foodeatup-tutoriel/`.
- `foodeatup` 1.11.5 : la passerelle d'onboarding pointe vers les nouveaux
  skills.

## Studio UX/UI — rapido-design (2026-07-15)

Nouveau plugin **`rapido-design`** (25e) — le **studio UX/UI** qui orchestre toute la
chaîne **charte → direction artistique → sitemap/flows → maquettes hi-fi Figma → design
system → MVP Lovable animé**, avec **les mêmes tokens du début à la fin**.

- **Audit D0** (`docs/IMPORTS-DESIGN.md`, `docs/PASSERELLES-REELLES.md`) : 5 dépôts **MIT**
  relus (hue, styleseed, qiaomu, work-with-design-systems, figgo) — Trystan-SA
  (reverse-engineered) **exclu**. Passerelles **vérifiées en direct** : charte CMS → Figma
  OK (**`font_family` = 9 web-safe** ; la vraie police vit dans le DS), mécanisme
  design system Lovable validé (0 DS dans le workspace → créé par le pipeline).
- **Fondations** : `pipeline-design.md` (7 étapes), `passerelles.md` (CMS↔Figma↔Lovable
  outil par outil), `jugement-design.md` (**anti-goût-IA** : gradients violets,
  glassmorphism, cartes clonées… + quand dire non), `motifs-animation.md` (sobriété +
  `prefers-reduced-motion`), hook `garde-charte`.
- **4 skills** : `direction-artistique` (DA ↔ charte CMS, la charte existante **prime**),
  `architecture-info` (structure **validée avant tout pixel**), `studio-maquette` (**DS
  Figma d'abord**, écrans qui **consomment les variables**, gates critique + WCAG, handoff
  Lovable), `animations-web` (motion sobre, `prefers-reduced-motion` **obligatoire**).
  **Agent** `directeur-ux` (tient le fil rouge des tokens, **zéro divergence**).
- **Articulation** (patchs croisés) : `rapido-lovable:mvp-lovable` (le MVP démarre du DS
  Lovable), `ui-ux-pro-max` (bibliothèque de styles vs pipeline qui l'exploite),
  `rapido-prompteur:prompt-lovable` (tokens du DS), `rapidocms:gestion-marques` (sync DA
  bidirectionnel). Runbook `docs/RECETTE-DESIGN.md`. **Validation** : TOUT VALIDE
  (25 plugins) ; tester 0/0/0.

## Copywriter 4 réseaux (2026-07-15)

Nouveau plugin **`rapido-copywriter`** (24e) — le copywriter **LinkedIn · Facebook ·
Instagram · TikTok** : il connaît chaque réseau, produit la copy plateforme par
plateforme et **apprend de ses vrais résultats**.

- **Audit CW0** (`docs/IMPORTS-COPYWRITER.md`) : 3 dépôts **MIT** relus (linkedin-skills,
  social-media-skills, social-creative-director) avec anti-verbatim renforcé (hooks
  re-dérivés, humanizer francisé). **Relevé live décisif** : `post_insights` expose par
  réseau exactement **`liked`/`shares`/`views`/`comments`** → ce qui fonde le scoring.
- **Fondations** : `grammaires-reseaux.md` (4 fiches **datées**, révision trimestrielle),
  `banque-hooks.md` (patterns par réseau, tag GAGNANT/NEUTRE + compteur), `anti-voix-ia.md`
  (tics **français** + passe finale), `articulations.md` (frontières).
- **4 skills** : `copy-linkedin`, `copy-meta` (FB+IG), `copy-tiktok` (script de tournage),
  `declinaison-multi-reseaux` (1 idée → 4 déclinaisons natives). **Agent**
  `copywriter-social`. **Boucle** `scripts/score_hooks.py` (interactions = liked + shares
  + comments ; GAGNANT si > médiane du réseau — aucune métrique inventée).
- **Garde-fous** : gate voix de marque + passe anti-voix-IA obligatoires, hook
  `garde-voix-marque`, **brouillons CMS uniquement (jamais de publication directe)**,
  anti-clickbait, preuves réelles, hooks re-dérivés. **Frontière stricte** : profil perso
  = `social-selling-linkedin` ; pages marque = ce plugin. Runbook
  `docs/RECETTE-COPYWRITER.md`. **Validation** : valider TOUT VALIDE (24 plugins) ;
  tester 0/0/0.

Plugins touchés : nouveau `rapido-copywriter` ; `rapidocms` 1.11.6→1.11.7,
`rapido-marketing` 0.18.2→0.18.3.

---

## rapido-lovable v2 — kit connecteur MCP + usine MVP (2026-07-15)

Upgrade majeur de `rapido-lovable` (1.1.0 → 1.5.0) : n'importe quel client demande
« connecte mon site au MCP FoodEatUp » → **toujours les mêmes prompts**, même sécurité,
même scope. Fondé sur le code de production `academyrapido` (canonisé, pas théorisé).

- **Audit LV0** : `docs/REFERENCE-AGENT-LOVABLE.md` canonise deux patterns de prod —
  `agent-chat` (RAG Supabase via passerelle Lovable) et **`execute-prompt`** (LE pattern
  MCP : API Anthropic + `mcp_servers` type url, beta `mcp-client-2025-04-04`, parsing par
  type). `docs/IMPORTS-LOVABLE-V2.md` : 4 dépôts (awesome-cursorrules CC0, VibeSec
  Apache-2.0, vibecode-pro-max MIT, lovable-prompt-builder MIT). **Découverte structurante**
  → `docs/OUTILS-MCP-MANQUANTS.md` §11 : **auth multi-tenant** (token par établissement)
  = prérequis produit **absolu** (les URLs MCP de prod sont globales, non scopées).
- **Kit v1** (`reference/kit-connecteur-mcp/`) : `_commun.md` (template edge function
  durci multi-tenant, 7 points sécurité, critères d'acceptation, versioning) + fiches
  `foodeatup`/`crm`/`cms`/`rh` (env immuables, familles d'outils, system prompt, scope).
  `regles-stack-lovable.md` (CC0), `gate-securite.md` (VibeSec adapté, bloquant).
- **2 skills** : `connecteur-mcp-lovable` (kit → prompts étagés P1-P5), `mvp-lovable`
  (spec-driven, série P1-P8). **Agent** `architecte-lovable`. Volet **workspace sync**
  (`sync-marque-lovable` pousse le kit en workspace skill versionné). Patchs
  `agent-ia-produit`/`usine-a-landing`/`site-restaurant` + `rapido-prompteur:prompt-lovable`.
- **Sécurité** : clés du **client** (jamais BraindCode), appels **serveur**, **scope
  injecté serveur**, **écritures confirmées** (symétrie hooks Claude Code), gate VibeSec.
  Runbook `docs/RECETTE-LOVABLE-V2.md` (GoSushi, établissement démo 2). **Validation** :
  valider TOUT VALIDE (23 plugins) ; tester 0/0/0.

Plugins touchés : `rapido-lovable` 1.1.0→1.5.0, `rapido-prompteur` 0.3.0→0.3.1.

---

## Usine à lead magnets (2026-07-15)

Nouveau plugin **`rapido-leadmagnet`** (23e) — l'**usine d'exécution** des lead magnets :
la conception reste à `rapido-marketing:lead-magnet-machine`, l'usine **fabrique →
capture → diffuse → organise en RH → mesure**, en orchestrant les skills existants.

- **Audit d'abord** (`docs/IMPORTS-LEADMAGNET.md`) : 5 dépôts **MIT** relus (verdicts +
  anti-verbatim ; GPL AI-eBook exclu) et **inventaire MCP réel** décisif — **pas de
  `create_formulaire`/`create_cta`** (lecture seule), `create_editor_template` supporte
  `landing_page` (formulaire intégré prouvé en prod), et **les agents IA sont de vrais
  users RH** (assignation directe). 3 décisions : **Route B Lovable** (landing+capture),
  **LinkedIn semi-auto**, **formulaire Lovable mode B**.
- **4 skills** : `fabrication-lead-magnet` (rédaction + **gate qualité** + PDF brandé
  `templates/lead-magnet.html` → bibliothèque CMS), `page-et-capture` (landing Lovable +
  segment `LM-{slug}` + pipeline + livraison + **test de bout en bout** + **RGPD
  bloquant**), `campagne-lead-magnet` (organique + Meta **PAUSED** + nurturing **gated** +
  mesure `scripts/stats_leadmagnet.py`), `projet-rh-lead-magnet` (~20 tâches **affectées
  aux agents IA** résolus dynamiquement). Agent **`chef-usine-leadmagnet`**.
- **Garde-fous** : hook `garde-budget-ads` (Meta PAUSED + coût max), RGPD/double opt-in,
  gate délivrabilité, LinkedIn semi-auto, `self_ai_disclosure`, **un seul LM en prod à la
  fois**. `NOTICE.md` (5 sources MIT francisées).
- **Ponts** `rapido-marketing` (`lead-magnet-machine` → l'usine exécute ; `machine-inbound`
  source de capture ; `lead-scoring` tag = signal d'engagement) + 3 outils au
  `docs/OUTILS-MCP-MANQUANTS.md`. Runbook `docs/RECETTE-LEADMAGNET.md` (checklist HACCP,
  **recette réelle déférée au client**). Livré **0.5.0** feature-complete (4 skills +
  1 agent) ; **1.0.0** après un run réel. **Validation** : valider TOUT VALIDE
  (23 plugins) ; tester 0/0/0.

Plugins touchés : nouveau `rapido-leadmagnet` ; `rapido-marketing` 0.18.1→0.18.2.

---

## Sourcing Google Maps → CRM (2026-07-15)

Nouveau plugin **`rapido-gmaps`** (22e) — le **chaînon manquant de la prospection** :
sourcer des leads depuis Google Maps (`gosom/google-maps-scraper`, MIT), les scorer,
dédupliquer et verser dans le pipeline RapidoCRM.

- **Audit d'abord** (`docs/AUDIT-GMAPS.md`) : chaîne technique **prouvée en session**
  (build natif Go, driver Playwright reconstruit, Chromium, moteur scrapemate) ; seul
  l'**egress navigateur vers Google Maps** est bloqué par le bac à sable → mesures de
  scrape réelles **déférées** au poste/VPS du client. Struct `Entry`, contrat API et
  mapping CRM **vérifiés sur source**.
- **4 skills** : `sourcing-gmaps` (requête → scrape → scoring → dédup → import confirmé),
  `enrichissement-fiches` (diff, jamais d'écrasement silencieux), `detection-opportunites`
  (ICP FoodEatUp, signal « sans système numérique »), `veille-concurrents-gmaps`. Agent
  **`chasseur-leads`**. **Scoring par script** `score_leads_gmaps.py`
  (`rating × ln(avis+1) × signal`).
- **Deux modes d'exécution** (Docker local **ou** API SaaS auto-hébergée), hook
  `garde-scraping` (volume + import en lot), CGU/RGPD (emails B2B + opt-out, plafonds,
  déduplication obligatoire). Routine **`GMAPS-HEBDO`** (n8n `recettes-gmaps.md` + registre
  unifié `GMAPS-*`). 3 outils au `docs/OUTILS-MCP-MANQUANTS.md`. Runbook
  `docs/RECETTE-GMAPS.md`. Livré **0.5.0** feature-complete. **Validation** : valider
  TOUT VALIDE ; tester 0/0/0.

Plugins touchés : nouveau `rapido-gmaps` ; `rapido-marketing` 0.18.0→0.18.1,
`rapido-n8n` 1.5.0→1.6.0.

---

## Commercial & relation client (2026-07-15)

Le pont **forge → opérations** : appliquer les méthodes (SONCAS, AARRR, BANT, NPS,
100 jours…) aux **données MCP réelles**, sans dupliquer les exercices forge ni les livres.

- **Pont forge → opérations** (`reference/pont-forge-operations.md`) : tout skill
  opérationnel **lit le livrable forge** correspondant ; 12 skills forge pointent vers
  leur skill opérationnel (tous existent désormais).
- **`rapidocrm` (1.7.0)** — vente terrain : `preparation-rdv` (SONCAS opérationnel),
  `qualification-deals` (BANT/MEDDIC, multi-threading), `coach-de-vente` (routeur
  multi-livres), `playbook-objections-vivant`, `funnel-aarrr-reel` (AARRR via catalogue-kpi).
- **`rapido-relation-client` (0.2.0)** — nouveau plugin (21e) : `pilotage-service-client`
  (SLA), `boucle-nps`, `sante-client` (health score script), `cent-premiers-jours`
  (100 jours), `segmentation-rfm`, `coach-relation-client` (routeur fidélité). Routines
  `RC-HEBDO`/`RC-NPS-TRIMESTRE`/`RC-SANTE-MENSUEL`.
- **`rapido-marketing` (0.18.0)** — `operations-influenceurs` (sourcing → brief → contrat
  → tracking → ROI), routine `MKT-INFLUENCE-MENSUEL`.
- **`catalogue-kpi`** enrichi (source unique) : taux **AARRR** (activation/rétention/
  referral), **NPS**, **ROI**, part organique/payante. Health score = script composite
  plugin-spécifique (documenté au registre des KPIs).
- La **boucle se ferme** : 100 premiers jours → NPS promoteur → ambassadeur → nouveaux
  leads → preparation-rdv → … **Validation** : valider TOUT VALIDE (21 plugins) ; tester 0/0/0.

Plugins touchés : nouveau `rapido-relation-client` ; `rapidocrm` 1.6.0→1.7.0,
`rapido-marketing` 0.17.0→0.18.0, `rapido-forge` 1.1.2→1.1.3, `rapido-startup`
1.9.1→1.9.3, `rapido-n8n` 1.4.0→1.5.0.

---

## Acquisition organique & payante (2026-07-15)

3 nouveaux plugins + intégration dans les boucles (SENSE enrichi, attribution étendue,
registre + recettes n8n) — **13 nouveaux skills, 4 routines**.

- **`rapido-seo` (0.1.0)** — acquisition **organique** : `audit-seo-technique`,
  `recherche-mots-cles` (≠ `geo-optimization`), `netlinking`, `performance-organique`
  (GSC+GA4), `tendances-marche`, **`pilotage-seo`** (sous-domaine organique de
  `pilotage-marketing`). Coûts DataForSEO gouvernés ; GA4/GSC read-only ; fraîcheur GSC dite.
- **`rapido-google-ads` (0.1.0)** — SEA **lecture seule** : `pilotage-performance-google-ads`,
  `recherche-mots-cles-sea`, `audit-compte-google-ads`, **`synergie-seo-sea`**. Analyse
  et recommande (exécution manuelle guidée).
- **`rapido-tiktok-ads` (0.1.0)** — **verrouillé argent réel** : `pilotage-performance-tiktok`,
  `lancement-campagne-tiktok` (100 % inactif), `tendances-creatives-tiktok`. Création
  active **refusée** (hook DENY).
- **Intégration** : `pilotage-marketing` SENSE (SEO/SEA/TikTok « si installé ») + ACT
  paid Meta/Google/TikTok ; `attribution-kpi-marketing` sources étendues + KPI « part
  organique vs payante » ; routines `SEO-HEBDO`/`SEO-MENSUEL`/`SEA-HEBDO`/`TIKTOK-HEBDO`
  + `rapido-n8n/reference/recettes-seo.md` (rank-tracking DataForSEO **en n8n**).
- Serveurs SEO/Ads **non encore connectés** → skills écrits d'après les grammaires
  documentées (pattern « construire d'abord », comme ElevenLabs E1) ; checklist d'accès
  dans chaque README. **Validation** : valider TOUT VALIDE (20 plugins) ; tester 0/0/0.

Plugins touchés : nouveaux `rapido-seo`/`rapido-google-ads`/`rapido-tiktok-ads` ;
`rapido-marketing` 0.16.3→0.17.0, `rapido-n8n` 1.3.0→1.4.0.

---

## Boucle de vente — loop-engineering (2026-07-15)

Complète le loop-engineering du marketplace **sans rien refonder** (loop-engine-v2,
pilotage-marketing, autonomie.md et hooks inchangés — tout s'y branche).

- **Registre unifié des routines** (`reference/registre-routines.md`) — catalogue
  canonique préfixé par domaine (`FIN-*`/`STARTUP-*`/`GROWTH-*`/`VIDEO-*`/`MKT-*`/
  `VENTE-*`/`OPS-*`) ; anciens noms `R4…R9`, `R-MKT-*` conservés en **alias**
  (rétrocompatibilité, aucun déclencheur cassé). **Registre des KPIs** : source unique
  des formules = `rapido-startup:catalogue-kpi`.
- **`rapidocrm:pilotage-commercial`** (`1.6.0`) — orchestrateur de la boucle
  commerciale (Sense→Plan→Act→Feed→Report), calculs délégués à `catalogue-kpi`.
  Routines **`VENTE-HYGIENE`** (hygiène /100), **`VENTE-RELANCES`** (relances
  quotidiennes, table `vente_relances_journal`), **`VENTE-REVUE`** (couverture).
- **`rapidocrm:expansion-clients`** + **`programme-ambassadeurs`** — tunnel
  Studio→Agence→SaaS + programme 10 %/20 %, routine **`VENTE-EXPANSION`**.
- **`rapido-n8n` (`1.3.0`)** — recettes événementielles **`OPS-LEAD-CHAUD`**,
  **`OPS-CLIENT-GAGNE`**, **`OPS-ALERTE-CHURN`** (tables mémoire obligatoires ;
  installées sur confirmation, aucun workflow créé d'office).
- **KPI anti-divergence** — `catalogue-kpi` décrété source des formules ;
  `attribution-kpi-marketing` réduit à ce qui lui est propre (attribution par canal,
  LTGP/ROI ≠ LTV), commentaires « source : catalogue-kpi ».
- Descriptions `marketplace.json` périmées corrigées (rapido-startup, rapido-marketing).
- **Validation** : `valider-plugins.py` TOUT VALIDE (17 plugins) ; `tester-skills.py`
  0 FAIL/0 WARN/0 INFO ; dry-run lecture seule « pilote mon commercial » →
  `get_stats_pipeline_global` OK (chaîne SENSE résolue, données réelles).

Plugins touchés : `rapidocrm` 1.4.3→1.6.0, `rapido-n8n` 1.2.0→1.3.0,
`rapido-marketing` 0.16.1→0.16.3, `rapido-startup` 1.9.0→1.9.1.

---

# Notes de release — v1.0.0 (2026-07-10)

## Ajout — rapido-forge 1.1.0 (2026-07-10)

Tags (taxonomie fermée à 12) + niveaux sur les 180 exercices, prérequis
(graphe validé sans cycle, CI), `catalogue.json` machine-readable,
recherche sémantique hors-ligne (TF-IDF stdlib, synonymes FR→EN) + skill
`selecteur-framework`, agents branchés sur le catalogue, et orchestrateur
`lancement-projet-360` côté rapido-suite (1.2.0) — Forge pense, les
plugins exécutent.

## Ajout — rapido-forge 1.0.0 (2026-07-10)

Nouveau plugin **rapido-forge** : la source StartupsForge (PrendsTaPart)
mise aux conventions Rapido — 180 exercices en 3 parcours (dont les
46 skills bootcamp enrichis d'une méthode pas à pas), ~146 renvois croisés
vérifiés vers les plugins métier, 4 agents mentors (directeur-programme +
3 mentors de parcours). Livrables consignés dans
`./rapido-kb/startup/forge/`, hooks garde-ecriture-kb et rappel
« argent réel » Meta Ads.

Première version publique de la **marketplace Rapido** : des plugins Claude
Code pour piloter une entreprise via les systèmes Rapido (FoodEatUp,
RapidoCRM, RapidoCMS, RapidoRh) et leurs outils satellites (Canva, Lovable,
Meta Ads, n8n, Google Workspace).

## En chiffres

- **11 plugins**, **119 skills**, **17 agents** (personas) — chiffres
  recomptés depuis les fichiers au moment du tag.
- **8 plugins avec hooks** déterministes — 13 scripts de garde testés
  fonctionnellement sur stdin, plus des hooks Stop (récapitulatif exigé) et
  SessionStart (détection de la KB).
- 40 des 119 skills importés de 4 dépôts open source, attribués et licenciés ;
  audit de vérité des 3 serveurs Rapido CLOS (100 % des outils couverts ou
  ignorés volontairement avec raison — reference/audit-tools-2026-07-10.md).
- 2 scripts de validation stdlib + une CI GitHub Actions qui les rejoue.

## Les 5 points forts

1. **Garde-fous déterministes** — indépendants du modèle : confirmation
   forcée sur le destructif et les dépenses réelles (Meta Ads), refus pur des
   patterns interdits (transitions de facture hors DGFiP, températures
   invraisemblables, budgets au-delà du plafond maison), mode production n8n
   verrouillé — y compris quand le paramètre est absent.
2. **Base de connaissance `./rapido-kb/`** — construite par l'onboarding dans
   le répertoire de travail du CLIENT (jamais dans les plugins) : seuils,
   charte, personas et ton PRIMENT partout sur les défauts secteur ; le dépôt
   reste un produit portable, sans aucune donnée client.
3. **Dossier startup 360** (`rapido-suite`) — la mémoire de l'entreprise en
   8 fichiers (vision, persona, marché, offre, identité, traction, pitch,
   roadmap) que tous les agents lisent avant de produire, avec chiffres
   sourcés MCP et publication CMS/RH.
4. **Skills tiers attribués** — 40 skills d'anthropics/knowledge-work-plugins,
   anthropics/skills, wondelai/skills et nextlevelbuilder : LICENSE dans
   chaque dossier, ATTRIBUTIONS.md par plugin, clé `source:` dans chaque
   frontmatter, descriptions francisées pour le déclenchement, corps
   originaux intacts.
5. **CI de validation** (`.github/workflows/validation.yml`) — à chaque push
   et pull request : validation structurelle, batterie de tests
   skills/agents/hooks (0 FAIL, 0 WARN exigés), compilation de tous les .py,
   `bash -n` de tous les .sh — sans aucune dépendance pip (100 % stdlib).

## Limites connues

- **`N8N_MCP_URL` requise** pour `rapido-n8n` et le volet automatisations de
  `rapido-direction` (URL du serveur MCP de votre instance n8n). Sans elle,
  dégradation propre. Les comptes tiers (Canva, Lovable, Meta Ads,
  HyperFrames, Google) s'authentifient via leurs connecteurs/OAuth.
- ~~Endpoints Google à confirmer~~ — **résolu en 1.0.1** : les URLs de
  `rapido-direction/.mcp.json` sont désormais celles de la documentation
  officielle Google Workspace MCP
  (`gmailmcp`/`calendarmcp`/`drivemcp.googleapis.com/mcp/v1`, vérifiées le
  2026-07-06). La doc Gmail confirme au passage le design « brouillons
  uniquement » du plugin : le serveur crée des drafts et labellise, il
  n'envoie pas.
- **67 outils MCP « à vérifier en ligne »** : les catalogues facebook-ads,
  n8n et Google vivent sur les serveurs distants — checklist manuelle avant
  usage intensif dans `tests/rapports/outils-a-verifier-en-ligne.md`.
- Le contenu des 40 skills tiers reste en anglais (seules leurs descriptions
  de déclenchement sont francisées).

## Contribuer

Conventions, structure d'un skill/plugin, principe anti-donnée-inventée et
validation obligatoire avant PR : voir [CONTRIBUTING.md](CONTRIBUTING.md).
Sécurité et signalement de vulnérabilité : [SECURITY.md](SECURITY.md).
Licence : [Apache 2.0](LICENSE).
