# foodeatup-tutoriel

L'**Académie FoodEatUp** dans Claude : se former, enseigner et fabriquer des
cours — reliés aux vrais besoins du restaurant que les plugins `foodeatup`
détectent. Le principe : **la formation part du symptôme** (une erreur de
caisse, un registre HACCP troué), pas d'un catalogue.

## Les 4 skills (un par rôle) + l'agent

| Rôle | Skill | Outils couverts |
|---|---|---|
| Apprenant | `se-former-foodeatup` | `academy_search`, `academy_list_parcours`, `academy_get_parcours`, `academy_get_cours`, `me_progression`, `me_mark_cours_complete`, `me_favorites_add`/`me_favorites_remove`, `me_mes_achats`, `me_reservations_upcoming` |
| Formateur | `enseigner-foodeatup` | `formateur_apprenants_list`, `formateur_agenda_list`, `formateur_revenus_summary` |
| Administrateur | `fabriquer-des-cours` | `admin_cours_create`, `admin_parcours_create`, `admin_prompt_create` (brouillons), `admin_publish_toggle` (confirmé), `admin_users_search`, `admin_user_role_set` (confirmé), `admin_candidatures_list`, `admin_paiements_summary`, `admin_mcp_audit_tail` |
| Tous | `prompts-academie` | `marketplace_list_prompts`, `marketplace_get_prompt`, `academy_get_public_link`, `academy_list_public_links` |

Agent : **`professeur-foodeatup`** — diagnostique la compétence manquante
depuis l'usage réel, recommande 1 à 3 cours avec leur raison, fait pratiquer
chaque cours avec le skill foodeatup correspondant.

Couverture : les **26 outils** du serveur (liste versionnée
`docs/inventaires/academy-foodeatup-tools-live.txt`, relevée en session
connectée du 2026-07-28 — serveur injoignable au moment de l'écriture du
plugin, liste à re-vérifier à la prochaine connexion).

## Garde-fous

- **Règle du serveur, relayée partout** : tout contenu créé par l'IA reste en
  **brouillon** (`published=false`) — un humain valide dans
  `/admin/contenu-cours`. Toutes les actions sont journalisées côté serveur.
- Hook `garde-academie.py` (testé en CI) : `admin_publish_toggle` (publication
  visible des apprenants) et `admin_user_role_set` (gouvernance des comptes)
  exigent une confirmation humaine.
- Jamais de cours marqué complet à la place de l'apprenant ; progression lue,
  jamais estimée.

## Prérequis

- Serveur **MCP Academy FoodEatUp** connecté :
  `export ACADEMY_FOODEATUP_MCP_URL=…` (URL d'instance — pas de valeur par
  défaut dans le dépôt). Sans lui, le plugin le dit et s'arrête.
- Les travaux pratiques renvoient aux plugins `foodeatup` (faire) — ce plugin
  apprend à faire, il n'exécute pas l'opération.

## Installation

```
/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
/plugin install foodeatup-tutoriel@rapido
```
