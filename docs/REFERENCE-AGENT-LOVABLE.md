# Référence — l'agent Lovable en production (academyrapido)

**Date** : 2026-07-15 · **Source** : projet Lovable `academyrapido`
(`a01393c8-…`, workspace `7gbZqk6lsnITUluFMgSc`), lecture directe via MCP Lovable
(`read_file`, commit `1fde1cc`). On **canonise du code qui tourne** — pas de théorie.

> **Fait structurant** : il y a **deux patterns distincts** en prod, pas un seul.
> `agent-chat` = **RAG sur Supabase via la passerelle Lovable** (aucun MCP).
> `execute-prompt` = **le vrai pattern MCP** (API Anthropic + `mcp_servers`). Le kit
> connecteur se fonde sur **`execute-prompt`**. ⚠️ Ce pattern MCP de référence appelle
> des **URLs MCP globales non scopées** avec une **clé Anthropic plateforme partagée** —
> **aucun scope par client/établissement** (voir §Gap → spec Tunis).

## 1. `agent-chat` — chat RAG (Lovable AI Gateway, PAS de MCP)

- **Moteur** : `POST https://ai.gateway.lovable.dev/v1/chat/completions` (streaming
  SSE), modèle `cfg.model || "openai/gpt-5-mini"`. **Pas** l'API Anthropic, **pas** de
  `mcp_servers`.
- **System prompt** : construit (`buildSystemPrompt`) depuis `agent_config` (table
  Supabase singleton : ton, objectifs, argumentaires, garde-fous, langue, seuil démo…).
- **Connaissance** : `buildKnowledgeContext(supabase, lastUser, …)` → RAG **sur les
  tables Supabase** (prompts, parcours) rendu en texte, injecté à chaque tour. Règle
  forte : « INTERDIT d'inventer un prompt… recommander UNIQUEMENT ce qui est en base ».
- **Secrets (env, serveur)** : `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`,
  `LOVABLE_API_KEY`. **Aucun secret côté navigateur.**
- **Garde-fous** : rate-limit 20 req/60 s par IP ; historique tronqué (20 derniers,
  4000 car.) ; **journalisation anonymisée** (besoins/prompts/actions, pas de PII).
- **Sortie structurée** : blocs `[PROMPT_CARD]{…}[/PROMPT_CARD]` et `[ACTION]{…}[/ACTION]`
  parsés par regex côté client.

→ **Réutilisable pour le kit** : la forme du **system prompt** (ton, langue,
confirmation, honnêteté « rien d'inventé »), la **journalisation anonymisée**, le
**rate-limit**, la **sortie structurée**. **PAS** le moteur (Gateway ≠ MCP).

## 2. `execute-prompt` — LE pattern MCP (API Anthropic + `mcp_servers`) 🎯

C'est la **base canonique du kit connecteur**.

- **Appel** : `POST https://api.anthropic.com/v1/messages`, en-têtes
  `x-api-key`, `anthropic-version: 2023-06-01`, **`anthropic-beta: mcp-client-2025-04-04`**,
  corps :
  ```json
  { "model": "claude-sonnet-4-5", "max_tokens": 2048,
    "messages": [{ "role": "user", "content": "<prompt>" }],
    "mcp_servers": [{ "type": "url", "url": "<mcp_url>", "name": "<nom>" }] }
  ```
- **Registre MCP** (dans la fonction) : `crm → crm.rapidosoftware.com/mcp` (`rapidocrm`),
  `cms → cms.rapidosoftware.com/mcp` (`rapidocms`), `rh → rh.rapidosoftware.com/mcp/rapidorh`
  (`rapidorh`), `foodeatup → foodeatup.com/api/mcp` (`foodeatup`). Mono-MCP (`mcp_cible`)
  ou multi-MCP (`mcps_impliques`, `orchestration:true`).
- **Disponibilité** : lecture Supabase `mcp_connexions` (type, actif, url, statut) →
  refus 503 « connexion indisponible » si inactif (dégradation propre).
- **Clé Anthropic** : lue en base Supabase `settings` (clé `ANTHROPIC_API_KEY`) — **côté
  serveur uniquement**.
- **Auth utilisateur** : `supabase.auth.getUser(Bearer)` → `userId` ; rate-limits
  **burst 10/60 s** + **horaire 60 (connecté) / 10 (anonyme)**.
- **Sécurité entrée** : `looksSuspicious` (patterns d'injection : « ignore previous
  instructions », « reveal system prompt », « print api_key »…) → 400 ; `sanitize`
  (retire les caractères de contrôle) ; **longueur ≤ 20 000**.
- **Parsing de la réponse — PAR TYPE, jamais par position** :
  - `text` → blocs texte ;
  - `mcp_tool_use` → `{id, name, input, server_name}` (mappé `server_name → clé MCP`) ;
  - `mcp_tool_result` → `{tool_use_id, is_error, content}` (relié au tool_use).
  Retour : `{ text, tool_uses[], tool_results[], stop_reason, usage, mcps[] }`.
- **Télémétrie** : `events` (type `prompt_executed`, compte tool_uses/erreurs, user_id) ;
  `prompts.exec_count++`.

→ **Réutilisable pour le kit (canonique)** : l'appel `mcp_servers` type `url` + le
**beta header**, le **parsing par type**, la **table de disponibilité** MCP, la clé en
**secret serveur**, les **rate-limits**, le **filtre d'injection** + `sanitize`, la
**télémétrie**.

## 3. `agent-knowledge` (annexe)

Constructeur/expose de la base de connaissance RAG (Supabase) consommée par
`agent-chat` (`_shared/knowledge.ts`). Hors périmètre MCP.

## 4. ⚠️ Gap — pas de multi-tenant (spec prioritaire Tunis)

Le pattern MCP de référence, tel qu'il tourne :

1. **URLs MCP globales, non scopées** : `mcp_servers` porte `url` + `name`, **sans
   token ni `establishment_id`/`company_id`**. La fonction n'injecte **aucun scope
   client** — elle parle au MCP **global**. (En session Claude Code, l'accès MCP passe
   par un **OAuth interactif par utilisateur** ; ce mécanisme n'existe pas pour un
   edge function serveur-à-serveur.)
2. **Clé Anthropic plateforme partagée** (`settings.ANTHROPIC_API_KEY`) — c'est la clé
   **de BraindCode**, pas celle du client.

**Conséquence produit** : en l'état, on **ne peut pas** livrer à chaque restaurateur un
site agentique **scopé sur SON établissement avec SES identifiants**. Il manque un
**mécanisme d'auth MCP par tenant** (token par établissement/compte, scope serveur,
rotation). → **Spec prioritaire** consignée dans `docs/OUTILS-MCP-MANQUANTS.md` (§11).
C'est **le** prérequis qui transforme le kit d'outil interne en **produit vendable**.

## 5. Ce que le kit canonise (LV1)

- **Template edge function** = `execute-prompt` **durci multi-tenant** : `mcp_servers`
  type url **+ auth par tenant** (quand le mécanisme existera ; d'ici là, scope injecté
  serveur depuis l'env, jamais depuis le front), parsing par type, rate-limits, filtre
  d'injection, clé en secret serveur.
- **System prompt canonique** : dérivé de `agent-chat` (ton, langue, confirmation avant
  écriture, honnêteté).
- **Sortie structurée** + **journalisation anonymisée** + **table de disponibilité**.
