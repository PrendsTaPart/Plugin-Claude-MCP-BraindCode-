---
name: comprendre-foodeatup
description: Utiliser quand quelqu'un veut comprendre le logiciel avant d'apprendre un geste, dit « c'est quoi FoodEatUp », « explique-moi le principe des boucles », « pourquoi tout est lié », « c'est quoi un KDS ». Explique le modèle des 8 boucles, définit les termes du métier et situe les capacités, sans entrer dans un tutoriel précis.
---

# Comprendre FoodEatUp (le modèle avant les gestes)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **Le principe** : `comprendre_foodeatup` — le modèle des 8 boucles et la
   logique « une saisie, pas dix ». Restituer avec les mots du serveur,
   illustrés par la situation de l'utilisateur si on la connaît (KB).
2. **Un terme obscur** : `glossaire_foodeatup` (`terme`) — KDS, shift,
   relevé HACCP, MCP… Vide = tout le glossaire ; n'en donner que ce qui
   sert.
3. **« Et concrètement, ça couvre quoi ? »** : `capacites_foodeatup`
   (filtre `domaine` possible : « stock », « HACCP »…) — citer les domaines
   et compteurs renvoyés avec leur date. Attention (piège vérifié) : cet
   outil décrit le PRODUIT FoodEatUp, pas les 36 outils de l'Académie.
4. Pour aller plus loin : la série vidéo des 8 boucles vit dans le module
   `les-8-boucles` (skill `explorer-un-module`), et le plugin
   `foodeatup-boucles` outille le diagnostic par boucle sur un compte réel.
5. La personne est convaincue et veut démarrer → skill `demarrer-academie`.

## Garde-fous

- Aucun chiffre (nombre d'outils, de tutoriels, prix) sans l'outil qui le
  renvoie ET sa date de vérification.
- Les questions de prix partent vers le skill `decouvrir-l-offre`, jamais
  d'un souvenir.
