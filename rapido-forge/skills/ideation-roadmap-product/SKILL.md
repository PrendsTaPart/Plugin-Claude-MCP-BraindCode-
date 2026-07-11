---
name: ideation-roadmap-product
description: "Utiliser quand l'utilisateur veut définir les fonctionnalités essentielles du MVP à développer en premier (parcours idéation StartupsForge)."
---

# Roadmap Product

**Catégorie** : Idéation  
**Durée** : 35-45 min

## Pourquoi

Le MVP (Minimum Viable Product) te permet de valider ton hypothèse avec un minimum d'investissement. 90% des fonctionnalités que tu imagines ne seront jamais utilisées - concentre-toi sur l'essentiel.

## Objectif

Définir les fonctionnalités essentielles du MVP à développer en premier.

## Livrable attendu

Liste priorisée des features MVP avec critères MoSCoW (Must/Should/Could/Won't)

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister TOUTES les fonctionnalités** — Brainstorme sans filtre - 30+ idées
2. **Évaluer chaque feature** — Impact client (1-5) × Effort de développement (1-5)
3. **Appliquer MoSCoW** — Must (critique), Should (important), Could (nice), Won't (jamais)
4. **Définir le MVP** — Seulement les 'Must' = ton MVP
   > Prompt: Évalue ces fonctionnalités selon MoSCoW pour un MVP de [PRODUIT] : [LISTE]
5. **Créer la roadmap** — V1 (Must), V1.1 (Should), V2 (Could)

## Pro tips

- Le MVP doit résoudre UN problème mieux que quiconque
- Si tu n'as pas honte de ta V1, tu l'as lancée trop tard
- Chaque feature doit avoir un objectif business clair

## Erreurs fréquentes

- Trop de 'Must' - sois impitoyable dans ta priorisation
- Construire ce que tu veux vs ce que le client veut
- Oublier les fonctionnalités d'infrastructure (auth, paiement)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **RapidoRh** (`rapidorh`) pour décliner en projet/tâches

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-roadmap-product.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
