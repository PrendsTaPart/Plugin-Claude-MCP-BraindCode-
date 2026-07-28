---
name: boissons-offres-livraison
description: Utiliser quand l'utilisateur parle de sa carte des boissons, d'un happy hour ou de ses zones de livraison — « ajoute ce cocktail à la carte », « retire ce vin », « mets un happy hour jeudi 18-20h », « jusqu'où je livre », « ajoute un quartier en zone de livraison ». Gère boissons, happy hours et zones de livraison FoodEatUp.
---

# Boissons, happy hours & zones de livraison

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et l'appliquer.
2. S'assurer d'avoir l'`establishment_id` (le demander si absent).

## 1. Carte des boissons

- `list_beverages` d'abord : l'existant, jamais de doublon par re-création.
- `upsert_beverage_item` : ajout OU mise à jour (l'upsert écrase sur le même
  nom — relire avant d'écrire, récapituler l'avant/après si l'item existe).
  TVA boissons : 10 % sans alcool servi, 20 % alcool — cohérence avec
  `list_tva` (skill `recette-cout-marge` pour le calcul de marge).
- `remove_beverage_item` : retrait définitif de la carte → confirmation
  explicite avec le nom exact de l'item.

## 2. Happy hours

- `list_happy_hours` avant tout : pas de chevauchement de créneaux sur les
  mêmes produits.
- `upsert_happy_hour` : créneau (jours, heures), produits/catégories ciblés,
  remise. Vérifier la marge au prix remisé (`get_recipe` pour les cocktails
  maison) : un happy hour à marge négative se signale AVANT d'écrire.
- Un happy hour sur un produit en stock bas (`list_low_stocks`) est une
  incohérence : le dire, proposer un autre produit.

## 3. Zones de livraison

- `list_delivery_zones` : zones actuelles, frais et minimums.
- `upsert_delivery_zone` : zone, frais de livraison, minimum de commande.
  Récapituler l'impact (« la zone X passe de 3 € à 5 € de frais ») avant
  d'écrire — les clients du site voient ces valeurs immédiatement.

## Ce que ce skill NE fait PAS

- La carte des plats et formules en ligne → skill `carte-vitrine`.
- Les recettes et marges des cocktails → skill `recette-cout-marge`.
- Communiquer sur un happy hour → skill `campagnes-restaurant`.
