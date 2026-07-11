---
name: ideation-quiz-generator
description: "Utiliser quand l'utilisateur veut créer un quiz interactif pour engager et qualifier les visiteurs (parcours idéation StartupsForge)."
---

# Quiz Generator

**Catégorie** : Idéation  
**Durée** : 35-45 min

## Pourquoi

Les quiz ont un taux de complétion de 80%+ et génèrent de l'engagement massif. Ils qualifient aussi les leads selon leurs réponses.

## Objectif

Créer un quiz interactif pour engager et qualifier les visiteurs.

## Livrable attendu

Quiz de 5-10 questions avec résultats personnalisés

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir l'objectif** — Qualifier, éduquer, segmenter ?
2. **Créer les questions** — 5-10 questions progressives
   > Prompt: Crée un quiz de 7 questions pour aider [PERSONA] à découvrir leur [RÉSULTAT]. Chaque question doit être fun et rapide à répondre
3. **Définir les résultats** — 3-4 profils/résultats possibles
4. **Configurer la logique** — Score par réponse, branchements
5. **Ajouter la capture email** — Email requis avant résultats

## Pro tips

- Les quiz courts (5-7 questions) convertissent mieux
- Les résultats doivent être positifs et actionnables
- Capture l'email AVANT de montrer les résultats

## Erreurs fréquentes

- Questions trop sérieuses ou ennuyeuses
- Résultats tous identiques
- Pas de CTA après les résultats

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-quiz-generator.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:animation-client` — sondage/jeu concours réel dans le CRM
