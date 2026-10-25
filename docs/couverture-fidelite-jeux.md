# Couverture MCP du moteur fidélité & jeux FoodEatUp (P4.1)

> Vérification outil par outil contre la liste réelle du serveur
> (`docs/inventaires/foodeatup-tools-live.txt`, 264 outils, session 2026-10-19).
> Règle d'honnêteté : un utilisateur qui demande « crée-moi un jeu » doit
> obtenir la vérité sur ce qui est faisable en MCP, pas une tentative qui échoue.

## Roues cadeaux

| Besoin | Outil MCP | Verdict |
|---|---|---|
| Lister les roues existantes | `list_wheel_games` | ✅ disponible (lecture) |
| Statistiques d'une roue | `get_wheel_stats` | ✅ disponible (lecture) |
| Créer une roue | `create_wheel_game` | ✅ disponible depuis 2026-10 — créée INACTIVE par défaut (`active: true` possible à la création) |
| Activer/désactiver une roue | — | ❌ aucun outil `update_wheel*` / `toggle_wheel*` |
| Modifier les lots | — | ❌ absent |

**Conclusion (mise à jour 2026-10-19) : création possible, pilotage ensuite en
back-office.** Claude peut créer une roue (segments, probabilités = 100 %, lots
fournis par le restaurateur), mesurer (stats) et détecter une roue à l'arrêt ;
l'activation ou la modification d'une roue existante se font dans le
**back-office FoodEatUp**.

## Sondages

| Besoin | Outil MCP | Verdict |
|---|---|---|
| Lister les sondages | `list_surveys` | ✅ disponible (lecture) |
| Résultats d'un sondage | `get_survey_results` | ✅ disponible (lecture) |
| Créer un sondage | `create_survey` | ✅ disponible depuis 2026-10 — créé INACTIF par défaut |
| Clore/diffuser un sondage | — | ❌ absent |

**Conclusion (mise à jour 2026-10-19) :** création possible (`create_survey`,
inactif par défaut), analyse par Claude ; clôture et diffusion en back-office. (Nuance : le serveur **RapidoCRM** expose
`create_sondage` et `lancer_sondage_entreprise` — c'est le sondage CRM B2B,
pas le sondage restaurant FoodEatUp ; ne pas les confondre.)

## Programme de fidélité, récompenses, bons, cartes cadeaux

| Besoin | Outil MCP | Verdict |
|---|---|---|
| Lire le programme (dont `active`) | `get_loyalty_program` | ✅ lecture |
| Modifier/réactiver le programme | `update_loyalty_program` | ✅ écriture — hook : confirmation |
| Compte de points d'un client | `get_loyalty_account` | ✅ lecture |
| Geste commercial sur les points | `adjust_points` | ✅ écriture — garde serveur ±1000 + motif, hook : confirmation |
| Catalogue de récompenses | `list_loyalty_rewards` / `upsert_loyalty_reward` | ✅ lecture + écriture |
| Bons émis / validation | `list_redemptions` / `validate_redemption` | ✅ (validation à usage unique, dédup serveur) |
| Cartes cadeaux | `list_gift_cards` / `check_gift_card` | ✅ lecture (pas de création par MCP) |

## Réponse type à « crée-moi un jeu » (mise à jour 2026-10)

> Je peux créer la roue cadeaux par MCP (`create_wheel_game`) : segments et
> probabilités (somme 100 %), lots chiffrés sur tes marges réelles, période,
> cooldown. Elle est créée **INACTIVE** — l'activation est ta décision, dans le
> back-office. Avant ça : 1) je vérifie que le programme de fidélité est actif
> (sinon le jeu ne produira rien), 2) je te propose les lots et leur coût à
> partir de tes marges réelles, 3) après activation, je suis les stats
> (`get_wheel_stats`) et le taux de capture (`get_loyalty_capture`).

Le skill `campagnes-restaurant` (plugin `foodeatup`) porte la création ; le
skill `boucle-7-fidelite` (plugin `foodeatup-boucles`) le diagnostic. La
distinction qui demeure : **créer = MCP, activer = back-office**.
