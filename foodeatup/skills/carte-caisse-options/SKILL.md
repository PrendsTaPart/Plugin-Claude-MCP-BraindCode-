---
name: carte-caisse-options
description: Utiliser quand l'utilisateur veut modifier sa carte telle que la caisse, la borne et le QR de table la vendent — catégories de plats, formules (menus à prix fixe), options (cuissons, suppléments, retraits), changements de prix ou de TVA en masse, photos de plats en lot, plat épuisé aujourd'hui, suivi des portions, ou état de la synchronisation HubRise avec les plateformes de livraison.
---

# Carte en caisse : catégories, formules, options, ruptures

Complète `carte-vitrine` (carte en ligne, `import_storefront_menu`) : ici, la
carte **vendue** en caisse, borne, QR de table et boutique.

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — si `ambiguous=true`,
   présenter les candidats et DEMANDER confirmation. Jamais d'ID deviné.

## 1. Catégories de plats

- `list_dish_categories` AVANT toute création : catégories de **plats**
  (≠ `list_categories` = ingrédients/produits), parent (2 niveaux), visibilité
  vitrine, nombre de plats.
- `update_dish_category` (`category_id` ; `name`, `parent_id` — null = premier
  niveau —, `description`, `show_on_storefront`).
- `delete_dish_category` : refusé s'il reste des plats actifs sauf
  `reassign_to`. Aperçu sans `confirm`, puis `confirm: true` après accord.

## 2. Formules vendables

- `list_formules` : formules telles que la caisse les vend, avec « vendable »
  ou la raison sinon (étape sans plat relié, formule de brochure).
- `save_formule` (`title`, `price` TTC, `steps` : `[{title, min, max,
  choices: [{dish_id, price_delta}]}]` ; `formule_id` pour remplacer). À
  préférer à un faux plat « Menu … » : chaque composant garde SA TVA,
  ventilation automatique. Remplacer désactive les anciennes étapes →
  confirmer.

## 3. Options (cuissons, suppléments, retraits)

- `list_option_groups` : groupes, choix, prix, rattachements.
- `save_option_group` (`name`, `type` ∈ choix | supplement | retrait, `items`
  `[{label, price_delta, id}]`, `min`, `max` — null = sans limite) : à préférer
  aux faux plats « Supplément … ». Un choix absent d'une modification est
  désactivé, jamais supprimé.
- `link_option_group` (`group_id`, `category_ids` et/ou `dish_ids` ; `mode:
  retire` sur un plat pour retirer un groupe hérité ; `remove: true` détache).

## 4. Modifications en masse

- `bulk_update_dishes` : `items` (valeurs par plat) OU `dish_ids` + `set`
  (`price`, `tva_nature`, `category_id`, `active`). Tout ou rien, 500 max.
  Appeler **sans `confirm`** → aperçu avant/après à faire valider, puis
  `confirm: true`.
- `bulk_update_dish_images` (`items` `[{dish_id, image_url}]`, 50 par appel,
  URL https directes) : résultat ligne par ligne ; remplacer une photo
  existante exige `confirm: true`.
- Ingrédients en masse → `bulk_update_ingredients` (skill `reappro-fournisseurs`).

## 5. Service du jour : ruptures et portions

- `set_dish_sold_out` (`dish_ids`, `sold_out`) : épuisé **aujourd'hui** partout
  (caisse, QR, borne, boutique, menu boards) ; retombe seul à la bascule de
  journée. Retrait durable = `update_dish` `active: false`, pas cet outil.
- `get_dish_portions` (`dish_id` optionnel) : solde, portions encore vendables.
- `set_dish_portions` (`dish_id` ; `suivi`, `portions_par_vente`,
  `seuil_alerte`, `count` = inventaire compté, `loss` + `motif` = perte) —
  chiffres DICTÉS par l'utilisateur uniquement.

## 6. Plateformes (HubRise)

`get_hubrise_status` : connexion, plats sans `sku_ref` (bloqués au push),
commandes en attente côté plateformes. Signaler les plats bloqués.

## Garde-fous

- Prix et TVA : fournis par l'utilisateur ou issus de `list_dishes` /
  `recette-cout-marge`, jamais de tête. Nature TVA : voir `pieges-outils.md`.
- Écritures en masse et suppressions : aperçu → confirmation (hook
  `garde-destructif`), jamais `confirm: true` d'office.
- Récapituler : catégories, formules, groupes d'options (IDs), plats modifiés,
  ruptures posées/levées.
