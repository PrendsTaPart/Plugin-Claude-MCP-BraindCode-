---
name: scale-financial-projections
description: "Utiliser quand l'utilisateur veut créer un P&L prévisionnel sur 3 ans avec hypothèses détaillées (parcours scale StartupsForge)."
tags: [finance]
niveau: expert
prerequis: [ideation-financial-forecast]
---

# Financial Projections

**Catégorie** : Scale  
**Durée** : 120 min

## Pourquoi

Les projections financières sur 3 ans sont incontournables pour lever des fonds. Elles montrent ta vision et ta capacité à planifier. Les investisseurs scrutent la cohérence des hypothèses.

## Objectif

Créer un P&L prévisionnel sur 3 ans avec hypothèses détaillées.

## Livrable attendu

P&L 3 ans + hypothèses + scénarios + cash flow

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir les hypothèses de revenus** — Croissance clients, ARPU, upsell, churn mois par mois
2. **Projeter les coûts** — Fixes, variables, recrutements, marketing
   > Prompt: Quels coûts prévoir pour une startup SaaS passant de 0 à 100K€ MRR ?
3. **Construire le P&L** — Revenus - CoGS = Marge brute - Opex = EBITDA
4. **Ajouter le cash flow** — Encaissements, décaissements, BFR, runway
5. **Créer les scénarios** — Pessimiste (-30%), Réaliste, Optimiste (+50%)

## Pro tips

- Bottom-up (client par client) est plus crédible que top-down (%marché)
- Chaque hypothèse doit être justifiable et défendable
- Le cash flow est plus important que le P&L pour une startup

## Erreurs fréquentes

- Hypothèses 'hockey stick' non justifiées
- Oublier le besoin en fonds de roulement (BFR)
- Sous-estimer le temps de recrutement et montée en charge

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-financial-projections.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-startup:plan-financier-previsionnel` — calculs par script, scénarios
