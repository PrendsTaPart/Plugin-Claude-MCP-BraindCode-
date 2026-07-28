# Couverture MCP du moteur fidélité & jeux FoodEatUp (P4.1)

> Vérification outil par outil contre la liste réelle du serveur
> (`docs/inventaires/foodeatup-tools-live.txt`, 177 outils, session 2026-07-28).
> Règle d'honnêteté : un utilisateur qui demande « crée-moi un jeu » doit
> obtenir la vérité sur ce qui est faisable en MCP, pas une tentative qui échoue.

## Roues cadeaux

| Besoin | Outil MCP | Verdict |
|---|---|---|
| Lister les roues existantes | `list_wheel_games` | ✅ disponible (lecture) |
| Statistiques d'une roue | `get_wheel_stats` | ✅ disponible (lecture) |
| Créer une roue | — | ❌ aucun outil `create_wheel*` sur le serveur |
| Activer/désactiver une roue | — | ❌ aucun outil `update_wheel*` / `toggle_wheel*` |
| Modifier les lots | — | ❌ absent |

**Conclusion : lecture seule.** Création, activation et paramétrage des lots se
font dans le **back-office FoodEatUp**. Claude peut : mesurer (stats), détecter
une roue à l'arrêt, proposer la configuration à saisir — pas l'exécuter.

## Sondages

| Besoin | Outil MCP | Verdict |
|---|---|---|
| Lister les sondages | `list_surveys` | ✅ disponible (lecture) |
| Résultats d'un sondage | `get_survey_results` | ✅ disponible (lecture) |
| Créer un sondage | — | ❌ aucun outil `create_survey` sur le serveur |
| Clore/diffuser un sondage | — | ❌ absent |

**Conclusion : lecture seule.** Même partage que la roue : analyse par Claude,
création en back-office. (Nuance : le serveur **RapidoCRM** expose
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

## Réponse type à « crée-moi un jeu »

> Je ne peux pas créer la roue cadeaux par MCP — le serveur n'expose que la
> lecture (`list_wheel_games`, `get_wheel_stats`). Voici ce que je peux faire :
> 1) vérifier que le programme de fidélité est actif (sinon le jeu ne produira
> rien), 2) te proposer les lots et leur coût à partir de tes marges réelles,
> 3) te donner la configuration exacte à saisir dans le back-office FoodEatUp,
> 4) suivre les stats de la roue une fois créée.

Le skill `boucle-7-fidelite` (plugin `foodeatup-boucles`) et le skill
`fidelite-restaurant` (plugin `foodeatup`) appliquent cette distinction
« pilotable par Claude » / « à faire en back-office ».
