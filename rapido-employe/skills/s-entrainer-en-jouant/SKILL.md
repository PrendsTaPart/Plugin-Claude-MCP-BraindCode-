---
name: s-entrainer-en-jouant
description: Utiliser quand l'entraînement passe par le jeu, que l'utilisateur dit « lance le restaurant 3D », « on fait une partie de caisse express », « entraîne-toi en jouant ». Sert les deux jeux MCP Apps de l'Academy — restaurant 3D et jeu de caisse — puis débriefe à partir du résultat réellement renvoyé.
---

# S'entraîner en jouant (le jeu, puis le débrief)

Famille engagée : **apprendre** (Confirmé ; `start_game_session`,
`submit_game_action`, `finish_game_session` sont des écritures Academy).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **Choisir le jeu** selon la compétence à muscler :
   - `restaurant_3d` — le restaurant en 3D (widget MCP Apps rendu par le
     serveur : la scène s'affiche dans la conversation) ;
   - `jeu_caisse_express` — l'entraînement caisse (widget MCP Apps).
   Ces outils rendent leur propre interface : la servir telle quelle, ne pas
   la réécrire en texte.
2. **La partie** : `start_game_session`, puis `submit_game_action` au fil du
   jeu, `get_game_session` / `get_game_progress` pour l'état, et
   `finish_game_session` à la fin.
3. **Le débrief** : `get_game_results` — à partir du RÉSULTAT RENVOYÉ
   uniquement : points forts, erreurs, et le geste réel à retravailler
   (renvoi vers la mission de formation ou le tutoriel correspondant,
   skill `chemin-de-formation`).
4. Un score qui progresse se note au journal de la routine d'entraînement
   si elle existe (`log_routine_run`).

KPI : `objectifs-atteints` (compétences du profil). Formations : `foodeatup`
(caisse), `logiciel`.

## Garde-fous

- Le débrief cite le résultat du serveur — jamais un score estimé ni une
  partie « racontée ».
- Le jeu reste de l'entraînement : aucune écriture vers un vrai compte
  FoodEatUp pendant une partie.
