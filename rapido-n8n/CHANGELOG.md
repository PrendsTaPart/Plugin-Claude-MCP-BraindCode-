# Changelog — plugin rapido-n8n

## 0.1.0 — 2026-07-06

- Version initiale — plugin GÉNÉRALISTE : chaque client connecte SA propre
  instance n8n via la variable d'environnement N8N_MCP_URL (aucune URL en
  dur). `.mcp.json` : n8n + les 4 serveurs Rapido.
- `README-installation.md` : trouver l'URL MCP de son instance (cloud/self-
  hosted), export N8N_MCP_URL, vérification par search_workflows, credentials
  dans l'UI de l'instance.
- Références : `pieges-n8n.md` (cycle de fabrication get_sdk_reference →
  search_nodes/get_node_types avec discriminants → get_suggested_nodes →
  validate_workflow → pin data réaliste en {"json": {...}} → test_workflow →
  publish confirmé ; execute_workflow rend un ID immédiat, executionMode
  ABSENT = production ; credentials UI uniquement ; deux sens d'intégration
  Rapido HTTP/webhook), `directives-outils.md` (règle de routage ponctuel =
  Claude / récurrent = workflow, registre KB).
- Hooks testés (6 cas) : `garde-production.py` (ask sur publish/unpublish/
  archive et execute_workflow en production — y compris executionMode
  absent ; manual explicite libre), SessionStart vérifiant N8N_MCP_URL
  (message guidé si absente), Stop avec statut draft/PUBLIÉ + registre.
- Skills : `usine-automatisations` (cycle complet + registre KB),
  `recettes-metier` (relance-devis, alerte-stock, rappel-haccp, lead-entrant,
  recap-hebdo, anniversaires-clients — envois externes en brouillon tant que
  la KB n'autorise pas l'envoi direct), `surveillance-automatisations`
  (actifs, taux de succès, diagnostic des échecs 7 j),
  `memoire-operationnelle` (tables de données : une table = un usage
  documenté, pattern anti-doublon).
