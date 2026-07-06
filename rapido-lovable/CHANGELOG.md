# Changelog — plugin rapido-lovable

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (lovable + foodeatup + rapidocms + rapidocrm
  + rapidorh).
- Références : `architecture-lovable.md` (mode A build-time connecteurs via
  dashboard ; mode B runtime API Anthropic /v1/messages + mcp_servers, blocs
  parsés par type, clé API côté serveur ; pièges : enable_database avant
  query_database, query_database = production, set_*_knowledge remplace tout,
  crédits via get_workspace, plan_mode, deploy = URL publique),
  `directives-outils.md` (IDs, KB, confirmations, crédits).
- Skills : `site-restaurant` (contenu réel FoodEatUp, résa mode B
  availability→create, QR carte digitale), `usine-a-landing` (campagne CRM +
  KB, formulaire → prospect mode B, boucle analytics↔stats campagne),
  `agent-ia-produit` (rôle, system prompt dérivé des personas/KB, plan mode,
  autonomie héritée : lecture libre / écriture confirmée, tests guidés avant
  deploy), `sync-marque-lovable` (KB → workspace knowledge fusionné + skill
  charte-<société>).
