---
name: performance-organique
description: Utiliser quand l'utilisateur demande « ma performance SEO », « mes positions Google », « quelles pages convertissent en organique », ses requêtes en striking distance ou ses pages à faible CTR. Réunit Search Console (positions, impressions, CTR) et GA4 (atterrissages organiques qui convertissent) ; précise toujours le décalage de fraîcheur GSC.
---

# Performance organique (GSC + GA4)

Le tableau de bord organique réel : où on est positionné, ce qui est à portée, ce
qui convertit. **Lecture seule** (GA4 & GSC).

## Étape 0
`reference/garde-fous-seo.md` (fraîcheur GSC, lecture seule). Cibles
`./rapido-kb/seo/seo-cibles.md`.

## Sense
- **Search Console** (famille `search_analytics`) : requêtes, positions, impressions,
  clics, CTR — période récente en **précisant la fraîcheur** (données au **J-3**,
  requêtes rares **anonymisées**).
- **GA4** (`run_report`) : atterrissages **organiques** par page, conversions par
  **source/medium** (`organic`), engagement. Trafic issu des **LLMs** si mesurable
  (referrers IA) — sinon le dire.

## Plan (les 3 leviers)
- **Striking distance** : requêtes en **position 8-20** à **fortes impressions** →
  gains rapides (contenu/maillage). Formule de priorité affichée (impressions ×
  proximité du top 3).
- **CTR anormalement bas** : pages bien positionnées mais peu cliquées → title/meta
  à retravailler.
- **Pages qui convertissent** (GA4) : renforcer ce qui transforme, pas seulement ce
  qui fait du volume.

## Report — une page
Positions clés, **striking distance** priorisée, pages CTR-bas, pages organiques qui
convertissent — **avec la mention de fraîcheur GSC**. Corrections de title/meta
proposées (exécution RapidoCMS sur accord).

## Garde-fous
Lecture seule ; **fraîcheur GSC précisée** systématiquement ; conversions via GA4
réelles ; calculs via `rapido-startup:catalogue-kpi` ; serveur absent = le dire.
