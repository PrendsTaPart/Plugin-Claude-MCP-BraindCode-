---
name: prompts-de-mes-outils
description: Utiliser quand les prompts d'outils des connecteurs personnels se génèrent, que l'utilisateur dit « génère les prompts de mes outils », « quels outils de mon MCP n'ont pas encore de prompt », « mets à jour le prompt de cet outil ». Prévisualise TOUJOURS avant d'appliquer, outil par outil ou en masse.
---

# Prompts de mes outils (aperçu d'abord, toujours)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`list_my_mcp_tools`** — les outils des connecteurs PERSONNELS de
   l'utilisateur (pas le catalogue public), avec pour chacun : a-t-il déjà
   un prompt privé lié, et son ID.
2. **`preview_my_tool_prompts`** — TOUJOURS avant d'écrire : pour chaque
   outil, l'action (create ou update), le titre, le contenu dérivé de la
   description de l'outil, les variables typées extraites du schéma. L'aperçu
   se montre à l'utilisateur.
3. **Appliquer** :
   - un outil précis → **`apply_my_tool_prompt`** (couple mcp_key +
     tool_name) ;
   - tout un connecteur (ou tous) → **`apply_all_my_tool_prompts`** —
     annoncer d'abord combien de prompts seront créés/mis à jour (l'aperçu
     le dit).
4. Les prompts générés se retrouvent ensuite dans la bibliothèque (skill
   `bibliotheque-de-prompts`) et se planifient via `list_task_prompts`.

## Garde-fous

- Jamais d'apply sans preview dans la même séance : l'utilisateur voit ce
  qui sera écrit AVANT.
- Un prompt existant modifié par l'apply se signale (action « update » dans
  l'aperçu) — pas d'écrasement silencieux.
