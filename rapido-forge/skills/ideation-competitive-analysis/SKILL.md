---
name: ideation-competitive-analysis
description: "Utiliser quand l'utilisateur veut cartographier le paysage concurrentiel avec forces, faiblesses et opportunités de différenciation (parcours idéation StartupsForge)."
tags: [strategie]
niveau: debutant
---

# Competitive Analysis

**Catégorie** : Idéation  
**Durée** : 40-60 min

## Pourquoi

Connaître tes concurrents te permet de te différencier, d'éviter leurs erreurs et de trouver des opportunités de marché. 'Nous n'avons pas de concurrents' est un red flag majeur pour les investisseurs.

## Objectif

Cartographier le paysage concurrentiel avec forces, faiblesses et opportunités de différenciation.

## Livrable attendu

Matrice concurrentielle avec 5-10 concurrents directs/indirects, leurs forces/faiblesses et ton positionnement

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Identifier les concurrents directs** — Qui résout le même problème pour le même persona ?
   > Prompt: Liste les 5 principales entreprises qui aident [PERSONA] à résoudre [PROBLÈME]
2. **Identifier les concurrents indirects** — Solutions alternatives ou substituts (Excel, papier, rien faire)
3. **Collecter les données** — Pricing, features, avis clients, taille équipe, financement
4. **Créer la matrice comparative** — Tableau avec critères clés et notes 1-5 pour chaque concurrent
5. **Identifier ton positionnement** — Où te places-tu ? Quel est ton angle différenciant ?

## Pro tips

- Utilise Perplexity AI pour une recherche rapide et sourcée
- Inscris-toi à leurs newsletters et teste leurs produits
- Les avis négatifs sur leurs produits sont des opportunités pour toi
- Mets à jour cette analyse tous les trimestres

## Erreurs fréquentes

- Sous-estimer les concurrents ou dire 'nous n'en avons pas'
- Oublier les concurrents indirects (le statu quo est ton plus grand concurrent)
- Ne pas tester vraiment les produits concurrents

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-competitive-analysis.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:account-research` — renseignement web + CRM sur chaque concurrent
