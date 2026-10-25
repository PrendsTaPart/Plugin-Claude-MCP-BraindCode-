---
name: decouvrir-planit
description: Utiliser quand on découvre ce que Plan'It sait faire, que l'utilisateur dit « qu'est-ce que Plan'It peut faire », « montre-moi les outils de la catégorie KPI », « c'est quoi les capacités vidéo ». Liste les capacités par catégorie, avec le drapeau destructif de chacune.
---

# Découvrir Plan'It (les capacités, par catégorie)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`get_tools`** — les 63 capacités : nom, catégorie, description,
   `is_destructive` (celles qui exigent une confirmation).
2. **`get_tools_filtered`** par catégorie quand la question est ciblée :
   `tasks`, `routines`, `prompts`, `kpi`, `mcp`, `orchestration`,
   `discovery`, `events`, `catalog`, `media`.
3. **Restituer** par familles d'usage, en marquant d'un 🔒 les outils
   destructifs (confirmation) et d'un 💳 les payants (coût annoncé avant) —
   familles de `reference/outils-sensibles.json`.
4. Orienter vers le skill qui fait : tâches → `mes-taches`, routine neuve →
   `creer-une-routine`, mesure → `boucles-kpi`, connecteurs →
   `connecteurs-mcp`, vidéo → `video-courte`…

## Garde-fous

- La liste du jour fait foi (le serveur évolue) ; l'inventaire versionné
  docs/inventaires/planit-tools-live.txt sert de référence CI, pas de
  réponse à l'utilisateur.
