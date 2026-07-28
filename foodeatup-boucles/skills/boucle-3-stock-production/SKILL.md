---
name: boucle-3-stock-production
description: Utiliser quand l'utilisateur veut l'état de la boucle ③ Stock/Production — « où en est ma boucle stock », « suis-je prêt pour le service côté production », « bilan stock et production », « quels ingrédients vont manquer cette semaine ». Diagnostic chaîne amont (stocks, recettes, production, fournisseurs), pas l'exécution d'un plan de production.
---

# Boucle ③ — Stock / Production (chaîne amont)

## Quand l'utiliser

Pour l'**état de la chaîne amont** : niveaux de stock, alertes, plans de
production à venir, dépendances fournisseurs. La question à laquelle répond la
boucle : « puis-je servir ce que je prévois de vendre ? »

## Enchaînement d'outils MCP (l'ordre compte)

1. `list_low_stocks` d'abord (les urgences), puis `list_stocks` pour le panorama.
2. `list_production_plans` + `list_production_alerts` : plans à venir,
   `get_production_ingredients` pour vérifier que les ingrédients suivent.
3. Croiser avec la demande réelle : `list_reservations` et `list_orders`
   (boucle ⑤). Une production planifiée sans demande correspondante est un
   gaspillage annoncé — c'est une détection du skill `croisement-service`.
4. `list_top_productions` pour l'historique (que produit-on vraiment ?).
5. Réappro : `list_suppliers`, puis `create_supplier_order` sur accord ;
   réception contrôlée en boucle ④ (`create_haccp_reception`).
6. Ajustements : `adjust_stock` (toujours motivé : inventaire, casse, erreur).

## Règles métier

- Un stock bas d'ingrédient principal d'un plat **mis en avant en campagne**
  (boucle ⑥) est une incohérence majeure : la signaler immédiatement.
- `validate_production` seulement après vérification des quantités réelles.
- Jamais de commande fournisseur sans lecture préalable des livraisons en cours
  (`list_deliveries`) — éviter la double commande.

## Garde-fous (opérations exigeant confirmation)

- `delete_ingredient`, `delete_product`, `delete_recipe`, `delete_dish` sont
  interceptés par le hook du plugin (une recette supprimée casse les coûts).
- `adjust_stock` sans motif explicite : refuser et demander le motif.

## Sortie attendue

Un tableau `[sujet | état | seuil | action proposée]` sur : stocks bas, plans de
production vs demande, fournisseurs en attente, ajustements récents.

## Ce que ce skill NE fait PAS

- Créer une recette et calculer son coût → skill `recette-cout-marge` (plugin
  foodeatup).
- Planifier/valider une production pas à pas → skill `production-stock`.
- Passer les commandes fournisseurs de bout en bout → skill `reappro-fournisseurs`.
- La coordination du service en cuisine (KDS) → skill `coordination-cuisine`.
