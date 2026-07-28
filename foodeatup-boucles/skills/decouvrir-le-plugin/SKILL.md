---
name: decouvrir-le-plugin
description: Utiliser quand l'utilisateur demande ce que sait faire son installation — « que sais-tu faire », « quels sont mes skills », « aide-moi à démarrer », « quels plugins j'ai », « par où commencer avec FoodEatUp ». Présente la carte des plugins rapido par domaine, les phrases déclencheuses et les limites, depuis un fichier généré du dépôt réel.
---

# Découvrir le plugin (et la marketplace rapido)

## Quand l'utiliser

Quand l'utilisateur ne sait pas ce que son installation sait faire. L'audit l'a
montré : sans auto-formation, personne ne sait ce que contient le plugin.

## Source de vérité

Charger `${CLAUDE_PLUGIN_ROOT}/reference/carte-marketplace.md` et répondre
depuis ce fichier — **jamais de mémoire**. Ce fichier est généré depuis le
dépôt réel par la commande `python3 scripts/generer-carte-boucles.py` (dépôt de
la marketplace) ; s'il est absent, le dire et indiquer cette commande au lieu
d'improviser une liste.

## Ce qu'on présente

1. **La carte par domaine** : restaurant, ventes/CRM, contenu, publicité,
   vidéo, équipe, direction, sites/apps, formation — avec, pour chaque domaine,
   les 3 phrases types qui déclenchent le bon skill (elles sont dans la carte).
2. **Les 8 boucles de ce plugin** : `/boucles` pour l'état d'ensemble,
   `/boucle <n>` pour le détail, `/croisement` pour les incohérences,
   `/sante-donnees` pour savoir si les données suffisent.
3. **Ce que ça ne peut PAS faire** : la section « limites connues » de la
   carte (roue cadeaux et sondages en back-office, pas d'envoi ni de
   publication sans confirmation humaine, rien d'estimé sans outil).

## Parcours de démarrage en 5 étapes

1. Vérifier la connexion MCP : `get_daily_brief` répond ? Sinon, connecter le
   serveur FoodEatUp d'abord (prérequis du README du plugin).
2. `/boucles` — premier état des 8 boucles, lecture seule.
3. Ouvrir la boucle la plus rouge avec `/boucle <n>` et traiter UNE action.
4. `/sante-donnees` — savoir quelles recommandations sont fiables aujourd'hui.
5. Quand au moins deux boucles vivent : `/croisement` pour les incohérences.

## Sortie attendue

Une réponse orientée « prochain geste » : la carte résumée au domaine pertinent
pour l'utilisateur, 3 phrases à essayer tout de suite, et l'étape du parcours
où il se trouve.

## Ce que ce skill NE fait PAS

- Exécuter les boucles elles-mêmes → skills `boucle-1-configuration` à
  `boucle-8-comptabilite` et `croisement-service`.
- Documenter les prompts de la marketplace Braindcode (serveur
  Braindcode_Plugin) → hors périmètre de ce plugin.
