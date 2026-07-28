---
name: catalogue-produits-crm
description: Utiliser quand l'utilisateur gère son catalogue de produits ou services CRM — « ajoute cette prestation au catalogue », « change le prix de ce produit », « liste mes produits », « ce produit n'existe plus ». Référentiel produits/services qui alimente devis et factures, pas le stock restaurant.
---

# Catalogue produits & services (CRM)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` si présent et
   l'appliquer.
2. Les prix viennent de l'utilisateur ou du catalogue existant — jamais
   inventés ni « estimés ».

## 1. Lire avant d'écrire

- `list_products` : le catalogue actuel — TOUJOURS avant une création (pas de
  doublon sous un nom voisin).
- `get_product` : la fiche exacte (prix, TVA, description) avant toute
  modification ou insertion dans un devis.

## 2. Créer et faire vivre

- `create_product` : nom, prix HT, TVA, description. Un produit se crée une
  fois — les variantes de prix se gèrent au devis, pas en dupliquant la fiche.
- `update_product` : récapituler l'avant/après (prix surtout : un changement
  de prix ne modifie PAS les devis déjà émis — le dire explicitement).
- `delete_product` : garde-fou du plugin (suppression confirmée) ; préférer
  une mention « obsolète » dans la description si le produit figure dans des
  devis/contrats actifs.

## 3. Le catalogue au service des devis

- Un devis (`create_devis`, skill `devis-facture-relance`) référence des
  produits du catalogue : vérifier ici que la fiche est à jour AVANT le devis,
  pas après l'envoi.
- Produits les plus vendus vs catalogue : croiser `list_products` avec
  `get_top_clients` et les devis récents (`list_devis`) pour repérer les
  fiches mortes et les prix qui n'ont pas suivi.

## Ce que ce skill NE fait PAS

- Devis, factures, relances → skill `devis-facture-relance`.
- Le stock et les produits du restaurant → plugin foodeatup
  (skill `production-stock`).
- Les contrats et leurs modèles → skill `contrats-clients`.
