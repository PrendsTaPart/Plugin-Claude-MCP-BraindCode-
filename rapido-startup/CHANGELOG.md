# Changelog — plugin rapido-startup

## 1.1.0 — 2026-07-10

- Skill `interview-business-plan` : interview en 9 phases (executive summary
  rempli en dernier, entreprise/équipe, problème/PVU, marché TAM/SAM/SOM en
  bottom-up — refus du « 1 % du marché » —, concurrence, BMC 9 blocs,
  go-to-market/traction, plan opérationnel, plan financier) ; une question à
  la fois, Mom Test, relances sur réponses faibles ; hypothèses sourcées et
  datées dans ./rapido-kb/startup/business-plan/hypotheses.md ; sortie en
  9 fichiers + BUSINESS-PLAN.md (section risques obligatoire) ; annexes
  questionnaire-9-phases.md (≈80 questions avec objectif/signal faible/
  relance), frameworks.md (BMC, Lean Canvas, TAM/SAM/SOM, SWOT, 5 questions
  investisseurs), template-bp.md.
- Agent `coach-startup` : coach d'incubateur exigeant mais bienveillant —
  Mom Test permanent, interdit des projections non sourcées, contexte chargé
  depuis ./rapido-kb/ (jamais reposé), lecture seule pendant le coaching.
- tests/evals.md : scénarios de déclenchement et de comportement (routage,
  KB, refus du top-down, sortie, agent).

## 1.0.0 — 2026-07-10

- Squelette initial : `.mcp.json` (serveur Stripe officiel https://mcp.stripe.com
  + les 4 serveurs Rapido), références `directives-outils.md`,
  `pieges-outils.md` (pièges communs multi-serveurs + Stripe lecture seule,
  montants en centimes, format `post_heure`) et `seuils-defaut.md`
  (benchmarks finance/startup, utilisés SEULEMENT si absents de
  `./rapido-kb/`), hook déterministe `garde-stripe-write` (confirmation
  forcée sur toute écriture Stripe). Dossiers `agents/`, `skills/` et
  `tests/` prêts — skills à venir.
