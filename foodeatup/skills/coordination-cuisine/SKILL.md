---
name: coordination-cuisine
description: Utiliser quand, pendant le service, l'utilisateur parle du pass, d'un plat prêt/en préparation, du KDS ou de coordonner cuisine et salle. Fait avancer les plats commande par commande (update_kds_item_status) et propose le passage de la commande quand tout est prêt.
---

# Coordination cuisine (pass / KDS)

Pendant le service, la cuisine dicte l'état des plats (« le tartare de la 12
est prêt ») et ce skill tient le KDS à jour, plat par plat, jusqu'au passage
de la commande complète. Complète `gestion-commandes` (statut de la COMMANDE)
en travaillant au niveau de l'ITEM.

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.

## Machine à états d'un plat (KDS)

`pending → in_progress → ready → served` — vérifié serveur.
`served` existe côté serveur (plat envoyé en salle) : l'utiliser quand la
salle confirme l'envoi, pas avant. Pas de saut en arrière sans demande
explicite.

## Workflow

1. **Vue du pass** — `list_orders` (`establishment_id`,
   `status: "en_preparation"` — ajouter `confirmee` si la cuisine veut voir ce
   qui arrive) : commandes en cours avec leurs items. L'`item_id` d'un plat
   est l'ID de l'ITEM DE COMMANDE (ligne `boutique_commande_items` renvoyée
   dans la commande) — jamais l'ID du plat au menu.
2. **Résoudre les noms dictés à l'oral** — quand l'utilisateur nomme un plat
   (« le burger », « la 12 »), croiser d'abord avec les items des commandes en
   cours ; si le nom reste ambigu, `search_entities` (`establishment_id`,
   `query`, `types: ["dish", "table"]`) pour retrouver le plat ou la table —
   si `ambiguous=true`, DEMANDER confirmation avant d'agir. Ne jamais deviner
   quel item d'une commande correspond à un nom flou.
3. **Faire avancer les plats** — `update_kds_item_status`
   (`establishment_id`, `item_id`, `status`) plat par plat :
   `pending → in_progress` quand la cuisine attaque, `→ ready` quand le plat
   est au pass, `→ served` quand la salle l'a envoyé. Annoncer chaque
   changement (« Tartare table 12 → prêt »).
4. **Commande complète** — quand TOUS les plats d'une commande sont `ready`,
   le signaler et PROPOSER `update_order_status` (`order_id`,
   `status: "prete"`) — décision de l'utilisateur, jamais automatique
   (machine à états des commandes : voir `gestion-commandes`).

## Garde-fous

- Item ≠ plat au menu : `update_kds_item_status` prend l'ID de la ligne de
  commande. En cas de doute, relister la commande (`get_order`) avant d'agir.
- Un nom ambigu (plusieurs commandes contiennent le même plat) = question à
  l'utilisateur, jamais un choix silencieux.
- Le passage de la commande en `prete` est PROPOSÉ, pas imposé : la cuisine
  peut vouloir tenir un plat au chaud.
- Récapituler en fin de séquence : items avancés (IDs + nouveaux statuts),
  commandes proposées au passage.
