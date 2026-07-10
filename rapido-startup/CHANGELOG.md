# Changelog — plugin rapido-startup

## 1.0.0 — 2026-07-10

- Squelette initial : `.mcp.json` (serveur Stripe officiel https://mcp.stripe.com
  + les 4 serveurs Rapido), références `directives-outils.md`,
  `pieges-outils.md` (pièges communs multi-serveurs + Stripe lecture seule,
  montants en centimes, format `post_heure`) et `seuils-defaut.md`
  (benchmarks finance/startup, utilisés SEULEMENT si absents de
  `./rapido-kb/`), hook déterministe `garde-stripe-write` (confirmation
  forcée sur toute écriture Stripe). Dossiers `agents/`, `skills/` et
  `tests/` prêts — skills à venir.
