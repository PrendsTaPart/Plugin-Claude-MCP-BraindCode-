---
name: evenements-prives
description: Utiliser quand l'utilisateur parle de privatisation ou d'événement privé — « une demande de privatisation est arrivée », « réponds à la demande de groupe de samedi », « fais un devis pour cet anniversaire », « privatise la salle du fond ». Cycle demande → qualification → devis → réservation → facture pour les événements privés FoodEatUp.
---

# Événements privés & privatisations

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et l'appliquer.
2. S'assurer d'avoir l'`establishment_id` (le demander si absent).

## 1. Traiter les demandes entrantes

- `list_private_event_requests` : demandes en attente, la plus ancienne
  d'abord. **Une demande sans réponse depuis plus de 48 h passe en tête** —
  un événement se réserve ailleurs en deux jours.
- Qualifier chaque demande : date, nombre de couverts, budget, besoins
  (menu, boissons, matériel). Ce qui manque se demande au client, ne se
  suppose pas.

## 2. Vérifier la faisabilité (lecture)

- `reservation_availability` sur la date : capacité restante, conflit avec le
  service normal.
- Croiser avec `list_reservations` (le soir est-il déjà chargé ?) et le
  planning d'équipe (`list_plannings`) : privatiser sans staff est un refus
  déguisé.

## 3. Chiffrer et répondre

- `create_quote` : devis à partir des vrais coûts (menus via `get_recipe`,
  boissons via `list_beverages`) — marge visible pour l'utilisateur avant envoi.
- `update_event_request_status` : accepter/refuser/répondre — chaque changement
  de statut est récapitulé (demande, client, décision) avant écriture.
- `update_quote_status` quand le client répond ; relance après 7 jours sans
  réponse (la relance passe par le skill `campagnes-restaurant` ou un contact
  direct, selon le canal du client).

## 4. Conclure

- Devis accepté → `create_reservation` (bloquer la date/salle) puis
  `create_invoice` (acompte ou solde, selon les conditions dites par
  l'utilisateur).
- Jour J : le service se pilote avec les skills `service-salle` et
  `coordination-cuisine` ; l'encaissement avec `caisse-du-jour`.

## Ce que ce skill NE fait PAS

- Les réservations ordinaires → skill `service-salle`.
- Les devis/factures hors événement → skill `boucle-8-comptabilite` (plugin
  foodeatup-boucles) pour le suivi, `caisse-du-jour` pour l'encaissement.
- La promotion des privatisations → skill `campagnes-restaurant`.
