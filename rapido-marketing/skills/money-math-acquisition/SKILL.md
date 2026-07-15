---
name: money-math-acquisition
description: Utiliser quand l'utilisateur veut savoir combien il peut dépenser pour acquérir un client, si ses publicités sont rentables, son ratio LTGP:CAC, ou comment financer son acquisition avec le cash des clients. Cadre les nombres (LTGP, CAC, ratio, remboursement 30 jours) et délègue TOUT calcul au script KPI.
---

# Money Math de l'acquisition — LTGP:CAC

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation** :
> `docs/methodo/100m-leads/04-ltgp-cac.md` (source MIT founder-playbook).
> Reformulé, citations < 15 mots.

## Étape 0 — Charger (obligatoire)
- Fiche `docs/methodo/100m-leads/04-ltgp-cac.md`.
- `./rapido-kb/marketing/` si présent + `processus-internes.md` (seuils maison).
- `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-marketing.md` (règle e : jamais de
  KPI de tête).

## Méthode

1. **LTGP** = marge brute sur la durée de vie (revenus − coût de livraison) —
   **pas la LTV** (le LTGP retire le coût de livraison).
2. **CAC** = coût d'acquisition d'un client (dépense ÷ clients acquis).
3. **Ratio LTGP:CAC** — règles de lecture : < 3:1 dur à scaler · 3:1 minimum ·
   > 3:1 prêt à scaler. CAC > 3× la moyenne secteur → corriger les **pubs** ;
   sinon → corriger le **modèle** (augmenter le LTGP).
4. **Acquisition financée par le client** : remboursement en ~30 jours →
   réinvestissement quasi illimité. Leviers : prix d'entrée, order bumps,
   upsell jour 1, annuel, frais de setup.

## Livrable type
Un **tableau LTGP:CAC** (valeurs + formules affichées) + **verdict**
(scaler / corriger pubs / corriger modèle) + 2-3 leviers d'amélioration chiffrés.

## Délégation de l'exécution
- **TOUT calcul** (LTGP, CAC, ratio, point de remboursement) → skill
  `catalogue-kpi` (son script calcul_kpi, formule visible) — **jamais de tête**
  (hook « KPI sans script »).
- **Données** : revenus/marge → `get_revenue_summary`, `get_top_clients`
  (rapidocrm) ; dépenses pub → `list_depenses` (rapidocrm) + insights
  rapido-meta-ads ; surveillance runway → routine **R7 CASH-SENTINEL**.

## Cas d'usage croisés
- Bibliothèque de formules (MRR, CAC, LTV, runway…) → skill `catalogue-kpi`.
- Trésorerie / runway 30-60-90 j → skill `cash-flow-snapshot`.
- Tarification / hausse du LTGP par le prix → le framework
  `monetizing-innovation` (benchmark, pas encore un skill — voir
  `docs/BENCHMARK-FOUNDER-PLAYBOOK.md`) et le skill `hundred-million-offers`.

## Garde-fous
Aucun ratio ni seuil **estimé** : chiffres calculés par script, sources datées ;
priorité aux données CRM live > KB (priorite-mcp).
