# Garde-fous SEA (Google Ads)

> MCP officiel Google Ads **non connecté** ici : skills écrits d'après la grammaire
> documentée (lecture seule) ; noms d'outils exacts confirmés à la connexion.

## Lecture seule assumée
- Le MCP Google Ads est **read-only by design**. Ce plugin **analyse et recommande**,
  il **n'exécute pas** : les modifications se font **manuellement dans l'interface
  Google Ads**, guidées par des **instructions écran par écran**.
- **Jamais de promesse d'exécution** (« je lance », « j'active » interdits).
- Filet : hook `garde-ecriture-google-ads` (ask si un outil `mutate`/`create`
  apparaît — au cas où le serveur évoluerait vers l'écriture).

## Recommandations chiffrées
- **Toute recommandation cite sa donnée source** (campagne, période, métrique) —
  aucune affirmation sans chiffre.
- Les **budgets proposés respectent les plafonds** `./rapido-kb/` (budget pub max/jour),
  jamais un montant en dur.
- Calculs (CPA, ROAS, ratios) via `rapido-startup:catalogue-kpi` (source unique).

## Croisements
- **CPC/volumes** payants : via **DataForSEO Keywords** si le MCP Google Ads ne les
  expose pas — coût DataForSEO **annoncé** (même règle que rapido-seo).
- **Conversions** : croiser Google Ads et **GA4** (`run_report`) — signaler les
  **écarts de conversions** Google Ads vs GA4.
