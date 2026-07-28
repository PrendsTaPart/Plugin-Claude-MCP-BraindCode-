---
name: mesure-apprentissage-iris
description: Utiliser quand l'utilisateur veut savoir ce que la com a rapporté et améliorer la suite — « qu'est-ce que le post du saumon a donné », « bilan des publications d'Iris », « est-ce que ça ramène des commandes », « pourquoi Iris ne propose plus ça ». Insights réels, commandes attribuées, capitalisation des prompts gagnants, prise en compte des refus.
---

# Mesure & apprentissage (ce qui referme la boucle)

Sans cet étage, Iris est un générateur. Avec lui, elle apprend.

## 1. Collecter (chiffres réels uniquement)

- `post_insights` par publication, `ingishts_campagne` par campagne
  (impressions, engagements, clics) — les chiffres se lisent, jamais
  s'extrapolent : moins de 48 h de vie = « trop tôt pour juger ».
- Photo des planifications : `list_scheduled_posts` (publié vs en attente).

## 2. Attribuer (la seule métrique qui compte)

- Croiser chaque publication avec `list_orders` sur les **48 h suivantes** :
  commandes du plat mis en avant vs sa moyenne habituelle
  (`list_top_productions` pour la base de comparaison).
- Honnêteté statistique : sans code promo ni lien tracké (backlog produit,
  voir docs/FAISABILITE-IRIS.md), l'attribution est une **corrélation**, pas
  une preuve — l'écrire tel quel (« +9 commandes du plat vs moyenne, publication
  la veille — corrélation, pas attribution certaine »).
- Sous 3 commandes d'écart, verdict : « données insuffisantes ».

## 3. Apprendre (et le montrer)

Tout vit dans `./rapido-kb/iris/apprentissage.md` :

- **Prompts gagnants** : un prompt visuel dont les publications performent
  au-dessus de la moyenne de l'établissement est capitalisé via `add_prompt`
  (RapidoCMS) et noté (canal, type de signal, performance).
- **Motifs de refus** : ils pondèrent le scoring des signaux suivants du même
  type — un type de contenu refusé **trois fois de suite** cesse d'être
  proposé (et le journal le dit, pour que le restaurateur puisse le réactiver).
- **Rythme** : les heures/canaux qui performent remontent dans les
  propositions du skill `calendrier-iris`.

## Sortie attendue

Un tableau `[publication | canal | raison d'origine | impressions/engagements |
commandes du plat vs moyenne | verdict]`, puis les enseignements appliqués
(« le format vidéo 9:16 sur les plats du jour surperforme → priorisé »).

## Ce que ce skill NE fait PAS

- L'analyse de contenu généraliste multi-comptes → plugin rapidocms (skill
  `analyse-performance-contenu`).
- Prédire la viralité d'une vidéo avant publication → `virality_predictor`
  dans le skill `video-virale-plats`.
