# Architecture Lovable × Rapido — référence OBLIGATOIRE

À charger avant tout usage des outils Lovable. Deux modes de croisement entre
les apps Lovable et les serveurs MCP Rapido — bien choisir, ils ne font pas la
même chose.

## MODE A — Build-time : les MCP Rapido comme CONNECTEURS de construction

L'agent Lovable utilise les MCP Rapido PENDANT la construction pour lire les
données réelles (plats, prix, offres) et produire une UI juste — mais l'app
finale n'appelle PAS les MCP à l'exécution.

- Les connecteurs s'ajoutent UNIQUEMENT via le dashboard Lovable :
  `add_connector` ne fait que renvoyer l'URL du dashboard (deep link) —
  l'UTILISATEUR clique et connecte lui-même. Ne jamais prétendre avoir ajouté
  un connecteur programmatiquement.
- Parcours : `list_available_connectors` (IDs du catalogue) → `add_connector`
  (`connector_id`) → transmettre l'URL à l'utilisateur → vérifier avec
  `list_connections` une fois qu'il a confirmé.
- Usage type : « construis la page menu avec MES plats réels » — l'agent
  Lovable lit FoodEatUp au build et fige le contenu (ou le charge depuis la
  base du projet).

## MODE B — Runtime : l'app déployée appelle l'API Anthropic avec mcp_servers

C'est ainsi qu'un agent IA EMBARQUÉ dans l'app agit vraiment (créer une
réservation, un prospect…) : l'app appelle `POST /v1/messages` de l'API
Anthropic avec le paramètre `mcp_servers` pointant vers les MCP Rapido (URLs
publiques).

Squelette à faire générer par Lovable (edge function) :

```
POST https://api.anthropic.com/v1/messages
headers: x-api-key: <clé côté serveur>, anthropic-version: 2023-06-01,
         anthropic-beta: mcp-client-2025-04-04
body: {
  model, max_tokens, system: <prompt de l'agent>,
  messages: [...],
  mcp_servers: [
    {"type": "url", "url": "https://foodeatup.com/api/mcp", "name": "foodeatup"},
    {"type": "url", "url": "https://crm.rapidosoftware.com/mcp", "name": "rapidocrm"}
  ]
}
```

Règles NON NÉGOCIABLES du code généré :
- **Parser les blocs de réponse par TYPE** (`mcp_tool_use`, `mcp_tool_result`,
  `text`), JAMAIS par position (`content[0]` est un bug : l'ordre varie selon
  les tours d'outils).
- **Clé API côté SERVEUR uniquement** (edge function + variable
  d'environnement/secret) — jamais en clair côté client, jamais committée.
- Boucle de conversation gérée côté serveur (renvoyer l'historique complet à
  chaque tour) ; timeouts et erreurs API affichés proprement à l'utilisateur
  final.
- N'exposer à l'agent embarqué QUE les serveurs MCP nécessaires à son rôle.

## PIÈGES Lovable (schémas vérifiés)

| Outil | Piège | Parade |
|---|---|---|
| `enable_database` | 30-60 s de provisioning, UNE seule fois | `get_database_status` d'abord ; activer avant tout `query_database` |
| `query_database` | écrit en PRODUCTION (INSERT/UPDATE/DELETE/DDL permanents) | préférer SELECT ; toute écriture = confirmation explicite de l'utilisateur |
| `set_workspace_knowledge` / `set_project_knowledge` | REMPLACE tout le contenu (max 10 000 caractères) | TOUJOURS `get_*_knowledge` avant, fusionner, puis set |
| `get_workspace` | — | vérifier les CRÉDITS avant un gros chantier (create_project + itérations consomment les crédits du workspace) |
| `send_message` | chaque message consomme des crédits ; l'agent code directement | `plan_mode: true` pour discuter l'architecture AVANT de coder (pas d'édition de code en plan mode) |
| `deploy_project` | publie une URL PUBLIQUE (lovable.app) | confirmation niveau 2 : récapituler ce qui devient public avant l'appel |
| `create_project` | `workspace_id` requis si plusieurs workspaces (sinon renvoie `available_workspaces`) | choisir/demander le workspace, rappeler avec `workspace_id` |
| `get_project_analytics` | `start_date`/`end_date` REQUIS au format RFC 3339 (ex. 2026-07-01T00:00:00Z) | convertir la période avant l'appel |
| `create_workspace_skill` | réservé aux admins/owners ; frontmatter `name` = `skill_name` | vérifier le rôle ; frontmatter valide |

## Règle générale

Un `initial_message` / `send_message` DÉTAILLÉ vaut dix itérations : contenu
réel (données MCP), palette hex exacte (KB), structure de pages, contraintes
(mobile-first, accessibilité). L'agent Lovable ne connaît ni la KB ni les MCP
Rapido par défaut — tout ce qui doit être respecté doit être DANS le message
(ou dans le knowledge du workspace — voir skill sync-marque-lovable).

## LE KIT CONNECTEUR MCP — source canonique (v2)

Le **Mode B/C (agent embarqué connecté à un MCP)** ne se réimprovise plus : il est
**canonisé** dans `reference/kit-connecteur-mcp/` (v1) — une fiche par MCP (`foodeatup`,
`crm`, `cms`, `rh`) + `_commun.md` (template d'edge function, system prompt, spec UI,
critères d'acceptation, **7 points sécurité**, versioning). Fondé sur le code de
production `academyrapido:execute-prompt` (`docs/REFERENCE-AGENT-LOVABLE.md`).

- **Toujours** partir du kit pour brancher un MCP (skill `connecteur-mcp-lovable`, LV2) :
  variables d'env **immuables**, appel **serveur** Anthropic + `mcp_servers` type url,
  parsing **par type**, **scope injecté serveur**, **écritures confirmées**.
- **Règles de stack** (`reference/regles-stack-lovable.md`, CC0) injectées dans chaque
  prompt ; **gate sécurité** (`reference/gate-securite.md`, VibeSec adapté) **bloquant**
  avant livraison.
- ⚠️ **Multi-tenant** : le kit est écrit prêt (`<MCP>_MCP_TOKEN`, `SCOPE_ID`) mais
  l'isolation dure dépend de l'auth par tenant côté serveur Rapido
  (`docs/OUTILS-MCP-MANQUANTS.md` §11). Ne jamais promettre l'isolation tant que le token
  par établissement n'est pas livré.
- Distribution en 3 endroits synchronisés (repo → workspace skill Lovable → knowledge
  projet), versionnée (LV4).
