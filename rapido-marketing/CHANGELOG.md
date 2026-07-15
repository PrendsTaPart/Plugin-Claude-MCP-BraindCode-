# Changelog — plugin rapido-marketing

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
