---
name: recette-cout-marge
description: Utiliser quand l'utilisateur veut créer une recette, calculer le coût d'une recette, une marge, ou fixer un prix de vente. Encode les règles de TVA restauration et le calcul de marge.
---

# Recette, coût et marge

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.

## Workflow

1. **Collecter la recette** : nom, portions (`how_many_people`), ingrédients avec
   quantités en **poids BRUT** (avant cuisson/parage) et unités (g, kg, ml, L, pièce),
   étapes de préparation, temps, difficulté (1-3), coefficient/rendement de cuisson
   si pertinent.
2. **Déterminer la TVA** selon la nature du plat (règles françaises) :
   - `immediate` (consommation immédiate : plat servi, boisson sans alcool ouverte)
     → **10 %** ;
   - `conservable` (produit vendu emballé, conservable) → **10 % sur place / 5,5 %
     à emporter** — demander le canal de vente si ambigu ;
   - `alcohol` (boisson alcoolisée) → **20 %**.
   Toujours choisir la bonne nature AVANT de fixer `tax_rate` ; en cas de doute,
   demander à l'utilisateur.
3. **Créer la recette** — `create_recipe` avec :
   - `establishment_id`, `name`, `desc` (courte description générale UNIQUEMENT —
     ne JAMAIS mettre les étapes ni la liste d'ingrédients dans `desc`) ;
   - `ingredients` : tableau `{name` ou `ingredient_id, quantity` (poids BRUT),
     `unit, price_per_unit` si l'ingrédient doit être créé} — les ingrédients sont
     retrouvés par nom ou créés s'ils n'existent pas ;
   - `steps` : tableau `{description, preparation_time}` dans l'ordre (numérotation
     automatique) ;
   - `tax_rate` (en %, selon l'étape 2), `price_includes_tax` (préciser si le prix
     discuté est HT ou TTC — défaut HT) ;
   - marge : `target_margin_rate` (%) avec `margin_basis` = `marge`
     ((PV−coût)/coût, défaut) ou `coefficient` ; ou bien `recommended_price` si
     l'utilisateur impose un prix ;
   - optionnels : `how_many_people`, `preparation_time`, `dificulty`,
     `category_names` (créées si absentes).
4. **Restituer** : coût matière calculé, prix conseillé, marge obtenue. Vérifier
   avec `get_recipe` / `list_recipes` si besoin.

## Garde-fous

- Quantités toujours en poids brut ; si l'utilisateur donne du poids net, convertir
  avec le rendement ou lui demander le brut.
- Ne jamais deviner un prix d'ingrédient : demander `price_per_unit` pour tout
  ingrédient nouveau, ou laisser le prix existant faire foi.
- Si la marge obtenue est inférieure à la marge cible annoncée, le signaler
  explicitement et proposer un ajustement (prix, portions, ingrédients).
