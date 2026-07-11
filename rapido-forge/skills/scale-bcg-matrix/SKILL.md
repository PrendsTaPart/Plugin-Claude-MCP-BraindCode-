---
name: scale-bcg-matrix
description: "Utiliser quand l'utilisateur veut analyser son portefeuille produits/services pour identifier les Stars à développer, les Vaches à lait à optimiser, les Dilemmes à arbitrer et les Poids morts à abandonner (parcours scale StartupsForge)."
tags: [strategie]
niveau: intermediaire
---

# Bcg Matrix

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

La matrice BCG (Boston Consulting Group) est essentielle pour optimiser ton portefeuille produits. Elle t'aide à décider où investir tes ressources limitées en classifiant tes produits selon leur croissance et part de marché. Les startups qui maîtrisent cette analyse font 40% moins d'erreurs d'allocation de ressources.

## Objectif

Analyser ton portefeuille produits/services pour identifier les Stars à développer, les Vaches à lait à optimiser, les Dilemmes à arbitrer et les Poids morts à abandonner.

## Livrable attendu

Matrice BCG complète avec positionnement de chaque produit et plan d'action stratégique

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister tes produits/services** — Identifie tous tes produits, fonctionnalités ou lignes de service actuelles
2. **Évaluer la croissance du marché** — Pour chaque produit, estime le taux de croissance de son marché (faible <10%, élevée >10%)
   > Prompt: Analyse le taux de croissance du marché [SECTEUR] pour les 3 prochaines années
3. **Calculer ta part de marché relative** — Compare ta part de marché à celle du leader (ratio >1 = leader, <1 = suiveur)
4. **Positionner sur la matrice** — Place chaque produit dans le quadrant approprié : Star, Vache à lait, Dilemme, Poids mort
5. **Définir la stratégie par quadrant** — Star → Investir, Vache à lait → Maintenir, Dilemme → Décider, Poids mort → Désinvestir

## Pro tips

- Utilise des cercles de tailles différentes pour représenter le CA de chaque produit
- Réévalue ta matrice chaque trimestre car les positions évoluent
- Les Stars d'aujourd'hui sont les Vaches à lait de demain - planifie la succession
- Un Dilemme qui ne devient pas Star en 18 mois devient généralement Poids mort

## Erreurs fréquentes

- Confondre croissance du produit et croissance du marché
- Garder des Poids morts par attachement émotionnel
- Ignorer les Dilemmes jusqu'à ce qu'ils meurent

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-bcg-matrix.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
