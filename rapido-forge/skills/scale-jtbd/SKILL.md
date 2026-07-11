---
name: scale-jtbd
description: "Utiliser quand l'utilisateur veut identifier les 'jobs' fonctionnels, émotionnels et sociaux que ses clients veulent accomplir (parcours scale StartupsForge)."
tags: [produit]
niveau: intermediaire
---

# Jtbd

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

Jobs To Be Done (JTBD) révèle pourquoi les gens achètent vraiment. Les clients n'achètent pas un produit, ils 'embauchent' une solution pour faire un 'job'. Cette compréhension triple tes taux de conversion.

## Objectif

Identifier les 'jobs' fonctionnels, émotionnels et sociaux que tes clients veulent accomplir.

## Livrable attendu

Job Stories complètes + Forces Diagram (push, pull, anxieties, habits)

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Identifier le job principal** — Quel progrès ton client essaie-t-il d'accomplir dans sa vie ?
2. **Décomposer en 3 dimensions** — Job fonctionnel (pratique), émotionnel (ressenti), social (perception)
   > Prompt: Pour [PERSONA], quels sont les jobs fonctionnels, émotionnels et sociaux liés à [PROBLÈME] ?
3. **Analyser les forces du changement** — Push (problème actuel), Pull (attraction solution), Anxieties (peurs), Habits (inertie)
4. **Écrire les Job Stories** — Format : 'Quand [situation], je veux [motivation], pour que [résultat attendu]'
5. **Prioriser les jobs** — Classe les jobs par importance et fréquence

## Pro tips

- Le job n'est jamais le produit - 'faire un trou' pas 'acheter une perceuse'
- Les jobs émotionnels et sociaux sont souvent plus puissants que fonctionnels
- Interview des clients sur 'pourquoi avez-vous changé/acheté ?' pas 'que voulez-vous ?'

## Erreurs fréquentes

- Définir le job comme ton produit
- Ignorer les forces de résistance (anxieties, habits)
- Ne pas interviewer de vrais clients qui ont 'switché'

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-jtbd.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
