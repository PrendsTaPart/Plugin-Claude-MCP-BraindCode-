---
name: scale-cost-waterfall
description: "Utiliser quand l'utilisateur veut cartographier et catégoriser tous ses coûts fixes et variables (parcours scale StartupsForge)."
---

# Cost Waterfall

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

Le Waterfall des coûts te donne une vision granulaire de où part chaque euro. C'est la base pour optimiser ta structure de coûts et améliorer tes marges.

## Objectif

Cartographier et catégoriser tous tes coûts fixes et variables.

## Livrable attendu

Waterfall chart des coûts + catégorisation + quick wins d'optimisation

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister tous les coûts** — Export banque, factures, abonnements - TOUT
2. **Catégoriser** — Fixe/Variable, Produit/Marketing/G&A/R&D
   > Prompt: Comment catégoriser les coûts d'une startup SaaS en early stage ?
3. **Créer le waterfall** — Du revenu brut au résultat net, couche par couche
4. **Identifier les anomalies** — Coûts trop élevés, doublons, gaspillages
5. **Prioriser les optimisations** — Quick wins vs optimisations structurelles

## Pro tips

- Les abonnements SaaS s'accumulent vite - fais un audit régulier
- Négocie les contrats annuels pour 20-40% de réduction
- Le coût le plus dangereux est celui qu'on ne voit pas

## Erreurs fréquentes

- Oublier les micro-coûts qui s'additionnent
- Ne pas distinguer clairement fixe et variable
- Optimiser les petits coûts en ignorant les gros

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-cost-waterfall.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:gestion-depenses` — dépenses réelles du CRM
