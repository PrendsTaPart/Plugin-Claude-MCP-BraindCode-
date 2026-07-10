---
name: production-stock
description: Utiliser quand l'utilisateur veut planifier une production, consulter les alertes de production ou valider une production réalisée. Enchaîne planification → vérification des ingrédients → validation avec mise à jour du stock.
---

# Production et stock

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — fuzzy FR géré par le
   serveur (accents, pluriels) ; si `ambiguous=true`, présenter les
   candidats et DEMANDER confirmation avant d'agir. Jamais d'ID deviné.

## Workflow

1. **Planifier** — `create_production_plan` (`establishment_id`, `item_id`,
   `planned_quantity`, `planned_date` YYYY-MM-DD, `planned_time` HH:MM défaut 09:00,
   `notes` optionnel).
   - `item_id` : ID du **plat** en entier (ex. `"42"`), ou de la **recette** avec le
     préfixe `recipe_` (ex. `"recipe_12"`). Si l'utilisateur ne donne qu'un nom,
     le résoudre via `search_entities` (`types: ["dish", "recipe"]` — règle
     « Résolution des noms », directives § 1 ter) ; confirmation si
     `ambiguous=true`.
2. **Vérifier les ingrédients** — `get_production_ingredients` (`establishment_id`,
   `production_id`) : contrôler le statut suffisant/manquant de chaque ingrédient.
   Si des ingrédients manquent, le signaler et proposer le skill
   réappro-fournisseurs avant la date de production.
3. **Surveiller les alertes** — `list_production_alerts` (`establishment_id`,
   `days` horizon en jours, défaut 7) : ingrédients manquants pour les productions
   planifiées à venir. Vue d'inventaire COMPLÈTE : `list_stocks`
   (`establishment_id` — tous les articles) ; les seuls articles sous seuil :
   `list_low_stocks` (réassort : skill `reappro-fournisseurs`).
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
