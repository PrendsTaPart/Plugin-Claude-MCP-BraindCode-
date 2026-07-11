---
name: scale-upsell-crosssell
description: "Utiliser quand l'utilisateur veut cartographier les opportunités d'upsell et cross-sell par segment client (parcours scale StartupsForge)."
---

# Upsell Crosssell

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

Vendre à un client existant coûte 5x moins cher que d'en acquérir un nouveau. L'upsell et cross-sell peuvent représenter 30% de ton CA additionnel sans coût d'acquisition.

## Objectif

Cartographier les opportunités d'upsell et cross-sell par segment client.

## Livrable attendu

Matrice upsell/cross-sell + triggers d'activation + scripts

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister tes produits/services** — Catalogue complet avec prix et segments cibles
2. **Identifier les synergies** — Quels produits se complètent naturellement ?
   > Prompt: Pour [PRODUIT A], quels produits complémentaires pourraient intéresser le client ?
3. **Définir les triggers** — À quel moment proposer (usage, milestone, renouvellement) ?
4. **Créer les scripts** — Email, in-app, call - adapté au moment
5. **Définir les métriques** — Taux d'upsell, expansion revenue, NRR

## Pro tips

- Le meilleur moment pour upsell = quand le client vient d'avoir un succès
- Cross-sell = produit différent, Upsell = version supérieure
- Les prix d'upsell doivent suivre la règle des 25% (max 25% du prix actuel)

## Erreurs fréquentes

- Proposer l'upsell trop tôt avant que le client ait vu la valeur
- Pousser des produits non pertinents pour le client
- Ne pas tracker le Net Revenue Retention

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-upsell-crosssell.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:campagne-marketing` — campagne ciblée sur segment client
