# Changelog — plugin rapido-marketing

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
