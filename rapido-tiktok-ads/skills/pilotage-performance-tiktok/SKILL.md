---
name: pilotage-performance-tiktok
description: Utiliser quand l'utilisateur demande la performance de ses pubs TikTok, « comment vont mes TikTok Ads », son CPM/CPC/CPA TikTok, la performance par créatif, ou veut arbitrer le budget TikTok vs Meta. Analyse dépense, CPM/CPC/CPA, performance par créatif TikTok, et compare avec Meta Ads (mêmes KPIs, même période) pour l'arbitrage budgétaire inter-plateformes.
---

# Pilotage performance TikTok Ads

Le point de performance TikTok + l'arbitrage vs Meta. **Lecture** (aucune écriture ici).

## Étape 0
`reference/garde-fous-tiktok.md`. Objectifs et plafonds `./rapido-kb/marketing/`.

## Sense (lecture — TikTok Ads)
- Dépense, **CPM / CPC / CPA**, conversions, **performance par créatif** (quel hook/
  format performe). Tendance vs période précédente, anomalies.

## Plan (arbitrage, catalogue-kpi)
- KPIs calculés par `rapido-startup:catalogue-kpi` (formules uniques).
- **Comparaison TikTok vs Meta** : mêmes KPIs, **même période** — via
  `rapido-meta-ads:pilotage-performance-ads` pour le côté Meta. Où l'euro rend le
  mieux → recommandation d'arbitrage (décision finale = `rapido-marketing` directeur-marketing).

## Report — une page
CPM/CPC/CPA TikTok, top créatifs, comparatif TikTok vs Meta, recommandation
d'allocation (dans les plafonds KB). Actions d'écriture éventuelles → passent par
`lancement-campagne-tiktok` (verrouillé).

## Anti-collision
- **`rapido-meta-ads:pilotage-performance-ads`** = Meta. Ici = **TikTok** (préciser
  « TikTok » partout). Ce skill **lit** Meta pour comparer, il ne le pilote pas.

## Garde-fous
Lecture ; KPIs via catalogue-kpi ; comparaison **même période/mêmes KPIs** ; données
réelles ; serveur absent = le dire.
