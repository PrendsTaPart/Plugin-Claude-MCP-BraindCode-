---
name: boucle-8-comptabilite
description: Utiliser quand l'utilisateur veut l'état de la boucle ⑧ Comptabilité — « où en est ma boucle compta », « bilan factures, devis et dépenses », « qu'est-ce qui traîne en facturation », « synthèse financière du mois ». Diagnostic des flux facturés (impayés, devis en attente, dépenses), pas la comptabilité générale ni la trésorerie bancaire.
---

# Boucle ⑧ — Comptabilité (factures, devis, dépenses)

## Quand l'utiliser

Pour l'**état des flux facturés** dans FoodEatUp : factures impayées, devis sans
réponse, dépenses de la période, synthèse financière. La question de la boucle :
« ce qui a été vendu a-t-il été facturé, et ce qui a été facturé, payé ? »

## Enchaînement d'outils MCP (l'ordre compte)

1. `finance_summary` pour le cadre (période, totaux).
2. `list_invoices` filtré par statut : impayées et en retard d'abord —
   proposer `update_invoice_status` seulement sur preuve de paiement.
3. `list_quotes` : devis en attente, relances à faire (la relance elle-même
   passe par la boucle ⑥ et ses garde-fous d'envoi) ; `update_quote_status`
   quand le client a répondu.
4. `list_expenses` sur la période, `create_expense` pour saisir au fil de l'eau.
5. Rapprochement caisse : `get_pos_report` et `list_pos_payments` (boucle ⑤)
   vs factures — les écarts sont le livrable le plus utile.
6. `create_invoice` / `create_quote` à la demande (note : `create_order` génère
   déjà facture + devis automatiquement — ne pas doubler).

## Règles métier

- Un statut de facture ne passe à « payée » que sur information explicite de
  l'utilisateur, jamais par déduction.
- Les montants viennent des outils ; aucun total recalculé « de tête » —
  si un chiffre est absent, écrire « non disponible ».
- Les marges par plat ne sont pas ici → analyse via le skill
  `analyse-rentabilite-carte` (plugin foodeatup).

## Garde-fous (opérations exigeant confirmation)

- Aucune suppression de facture n'est exposée par le MCP (c'est sain).
- `record_pos_payment` (encaissement réel, boucle ⑤) est intercepté par le
  hook du plugin ; le rapprochement se fait en lecture.
- Toute écriture de statut (`update_invoice_status`, `update_quote_status`)
  est récapitulée avant exécution : facture, montant, ancien → nouveau statut.

## Sortie attendue

Un tableau `[flux | volume | montant | plus ancien | action proposée]` pour :
factures impayées, devis en attente, dépenses de la période, écarts caisse.

## Ce que ce skill NE fait PAS

- Trésorerie bancaire, prévisionnel, unit economics → plugin rapido-startup.
- Facturation CRM (clients B2B hors restaurant) → plugin rapidocrm.
- Encaisser → skill `caisse-du-jour` (plugin foodeatup).
