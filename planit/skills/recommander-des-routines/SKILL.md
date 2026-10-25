---
name: recommander-des-routines
description: Utiliser quand on cherche quoi automatiser, que l'utilisateur dit « qu'est-ce que je devrais automatiser », « propose-moi des routines », « qu'est-ce que je refais à la main tout le temps ». Sert les candidats calculés par le serveur avec leur preuve et leur coût, puis enregistre la proposition retenue — un candidat n'est jamais présenté comme actif.
---

# Recommander des routines (les candidats calculés, pas les idées en l'air)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. `list_pending_routine_actions` d'abord : rien ne se repropose qui attend
   déjà une décision.

## Workflow

1. **`recommend_routines`** — focus possible : `recurring_tasks` (tâche
   recréée à la main ≥ 3 fois en 30 jours), `kpi_without_routine`,
   `unused_connector`, `catalog_template`, `knowledge_base`, ou une clé de
   connecteur. Les candidats déjà proposés ou refusés sont écartés par le
   serveur.
2. **Présenter chaque candidat** avec SA preuve : `reason`, `evidence`,
   effet attendu, coût mensuel estimé (base dite si flat_price/default).
   JAMAIS présenté comme déjà actif : c'est un candidat.
3. **Le candidat retenu** → **`propose_routine`** (la proposition prête du
   candidat, complétée au besoin par la chaîne du skill
   `creer-une-routine`) — enregistrée, pas créée.
4. **Le candidat écarté par l'utilisateur** → `decline_routine_proposal`
   avec la raison qu'il donne (le refus est définitif à l'identique — le
   rappeler).
5. L'acceptation éventuelle suit le skill `creer-une-routine` (coût annoncé,
   accord explicite).

## Garde-fous

- Ne jamais enjoliver l'`evidence` du serveur ni en inventer une.
- Refuser à la place de l'utilisateur est interdit (hook garde-planit :
  decline = famille « tranchent »).
