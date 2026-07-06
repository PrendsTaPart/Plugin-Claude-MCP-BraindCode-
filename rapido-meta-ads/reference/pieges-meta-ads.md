# Pièges Meta Ads — règles OBLIGATOIRES (argent réel)

À charger avant TOUT usage des outils facebook-ads. Ce plugin peut dépenser de
l'argent réel : ces règles ne sont pas optionnelles.

## 1. ARGENT RÉEL — activation

- TOUT est créé en `PAUSED` : campagnes, ad sets, ads. Rien ne diffuse, rien
  ne dépense tant que ce n'est pas activé.
- `ads_activate_entity` = DÉBUT DE DÉPENSE → TOUJOURS une confirmation
  explicite avec récapitulatif : budget/jour, durée, cible, **coût maximum
  estimé** (budget/jour × jours).
- Activer du HAUT vers le BAS : campagne → ad set → ad. Les 3 niveaux doivent
  être ACTIVE pour diffuser ; activer une ad sous une campagne en pause ne
  diffuse rien (et inversement, activer la campagne en dernier déclenche tout).

## 2. BUDGETS — centimes et devise du compte

- Budgets TOUJOURS en centimes / plus petite unité de la devise du COMPTE.
- Lire `currency` et `min_daily_budget_cents` via `ads_get_ad_accounts` AVANT
  toute création — ne JAMAIS supposer USD ni convertir de tête.
- Vérifier aussi `is_ads_mcp_enabled` du compte (sinon les écritures échouent).

## 3. CBO — budget au niveau campagne (défaut)

- Le budget se met sur la CAMPAGNE (`ads_create_campaign`).
- Ne JAMAIS passer `daily_budget` sur un ad set dont la campagne parente porte
  déjà un budget → rejet « Must Use Campaign Bid Strategy ».
- Budget au niveau ad set : uniquement si la campagne n'en a pas (cas avancé).

## 4. OBJECTIFS — ODAX uniquement

- Valeurs autorisées : `OUTCOME_TRAFFIC`, `OUTCOME_SALES`, `OUTCOME_LEADS`,
  `OUTCOME_ENGAGEMENT`, `OUTCOME_AWARENESS`, `OUTCOME_APP_PROMOTION`.
  (Les anciens objectifs type CONVERSIONS/LINK_CLICKS sont rejetés.)
- Respecter la matrice objectif → `optimization_goal` de `ads_create_ad_set` ;
  utiliser le `recommended_optimization_goal` renvoyé par la CRÉATION de la
  campagne plutôt que deviner.

## 5. CIBLAGE

- Ne JAMAIS inventer d'IDs d'intérêts (ils sont numériques et introuvables de
  tête) — par défaut : ciblage LARGE par `geo_locations` (pour un restaurant :
  sa ville + rayon).
- Union européenne : les champs DSA (bénéficiaire/payeur) sont auto-remplis
  par l'outil — ne pas les bricoler.

## 6. BOOST INSTAGRAM — toujours en deux temps

1. `ads_boost_ig_post` avec `confirmed: false` → l'outil renvoie le PLAN
   résolu (budget dans la devise réelle du compte, durée, cible, media).
2. Montrer ce plan à l'utilisateur, obtenir l'accord.
3. SEULEMENT ALORS rappeler avec `confirmed: true`.
Le boost créé reste PAUSED : l'activation (`ads_activate_entity`) se confirme
séparément.

## 7. INSIGHTS

- `ads_get_ad_entities` EXIGE `time_range` ou `date_preset` pour toute
  métrique — sans période, pas de chiffres.
- Vérifier les champs disponibles avec `ads_get_field_context` AVANT la
  requête (ne pas demander un champ inexistant).

## 8. AUDIENCES

- PII : l'outil HASHE LUI-MÊME les emails/téléphones — envoyer les valeurs
  brutes telles quelles (pas de pré-hash, pas de normalisation maison).
- AVANT toute suppression d'audience : `ads_get_custom_audience_adsets` +
  avertir l'utilisateur que les ad sets liés seront MIS EN PAUSE.
- Lookalike : l'audience d'origine doit être une CUSTOM (jamais une lookalike
  comme origine), ratio 1 % par défaut, ne PAS demander de pays (déduit).

## 9. PIXEL

- Les événements sont créés INACTIVE → activer via `ads_pixel_event_update`
  puis VÉRIFIER dans Test Events (vérification guidée avec l'utilisateur).
- L'événement `Purchase` exige les paramètres `value` + `currency`.

## 10. advertiser_request — exigence du MCP

Recopier les MOTS EXACTS de l'utilisateur dans le paramètre
`advertiser_request` à CHAQUE appel d'outil facebook-ads — pas de paraphrase.

## 11. Catégories spéciales

Crédit, emploi, logement, politique/élections (`special_ad_categories` :
CREDIT, EMPLOYMENT, HOUSING, ISSUES_ELECTIONS_POLITICS) : si le secteur du
client est concerné, DEMANDER avant de créer — les déclarer change le ciblage
autorisé ; ne pas les déclarer expose au rejet/blocage du compte.
