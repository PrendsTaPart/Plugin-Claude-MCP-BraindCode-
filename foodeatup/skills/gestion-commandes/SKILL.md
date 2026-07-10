---
name: gestion-commandes
description: Utiliser quand l'utilisateur veut créer une commande, suivre les commandes en cours ou changer le statut d'une commande (confirmée, en préparation, prête, livrée) dans son restaurant.
---

# Gestion des commandes

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — fuzzy FR géré par le
   serveur (accents, pluriels) ; si `ambiguous=true`, présenter les
   candidats et DEMANDER confirmation avant d'agir. Jamais d'ID deviné.

## Machine à états des commandes (à respecter strictement)

`en_attente → confirmee → en_preparation → prete → livree` (+ `annulee`).
Pas de saut d'étape en avant (une commande ne passe pas de `en_attente` à
`prete`) ; `annulee` possible depuis tout état non terminé mais avec
confirmation explicite de l'utilisateur.

## Workflow

1. **Créer une commande** — `create_order` (`establishment_id`, `items` =
   `[{name, quantity, unit_price, tax_rate}]`) :
   - prix et TVA depuis `list_dishes`/`list_products` — jamais de tête (TVA
     selon la nature : immediate 10 %, conservable 10 %/5,5 %, alcohol 20 %) ;
   - `service_mode` ∈ livraison | emporter | sur_place ; `channel` (défaut
     manuel) ; `covers` ;
   - SUR PLACE : passer `table_id` — la commande est liée à la table du plan
     de salle. Rappel : `checkin_reservation` et `seat_waitlist` créent DÉJÀ
     la commande — ne pas en créer une seconde pour la même table ;
   - LIVRAISON/EMPORTER : `customer_name`, `customer_phone`,
     `customer_address` si livraison ;
   - la création génère AUTOMATIQUEMENT facture + devis : ne pas appeler
     `create_invoice` en plus.
2. **Suivre** — `list_orders` (filtres) / `get_order` : commandes en cours par
   statut ; croiser avec `floor_plan_status` pour la vue salle.
3. **Avancer les statuts** — `update_order_status` (`establishment_id`,
   `order_id`, `status`) en respectant la machine à états.
   - Effets de bord automatiques : le statut se répercute sur la facture/devis
     liés, et une commande payée passe la table en `cleaning` — ne pas
     déplacer la table à la main en plus (voir `service-salle`).
4. **Annulation** — `update_order_status` avec `annulee` : action
   irréversible, confirmation explicite obligatoire, motif consigné en note.

## Garde-fous

- Jamais de commande sans articles vérifiés (nom, quantité, prix unitaire,
  TVA) et validés par l'utilisateur.
- Une commande de table existante se retrouve via `floor_plan_status` (la
  commande active y figure) — ne pas en créer une en double.
- Récapituler en fin de séquence : commandes créées (IDs), changements de
  statut, impacts table/facture.
