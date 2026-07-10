# Changelog — plugin rapido-startup

## 1.3.0 — 2026-07-10

- Skill `plan-financier-previsionnel` : modèle mois par mois sur 36 mois
  (clients avec churn composé, MRR, CA, COGS, salaires chargés ×1,45,
  marketing piloté par le CAC, coûts fixes, résultat, trésorerie cumulée) ;
  point mort, besoin de financement (creux de trésorerie max) ; 3 scénarios
  base / upside (+20 % croissance) / downside (churn +2 pts, CAC +30 %) ;
  matrice de sensibilité churn × CAC ; sortie CSV + PREVISIONNEL.md dans
  ./rapido-kb/startup/business-plan/previsionnel/. Rappels : pas de conseil
  d'investissement, scénarios ≠ promesses, document vivant.
- Hook PreToolUse `garde-projection-realiste` (+ mêmes contrôles dans le
  script) : REJET churn = 0 ; REJET croissance > 30 %/mois au-delà du mois 6
  sans justification_croissance recopiée d'hypotheses.md.
- 14 tests unitaires (tests/test_previsionnel.py) ; interview-business-plan
  référence désormais le skill réel (plus « à venir »).

## 1.2.0 — 2026-07-10

- Skill `catalogue-kpi` : 22 KPI avec formule exacte, outils MCP par KPI,
  fréquence, seuil (KB prioritaire sinon seuils-defaut) et pièges (churn
  annuel COMPOSÉ jamais ×12, centimes Stripe, contrat annuel = MRR/12) ;
  règle absolue « le script calcule, pas le modèle » — collecte MCP → JSON
  d'entrées → scripts/calcul_kpi.py → formule TOUJOURS affichée.
- scripts/calcul_kpi.py (stdlib, fonctions pures + CLI JSON) : sortie
  {kpi, valeur, formule_appliquee, entrees, seuil, statut} ; seuils par
  défaut embarqués, seuil maison prioritaire. 17 tests unitaires
  (tests/test_calcul_kpi.py), dont l'exemple de référence LTV 1584.
- Hook Stop `garde-calcul-script` : bloque toute réponse annonçant un KPI
  chiffré sans exécution de calcul_kpi.py dans le tour (« KPI sans
  script ») — testé sur transcripts simulés, fail-open.
- NOTE : la « Partie 3 » du master plan (placeholder non fourni dans le
  brief) — catalogue construit depuis la spec et l'exemple de référence,
  à réconcilier si le master plan diverge.

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
