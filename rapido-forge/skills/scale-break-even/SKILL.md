---
name: scale-break-even
description: "Utiliser quand l'utilisateur veut calculer son point mort et définir la trajectoire pour l'atteindre (parcours scale StartupsForge)."
tags: [finance]
niveau: expert
prerequis: [ideation-financial-forecast]
---

# Break Even

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

Le seuil de rentabilité te dit combien de clients/ventes tu dois atteindre pour être à l'équilibre. C'est une milestone critique pour la crédibilité auprès des investisseurs.

## Objectif

Calculer ton point mort et définir la trajectoire pour l'atteindre.

## Livrable attendu

Analyse break-even avec graphique + scénarios + timeline

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister les coûts fixes** — Loyer, salaires, outils, assurances (mensuels)
2. **Calculer la marge de contribution** — Prix de vente - coûts variables par unité
   > Prompt: Pour un produit vendu [X]€ avec des coûts variables de [Y]€, quelle est la marge de contribution ?
3. **Calculer le break-even point** — Coûts fixes ÷ Marge de contribution = unités nécessaires
4. **Tracer le graphique** — Revenus et coûts en fonction du volume
5. **Définir la timeline** — À quelle croissance, quand atteins-tu le BE ?

## Pro tips

- Distingue bien coûts fixes et variables - c'est souvent mal fait
- Fais 3 scénarios : pessimiste, réaliste, optimiste
- Le break-even change si ton pricing ou tes coûts changent

## Erreurs fréquentes

- Oublier des coûts fixes (overhead, frais bancaires)
- Confondre coûts fixes et variables
- Ne pas mettre à jour après chaque changement de pricing

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-break-even.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-startup:catalogue-kpi` — point mort par script
