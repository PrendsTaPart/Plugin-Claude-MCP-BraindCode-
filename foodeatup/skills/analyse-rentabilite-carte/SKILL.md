---
name: analyse-rentabilite-carte
description: Utiliser quand l'utilisateur veut analyser sa carte, savoir quels plats garder ou parle d'ingénierie de menu. Applique la matrice popularité × marge (Stars, Plow-horses, Puzzles, Dogs) sur les données réelles des recettes et des ventes.
---

# Analyse de rentabilité de la carte (ingénierie de menu)

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.

## Méthode — matrice popularité × marge

Chaque plat est classé sur deux axes, calculés sur des DONNÉES RÉELLES :
- **Marge** : marge brute unitaire = prix de vente HT − coût matière.
  Food cost = coût matière / prix de vente HT (cible ≤ 30 %).
- **Popularité** : volume vendu/produit sur la période, comparé à la popularité
  moyenne de la catégorie (seuil classique : 70 % de la moyenne).

| | Marge haute | Marge basse |
|---|---|---|
| **Populaire** | ⭐ **Stars** | 🐴 **Plow-horses** |
| **Peu populaire** | 🧩 **Puzzles** | 🐶 **Dogs** |

## Workflow

1. **Collecter les données** — aucun chiffre inventé :
   - `list_dishes` + `list_recipes` : la carte et ses fiches ;
   - `get_recipe` par plat : coût matière, prix, marge (si une fiche n'a pas de
     coût complet, le signaler — le plat sort de l'analyse au lieu d'être estimé) ;
   - `list_top_productions` et/ou `list_orders` sur la période : volumes réels
     (préciser la période analysée ; défaut : 30 derniers jours).
2. **Calculer** pour chaque plat : food cost %, marge unitaire, indice de
   popularité vs moyenne de sa catégorie.
3. **Classer** dans la matrice et restituer un tableau : plat | catégorie |
   food cost % | marge € | popularité | quadrant.
4. **Recommander par quadrant** :
   - ⭐ **Stars** (populaire + marge haute) : ne pas toucher — mettre en avant
     (position sur la carte, suggestion serveur). Surveiller la constance.
   - 🐴 **Plow-horses** (populaire + marge basse) : REPRICER ou re-costifier —
     hausse de prix modérée (1-2 tests), réduction du coût matière (portion,
     ingrédient, négociation fournisseur) SANS dégrader la qualité perçue.
   - 🧩 **Puzzles** (peu populaire + marge haute) : REPOSITIONNER — renommer,
     déplacer sur la carte, faire vendre par l'équipe, photo/description. Si
     toujours invendu après repositionnement : retirer.
   - 🐶 **Dogs** (peu populaire + marge basse) : RETIRER — ou transformer
     (recette revisitée, plat du jour pour écouler). Jamais plus d'un cycle de
     seconde chance.
5. **Plan d'action** : 3 à 5 actions maximum, priorisées par impact sur la marge
   globale, chacune adossée au skill concerné (`recette-cout-marge` pour
   re-costifier/repricer, `update_dish`/`update_recipe` pour appliquer — avec
   confirmation).

## Garde-fous

- L'analyse ne MODIFIE rien : les actions (prix, retrait de plat) ne s'exécutent
  qu'après validation explicite de l'utilisateur, plat par plat.
- Toujours indiquer la période et les plats exclus faute de données.
- Rappeler l'ordre de priorité maison : jamais une hausse de marge au détriment
  de la sécurité alimentaire ou de l'expérience client.
