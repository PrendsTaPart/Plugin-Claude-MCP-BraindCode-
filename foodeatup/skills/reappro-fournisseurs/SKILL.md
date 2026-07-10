---
name: reappro-fournisseurs
description: Utiliser quand l'utilisateur parle de stock bas, de commande fournisseur ou de réapprovisionnement. Enchaîne détection des stocks bas → commande fournisseur → réception (contrôle HACCP + ajustement du stock).
---

# Réapprovisionnement fournisseurs

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

1. **Détecter les stocks bas** — `list_low_stocks` (`establishment_id`) : articles
   avec `is_low = true`. Présenter la liste à l'utilisateur avec les quantités.
2. **Préparer la commande** — regrouper les articles par fournisseur. Retrouver le
   `fournisseur_id` via `list_suppliers` / `get_supplier` ; si un article n'a pas de
   fournisseur évident, demander à l'utilisateur.
3. **Commander** — `create_supplier_order` (`establishment_id`, `fournisseur_id`,
   `items` = tableau `{ingredient_id, quantity, unit}`, `note` optionnelle).
   Faire valider le contenu (articles + quantités) par l'utilisateur AVANT l'appel :
   une commande engage un achat.
4. **Suivre les livraisons attendues** — `list_deliveries`
   (`establishment_id`, `status` ∈ en_attente, reçue, annulee) : ce qui doit
   arriver, ce qui est arrivé, ce qui a été annulé.
5. **À réception de la livraison** :
   a. **Contrôle HACCP** — `create_haccp_reception` (`establishment_id`,
      `date_controle`, `heure_controle`, `etat_livraison` = `conforme` |
      `non_conforme`, avec `non_conformites` si non conforme,
      `temperature_produits_frais` et `reference_bl` si connus).
   b. **Enregistrer la dépense** — `create_expense` (`establishment_id`,
      `items` = `[{name, quantity, unit_price ; tax_rate}]`, `supplier_id`,
      `supplier_invoice_reference`, `status` ∈ payee, en_attente, decline —
      défaut en_attente ; totaux auto-calculés) APRÈS confirmation : une
      dépense enregistre de l'argent sorti. Détail : `get_expense`
      (`expense_id`).
   c. **Mise à jour du stock** — `adjust_stock` (`establishment_id`,
      `establishment_product_id` = champ `id` retourné par `list_products`,
      `quantity`, `mode` = `increment` pour AJOUTER la quantité reçue — ne pas
      utiliser `set` qui remplace la valeur, sauf inventaire complet).

## Garde-fous

- Jamais de commande fournisseur sans validation explicite de l'utilisateur sur les
  articles, quantités et fournisseur.
- À réception : le contrôle HACCP (4a) se fait AVANT l'ajustement de stock (4b) ;
  ne pas entrer en stock une livraison `non_conforme` sans accord de l'utilisateur.
- `mode: increment` pour une réception partielle ou totale ; `mode: set` réservé aux
  inventaires (confirmer avant, car il écrase la valeur existante).
