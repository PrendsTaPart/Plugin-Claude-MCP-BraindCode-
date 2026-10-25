---
name: plugin-prive-sur-mesure
description: Utiliser quand le catalogue privé Plan'It s'enrichit, que l'utilisateur dit « propose-moi un plugin pour mon connecteur », « qu'y a-t-il dans mon catalogue privé », « ajoute une consigne à mon plugin privé ». Ouvre une proposition avec son consentement, respecte les refus passés, et ne crée directement que sur demande expresse.
---

# Plugin privé sur mesure (proposer, l'utilisateur dispose)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`list_my_private_catalog`** — l'existant d'abord : plugins (slug,
   connecteurs requis, origine import/builder) et consignes avec leur plugin
   parent. On ne propose pas ce qui existe.
2. **`open_private_proposal`** sur le connecteur visé — EXIGE le
   consentement de l'utilisateur pour CE connecteur (le demander en une
   phrase avant). La réponse donne : les éléments DÉJÀ REFUSÉS (à ne jamais
   reproposer), les DÉJÀ ACCEPTÉS (déjà dans le catalogue), et
   hooks_supported. Elle REMPLACE la proposition en attente du connecteur.
3. **`propose_private_item`** — UN élément à la fois : `plugin`, `skill`
   (dépend du plugin), `tool_prompt` (payload.tool_name), `routine`
   (payload.prompt, frequency, selected_tools, objective) ou
   `kpi_candidate`. **name + summary doivent suffire à décider** en les
   lisant — pas de visite du détail obligatoire. Idempotent par (type, slug).
4. L'utilisateur accepte ou refuse chaque élément DANS L'APP — on n'insiste
   pas, on ne retouche pas un refus.
5. **`create_private_plugin`** / **`create_private_skill`** : UNIQUEMENT sur
   demande expresse (« crée-le directement ») — idempotents par slug, jamais
   de doublon.

## Garde-fous

- Pas de proposition sans consentement préalable sur le connecteur ; les
  refus passés sont définitifs.
- Un élément routine proposé respecte les lois des routines (objectif
  chiffré, pas de once/custom).
