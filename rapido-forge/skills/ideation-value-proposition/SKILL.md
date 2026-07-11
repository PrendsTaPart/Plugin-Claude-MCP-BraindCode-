---
name: ideation-value-proposition
description: "Utiliser quand l'utilisateur veut identifier et articuler le problème précis que sa solution résout, avec son intensité et sa fréquence (parcours idéation StartupsForge)."
---

# Value Proposition

**Catégorie** : Idéation  
**Durée** : 25-35 min

## Pourquoi

Identifier clairement la douleur de ton client est ce qui différencie un produit 'nice to have' d'un produit 'must have'. Les startups qui résolvent une vraie douleur intense lèvent 3x plus de fonds et convertissent 5x mieux.

## Objectif

Identifier et articuler le problème précis que ta solution résout, avec son intensité et sa fréquence.

## Livrable attendu

Document détaillant le pain point principal, son intensité (1-10), sa fréquence et les solutions actuelles insatisfaisantes

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister les problèmes potentiels** — Brainstorme 10-15 problèmes que rencontre ton persona dans le domaine ciblé
   > Prompt: Liste 15 problèmes quotidiens rencontrés par [PERSONA] concernant [DOMAINE]
2. **Appliquer les 5 Pourquoi** — Pour chaque problème, demande 'pourquoi c'est un problème ?' 5 fois pour trouver la cause racine
3. **Évaluer l'intensité** — Note chaque problème de 1 à 10 : fréquence, intensité de la douleur, budget alloué actuellement
4. **Analyser les solutions existantes** — Comment les gens résolvent ce problème aujourd'hui ? Pourquoi c'est insatisfaisant ?
5. **Formuler le Pain Statement** — Rédige une phrase claire : '[PERSONA] souffre de [PROBLÈME] qui lui coûte [IMPACT]'

## Pro tips

- Un vrai pain point fait perdre du temps, de l'argent ou cause du stress mesurable
- Si les gens ne paient pas déjà pour résoudre ce problème, ce n'est probablement pas assez douloureux
- Les meilleurs problèmes sont ceux que les gens mentionnent spontanément en interview

## Erreurs fréquentes

- Inventer un problème que tu voudrais résoudre plutôt qu'un vrai problème client
- Se concentrer sur des inconvénients mineurs plutôt que des douleurs critiques
- Ne pas quantifier l'impact du problème (temps perdu, argent perdu)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-value-proposition.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
