# Méthode — audit MCP ↔ plugin

Les serveurs MCP évoluent (Tunis), les plugins doivent suivre. Un **outil serveur
sans skill** = valeur dormante ; un **skill citant un outil disparu ou modifié** =
bug silencieux. Ce harnais croise les deux, en une commande, de façon reproductible.

## 1. Lancer un audit

**a. Inventaire serveur** (introspection — le harnais ne devine rien). Générer/mettre
à jour `docs/inventaires/{serveur}-tools.json` en listant les outils réellement
exposés par le MCP **connecté** (nom + description + paramètres). Contrat du fichier :

```json
{
  "server": "foodeatup",
  "date": "2026-07-15",
  "source": "introspection du MCP connecté (session Claude Code)",
  "tool_count": 111,
  "tools": [
    { "name": "create_reservation",
      "description": "Crée une réservation de table…",
      "params_required": ["establishment_id", "customer_name", "party_size", "date", "time"],
      "params_optional": ["customer_email", "table_id", "zone"] }
  ]
}
```

> Générer l'inventaire par lots via l'introspection des schémas d'outils (nom exact,
> `required`, propriétés). Garder le fichier **courant** sous
> `{serveur}-tools.json` ; pour comparer un delta, conserver l'ancien et le passer en
> `--prev` (ou archiver `{serveur}-tools-{date}.json`).

> ⚠️ **Le registre d'outils de la session (ce que voit `ToolSearch`) peut être TRONQUÉ**
> et ne pas refléter tout ce que le serveur expose (constaté sur FoodEatUp : 111 vus en
> session vs **164** réels). **Toujours recroiser** le nombre et la liste avec la
> **console d'autorisations MCP du serveur** (ou sa doc). Un outil connu du serveur mais
> absent de la session se note dans l'inventaire avec `schema_introspected:false`
> (nom fiable, paramètres à introspecter plus tard) — il n'est jamais « inventé ».

**b. Croisement** :

```
python3 scripts/audit_mcp_plugin.py <serveur> ./<plugin> [--prev docs/inventaires/ancien.json]
# ex. : python3 scripts/audit_mcp_plugin.py foodeatup ./foodeatup
```

Écrit `docs/audits/AUDIT-{serveur}-{date}.md` (daté, idempotent, comparable).

## 2. Lire le rapport

| Section | Ce qu'elle dit |
|---|---|
| **En-tête** | couverture `n/N` outils exploités, nb d'orphelins, nb de références mortes |
| **1. Références mortes** | identifiants à **verbe d'action** cités par le plugin, absents de **tout** inventaire connu → drift probable. Une ⚠️ signale les serveurs secondaires déclarés (`.mcp.json`) **pas encore inventoriés** : un identifiant listé peut en venir |
| **1bis. Citations cross-serveur** | outils d'autres serveurs déclarés que le plugin appelle légitimement (attribués via leurs inventaires) — **rien à faire** |
| **2. Orphelins** | outils exposés cités par **aucun** skill, groupés par famille — la valeur dormante |
| **3. Couverture** | par skill, les outils serveur qu'il cite |
| **4. Delta paramètres** | params requis **apparus/disparus** depuis l'inventaire `--prev` |

## 3. Règle de décision

- **Référence morte** → **correctif immédiat** du skill (PRIORITÉ 1), c'est un bug.
  **Avant de corriger** : vérifier qu'elle ne provient pas d'un **serveur secondaire
  non encore inventorié** (⚠️). Auditer ce serveur lève le doute — s'il expose l'outil,
  c'est une citation cross-serveur légitime, pas un drift.
- **Citations cross-serveur** → légitimes, aucune action.
- **Orphelins** → **valeur dormante**. Ne PAS créer de skill d'office : produire un
  **plan d'intégration** (`docs/PLAN-{SERVEUR}-V2.md`) groupé par famille, **validé par
  Mo** avant exécution. Tout ne mérite pas un skill (outils trop dangereux ou sans cas
  d'usage → listés « non couverts » avec justification).
- **Delta paramètres** → **patch des skills concernés** : un `params_required` **apparu**
  casse les appels existants (à corriger en priorité) ; un param disparu = nettoyage.

## 4. Le cycle « release MCP → audit » (routine)

À chaque annonce de livraison MCP côté Tunis : régénérer l'inventaire du serveur
concerné, relancer le harnais avec `--prev` (l'ancien inventaire) pour le delta, et
appliquer la règle de décision. Le **plan** ne se rejoue que s'il apparaît de nouveaux
orphelins. Consolidation et rappel périodique : voir la série SYNC (S5).

> **Précision du harnais.** Les « références mortes » excluent les **paramètres**
> (seuls les tokens à verbe d'action sont retenus) et les **outils d'autres serveurs**
> déjà inventoriés (reclassés en cross-serveur). Plus il y a d'inventaires construits,
> plus la détection est précise : réauditer un plugin après avoir inventorié ses
> serveurs secondaires nettoie automatiquement ses faux positifs.
