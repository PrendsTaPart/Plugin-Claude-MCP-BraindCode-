---
name: boucle-1-configuration
description: Utiliser quand l'utilisateur veut l'état de la boucle ① Configuration — « ma configuration est-elle complète », « qu'est-ce qui manque dans mon paramétrage », « où en est la boucle configuration », « mes référentiels sont-ils à jour ». Diagnostic de complétude des référentiels (catégories, TVA, zones, tables, équipements), pas d'installation de zéro.
---

# Boucle ① — Configuration (référentiels de l'établissement)

## Quand l'utiliser

Pour diagnostiquer la **complétude et la cohérence** des référentiels d'un
établissement déjà créé : catégories, TVA, unités, zones, tables, équipements.
C'est la boucle amont — toutes les autres échouent silencieusement si elle est
trouée (un plat sans TVA, une salle sans tables, un relevé HACCP sans équipement).

## Enchaînement d'outils MCP (l'ordre compte)

1. `search_entities` si l'`establishment_id` n'est pas connu (le demander sinon).
2. Lectures, dans cet ordre : `list_categories`, `list_tva`, `list_units`,
   `list_zones`, `list_tables`, puis `list_dishes` et `list_products` pour croiser.
3. Croisement : chaque plat/produit doit pointer vers une catégorie et une TVA
   existantes ; chaque zone doit contenir au moins une table.
4. Corrections à la demande : `create_category` / `update_category`,
   `create_tva`, `create_zone`, `create_table`, `create_dish_category`,
   `create_equipment`.

## Règles métier

- TVA restauration France : 10 % sur place/à emporter alimentaire, 20 % alcool,
  5,5 % produits emballés — vérifier qu'aucun taux exotique ne traîne.
- Un équipement froid déclaré sans relevé de température récent est un trou de
  boucle ④, à signaler ici comme « équipement configuré mais non suivi ».
- Ne jamais inventer une valeur absente : écrire « non déclaré ».

## Garde-fous (opérations exigeant confirmation)

- `delete_category` est intercepté par le hook du plugin (confirmation humaine) :
  une suppression de catégorie orpheline ses produits.
- Aucune autre écriture de cette boucle n'est destructive, mais toute écriture se
  fait après récapitulatif (« je vais créer X, Y — d'accord ? »).

## Sortie attendue

Un tableau `[référentiel | présent | trous détectés | correction proposée]` puis
la liste des écritures proposées, en attente d'accord explicite.

## Ce que ce skill NE fait PAS

- Installer un établissement de zéro → skill `onboarding-restaurateur` (plugin
  foodeatup).
- Construire la carte en ligne → skill `carte-vitrine` (plugin foodeatup).
- Le paramétrage du site vitrine relève de la boucle ⑤ → skill `boucle-5-ecommerce`.
