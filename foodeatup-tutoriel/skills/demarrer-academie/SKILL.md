---
name: demarrer-academie
description: Utiliser quand quelqu'un débute sa formation FoodEatUp ou dit « par où je commence », « forme-moi sur FoodEatUp », « je viens d'ouvrir mon compte », « c'est quoi cette académie ». Cadre le secteur puis le métier via le diagnostic du serveur, et oriente vers premiers pas (compte neuf) ou parcours métier.
---

# Démarrer à l'Académie (cadrage obligatoire)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
   `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.
2. Si `./rapido-kb/entreprise.md` existe : y lire secteur et postes — ne pas
   redemander ce que la KB sait.
3. Si l'utilisateur donne un **code de reprise**, basculer sur le skill
   `carnet-de-reprise` (mode `decoder`) au lieu de recommencer le cadrage.

## Workflow

1. **`diagnostic_demarrage`** — premier appel de toute session de formation.
   Passer ce qu'on sait déjà (`secteurSlug`, `metierSlug`, `dejaConfigure`,
   `objectif` dans les mots de l'utilisateur, `minutesParSeance`) ; poser les
   questions de cadrage renvoyées, une par une.
2. **Confirmer le secteur** avec `secteur_foodeatup` (`restaurant`,
   `boulangerie` ou `reseau`) AVANT de proposer le moindre parcours : un
   boulanger n'est pas un chef de cuisine, un franchisé n'est pas un gérant
   indépendant.
3. **Compte non configuré** (`dejaConfigure: false`) →
   `premiers_pas_foodeatup` et dérouler sa configuration initiale dans
   l'ordre. Aucun parcours métier avant la fin de ces premiers pas.
4. Compte configuré → présenter l'Académie en une phrase
   (`onboarding_foodeatup` avec le `metierSlug` si connu) puis passer le
   relais au skill `parcours-sur-mesure`.
5. Première leçon : la mener avec le skill `lecon-guidee` (une leçon à la
   fois, vignette en bloc image, quiz puis exercice).

## Garde-fous

- Ne jamais sauter le diagnostic « parce que c'est évident » : le secteur
  change le parcours entier.
- Ce serveur enseigne et n'agit pas : pour créer quoi que ce soit dans le
  compte, c'est le connecteur produit (skill `passer-a-l-action`).
- En fin de séance, toujours proposer le code de reprise (skill
  `carnet-de-reprise`).
