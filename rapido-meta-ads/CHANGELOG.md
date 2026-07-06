# Changelog — plugin rapido-meta-ads

## 0.2.0 — 2026-07-06

- Passe de portabilité : section « dégradation propre » ; plafond du hook exprimé dans la devise du compte publicitaire et parsé avec ou sans symbole (€, code ISO, nu) — re-testé (4 cas).

## 0.1.0 — 2026-07-06

- Version initiale — LE PLUGIN LE PLUS VERROUILLÉ (argent réel) :
  `.mcp.json` (facebook-ads + rapidocms + rapidocrm + canva + lovable).
- Références : `pieges-meta-ads.md` (PAUSED partout, activation top-down avec
  coût max, budgets en centimes de la devise du compte, CBO, ODAX +
  recommended_optimization_goal, ciblage geo sans IDs inventés, boost en deux
  temps, insights avec période, audiences hashées par l'outil, pixel INACTIVE,
  advertiser_request en mots exacts, catégories spéciales), `CONFORMITE.md`
  (section Publicité : base légale RGPD pour les audiences clients, catégories
  spéciales, conservation des exports interdite), `directives-outils.md`.
- Hooks testés (10 cas) : `garde-argent-reel.py` (ask sur activate, boost
  confirmed=true, update de budget, delete audience, étude de lift — les
  plans/updates sans budget passent librement) et `plafond-budget.py` (deny
  au-delà du plafond de rapido-kb/processus-internes.md, défaut 50 €/jour ;
  lifetime comparé sur 30 j ; plan de boost non bloqué) ; Stop récap avec
  statuts PAUSED/ACTIVE et coût max obligatoires.
- Skills : `lancement-campagne-meta`, `boost-post-instagram`, `audiences-crm`,
  `creatifs-publicitaires`, `pixel-et-retargeting`,
  `pilotage-performance-ads`, `veille-ads-concurrents`, `tests-ab-meta`.
- Agent `media-buyer` : coût par résultat, test 10 €/j × 5 j avant scale,
  une variable à la fois, plafonds KB, refus d'activer sans récap ; écriture
  CRM/CMS limitée aux notes.
