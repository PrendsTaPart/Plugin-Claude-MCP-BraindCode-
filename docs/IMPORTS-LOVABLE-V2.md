# Imports & audit — rapido-lovable v2 (LV0)

**Date** : 2026-07-15 · **Portée** : audit uniquement — aucune création de skill,
aucune écriture (Lovable/Rapido). 4 dépôts clonés (licences relues), inventaire des
outils MCP Lovable réels, et la question **auth multi-tenant** (le prérequis produit).

> **Référence de production** : le pattern MCP canonique existe déjà dans
> `academyrapido` (fonction `execute-prompt`) — documenté à part dans
> `docs/REFERENCE-AGENT-LOVABLE.md`. Le kit se fonde dessus.

## 1. Moisson vibecoding (licences relues)

Anti-verbatim : on **francise/réimplémente** des méthodes ; aucun corps copié ;
attribution `NOTICE.md`. Licences confirmées dans chaque `LICENSE`.

### 1.a `PatrickJS/awesome-cursorrules` — **CC0-1.0** — 🥇 piocher librement
- Fichiers `.mdc` de règles par stack. Pertinents pour Lovable :
  `cursor-ai-react-typescript-shadcn-ui-…`, `…nextjs-14-tailwind-seo-…`,
  `javascript-typescript-code-quality-…`.
- **Verdict** : **PIOCHER** (CC0 = domaine public, aucune contrainte ; on crédite quand
  même, style maison) → `reference/regles-stack-lovable.md` : sélection francisée
  React/TS/Tailwind/shadcn/Supabase injectée dans chaque prompt généré.

### 1.b `BehiSecc/VibeSec-Skill` — **Apache-2.0** — 🥇 ADAPTER (gate sécurité)
- Guide de code sécurisé : access control (autorisation par utilisateur/ressource),
  validation serveur, encodage de sortie, defense in depth, fail-closed, moindre
  privilège.
- **Verdict** : **ADAPTER** en `reference/gate-securite.md` spécifique « app + clés MCP »
  (secrets exposés, appels client-side interdits, CORS, authz, scope). **Attribution +
  NOTICE Apache-2.0 obligatoires** (mention de modification).

### 1.c `withkynam/vibecode-pro-max-kit` — **MIT** — ✅ ADAPTER (spec-driven)
- Harnais **spec-driven** (specs avant prompts) : `process/`, `AGENTS.md`, manifeste,
  flux e2e.
- **Verdict** : **ADAPTER** l'**ossature spec-driven** de `mvp-lovable` (LV3) : SPEC
  validée → série de prompts étagés à critères de done. Méthode reprise, dépôt non fusionné.

### 1.d `AndreAlmeidaDC/lovable-prompt-builder` — **MIT** — ✅ ADAPTER (sur cible)
- Skill « du zéro au produit sur Lovable » (PT-BR) : intake, branding, LGPD, **prompts
  atomiques + boucle de feedback** ; `references/` (vibecode-core, platform-lovable),
  `security-checklist.md`, `templates/`.
- **Verdict** : **ADAPTER** (francisé) la logique **intake → prompts atomiques →
  feedback** dans `mvp-lovable` et `connecteur-mcp-lovable`. Texte PT-BR non copié.

### 1.e Benchmarks (non fusionnés)
- `KingLeoJr/prompts` (MIT) : déjà retenu côté `rapido-prompteur` — réutiliser.
- `vibeeval/vibecosystem` (MIT, 138 agents/295 skills) : 👁️ **benchmark d'architecture**.
- `sanjeed5/awesome-cursor-rules-mdc` (CC0) : complément éventuel d'awesome-cursorrules.
- `karozi/Awesome-Vibecoding` : **sans licence** → 👁️ **benchmark seul, jamais fusionné**.

## 2. Inventaire des outils MCP Lovable réels (live)

| Outil | Signature / limite | Usage kit |
|---|---|---|
| `create_workspace_skill` | `(workspace_id, skill_name, markdown ≤ 100 000)` — **admin/owner** ; frontmatter `name` obligatoire | Pousser le skill workspace « rapido-mcp-connect » (LV4) |
| `update_workspace_skill` | idem (remplace le SKILL.md) — lire `get_workspace_skill` d'abord | Versionner le kit (routine LV4) |
| `list_workspace_skills` / `get_workspace_skill` | lecture | Vérifier avant push |
| `set_workspace_knowledge` | `(workspace_id, content ≤ 10 000)` — **REMPLACE tout** (lire d'abord) | Méthode maison résumée (LV4) |
| `set_project_knowledge` | `(project_id, content ≤ 10 000)` — **REMPLACE tout** | Contexte client par projet (LV2) |
| `enable_project_skill` | `(project_id, skill_name)` | Activer le skill workspace sur un projet |
| `get_project` / `list_files` / `read_file` | lecture (ref/commit) | Inspecter un projet existant |
| `send_message` | envoi d'un message à l'agent Lovable (consomme des crédits) | Exécution assistée des prompts (LV2/LV3) |

> **Secrets** : il n'y a **pas** d'outil MCP « poser un secret ». Les secrets (clés,
> URLs) se saisissent dans l'**UI Lovable/Supabase** par l'utilisateur — c'est **le bon
> comportement de sécurité** (Claude ne manipule jamais la valeur d'un secret). Le kit
> génère des **prompts** qui disent QUELS secrets créer (noms standardisés), jamais leurs
> valeurs.
>
> **Limites à respecter** : knowledge ≤ 10 k (workspace & projet), skill workspace ≤ 100 k
> → le kit distribué en workspace doit être **condensé**.

## 3. Croisement maison — qui fait quoi demain (le kit UNIFIE, ne remplace pas)

`rapido-lovable` (v1.1.0) : `agent-ia-produit`, `usine-a-landing`, `site-restaurant`,
`sync-marque-lovable`, `ui-ux-pro-max`, `ui-styling`, `frontend-design`,
`web-artifacts-builder`. `rapido-prompteur` : `prompt-lovable`.

| Skill existant | Rôle | Après v2 |
|---|---|---|
| `rapido-prompteur:prompt-lovable` | **UN** brief one-shot (landing, page simple) | Inchangé ; référence le kit si le brief inclut un MCP |
| `usine-a-landing` | Landing + capture (mode B) | Inchangé ; « ajouter l'agent embarqué » → délègue `connecteur-mcp-lovable` |
| `site-restaurant` | Site resto vertical | Idem (délégation agent embarqué) |
| `agent-ia-produit` | Agent embarqué (mode C) | **Consomme le kit** (mode C canonisé) au lieu d'une recette locale |
| `sync-marque-lovable` | Marque → workspace | **Étendu** : pousse aussi le **kit** en workspace skill (LV4) |
| `ui-ux-pro-max` / `frontend-design` / `ui-styling` | Style/design | Style délégué par `mvp-lovable` / `architecte-lovable` |
| `web-artifacts-builder` | Artefacts HTML | Anti-collision (pas Lovable) |
| **`connecteur-mcp-lovable`** (LV2, nouveau) | Prompts qui câblent un MCP | Consomme le kit ; utilisé par tous |
| **`mvp-lovable`** (LV3, nouveau) | Brief → MVP (série P1…P8) | Spec-driven ; route vers les verticaux si besoin |
| **`architecte-lovable`** (agent, LV4) | Orchestration | brief → spec → prompts → connecteur → recette |

## 4. ⚠️ Auth multi-tenant des MCP Rapido — spec prioritaire (§11 manquants)

**Constat (live)** : le pattern MCP de référence (`execute-prompt`) appelle les URLs MCP
**globales** (`crm/cms/rh/foodeatup.rapidosoftware`) **sans token ni scope par client** ;
la clé Anthropic est **partagée** (plateforme). En session Claude Code, l'accès MCP passe
par un **OAuth interactif par utilisateur** — **inexploitable** par un edge function
serveur-à-serveur d'un site client.

**Il manque donc** un **mécanisme d'auth MCP par tenant** : token par
établissement/compte, **scope serveur** (`establishment_id`/`company_id` non
contournable par le front), rotation. **Sans lui, pas de site agentique scopé par
client** → consigné `docs/OUTILS-MCP-MANQUANTS.md` §11. **C'est le prérequis produit**
de tout le chantier.

## 5. STOP — validation avant LV1

1. **Référence** (`docs/REFERENCE-AGENT-LOVABLE.md`) : le kit se fonde sur
   **`execute-prompt`** (API Anthropic + `mcp_servers`), pas sur `agent-chat` (RAG
   Gateway). **OK ?**
2. **Auth multi-tenant** : confirmez-vous que le mécanisme **token-par-établissement**
   n'existe pas encore côté serveur Rapido (donc **spec prioritaire pour Tunis**) ? Le
   kit LV1 sera écrit **prêt pour le multi-tenant** mais fonctionnera d'abord en scope
   injecté serveur (sans exposer de clé au front), en attendant les tokens par tenant.

*Sources : `academyrapido` (lecture MCP live), 4 dépôts clonés (LICENSE relus),
schémas d'outils MCP Lovable (live). Aucune donnée inventée.*
