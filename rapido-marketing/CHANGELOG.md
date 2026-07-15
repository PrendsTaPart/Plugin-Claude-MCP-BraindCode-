# Changelog — plugin rapido-marketing

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
