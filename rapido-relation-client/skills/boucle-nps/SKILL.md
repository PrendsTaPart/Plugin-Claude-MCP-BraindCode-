---
name: boucle-nps
description: Utiliser quand l'utilisateur veut mesurer la satisfaction, lancer/lire un NPS, segmenter promoteurs/passifs/détracteurs, ou agir sur la fidélité. Lance/lit les sondages NPS via animation-client, segmente les clients réels, et déclenche les actions par segment (détracteurs → sauvetage, passifs → geste, promoteurs → ambassadeurs + avis). Historise le NPS par vague.
---

# Boucle NPS — la fidélité mesurée et actionnée

Mesure la satisfaction et **agit** par segment — la fidélité n'est pas qu'un chiffre.

## Étape 0 — Pont forge + seuils
- Livrable forge `scale-nps-survey` comme méthode ; absent → défauts en le disant.
- Seuils NPS : `./rapido-kb/relation-client/fidelite.md` (promoteur ≥ 9, passif 7-8,
  détracteur ≤ 6), jamais en dur.

## Sense (NPS réel)
- Lancer/lire les sondages NPS via **`rapidocrm:animation-client`** (délégation) ;
  lire les réponses réelles (`get_sondage_resultats`).

## Plan (segmentation)
- Segmenter les répondants : **promoteurs / passifs / détracteurs**. Calcul du **NPS**
  (% promoteurs − % détracteurs) — formule affichée.

## Act (actions par segment, confirmées)
- **Détracteurs** → **plan de sauvetage** (pont vers `sante-client` + la routine churn
  si présente) — priorité aux comptes de valeur.
- **Passifs** → **geste de considération** (brouillon confirmé).
- **Promoteurs** → **invitation au programme ambassadeurs** (`rapidocrm:programme-ambassadeurs`)
  + **demande d'avis public** (brouillon confirmé).

## Feed
- Historiser le NPS **par vague** dans `./rapido-kb/relation-client/nps-historique.md`
  (date, NPS, tailles de segments).

## Anti-collision
- `rapidocrm:animation-client` = **exécute** sondages/jeux/points ; **moi = la boucle**
  (mesurer → segmenter → agir → historiser).

## Garde-fous
Sondages **délégués** ; NPS **par formule** ; actions **confirmées** (brouillons) ;
historisation datée ; segments **réels** (jamais inventés).
