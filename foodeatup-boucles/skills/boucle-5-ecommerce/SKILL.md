---
name: boucle-5-ecommerce
description: Utiliser quand l'utilisateur veut l'état de la boucle ⑤ E-commerce/Vente — « où en est ma boucle vente », « bilan de mes canaux de vente », « mon site et mes commandes tournent-ils », « état réservations + caisse + site en un coup d'œil ». Diagnostic transversal des canaux d'encaissement, pas la gestion d'un service en cours.
---

# Boucle ⑤ — E-commerce / Vente & service

## Quand l'utiliser

Pour l'**état transversal des canaux de vente** : commandes, réservations,
caisse, site vitrine, zones de livraison, privatisations. La question de la
boucle : « par où l'argent entre-t-il, et quel canal fuit ? »

## Enchaînement d'outils MCP (l'ordre compte)

1. Demande : `list_orders` (période récente), `list_reservations` à venir,
   `reservation_availability` pour la capacité restante.
2. Encaissement : `get_pos_session` (session ouverte ?), `get_pos_report`,
   `list_pos_tabs` (ardoises ouvertes anormalement vieilles).
3. Site vitrine : `get_site_status` (publié ? domaine ? → `get_domain_status`),
   `get_site_stats` (trafic), `get_site_pages` (pages désactivées par erreur).
4. Canaux annexes : `list_delivery_zones`, `list_happy_hours`,
   `list_private_event_requests` (demandes sans réponse = clients perdus).
5. Écritures courantes : `update_order_status`, `confirm_reservation`,
   `update_event_request_status`, `upsert_delivery_zone`, `upsert_happy_hour`,
   pages du site (`add_site_page`, `update_section`, `toggle_site_page`).

## Règles métier

- Une demande d'événement privé sans réponse depuis plus de 48 h passe en tête
  des actions.
- Un site non publié avec du trafic attendu, ou publié avec des pages vides,
  est une fuite du canal — le dire tel quel.
- Les statistiques de vente sous 3 commandes sur la période ne fondent **aucune**
  recommandation (échantillon insuffisant — règle partagée avec le skill
  `croisement-service`).

## Garde-fous (opérations exigeant confirmation)

Interceptés par le hook du plugin (confirmation humaine obligatoire) :
- `publish_site`, `apply_site_template` — visibles du public immédiatement ;
- `import_storefront_menu` — réécrit toute la carte vitrine ;
- `close_pos_session` — clôture Z irréversible ;
- `record_pos_payment` — argent réel.

## Sortie attendue

Un tableau `[canal | activité récente | anomalie | action proposée]` pour :
commandes, réservations, caisse, site, livraison, événements privés.

## Ce que ce skill NE fait PAS

- Gérer le service en cours (installer, encaisser une note, suivre une table)
  → skills `service-salle`, `caisse-du-jour`, `gestion-commandes` (plugin
  foodeatup).
- Construire la carte en ligne → skill `carte-vitrine`.
- Les campagnes qui amènent du trafic → skill `boucle-6-communication`.
