# Changelog — plugin rapido-n8n

## 1.4.0 — 2026-07-15 — recettes d'acquisition (SEO/SEA/TikTok)

- `reference/recettes-seo.md` : **4 recettes** — **SEO-HEBDO** (positions GSC +
  striking distance, table `seo_positions_journal`), **SEO-MENSUEL** (backlinks
  new/lost + audit delta, `seo_backlinks_journal`), **SEA-HEBDO** (gaspillage +
  synergie SEO/SEA, `sea_synergie_journal`), **TIKTOK-HEBDO** (perf + arbitrage,
  `tiktok_perf_journal`). Le **rank-tracking DataForSEO vit en n8n** (coût gouverné),
  jamais en conversationnel.
- `recettes-metier/SKILL.md` référence `recettes-seo.md` ; recettes au registre unifié
  (`SEO-*`/`SEA-*`/`TIKTOK-*`). Installation sur confirmation, aucun workflow d'office.

## 1.3.0 — 2026-07-15 — recettes de vente événementielles

- `reference/recettes-vente.md` : **3 recettes OPS-*** au format des routines
  marketing (déclencheur, pseudo-nœuds, table mémoire, garde-fous) —
  **OPS-LEAD-CHAUD** (webhook lead chaud → pipeline Qualifié + créneaux Calendar +
  brouillon Gmail, jamais de réponse directe ; table `ops_leads_chauds`),
  **OPS-CLIENT-GAGNE** (devis accepté → deal gagné + acompte + projet RapidoRH +
  kick-off + bienvenue + relance ambassadeur J+60 ; table `ops_onboardings`),
  **OPS-ALERTE-CHURN** (hebdo → clients inactifs 30 j, alerte interne priorisée +
  plan de sauvetage ; table `ops_churn_alertes`).
- `recettes-metier/SKILL.md` référence `recettes-vente.md` ; les 3 recettes sont
  enregistrées au **registre unifié** (préfixe `OPS-*`).
- **Aucun workflow créé sur l'instance** : recettes installables, installation
  recette par recette sur confirmation via `usine-automatisations`. Toute action
  visible reste en brouillon ; pas de table mémoire = pas d'installation.

## 1.2.0 — 2026-07-11

- Nouvelle référence `reference/recette-r7-cash-sentinel.md` : la routine
  R7 du Loop Engine (rapido-startup) en workflow n8n autonome — 6 nodes
  (Schedule 08:00 → Stripe Balance en credential Bearer → Code calcul
  runway avec CONFIG en tête → If → alerte webhook / NoOp), activation en
  5 étapes côté client (credential restreinte lecture Balance, JAMAIS de
  clé en clair, test_workflow puis publication confirmée), limites
  assumées. Renvoi ajouté dans le skill `recettes-metier`.

## 1.1.0 — 2026-07-10

- Premier agent du plugin : `architecte-automatisations` — qualifie ce qui
  mérite d'être automatisé (et dit quand NE PAS automatiser), réutilise
  (recettes-metier, search_workflows) avant de construire, impose
  validate_workflow avant création et test_workflow avant publication,
  production sous confirmation (hook garde-production), surveille le parc
  et décide réparer/pause/retirer. tests/evals.md créé.

## 1.0.0 — 2026-07-06

- Première version publique.

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
