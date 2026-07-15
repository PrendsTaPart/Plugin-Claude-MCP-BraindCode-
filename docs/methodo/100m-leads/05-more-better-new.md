# More Better New — scaler ce qui marche

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation source** :
> founder-playbook (MIT © 2026 AgentSeal). Reformulation FR — voir `NOTICE.md`.

## Le framework

Un canal est profitable ? On le scale dans cet ordre :

1. **MORE (plus)** — en faire **10×** plus. Qu'est-ce qui vous en empêche ?
2. **BETTER (mieux)** — trouver la contrainte qui casse à ce volume, la corriger,
   puis refaire « plus ».
3. **NEW (nouveau)** — seulement après avoir épuisé plus + mieux :
   - nouveaux emplacements sur la **même** plateforme ;
   - **mêmes** emplacements sur une **nouvelle** plateforme ;
   - nouveaux emplacements sur une nouvelle plateforme ;
   - ajouter une autre activité du Core Four.

« Plus » et « mieux » travaillent ensemble : faire plus **jusqu'à ce que ça
casse**, puis améliorer, puis refaire plus.

## Le piège à éviter
Sauter directement à **NEW** (ajouter un canal) alors que le canal actuel n'est
pas encore poussé à fond. C'est la version « scaling » de l'erreur d'étalement
du Core Four (voir `01-core-four.md`).

## Exemple Rapido / FoodEatUp
Une campagne Meta rentable à 20 €/jour :
- **MORE** : monter progressivement le budget (+10-20 %), dupliquer l'ad set ;
- **BETTER** : quand le CTR baisse (fatigue créative), nouvelles variantes de
  visuel via `studio-visuel-marque` ;
- **NEW** : seulement ensuite, tester Google ou ajouter le contenu organique.

## Outils MCP Rapido pressentis

| Étape | Outils MCP Rapido |
|---|---|
| MORE (pousser le budget/volume) | rapido-meta-ads `ads_update_entity` (budget), `ads_create_ad_set` (dupliquer) |
| BETTER (repérer la contrainte) | rapido-meta-ads `ads_insights_performance_trend`/`ads_insights_anomaly_signal` ; `ads_get_opportunity_score` |
| BETTER (nouvelles créas) | rapidocms `studio-visuel-marque` / `images_to_image`, `create_creative` |
| NEW (autre plateforme/canal) | nouveau canal du Core Four → `01-core-four.md` |

> Toute hausse de budget = argent réel : confirmation explicite (hooks
> rapido-meta-ads), ads créées en **PAUSED**.

## Frontières
- **Quand** un canal est « maîtrisé » (prêt à scaler) → checklist dans
  `08-arbres-de-decision.md`.
- **Déléguer** le canal scalé → `07-lead-getters.md`.
