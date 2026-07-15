# Recette réelle — rapido-lovable v2 (runbook)

Site de démo **GoSushi** avec agent embarqué connecté au MCP FoodEatUp.

> **Statut : à exécuter côté opérateur.** Cette recette crée un **projet Lovable réel**
> (crédits), pose des **secrets** et branche un agent sur le MCP FoodEatUp de
> l'**établissement DÉMO** (`establishment_id 2` — **jamais** le 26 de production). Elle
> n'est pas jouée dans l'environnement de build pour ne pas créer de projet ni dépenser
> sans accord. Ci-dessous le mode opératoire + la grille de relevé. Aucun résultat simulé.

## Prérequis

- MCP **Lovable** connecté ; **FoodEatUp** accessible ; **clé Anthropic du compte démo**.
- Kit v1 présent (`reference/kit-connecteur-mcp/`) ; gate sécurité (`reference/gate-securite.md`).

## Déroulé

| # | Étape | Skill | Attendu | À relever |
|---|---|---|---|---|
| a | **Spec + MVP** | `mvp-lovable` | Spec 3 pages (accueil, carte, contact) validée → série P1-P8 | URL projet · durée |
| b | **Agent embarqué** | `connecteur-mcp-lovable` | Prompts P1-P5 : secrets (`FOODEATUP_MCP_URL`, `FOODEATUP_ESTABLISHMENT_ID=2`, `ANTHROPIC_API_KEY` en env Lovable), edge function `agent-foodeatup` (scope serveur), chat UI (carte de confirmation) | IDs edge/UI · secrets posés (noms) |
| c | **Validation live** | — | « quels sont mes stocks bas ? » **répondu par l'agent via le MCP** ; une **écriture** (réservation test) **PROPOSÉE puis confirmée** dans l'UI ; **tentative de changer d'établissement → bloquée** | captures / logs |
| d | **Gate sécurité** | `gate-securite.md` | Checklist passée : secrets hors bundle, appels serveur only, écriture confirmée, scope non contournable, injection filtrée | verdict (vert/rouge) |
| e | **Workspace skill** | `sync-marque-lovable` | Kit poussé (« rapido-mcp-connect ») → un **2ᵉ projet** du workspace voit la méthode | vérif |

## Grille de relevé (à remplir à l'exécution)

| Étape | Durée | Coût réel | Frictions / écarts du kit | IDs / URLs |
|---|---|---|---|---|
| a Spec + MVP | | crédits Lovable | | |
| b Agent embarqué | | crédits Lovable + Anthropic | | |
| c Validation live | | tokens Anthropic | | |
| d Gate sécurité | | 0 | | |
| e Workspace skill | | 0 | | |

## Garde-fous rappelés

- **Établissement DÉMO uniquement** (`establishment_id 2`), jamais la prod (26).
- **Secrets en env Lovable** (jamais dans le code/prompt) ; clé du **compte démo**.
- **Écritures confirmées** dans l'UI ; **scope injecté serveur** (non contournable).
- **Gate sécurité vert** avant toute mise en ligne.

> Écarts du kit constatés à l'exécution → corriger les fiches
> `reference/kit-connecteur-mcp/` (incrémenter la version du kit) avant de généraliser
> aux sites clients. Isolation multi-tenant **dure** = dépend du token par établissement
> côté serveur (`docs/OUTILS-MCP-MANQUANTS.md` §11).
