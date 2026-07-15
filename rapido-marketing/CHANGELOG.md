# Changelog — plugin rapido-marketing

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
