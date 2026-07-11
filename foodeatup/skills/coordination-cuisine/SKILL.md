---
name: coordination-cuisine
description: Utiliser quand, pendant le service, l'utilisateur parle du pass, de l'écran cuisine (KDS), d'un plat prêt, en préparation ou à lancer, ou de coordonner cuisine et salle. Fait avancer les plats commande par commande (update_kds_item_status), signale les commandes qui attendent trop et propose le passage quand tout est prêt.
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
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — fuzzy FR géré par le
   serveur (accents, pluriels) ; si `ambiguous=true`, présenter les
   candidats et DEMANDER confirmation avant d'agir. Jamais d'ID deviné.

## Machine à états d'un plat (KDS)

`pending → in_progress → ready → served` — vérifié serveur.
Transitions STRICTES : **jamais de saut en avant** (pending ne passe pas
directement à ready), **jamais de retour arrière sans confirmation
explicite**. `served` (plat envoyé en salle) : uniquement quand la salle
confirme l'envoi.

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
5. **Commandes qui attendent** — à chaque vue du pass, signaler toute
   commande en cours depuis plus que le seuil maison
   (`./rapido-kb/processus-internes.md`, défaut 15 min) : « ⏱ table 7
   attend depuis 18 min ». Proposer l'action, ne pas la décider.

## Mode coup de feu

Pendant le service : réponses ULTRA-COURTES — une ligne par action
(« ✅ Tartare table 12 → prêt »), pas de récapitulatif intermédiaire, un
« ✅ » de l'utilisateur vaut confirmation de la dernière proposition. Le
récapitulatif complet (IDs, statuts, retards) se fait EN FIN DE SERVICE.
L'agent `chef-de-pass` incarne ce mode.

## Garde-fous

- Item ≠ plat au menu : `update_kds_item_status` prend l'ID de la ligne de
  commande. En cas de doute, relister la commande (`get_order`) avant d'agir.
- Un nom ambigu (plusieurs commandes contiennent le même plat) = question à
  l'utilisateur, jamais un choix silencieux.
- Le passage de la commande en `prete` est PROPOSÉ, pas imposé : la cuisine
  peut vouloir tenir un plat au chaud.
- Récapituler en fin de séquence : items avancés (IDs + nouveaux statuts),
  commandes proposées au passage.
