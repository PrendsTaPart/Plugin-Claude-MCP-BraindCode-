---
name: plan-financier-previsionnel
description: Utiliser quand l'utilisateur veut un prévisionnel financier, un plan de trésorerie, un compte de résultat prévisionnel 3 ans, un point mort, des scénarios, ou finaliser la partie chiffrée de son business plan.
---

# Plan financier prévisionnel — 36 mois, 3 scénarios, sensibilité

Modélise mois par mois sur 36 mois : clients (nouveaux, churn composé), MRR,
CA, COGS, charges (salaires CHARGÉS ~1,45× le brut France, marketing piloté
par le CAC, coûts fixes), résultat et trésorerie cumulée — puis point mort,
besoin de financement, scénarios et matrice de sensibilité. **Tout est
calculé par `scripts/previsionnel.py`** — jamais de tête.

## Étape 0 — Références et hypothèses (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
   `${CLAUDE_PLUGIN_ROOT}/reference/seuils-defaut.md`.
2. **La source des hypothèses est
   `./rapido-kb/startup/business-plan/hypotheses.md`** (construite par le
   skill `interview-business-plan`) : chaque entrée du modèle doit y exister
   avec source/date/confiance. Hypothèse manquante → la collecter (question
   ou MCP : ARPU/churn réels via Stripe `stripe_api_read`, pipeline via
   `get_stats_pipeline_global`) et l'AJOUTER à hypotheses.md d'abord.
   Jamais de valeur sortie de nulle part.
3. Toute hypothèse « confiance faible » doit être visible dans la
   restitution — c'est elle que le scénario downside stresse.

## Workflow

1. **Assembler le JSON d'hypothèses** (clés canoniques du script :
   `tresorerie_initiale`, `clients_initiaux`, `nouveaux_clients_mois`,
   `croissance_mensuelle`, `churn_mensuel`, `arpu`, `cogs_pct`, `cac`,
   `salaires_bruts_mensuels`, `coeff_charges` (défaut 1,45), `embauches`
   [{mois, brut}], `couts_fixes_mensuels`, et `justification_croissance` si
   la croissance dépasse 30 %/mois au-delà du mois 6 — recopiée
   d'hypotheses.md). Montants en euros (centimes Stripe déjà convertis).
2. **Exécuter**
   `python3 ${CLAUDE_PLUGIN_ROOT}/skills/plan-financier-previsionnel/scripts/previsionnel.py`
   (JSON sur stdin). Le script écrit dans
   `./rapido-kb/startup/business-plan/previsionnel/` : les CSV mensuels des
   3 scénarios, `sensibilite.csv` et `PREVISIONNEL.md` (tableaux + synthèse).
3. **Restituer** : point mort (mois de croisement), besoin de financement
   (creux de trésorerie maximal), runway par scénario, matrice de
   sensibilité churn × CAC — en citant les hypothèses et leur confiance.
4. **Boucler** : proposer d'intégrer la synthèse dans le business plan
   (section 9 du skill `interview-business-plan`) et de suivre les KPI réels
   vs prévisionnel avec le skill `catalogue-kpi`.

## Les 3 scénarios (calculés systématiquement, jamais un seul)

- **Base** : les hypothèses telles quelles.
- **Upside** : croissance des nouveaux clients +20 % (relative).
- **Downside** : churn +2 points, CAC +30 %.
Le scénario présenté à une banque est le DOWNSIDE tenu, pas l'upside.

## Garde-fous

- **Hook `garde-projection-realiste`** (+ mêmes contrôles DANS le script) :
  croissance > 30 %/mois au-delà du mois 6 REJETÉE sans
  `justification_croissance` recopiée d'hypotheses.md ; **churn = 0 REJETÉ**
  (il n'existe pas d'entreprise sans churn).
- **Pas de conseil d'investissement** : le prévisionnel est un outil de
  pilotage et de dialogue avec les financeurs, pas une recommandation
  d'investir ; le dire si la question glisse vers « dois-je investir ».
- **Scénarios ≠ promesses** : chaque restitution le rappelle — ce sont des
  projections conditionnées aux hypothèses listées, pas des engagements.
- **Document vivant** : à mettre à jour à CHAQUE jalon (levée, embauche,
  pivot, écart réel > 30 % pendant 2 mois) — proposer la mise à jour quand
  un jalon est mentionné, et dater chaque version.
- Sortie UNIQUEMENT dans `./rapido-kb/startup/business-plan/previsionnel/`
  (répertoire du client, jamais dans le plugin).
