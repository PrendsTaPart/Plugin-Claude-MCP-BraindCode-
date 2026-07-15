---
name: agent-ia-produit
description: Utiliser quand l'utilisateur veut créer un agent IA, un chatbot pour ses clients ou un assistant connecté à ses données. Construit dans Lovable une app de chat dont l'agent embarqué appelle l'API Anthropic avec les MCP Rapido (mode B) — il agit vraiment (réservations, prospects…).
---

# Agent IA produit (Lovable × API Anthropic × MCP Rapido)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/architecture-lovable.md` (mode B en entier).
KB : `ton-et-accroches.md` (voix de l'agent), `produits-services.md` et
`propositions-valeur.md` (ce que l'agent sait), `processus-internes.md`
(limites, seuils).

## Workflow

1. **Définir le RÔLE de l'agent** — un agent = un métier :
   - réservation restaurant → MCP foodeatup (`reservation_availability`,
     `create_reservation`, `list_dishes` pour répondre sur la carte) ;
   - SAV / questions clients → lecture seule sur les serveurs concernés ;
   - qualification commerciale → MCP rapidocrm (`create_contact`,
     `ajouter_prospect_pipeline`, `create_rdv`).
   N'exposer à l'agent QUE les serveurs de son rôle (principe du moindre
   privilège).
2. **Écrire le SYSTEM PROMPT de l'agent** — dérivé des personas du plugin
   concerné et de la KB : ton et vocabulaire (`ton-et-accroches.md`), offres
   et prix (`produits-services.md`), limites (`processus-internes.md` : ce que
   l'agent ne promet pas, quand il passe la main à un humain). Y encoder les
   niveaux d'autonomie : LECTURE libre ; toute ÉCRITURE (réservation, prospect,
   RDV) = récapitulatif + confirmation de l'utilisateur FINAL avant l'appel.
   Faire valider ce prompt par l'utilisateur — c'est le contrat de l'agent.
3. **Valider l'architecture en PLAN MODE** — `get_workspace` (crédits) puis
   `create_project` (UI de chat minimale) et `send_message` avec
   `plan_mode: true` : discuter l'architecture SANS coder — edge function
   `/chat` (historique complet renvoyé à chaque tour, streaming éventuel),
   secrets (clé API Anthropic en variable serveur), `mcp_servers` limités au
   rôle, parsing par TYPE de bloc. Ne passer au code qu'après accord.
4. **Construire** — `send_message` (sans plan mode) pour implémenter :
   - UI de chat (historique, indicateur de frappe, erreurs propres) ;
   - edge function appelant `POST /v1/messages` (header
     `anthropic-beta: mcp-client-2025-04-04`, `mcp_servers` = URLs publiques
     des MCP du rôle, `system` = le prompt validé) ;
   - RÈGLES NON NÉGOCIABLES (architecture-lovable.md) : blocs parsés par TYPE
     (`mcp_tool_use` / `mcp_tool_result` / `text`), jamais par position ; clé
     API jamais côté client ; jamais de données personnelles en dur.
5. **Tests guidés** — dérouler avec l'utilisateur sur la preview :
   - le cas nominal du rôle (ex. réserver une table → l'agent vérifie la
     disponibilité PUIS demande confirmation PUIS crée) ;
   - un cas de refus (demande hors rôle → l'agent décline et redirige) ;
   - un cas d'erreur (MCP indisponible → message propre, pas de crash).
6. **Déployer** — `deploy_project` (confirmation niveau 2 : l'agent devient
   public et agit sur les vrais systèmes). Transmettre l'URL + rappeler la
   surveillance (`get_project_analytics`, et les objets créés visibles dans
   les serveurs Rapido).

## Garde-fous

- L'agent embarqué HÉRITE des niveaux d'autonomie de la marketplace : lecture
  libre, écriture = confirmation de l'utilisateur final, jamais d'action
  destructrice exposée (pas de delete_* dans son rôle).
- Un agent qui écrit dans les systèmes réels se déploie APRÈS les tests
  guidés, jamais avant.
- Pas de données personnelles en dur dans le code, le prompt ou les exemples ;
  le system prompt ne contient pas de secrets.

## Kit connecteur MCP (source canonique, v2)

Le branchement MCP (edge function, secrets, scope, écritures confirmées) suit désormais
**le kit** `reference/kit-connecteur-mcp/` — ne pas réimplémenter le pattern localement.
Pour câbler un MCP sur l'agent embarqué, **déléguer à `connecteur-mcp-lovable`** (prompts
étagés P1-P5) et **passer le gate** `reference/gate-securite.md` avant livraison. Rappels
non négociables : clés du **client** uniquement, appels **serveur**, **scope injecté
serveur**, **écritures confirmées** dans l'UI.
