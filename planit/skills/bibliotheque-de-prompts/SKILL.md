---
name: bibliotheque-de-prompts
description: Utiliser quand la bibliothèque de prompts Plan'It se gère, que l'utilisateur dit « mémorise cette consigne », « retrouve mon prompt de relance », « mets à jour le prompt du brief », « planifie une tâche avec ce prompt ». Crée, retrouve et entretient les prompts privés — variables typées, suppression sur confirmation.
---

# Bibliothèque de prompts (les consignes réutilisables)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`list_prompts`** (recherche par mot-clé) — l'existant d'abord : on ne
   crée pas un doublon d'un prompt qui existe.
2. **`get_prompt`** — description, contenu, variables d'un prompt nommé.
3. **`create_prompt`** — le contenu porte des variables typées
   `{{comme_ceci}}` ; la description courte dit QUAND l'utiliser et reste
   DISTINCTE du contenu (c'est elle qu'on lit dans les listes).
4. **`update_prompt`** — titre, description, contenu ou variables.
5. **`delete_prompt`** — sur confirmation seulement (définitif, hook en
   filet).
6. **Planifier un prompt** : `list_task_prompts` AVANT tout `create_task`
   avec `prompt_id` — seuls les prompts dont le connecteur est réellement
   connecté se planifient ; jamais pour un simple rappel.

## Garde-fous

- Une variable non typée ou un placeholder flou (« [à remplir] ») ne se
  crée pas : chaque variable a un nom parlant et un type.
- Un prompt qui déclenche des envois réels le dit dans sa description — la
  tâche qui le portera héritera des confirmations.
