---
name: scale-unit-economics
description: "Utiliser quand l'utilisateur veut calculer et optimiser ses métriques unitaires : CAC, LTV, ratio LTV/CAC (parcours scale StartupsForge)."
tags: [finance]
niveau: expert
prerequis: [ideation-financial-forecast]
---

# Unit Economics

**Catégorie** : Scale  
**Durée** : 60 min

## Pourquoi

Les Unit Economics déterminent si ton business peut être profitable. Un ratio LTV/CAC > 3 est le seuil minimal pour les investisseurs. Sans cette maîtrise, tu brûles du cash.

## Objectif

Calculer et optimiser tes métriques unitaires : CAC, LTV, ratio LTV/CAC.

## Livrable attendu

Tableau Unit Economics avec CAC, LTV, payback period et projections

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Calculer le CAC** — Total dépenses marketing & sales ÷ nouveaux clients
2. **Calculer le LTV** — ARPU × Gross Margin × Lifetime (1/churn rate)
   > Prompt: Comment calculer le LTV pour un SaaS avec un ARPU de [X]€ et un churn de [Y]% ?
3. **Calculer le ratio LTV/CAC** — Cible : >3 pour être sustainable
4. **Calculer le Payback Period** — CAC ÷ (ARPU × Gross Margin) = mois pour récupérer le CAC
5. **Identifier les leviers** — Comment améliorer chaque métrique ?

## Pro tips

- Le CAC doit inclure TOUS les coûts (salaires, outils, overhead)
- Segmente les Unit Economics par canal d'acquisition
- Un payback period > 12 mois est risqué sans financement

## Erreurs fréquentes

- Sous-estimer le CAC en oubliant les coûts cachés
- Calculer le LTV sur des hypothèses optimistes de churn
- Ignorer les différences par segment/cohorte

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-unit-economics.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-startup:catalogue-kpi` — CAC/LTV/marges par script
