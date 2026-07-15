---
name: caisse-du-jour
description: Utiliser quand l'utilisateur parle de caisse, de POS, d'ouvrir la caisse, d'encaisser une note, de rendu monnaie, de clôture Z, de rapport de caisse ou d'ardoises clients — « ouvre la caisse », « encaisse la table 5 », « fais le Z », « rapport de caisse ». Pilote la session de caisse FoodEatUp : ouverture, encaissements, rapport X/Z, clôture. À NE PAS utiliser pour la facturation (gestion-commandes) ni l'analyse de marge (margin-analyzer).
---

# Caisse du jour (POS FoodEatUp)

Cycle **ouverture → encaissements → rapport → clôture Z**. **Argent réel** : chaque
encaissement et la clôture sont **confirmés**. Rien d'inventé (montants, modes, rendu
viennent du serveur).

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et l'appliquer.
2. S'assurer d'avoir l'`establishment_id` (le demander si absent).
3. Un encaissement/une clôture exige un **opérateur** (`operator_id` = employé avec la
   permission caisse) — le résoudre via `list_employees` si besoin, jamais deviné.

## 1. Ouvrir la caisse

`open_pos_session` : `opening_float` (fond de caisse), `operator_id`. Vérifier qu'aucune
session n'est déjà ouverte (`get_pos_session`) avant d'ouvrir.

## 2. Encaisser une note

`record_pos_payment` : `order_id`, `amount`, `method` ∈
`especes`/`carte`/`titre_restaurant`/`cheque`, `operator_id` ; `tendered` (espèces, pour
le **rendu**). **Argent réel → confirmation** avant l'appel.
- **`titre_restaurant`** : **jamais de rendu** (ne pas renseigner un rendu).
- La note est **soldée quand le reste dû = 0** — vérifier avec `list_pos_payments`
  (paiements, montants, rendu, reste dû) plutôt que de supposer.

## 3. Rapport de caisse (X / Z)

`get_pos_report` : sans `session_id` = **rapport X** (session en cours) ; avec
`session_id` = **rapport Z** (session clôturée). CA, ticket moyen, par mode, par
opérateur, TVA, remises — **restitués tels quels**.

## 4. Clôturer (Z)

`get_pos_session` pour l'état, puis **clôture Z** : `close_pos_session` (`operator_id`,
`confirm` ; `counted_cash` optionnel pour le comptage des espèces, **écart calculé par le
serveur**). Le serveur **exige `confirm:true`** → le skill **résume le rapport X à
l'opérateur** (CA, écart annoncé) **puis** confirme, **jamais `confirm:true` d'office**.
Après clôture, présenter le Z (`get_pos_report` avec le `session_id`).

> Ardoises clients ouvertes (soldes dus) : `list_pos_tabs` — le règlement se fait en
> caisse (`record_pos_payment`).

## Passerelles

- Facture / devis d'une commande → `gestion-commandes`. Analyse marge/prix →
  `margin-analyzer` / `price-check`. Synthèse financière → `finance_summary`
  (skill `analyse-rentabilite-carte`).

## Règles

- **Argent réel** : `record_pos_payment` et `close_pos_session` **confirmés** (hook
  `garde-destructif` les gate en `ask`) ; `confirm:true` **jamais** posé d'office.
- **Modes de paiement** = enum strict ; `titre_restaurant` sans rendu.
- **Opérateur réel** (permission caisse) requis ; note soldée = reste dû 0.
- **Rien d'inventé** : montants, écarts et rendus viennent du serveur.
