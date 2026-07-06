# Directives communes d'utilisation des outils (rapido-meta-ads)

Règles applicables à TOUTE exécution de skill de ce plugin — LE PLUS VERROUILLÉ
de la marketplace : il peut dépenser de l'argent réel.
OBLIGATOIRE avant tout appel facebook-ads : charger
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-meta-ads.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md`.

## 1. Résolution d'ID et de contexte d'abord

- `ads_get_ad_accounts` AVANT toute création : devise (`currency`),
  `min_daily_budget_cents`, compte activé pour le MCP (`is_ads_mcp_enabled`).
- Pages via `ads_get_ad_account_pages` / `ads_get_user_pages` ; comptes IG via
  `ads_get_ig_accounts`. Jamais d'ID inventé (intérêts, pixels, audiences).
- `advertiser_request` : les mots EXACTS de l'utilisateur, à chaque appel.

## 1 bis. Base de connaissance entreprise (./rapido-kb/)

- `processus-internes.md` : PLAFOND de budget/jour (défaut 50 €), politique de
  remise pour les offres mises en avant.
- `propositions-valeur.md` + `ton-et-accroches.md` + `charte-graphique.md` :
  les créatifs et textes de pub.
- `cibles-personas.md` : le ciblage (zones, langages).
- `concurrents.md` : la veille publicitaire.
Sans KB : défauts du secteur, en le signalant.

## 2. Argent réel — confirmations étagées

- Création (campagne/ad set/ad/boost plan) : autorisée, tout naît en PAUSED.
- `ads_boost_ig_post` `confirmed: true`, `ads_activate_entity`, modification
  de budget, étude de lift, suppression d'audience : confirmation explicite
  avec récapitulatif chiffré (coût max estimé). Les hooks du plugin forcent
  ces confirmations et un plafond de budget — ne pas les contourner.
- Toujours donner le coût MAXIMUM estimé (budget/jour × durée), pas le budget
  journalier seul.

## 3. Ne jamais inventer de données

Budgets, cibles, offres, chiffres de pub : de l'utilisateur, du CRM/CMS ou de
la KB. Métriques : uniquement via les outils insights avec période explicite.

## 4. Gestion d'erreur

Lire le message d'erreur Meta (`ads_get_errors` pour le contexte compte) :
« Must Use Campaign Bid Strategy » = budget en double (CBO), objectif rejeté =
non-ODAX, budget rejeté = sous `min_daily_budget_cents`. Expliquer, corriger
UNE fois, sinon remonter. Jamais de retry aveugle sur un outil qui dépense.

## 4 bis. Dégradation propre

Si les outils facebook-ads sont ABSENTS de la session (connecteur non
activé, compte non autorisé) : le dire en une phrase, indiquer la marche à
suivre (activer le connecteur Meta / vérifier `is_ads_mcp_enabled` du
compte), et faire ce qui reste possible (préparer les créatifs via
Canva/CMS, l'audience côté CRM, le plan de campagne — prêt à lancer une fois
connecté). Jamais d'erreur brute.

## 5. Récapitulatif de fin de séquence

Objets créés avec IDs et STATUT (PAUSED/ACTIVE en toutes lettres), budgets en
devise réelle + coût max, audiences créées (taille), événements pixel,
liens CRM/CMS (campagne liée, notes) — et ce qui attend une confirmation.
