---
name: fidelite-restaurant
description: Utiliser quand l'utilisateur parle de fidélité, de points, de récompenses, de cartes cadeaux, de bons à valider ou d'un geste commercial — « mon programme de fidélité », « ajoute des points à ce client », « crée une récompense », « valide ce bon », « vérifie cette carte cadeau », « qui sont mes clients fidèles ». Pilote le programme de fidélité FoodEatUp (points, récompenses, redemptions, cartes cadeaux). À NE PAS utiliser pour un visuel de carte de fidélité (rapidocms) ni une campagne emailing (rapidocrm).
---

# Fidélité restaurant (programme, points, récompenses, cartes cadeaux)

Pilote la fidélité **FoodEatUp** : configuration du programme, récompenses, bons
(redemptions), cartes cadeaux et gestes commerciaux. **Rien d'inventé** : points,
soldes et catalogues viennent des outils, jamais estimés.

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et l'appliquer.
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.
3. Charger les seuils fidélité maison de `./rapido-kb/` s'ils existent (ils priment).

## 1. État du programme (lecture d'abord)

- `get_loyalty_program` : modes de gain (`per_euro`/`per_visit`/`hybrid`), taux,
  validité des points, points par visite.
- `list_loyalty_rewards` (catalogue + stock), `list_redemptions` (bons émis/utilisés),
  `list_gift_cards` (cartes vendues, encaissé, soldes).

## 2. Configurer / faire évoluer le programme

- **`update_loyalty_program`** (options : `active`, `earn_mode`, `earn_rate`,
  `points_validity_months`, `visit_points`) — **affecte TOUS les clients** →
  **confirmation niveau 2** (récapituler l'avant/après avant d'écrire).
- **`upsert_loyalty_reward`** : `kind` ∈ `product`/`amount`/`perk`, `label`,
  `points_cost` (requis) ; `reward_id` pour une mise à jour. Pour `kind=product`,
  `plat_id` désigne un **vrai plat** (résolu via `search_entities` / `list_dishes`)
  offert à 0 €. `stock`/`active` optionnels.

## 3. Geste commercial — ajout de points

`adjust_points` : `email`, `points`, `motif` (**obligatoire**). Le serveur **plafonne
à ±1000**, refuse un solde négatif et **journalise** le geste. Le skill **explique le
geste et le fait confirmer** (visible client, affecte le solde) — jamais d'ajustement
silencieux. Au-delà de ±1000, le fractionner en le disant, ou refuser.

## 4. En salle — valider un bon, vérifier une carte cadeau

- `validate_redemption` (`code`) : **usage unique** — la **déduplication est portée par
  le serveur**, ne pas re-tenter en cas de doute, relire `list_redemptions`.
- `check_gift_card` (`code`) : solde et validité avant encaissement.

## 5. Analyse — clients fidèles

Croiser `list_redemptions` + `list_gift_cards` (FoodEatUp) avec les points côté CRM
(`rapidocrm:get_loyalty_points` — même client, vision transverse). Restituer un top
clients **chiffré** (aucune estimation).

## Passerelles

- Visuel de récompense / carte → `rapidocms:studio-visuel-marque`. Emailing fidélité →
  `rapidocrm:campagne-marketing`. Points côté CRM → `rapidocrm:animation-client`.
- Jeux (roue) et sondages : outils exposés (`list_wheel_games`, `get_wheel_stats`,
  `list_surveys`, `get_survey_results`) — volet animation à venir (schémas à finaliser).

## Règles

- **Confirmation** : `update_loyalty_program` (tous clients, niveau 2), `adjust_points`
  (geste visible client), écritures récompenses. Le hook `garde-destructif` gate
  `adjust_points`/`update_loyalty_program` en `ask`.
- **Garde-fous serveur respectés** : ±1000 et motif sur `adjust_points` ; usage unique
  sur `validate_redemption` ; `kind=product` → plat réel.
- **Rien d'inventé** : soldes, points, stocks et récompenses viennent des outils.
