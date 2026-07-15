# Changelog — plugin rapido-startup

## 1.9.2 — 2026-07-15 — KPIs AARRR au catalogue

- `catalogue-kpi/scripts/calcul_kpi.py` : ajout des taux **AARRR** au catalogue
  (`taux_activation`, `taux_retention`, `taux_referral`) + `part_organique` (part
  organique vs payante du CA) — pour que `rapidocrm:funnel-aarrr-reel` et
  `attribution-kpi-marketing` calculent **via le catalogue** (jamais en local).
  Formules affichées, testées.

## 1.9.1 — 2026-07-15 — catalogue-kpi source unique des formules

- `catalogue-kpi/SKILL.md` : section **« Source unique des formules »** — ce skill
  est la source de vérité des formules KPI ; tout autre skill reprend la formule
  d'ici (jamais de variante locale). Frontière explicite avec
  `attribution-kpi-marketing` (répartition par canal) et `money-math-acquisition`
  (cadrage, calculs délégués).
- **Registre des KPIs** ajouté au registre unifié racine `reference/registre-routines.md`
  (chaque KPI : formule canonique, script propriétaire, skills autorisés) + audit des
  seuils en dur (conclusion : occurrences ~toutes pédagogiques ou déjà KB-sourcées ;
  aucun seuil de décision opérationnel à déloger).

## 1.9.0 — 2026-07-11

- R7 CASH-SENTINEL précisé : la phase Plan intègre la **projection
  30/60/90 jours** via le skill `cash-flow-snapshot` (rapido-suite) s'il
  est installé — sinon runway seul, en le disant ; et il est désormais
  explicite que R7 ne prépare JAMAIS de relances (il recommande de lancer
  R4, qui les prépare).
- Point ouvert n8n de R7 (le `TODO` historique) RÉSOLU : la sentinelle existe en **workflow n8n
  autonome** (Schedule 08:00 → Stripe Balance → calcul runway → alerte
  webhook, silence au vert) — créé NON PUBLIÉ sur l'instance de
  référence ; recette portable et étapes d'activation dans
  `rapido-n8n/reference/recette-r7-cash-sentinel.md` (renvoi depuis la
  routine).

## 1.8.0 — 2026-07-11

- catalogue-kpi : nouvelle formule `taux_conversion_etape` (passés ÷
  entrés, appliquée étape par étape — vues → clics CTA → soumissions →
  prospects ; jamais bout en bout seul) — fonction + entrée FORMULES dans
  calcul_kpi.py, ligne dédiée dans formules-kpi.md, 2 tests unitaires
  (19 au total). Consommée par campagne-marketing (rapidocrm 1.4.0) et la
  routine R6.

## 1.7.0 — 2026-07-10

- Nouvelle routine `R9-VIDEO-FACTORY` (references/routines/) : l'épisode
  vidéo du jour — Sense (sujet du calendrier éditorial, marque cible +
  logos depuis les assets, perfs des épisodes précédents), Plan (brief +
  composition committée dans le DÉPÔT DE PRODUCTION — CONFIG
  `depot_production`, défaut `PrendsTaPart/Video`), Act niveau 1
  (fabrication déléguée à video-marketing ; RENDU payant et PUBLICATION =
  niveau 3, jamais automatiques), Feed (journal + registre de série
  videos-episodes.md), Report (chaîne brief → preview → rendu → publication
  + perf J+7). Déclencheurs dans le SKILL.md : « lance R9 »,
  « épisode du jour », « vidéo du jour » ; autonomie.md : ligne R9 ;
  évals mises à jour.
- R4/R7 : source PRIMAIRE des dépenses = skill `gestion-depenses`
  (rapidocrm 1.3.0) — complément resto inchangé.

## 1.6.1 — 2026-07-10

- Correction documentaire (audit) : pieges-outils — ligne
  `update_invoice_status` (FoodEatUp) : enum élargi vérifié serveur,
  transitions DGFiP validées PAR LE SERVEUR (ne pas pré-filtrer, tenter et
  relayer l'erreur ; hook garde-destructif en confirmation).

## 1.6.0 — 2026-07-10

- Routines Loop Engine — câblage des utilitaires (schémas vérifiés
  serveur) :
  - R4 CFO-WEEKLY : source dépenses `list_depenses` (CRM) confirmée (déjà
    en place) ; alerte 🔴/🟡 diffusée EN PLUS via `create_notification`
    FoodEatUp (`type` danger/warning) quand le vertical resto est actif ;
  - R7 CASH-SENTINEL : `list_depenses` (CRM, `periode: "month"`) explicité
    comme source unique des dépenses ; même diffusion d'alerte FoodEatUp —
    cadrée comme CANAL D'ALERTE (pas une action métier), jamais au vert ;
  - R6 GROWTH-LOOP : phase Sense enrichie du funnel complet formulaires +
    CTA (`list_formulaires`, `get_formulaire_soumissions` — vues, clics,
    taux de conversion —, `list_cta`) et des sondages en cours
    (`list_sondages`, `get_sondage_resultats`) ; le funnel se lit
    vues → clics → soumissions → leads.
- `reference/autonomie.md` : règle 7 — la notification FoodEatUp est un
  canal d'alerte autorisé en routine (R4, R7) uniquement pour un verdict
  🔴/🟡, type danger/warning, ID récapitulé ; tableaux R4/R7 mis à jour.
- tests/evals.md : éval 9 (nouveaux câblages) + non-régression (2
  scénarios existants rejoués).

## 1.5.0 — 2026-07-10

- Skill `loop-engine-v2` : moteur des routines R4-R8 — un fichier par
  routine (references/routines/) avec bloc CONFIG interchangeable en tête
  (pattern client-resellable), phases Sense → Plan → Act → Feed → Report,
  calculs délégués à catalogue-kpi, journal ./rapido-kb/startup/
  routines-journal.md, installation/planification des routines (Calendar).
- reference/autonomie.md : gouvernance des routines — 4 niveaux (lecture
  seule par défaut, préparation, écriture confirmée par système, externe
  jamais automatique), tableau par routine (R7 = alerte seulement),
  écriture Stripe interdite en routine.
- Agent `cfo-virtuel` : ne calcule jamais de tête (scripts + formules
  affichées), priorité des sources Stripe > CRM > FoodEatUp > CSV, données
  manquantes signalées jamais estimées, pas de conseil d'investissement.
- NOTE : les « parties 4 » du master plan (prompts des routines et section
  Gouvernance) n'ont pas été fournies (placeholders vides dans le brief) —
  contenus rédigés depuis la spec, à réconcilier si le master plan diverge.
- `TODO` : workflow n8n équivalent de R7 CASH-SENTINEL pour tourner SANS
  Claude (via le skill usine-automatisations, plugin rapido-n8n) — proposé,
  non implémenté : Schedule Trigger quotidien → HTTP Stripe Balance +
  factures CRM en retard → calcul runway (Code node, mêmes formules que
  calcul_kpi.py) → IF runway < seuil KB → notification (email/webhook),
  sinon journal seul.

## 1.4.0 — 2026-07-10

- Skill `plan-execution-startup` (routine R5 STARTUP-BUILDER) : du business
  plan aux tâches — WBS de référence ~105-120 tâches FR en 6 phases
  (juridique/admin, produit, go-to-market, finance dont dossiers BPI/CII/
  JEI/French Tech, RH, pilotage) avec dépendances et durées types ;
  adaptation au BP puis PRÉSENTATION avant toute écriture ; création
  RapidoRH (ordre setup-projet : projet → colonnes par phase → tâches),
  jalons Google Calendar (serveur ajouté au .mcp.json, dégradation propre),
  tâches commerciales CRM ; mapping tracé dans
  ./rapido-kb/startup/plan-execution.md ; récap des IDs par système ;
  relances = delta uniquement. Réutilise les skills existants par référence.

## 1.3.0 — 2026-07-10

- Skill `plan-financier-previsionnel` : modèle mois par mois sur 36 mois
  (clients avec churn composé, MRR, CA, COGS, salaires chargés ×1,45,
  marketing piloté par le CAC, coûts fixes, résultat, trésorerie cumulée) ;
  point mort, besoin de financement (creux de trésorerie max) ; 3 scénarios
  base / upside (+20 % croissance) / downside (churn +2 pts, CAC +30 %) ;
  matrice de sensibilité churn × CAC ; sortie CSV + PREVISIONNEL.md dans
  ./rapido-kb/startup/business-plan/previsionnel/. Rappels : pas de conseil
  d'investissement, scénarios ≠ promesses, document vivant.
- Hook PreToolUse `garde-projection-realiste` (+ mêmes contrôles dans le
  script) : REJET churn = 0 ; REJET croissance > 30 %/mois au-delà du mois 6
  sans justification_croissance recopiée d'hypotheses.md.
- 14 tests unitaires (tests/test_previsionnel.py) ; interview-business-plan
  référence désormais le skill réel (plus « à venir »).

## 1.2.0 — 2026-07-10

- Skill `catalogue-kpi` : 22 KPI avec formule exacte, outils MCP par KPI,
  fréquence, seuil (KB prioritaire sinon seuils-defaut) et pièges (churn
  annuel COMPOSÉ jamais ×12, centimes Stripe, contrat annuel = MRR/12) ;
  règle absolue « le script calcule, pas le modèle » — collecte MCP → JSON
  d'entrées → scripts/calcul_kpi.py → formule TOUJOURS affichée.
- scripts/calcul_kpi.py (stdlib, fonctions pures + CLI JSON) : sortie
  {kpi, valeur, formule_appliquee, entrees, seuil, statut} ; seuils par
  défaut embarqués, seuil maison prioritaire. 17 tests unitaires
  (tests/test_calcul_kpi.py), dont l'exemple de référence LTV 1584.
- Hook Stop `garde-calcul-script` : bloque toute réponse annonçant un KPI
  chiffré sans exécution de calcul_kpi.py dans le tour (« KPI sans
  script ») — testé sur transcripts simulés, fail-open.
- NOTE : la « Partie 3 » du master plan (placeholder non fourni dans le
  brief) — catalogue construit depuis la spec et l'exemple de référence,
  à réconcilier si le master plan diverge.

## 1.1.0 — 2026-07-10

- Skill `interview-business-plan` : interview en 9 phases (executive summary
  rempli en dernier, entreprise/équipe, problème/PVU, marché TAM/SAM/SOM en
  bottom-up — refus du « 1 % du marché » —, concurrence, BMC 9 blocs,
  go-to-market/traction, plan opérationnel, plan financier) ; une question à
  la fois, Mom Test, relances sur réponses faibles ; hypothèses sourcées et
  datées dans ./rapido-kb/startup/business-plan/hypotheses.md ; sortie en
  9 fichiers + BUSINESS-PLAN.md (section risques obligatoire) ; annexes
  questionnaire-9-phases.md (≈80 questions avec objectif/signal faible/
  relance), frameworks.md (BMC, Lean Canvas, TAM/SAM/SOM, SWOT, 5 questions
  investisseurs), template-bp.md.
- Agent `coach-startup` : coach d'incubateur exigeant mais bienveillant —
  Mom Test permanent, interdit des projections non sourcées, contexte chargé
  depuis ./rapido-kb/ (jamais reposé), lecture seule pendant le coaching.
- tests/evals.md : scénarios de déclenchement et de comportement (routage,
  KB, refus du top-down, sortie, agent).

## 1.0.0 — 2026-07-10

- Squelette initial : `.mcp.json` (serveur Stripe officiel https://mcp.stripe.com
  + les 4 serveurs Rapido), références `directives-outils.md`,
  `pieges-outils.md` (pièges communs multi-serveurs + Stripe lecture seule,
  montants en centimes, format `post_heure`) et `seuils-defaut.md`
  (benchmarks finance/startup, utilisés SEULEMENT si absents de
  `./rapido-kb/`), hook déterministe `garde-stripe-write` (confirmation
  forcée sur toute écriture Stripe). Dossiers `agents/`, `skills/` et
  `tests/` prêts — skills à venir.
