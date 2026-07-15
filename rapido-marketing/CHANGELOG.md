# Changelog — plugin rapido-marketing

## 0.17.0 — 2026-07-15 — intégration acquisition (SEO/SEA/TikTok)

- `pilotage-marketing` : **SENSE enrichi** — SEO (`rapido-seo:pilotage-seo`), SEA
  (`rapido-google-ads`), TikTok (`rapido-tiktok-ads`), chacun « si installé, sinon
  sauté en le disant ». **ACT paid** route désormais Meta OU Google OU TikTok
  (arbitrage `directeur-marketing`). **Anti-collision** : `pilotage-seo` = sous-domaine
  organique (règle miroir).
- `attribution-kpi-marketing` : **sources étendues** (GA4 source/medium, GSC organique,
  Google Ads, TikTok) + KPI **« part organique vs payante du CA »** (registre des KPIs).
- `geo-optimization` : anti-collision explicite avec `rapido-seo:recherche-mots-cles`
  (GEO génératif vs search classique).

## 0.16.3 — 2026-07-15 — frontière KPI (anti-divergence)

- `attribution-kpi-marketing` : section **« Frontière KPI »** — `catalogue-kpi` est la
  source des formules ; le CAC par canal (`dépense/clients`) est **la même formule**,
  scopée par canal (pas concurrente). Ce qui est propre au skill : répartition par
  canal, modèle d'attribution, `LTGP`/`ROI` marketing (≠ LTV).
- `scripts/kpi_marketing.py` : commentaires **« source : catalogue-kpi »** sur le CAC
  et distinction explicite `LTGP` ≠ `LTV` (aucun changement de comportement).

## 0.16.2 — 2026-07-15 — anti-collision ambassadeurs

- **Patch croisé `rapidocrm`** : `lead-getters-systeme` gagne une section
  **anti-collision** avec `rapidocrm:programme-ambassadeurs` — lui choisit le **TYPE**
  de programme (stratégie), l'exécution du programme ambassadeurs BraindCode (10 %/20 %)
  revient à `rapidocrm:programme-ambassadeurs`. Règle miroir.

## 0.16.1 — 2026-07-15

- `tunnel-de-vente-360` (patch V5) : Acte 2 — **héros vidéo de landing monté
  localement (0 crédit)** via `rapido-video:montage-express` si les rushes existent ;
  génératif via `rapido-higgsfield` (coût confirmé).

## 0.16.0 — 2026-07-15

- **Croisements Higgsfield** (patch H9) : `tunnel-de-vente-360` Acte 2 (héros vidéo
  de landing) et Acte 4 (créatifs premium image/vidéo IA + `self_ai_disclosure OPT_IN`
  + gate viral) → `rapido-higgsfield` ; `machine-outbound` gagne l'option **vidéo
  d'outreach premium** pour les ~10 prospects les mieux scorés (coût confirmé). Tout
  conditionné à la présence du plugin.

## 0.15.0 — 2026-07-15

- Skill **`pilotage-marketing`** (orchestrateur) : boucle **Sense → Plan → Act →
  Feed → Report**, gouvernée par `rapido-suite/reference/autonomie.md` si présent,
  **sinon mode prudent** (tout écrit confirmé).
  - **SENSE** : `attribution-kpi-marketing`, `rapidocrm:coaching-pipeline`,
    `rapidocms:analyse-performance-contenu`, `rapido-meta-ads:pilotage-performance-ads`,
    `rapido-n8n:surveillance-automatisations`, `apprentissages.md`.
  - **PLAN** : `scripts/prioriser_actions.py` (ICE + allocation par machine +
    **détection de doublons** vs Kanban RapidoRH / interne, jamais de tête) ;
    règle de **coût IA** (`reference/cout-ia.md` : calcul→script, jugement→modèle,
    volume→routine n8n).
  - **ACT** : délégation aux agents M11 / skills, chaque action sensible confirmée.
  - **FEED** : capitalisation (`rapido-suite:mise-a-jour-kb`), **2 échecs → escalade
    humaine**, mise à jour du Kanban.
  - **REPORT** : une page (KPI vs objectifs, actions, décisions, prochaine
    itération, récap des IDs).
- **Routines n8n** (`reference/routines.md`, proposées puis installées sur
  confirmation via `rapido-n8n:usine-automatisations`) : **R-MKT-HEBDO** (rapport
  pilotage lundi), **R-MKT-QUOTIDIEN** (sentinelle leads > 24 h + soumissions
  orphelines), **R-MKT-MENSUEL** (board attribution + benchmarks) — chacune avec
  son workflow et sa table mémoire.
- **Anti-collision** : `pilotage-marketing` déclaré **sous-domaine** de
  `rapido-suite:pilotage-entreprise` (règle miroir dans les deux README).

## 0.14.2 — 2026-07-15

- **Fireflies devient un connecteur OPTIONNEL documenté, plus une dépendance.**
  - **Choix de format** : le format de plugin (`.mcp.json`) **ne supporte pas** de
    déclaration de serveur MCP « optionnel » — tout serveur listé est tenté à
    chaque session (une URL absente aurait produit une erreur de connexion). Donc
    **README uniquement** : l'entrée `fireflies` est **retirée de `.mcp.json`**.
  - `README.md` du plugin : section **« Connecteurs optionnels »** — MCP Fireflies,
    URL `https://api.fireflies.ai/mcp`, commande d'ajout Claude Code (transport
    HTTP), auth à la charge de l'utilisateur ; rappel : **aucune clé/secret dans le
    dépôt**. Variable `FIREFLIES_MCP_URL` supprimée (plus utilisée).
  - `sales-intelligence-fireflies` : **pré-check en Étape 0** — détection de
    l'absence des outils `fireflies_*` → message guidé (rôle du skill + commande
    d'ajout) puis **arrêt propre**, jamais d'erreur brute ni d'appel d'outil.
  - Éval **SIF-ABSENT** (Fireflies non connecté → message guidé, zéro appel).

## 0.14.1 — 2026-07-15

- `delivrabilite-email` : **paramètre de MODE** au contrat du skill.
  - **`outbound`** (défaut) : gate complet inchangé (scorecard + spam_check +
    plafonds + cadence/warmup).
  - **`newsletter`** (base opt-in) : scorecard d'hygiène (doublons/formats/rôle) +
    spam_check + **présence du lien de désinscription (bloquante)** + taille vs
    plafond ; **pas de règles de warmup/cadence**.
  - **Même seuil de refus, mêmes scripts** (aucune duplication) : `spam_check.py`
    gagne un contrôle `lien_desinscription` (détection stem FR/EN), exploité comme
    bloquant en mode newsletter ; `scorecard_liste.py` inchangé.
  - Prépare le câblage conditionnel côté `rapidocrm:campagne-marketing`.

## 0.14.0 — 2026-07-15

- `machine-outbound` **v2** (remplace le M8 initial) — deux intégrations nouvelles,
  pipeline inchangé sur le fond :
  - **GATE délivrabilité obligatoire (étape 3)** : `delivrabilite-email` sur CHAQUE
    lot (scorecard + spam_check + plafonds/cadence). **Lot refusé = pas d'envoi**,
    aucun contournement.
  - **Objections réelles → copy** : Étape 0 charge `objections.md` (produit par
    `sales-intelligence-fireflies`) ; les réponses aux objections fréquentes
    nourrissent les accroches des séquences.
  - **Priorisation** explicitée via `lead-scoring` 3 facteurs (fit × engagement ×
    fraîcheur) : les lots partent des mieux scorés.
  - Reste inchangé : sourcing CRM officiel + dédup, cadence J0/J3/J7/J14 rédigée
    par `rapidocrm:redaction-commerciale`, anti-doublon `rapido-n8n:memoire-operationnelle`,
    qualification `rapido-forge:scale-bant-qualification`, RDV
    `rapido-direction:secretariat-commercial`, mesure `stats_outbound.py` vs
    benchmarks, conformité RGPD non négociable (désinscription immédiate, pas
    d'achat de listes ni de scraping).
  - Évals machine-outbound portées à **4** (dont MO2 lot bloqué par le gate, MO3
    refus d'envoi sans confirmation).

## 0.13.0 — 2026-07-15

- `lead-scoring` **v2 — 3e facteur : fraîcheur du signal (intention)**. Modèle
  passé de 2 axes (fit × engagement) à **fit × engagement × fraîcheur** :
  - `reference/kb-templates/signaux.md` (nouveau) : catalogue de signaux
    **observables par NOS sources uniquement** (soumissions `get_formulaire_soumissions`,
    clics `list_cta`, réponses `get_interaction_stats`, mouvements `get_pipeline`/
    `get_historique_prospect`, actualité via `rapidocrm:account-research` : levée,
    recrutement, changement de poste) — chaque signal : source MCP, poids, **durée
    de validité**. Adapté de `docs/methodo/ops/signaux-intention.md` (gtm-flywheel,
    MIT ColdIQ).
  - `scripts/score_leads.py` : axe **intention** = `poids × fraîcheur`,
    `fraîcheur = max(0, 1 − âge/validité)` (signal périmé → 0 ; occurrence la plus
    récente par type — pas de double compte avec l'engagement) ; formule et
    fraîcheur affichées, jamais de score de tête.
  - `reference/kb-templates/scoring.md` : bloc `intention` (poids + validités) ajouté.
  - Sortie : **file de priorisation du jour** + 3 actions/tranche (chaud →
    `rapido-direction:secretariat-commercial` ; tiède → `machine-inbound` ; froid →
    `rapidocrm:campagne-marketing`) ; écritures CRM après confirmation.
  - Intent tiers (ZoomInfo/Bombora/6sense) = MCP manquant →
    `docs/OUTILS-MCP-MANQUANTS.md` (entrée 4).
- `icp-generator` : **inchangé** (déjà conforme — ICP = entreprise, analyse des
  clients gagnés via `analyse_clients.py`, `icp.md`, traduction prospection +
  `create_segment` après confirmation). Ce lot remplace le M5 initial.

## 0.12.0 — 2026-07-15

- Skill `delivrabilite-email` : **gate obligatoire avant tout lot d'envoi** +
  runbook incident. Exécution via RapidoCRM.
  - `scripts/scorecard_liste.py` (stdlib) : doublons, emails de rôle, formats
    invalides, diversité des titres, concentration de domaines, taille vs plafond
    → **note A-E + `refus`** si sous le seuil KB (formule affichée, jamais de tête).
  - `scripts/spam_check.py` (stdlib) : lexique à risque FR/EN, densité de liens,
    majuscules, promesses chiffrées → signalements + note de risque ; **réécriture
    déléguée** à `rapidocrm:redaction-commerciale` (pas de doublon).
  - `reference/kb-templates/delivrabilite.md` : plafond quotidien, calendrier de
    montée en charge (warmup), seuil de note minimale, règles de pause — copié
    dans `./rapido-kb/marketing/` à la 1re exécution.
  - **Invocation obligatoire** posée dans `machine-outbound` (avant tout lot ;
    câblage `rapidocrm:campagne-marketing` prévu M8-v2).
  - Suivi post-envoi sur ce que le serveur expose (`get_stats_campagne`) ;
    **bounces/plaintes fins non exposés** → consigné dans le nouveau
    `docs/OUTILS-MCP-MANQUANTS.md` (télémétrie délivrabilité, warmup/rotation,
    annulation d'envoi planifié) avec spec pour Tunis.
  - Adapté de `docs/methodo/ops/delivrabilite-email.md` + `cold-email-cadence.md`
    (coldoutboundskills, MIT GrowthEngineX).

## 0.11.0 — 2026-07-15

- Skill `sales-intelligence-fireflies` : pipeline qui transforme les transcripts
  de RDV réels (MCP Fireflies) en playbook d'objections chiffré + hooks de copy.
  - Schémas Fireflies vérifiés live (`fireflies_get_transcripts` filtré →
    `fireflies_get_summary`/`fireflies_get_transcript` par ID ;
    `fireflies_create_soundbite` startTime/endTime en secondes).
  - `scripts/mine_transcripts.py` (stdlib) : fréquence des objections par catégorie
    (prix/timing/concurrent/confiance/technique/autorité), questions récurrentes,
    verbatims horodatés **anonymisés** (fonction `anonymiser` : emails/tél/noms),
    patterns gagné vs perdu si l'issue CRM est connue — jamais de comptage de tête.
  - Articulation écrite : `rapido-forge:scale-objections-playbook` = FORMAT,
    `rapidocrm:mom-test` = grille de lecture (passé/concret) ; SOURCE de données,
    pas un doublon. Livrables → `objections.md` + hooks pour `redaction-commerciale`
    et `machine-outbound` ; leçons datées (≥2 occurrences) dans `apprentissages.md`.
  - Garde-fous : périmètre confirmé AVANT lecture ; transcript = donnée personnelle
    (KB interne) ; verbatims anonymisés, aucun nom publiable sans accord écrit ;
    write-backs (`log_activity`, `fireflies_create_soundbite`) confirmés un par un.
  - Adapté de `docs/methodo/ops/sales-intelligence.md` (gtm-flywheel, MIT ColdIQ).
- `.mcp.json` : serveur `fireflies` déclaré via `${FIREFLIES_MCP_URL}` (patron
  portable, comme n8n) ; mode dégradé si absent (import manuel + flag Tunis).

## 0.10.0 — 2026-07-14

- Couche mémoire sur les primitives EXISTANTES (rapido-kb + tables n8n), aucun
  nouveau système :
  - `reference/kb-templates/` : 6 modèles copiés dans `./rapido-kb/marketing/` à
    la 1re exécution (icp.md, scoring.md, offres.md, tunnels.md [registre à IDs],
    benchmarks.md [taux + sources], apprentissages.md [date | contexte | leçon |
    preuve | skill source]).
  - `reference/memoire.md` : mapping des 5 périmètres (longue durée = rapido-kb/
    marketing ; travail = session + projet RH Kanban ; projet = tunnels.md +
    projet RH ; client = fiches CRM source de vérité ; entreprise = rapido-kb/
    racine) + RAG en Étape 0 + mémoire d'exécution n8n (3 tables documentées :
    mkt_sequences_etat, mkt_relances_antidoublon, mkt_historique_envois).
  - Capitalisation AUTOMATIQUE encodée dans machine-inbound, machine-outbound,
    tunnel-de-vente-360, growth-experiments, attribution-kpi-marketing : Étape 0
    lit apprentissages.md + benchmarks.md AVANT tout plan (les leçons priment) ;
    à chaque clôture, 1-3 leçons datées et sourcées (chiffres du script) +
    mise à jour de benchmarks.md si un taux change.

## 0.9.0 — 2026-07-14

- Équipe marketing IA : 5 agents (frontmatter conforme au repo — name +
  description ; whitelist d'outils en section « Périmètre d'outils » comme les
  agents existants). Zéro doublon : ils DÉLÈGUENT aux rôles CRM/CMS/RH
  existants (directeur-commercial, responsable-marketing, community-manager,
  responsable-rh).
  - `directeur-marketing` : stratégie & arbitrage (OKR→KPI, choix acquisition,
    validation des plans, budgets — aucune activation sans confirmation),
    lecture seule, ne produit rien.
  - `inbound-manager` : pilote machine-inbound (SEO/GEO, blog, newsletter,
    social, lead magnets, landing) ; volet marque employeur avec responsable-rh.
  - `outbound-manager` : pilote machine-outbound (ICP, sourcing, séquences,
    qualification) ; délivrabilité + RGPD non négociables.
  - `funnel-builder` : exécute tunnel-de-vente-360 acte par acte, récap des IDs.
  - `growth-analyst` : growth + analytics, LECTURE SEULE, chiffres par script
    cités, propose sans activer.
- Section « Collaboration » commune (chaîne de saisine, handoff brief une page,
  escalade humaine après 2 échecs). tests/evals.md : 1 scénario par agent.

## 0.8.0 — 2026-07-14

- 2 skills « mesure » (comblent les derniers MANQUANT/PARTIEL M0) :
  - `attribution-kpi-marketing` : collecte multi-sources (CRM
    get_conversion_par_canal/get_dashboard_general_stats, CMS ingishts_campagne/
    post_insights, Meta pilotage-performance-ads), modèle d'attribution SIMPLE
    et honnête (premier/dernier point, limites documentées — pas de multi-touch
    inventé), CAC/LTV/ROI délégués à catalogue-kpi sinon scripts/kpi_marketing.py
    (stdlib) ; tableau par canal + 3 recos d'allocation ; benchmarks.md à jour.
  - `growth-experiments` : backlog scoré ICE (scripts/ice_score.py), protocole
    par expérience (hypothèse/métrique/échantillon/durée/arrêt), exécution
    déléguée (tests-ab-meta, landing CRM/Lovable, email-sequence), lecture des
    résultats par scripts/ab_result.py (test z 2 proportions → PASS/FAIL/
    INCONCLUSIF), leçons → apprentissages.md, renvois scale-ab-testing/
    scale-heatmaps.
- 3 scripts stdlib testés ; tests/evals.md : 2 déclenchements + 1 anti par skill.

## 0.7.0 — 2026-07-14

- Nouveau skill orchestrateur FLAGSHIP `tunnel-de-vente-360` : conçoit ET
  construit un tunnel de vente complet pour un produit, Rapido-first, en 5
  ACTES avec validation OBLIGATOIRE entre chaque (pattern lancement-projet-360).
  Acte 1 Stratégie (offre/value ladder via lead-magnet-machine/
  hundred-million-offers, icp-generator, funnel-tofu-mofu-bofu/
  storybrand-messaging → schéma dans tunnels.md) ; Acte 2 Pages
  (create_editor_template landing / usine-a-landing, formulaire + CTA trackés,
  visuels studio-visuel-marque) ; Acte 3 Séquences (email-sequence,
  devis-facture-relance, usine-automatisations/memoire-operationnelle, rien
  activé sans confirmation) ; Acte 4 Acquisition (machine-inbound/outbound,
  lancement-campagne-meta/pixel-et-retargeting, budget plafonné confirmé) ;
  Acte 5 Mesure (scripts/funnel_metrics.py : taux par passage + goulot,
  A/B via ideation-growth-experiments, apprentissages.md, registre tunnels.md
  avec IDs réels). Transversal : projet Kanban RapidoRH (setup-projet/
  flux-kanban), récap des IDs à chaque fin d'acte.
- scripts/funnel_metrics.py (stdlib) testé ; tests/evals.md : 4 scénarios
  (dont tunnel FoodEatUp en dry-run + activation confirmée + anti).

## 0.6.0 — 2026-07-14

- Nouveau skill orchestrateur `machine-outbound` : la chaîne outbound complète
  CRM-first, de l'ICP au RDV. S'appuie sur la méthodo `predictable-revenue`
  (référencée, non dupliquée). Sourcing via workflows CRM officiels
  (prospecter_*, rechercher_entreprise_siret) + dédup (rechercher_prospects) +
  enregistrer_tous_prospects validé ; enrichissement (account-research/
  draft-outreach) priorisé par lead-scoring ; séquences multi-touch
  J0/J3/J7/J14 (redaction-commerciale + schedule_email), volumes progressifs
  et plafond, CHAQUE lot confirmé (garde-envois), suivi deplacer_prospect_etape,
  mémoire anti-doublon via memoire-operationnelle (n8n) ; qualification
  scale-bant-qualification ; RDV secretariat-commercial ; mesure par
  scripts/stats_outbound.py (taux par séquence/segment vs benchmarks).
  Conformité RGPD encodée (consentement, désinscription immédiate, pas d'achat
  de listes ni scraping hors CRM). Modes dégradés sans n8n/envoi de masse.
- scripts/stats_outbound.py (stdlib) testé ; tests/evals.md : 3 scénarios
  (dont 1 refus d'envoi sans confirmation + 1 anti).

## 0.5.0 — 2026-07-14

- Nouveau skill orchestrateur `machine-inbound` : la chaîne inbound complète
  CMS-first, du contenu au RDV. 7 étapes, chacune avec outils MCP exacts,
  garde-fous, KPI et mode dégradé — 100 % en délégation (calendrier-editorial,
  generation-article-blog, geo-optimization, pipeline-contenu-social,
  orchestration-campagne, lead-magnet-machine, usine-a-landing/create_editor_
  template, usine-automatisations, email-sequence, lead-scoring,
  secretariat-commercial, setup-projet/flux-kanban). Étape 0 exige
  rapido-kb/marketing/icp.md (sinon icp-generator d'abord) ; aucun envoi/
  publication sans confirmation (hook garde-envois) ; chaque exécution
  alimente apprentissages.md (1-3 leçons datées). Mode dégradé sans Lovable :
  page de capture en voie 1 (create_editor_template landing_page).
- tests/evals.md : 3 scénarios (dont 1 mode dégradé sans Lovable + 1 anti).

## 0.4.0 — 2026-07-14

- 2 skills « visibilité » (comblent des MANQUANT/PARTIEL de la matrice M0) :
  - `social-selling-linkedin` : périmètre HONNÊTE — RapidoCMS publie sur les
    comptes connectés mais n'automatise pas les DM LinkedIn (pas de connecteur,
    M0). Produit stratégie de profil fondateur (ICP+KB), cadence de contenu
    perso déléguée à pipeline-contenu-social, scripts de connexion/DM PRÊTS À
    COPIER (jamais envoyés auto, conformité) personnalisés depuis le CRM
    (get_entreprise/account-research), suivi via enregistrer_prospect confirmé.
  - `geo-optimization` : checklist GEO déterministe sourcée d'etat-de-lart-2026
    (§8), audit d'un contenu via scripts/audit_geo.py (score 9 critères :
    réponse 40-60 mots, densité de faits, sources, schema, ancres, FAQ, auteur,
    style déclaratif, fraîcheur) → corrections proposées → mise à jour via les
    outils CMS après confirmation.
- 1 script stdlib (audit_geo.py) testé ; tests/evals.md : 2 déclenchements +
  1 anti par skill.

## 0.3.0 — 2026-07-14

- 2 skills « données » (comblent des MANQUANT de la matrice M0) :
  - `icp-generator` : profil d'ENTREPRISE cible (≠ persona → délégué à
    bootcamp-persona-deep/ideation-persona-maker) fondé sur l'analyse des
    clients gagnés (`analyse_clients.py`, stdlib — fréquences par secteur/
    taille/canal, jamais de tête), croisé KB → `rapido-kb/marketing/icp.md` +
    critères de prospection et `create_segment` (confirmé).
  - `lead-scoring` : modèle transparent 2 axes (fit ICP × engagement) éditable
    dans `rapido-kb/marketing/scoring.md`, calcul par `score_leads.py` (stdlib)
    sur données CRM réelles, tableau scoré + 3 actions par tranche (chaud → RDV
    via secretariat-commercial, tiède → nurturing, froid → réactivation) ;
    écriture CRM (étape/tâche) UNIQUEMENT après confirmation. Note M0 : pas de
    champ de score natif côté serveur (à demander au backend).
- 2 scripts stdlib testés ; tests/evals.md : 2 déclenchements + 1 anti par skill.

## 0.2.0 — 2026-07-14

- 4 skills **méthodo** (distillation de `docs/methodo/100m-leads/`, attribution
  Hormozi *$100M Leads* 2023, contenu reformulé, citations < 15 mots) :
  - `core-four-strategie` : choix de canal + cadence (règle des 100) + critère
    de maîtrise + scaling More Better New (fiches 01/03/05/08).
  - `lead-magnet-machine` : conception d'aimant à prospects en 7 étapes +
    nommage + distribution (fiche 02).
  - `money-math-acquisition` : LTGP:CAC + acquisition financée client, tout
    calcul délégué à `catalogue-kpi` (fiche 04).
  - `lead-getters-systeme` : parrainage/employés/agences/affiliés selon
    maturité (fiche 07).
- Chaque skill DÉLÈGUE l'exécution (skills existants nommés précisément ;
  exécuteurs transverses machine-inbound/outbound/tunnel-de-vente-360 à livrer)
  et liste ses cas d'usage croisés. tests/evals.md : 2 déclenchements +
  1 anti-déclenchement par skill.

## 0.1.0 — 2026-07-14

- Squelette du plugin **rapido-marketing** (slug immuable) : marketing &
  acquisition Rapido-first.
- `.mcp.json` : RapidoCRM/CMS/RH (prioritaires) + facebook-ads, canva, lovable,
  n8n, gmail, google-calendar (repli).
- `reference/priorite-mcp.md` : hiérarchie CRM > CMS > RH > secondaires, règle
  « voie Rapido d'abord, secondaire si capacité absente », mode dégradé
  (signaler, ne pas bloquer).
- `reference/garde-fous-marketing.md` : (a) tout envoi confirmé explicitement ;
  (b) RGPD (consentement avant séquence/audience, droit à l'effacement) ;
  (c) délivrabilité (volumes progressifs, désinscription, pas d'achat de listes
  ni de scraping hors CRM) ; (d) budgets pub plafonnés avant activation ;
  (e) score/KPI toujours par script stdlib, jamais de tête.
- `reference/pieges-outils.md` : pièges des outils marketing des 3 serveurs
  (repris de `docs/MATRICE-COUVERTURE.md`).
- `hooks/` : `garde-envois` (PreToolUse, confirmation FORCÉE sur send_email/
  send_sms/send_newsletter/lancer_campagne/schedule_email/schedule_sms,
  schedule_draft_tool/cancel_schedules_post, ads_activate_entity/boost/update)
  + Stop récap-actions (IDs + destinataires/date/coût sinon arrêt bloqué).
- README : table des skills prévus.
