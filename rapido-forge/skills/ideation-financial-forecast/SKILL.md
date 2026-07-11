---
name: ideation-financial-forecast
description: "Utiliser quand l'utilisateur veut créer des projections financières à 3 ans (parcours idéation StartupsForge)."
---

# Financial Forecast

**Catégorie** : Idéation  
**Durée** : 90-120 min

## Pourquoi

Les prévisions financières démontrent que tu as réfléchi à la viabilité de ton business. C'est obligatoire pour lever des fonds ou obtenir un prêt.

## Objectif

Créer des projections financières à 3 ans.

## Livrable attendu

Prévisionnel Excel/Sheets avec P&L, cash flow, bilan

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Estimer les revenus** — Clients × Prix × Fréquence
2. **Lister les coûts fixes** — Salaires, loyer, outils, etc.
3. **Calculer les coûts variables** — Par unité vendue
4. **Projeter sur 36 mois** — Conservateur, réaliste, optimiste
5. **Valider la cohérence** — Marge, point mort, BFR

## Pro tips

- Toujours présenter 3 scénarios
- Base tes hypothèses sur des données réelles
- Sois conservateur sur les revenus, réaliste sur les coûts

## Erreurs fréquentes

- Projections trop optimistes
- Oublier des coûts cachés
- Pas de saisonnalité prise en compte

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-financial-forecast.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-startup:plan-financier-previsionnel` — prévisionnel complet par script
