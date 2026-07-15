---
name: service-salle
description: Utiliser quand l'utilisateur parle de réservation, d'installer un client, de plan de salle, de file d'attente ou de table libre. Gère le cycle réservation → installation → suivi des tables d'un restaurant.
---

# Service en salle

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — fuzzy FR géré par le
   serveur (accents, pluriels) ; si `ambiguous=true`, présenter les
   candidats et DEMANDER confirmation avant d'agir. Jamais d'ID deviné.

## Machine à états des tables (à respecter strictement)

`free → reserved → occupied → cleaning → free` (+ statut `blocked` pour mise hors
service). Ne jamais sauter un état ni installer un client sur une table non libre.

## Workflow réservation

1. **Disponibilité d'abord** — appeler `reservation_availability`
   (`establishment_id`, `date` YYYY-MM-DD, `time` HH:MM, `party_size`) AVANT toute
   création. Si le créneau est indisponible, proposer une alternative ou la file
   d'attente — ne JAMAIS créer de réservation en double-booking.
2. **Créer** — `create_reservation` (`establishment_id`, `customer_name`,
   `party_size`, `date`, `time` ; optionnels : `customer_phone`, `customer_email`,
   `table_id` pour une table précise, `zone` ex. terrasse, `notes`).
3. **Confirmer** — `confirm_reservation` (`establishment_id`, `reservation_id`) :
   assigne une table si besoin, la table passe en `reserved`.
4. **Check-in à l'arrivée** — `checkin_reservation` (`establishment_id`,
   `reservation_id`, `table_id` si non encore assignée) : la table passe en
   `occupied` et la commande sur place est créée automatiquement — ne pas créer de
   commande séparée avec `create_order`.
5. **Absence / annulation** — `no_show_reservation` ou `cancel_reservation`
   (`establishment_id`, `reservation_id`). Actions irréversibles : demander
   confirmation explicite à l'utilisateur avant d'appeler.

## Suivi des tables

- **Vue d'ensemble** — `floor_plan_status` (`establishment_id`) : compteurs par
  statut + commande active par table. Consulter avant de choisir une table.
- **Changement d'état** — `update_table_status` (`establishment_id`, `table_id`,
  `status` ∈ free|reserved|occupied|cleaning|blocked). Après départ des clients :
  passer par `cleaning` puis `free`, jamais directement `occupied → free`.

## File d'attente (sans réservation)

1. `add_waitlist` (`establishment_id`, `party_size` ; `customer_name`,
   `customer_phone` recommandés).
2. Quand une table se libère (vérifier via `floor_plan_status` ou `list_waitlist`) :
   `seat_waitlist` (`establishment_id`, `waitlist_id`, `table_id`) — installe le
   client et crée la commande sur place.

## Garde-fous

- Toujours vérifier la disponibilité avant de créer ou déplacer une réservation.
- N'installer un client (`checkin_reservation`, `seat_waitlist`) que sur une table
  au statut `free` ou `reserved` pour lui.
- Confirmation utilisateur obligatoire avant `cancel_reservation` et
  `no_show_reservation`.

## Fichier clients (ajout SYNC S1)

Gérer le fichier clients du restaurant : `create_client` (`nom` requis ; email/téléphone/
adresse optionnels), `get_client`, `list_clients` (recherche, statut), `update_client`.
**`delete_client` = irréversible → confirmation** (hook `garde-destructif`). Le CRM
(plugin rapidocrm) reste la référence B2B ; ici, c'est le fichier resto.
