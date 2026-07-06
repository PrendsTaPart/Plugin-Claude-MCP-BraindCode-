---
name: production-stock
description: Utiliser quand l'utilisateur veut planifier une production, consulter les alertes de production ou valider une production réalisée. Enchaîne planification → vérification des ingrédients → validation avec mise à jour du stock.
---

# Production et stock

## Étape 0 — Établissement (obligatoire)

S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.

## Workflow

1. **Planifier** — `create_production_plan` (`establishment_id`, `item_id`,
   `planned_quantity`, `planned_date` YYYY-MM-DD, `planned_time` HH:MM défaut 09:00,
   `notes` optionnel).
   - `item_id` : ID du **plat** en entier (ex. `"42"`), ou de la **recette** avec le
     préfixe `recipe_` (ex. `"recipe_12"`). Retrouver l'ID via `list_dishes` ou
     `list_recipes` si l'utilisateur ne donne qu'un nom.
2. **Vérifier les ingrédients** — `get_production_ingredients` (`establishment_id`,
   `production_id`) : contrôler le statut suffisant/manquant de chaque ingrédient.
   Si des ingrédients manquent, le signaler et proposer le skill
   réappro-fournisseurs avant la date de production.
3. **Surveiller les alertes** — `list_production_alerts` (`establishment_id`,
   `days` horizon en jours, défaut 7) : ingrédients manquants pour les productions
   planifiées à venir.
4. **Valider la production réalisée** — `validate_production` (`establishment_id`,
   `production_id`, `produced_quantity` = quantité RÉELLEMENT produite,
   `temperature_log` optionnel pour la traçabilité HACCP, `notes`).
   - La validation met à jour le stock automatiquement : ne PAS appeler
     `adjust_stock` en plus pour la même production.

## Garde-fous

- Ne valider une production qu'à la demande explicite de l'utilisateur et avec la
  quantité réellement produite (elle peut différer du planifié — demander si doute).
- Ne jamais valider une production dont les ingrédients sont signalés manquants
  sans en avertir l'utilisateur d'abord.
- `list_production_plans` permet de retrouver un `production_id` si l'utilisateur
  ne le connaît pas.
