---
name: audit-compte-google-ads
description: Utiliser quand l'utilisateur veut un audit de son compte Google Ads, repérer le gaspillage publicitaire, vérifier son Quality Score, les chevauchements de campagnes, les extensions manquantes, ou le suivi des conversions. Audit structuré en lecture seule, avec croisement GA4 pour signaler les écarts de conversions.
---

# Audit de compte Google Ads (lecture seule)

Passe le compte au crible et sort un plan de nettoyage **à exécuter manuellement**.

## Étape 0
`reference/garde-fous-sea.md`. Cibles `./rapido-kb/marketing/`.

## Sense (lecture)
- **Gaspillage** : requêtes de recherche non pertinentes (à passer en négatifs),
  mots-clés à coût élevé sans conversion.
- **Quality Score** : mots-clés à QS faible (pertinence annonce/landing/CTR).
- **Chevauchements** de campagnes/groupes (cannibalisation d'enchères).
- **Extensions** manquantes (liens annexes, accroches, extraits).
- **Suivi des conversions** : cohérence Google Ads vs **GA4** (`run_report`) —
  **signaler les écarts** (conversions Google Ads ≠ GA4 = tracking à revoir).

## Plan
- Problèmes **priorisés par € gaspillés** (chiffre source), avec la correction et
  **où la faire dans l'interface**.

## Report — une page
Score de compte, top gaspillages chiffrés, écarts de tracking Google Ads/GA4,
extensions à ajouter — **corrections manuelles** (jamais exécutées ici).

## Garde-fous
Lecture seule ; gaspillage **chiffré et sourcé** ; écarts de conversions **signalés**
(pas corrigés d'office) ; calculs via catalogue-kpi.
