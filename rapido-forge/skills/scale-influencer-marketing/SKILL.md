---
name: scale-influencer-marketing
description: "Utiliser quand l'utilisateur veut identifier 20 micro-influenceurs pertinents et créer un plan d'approche (parcours scale StartupsForge)."
tags: [acquisition]
niveau: intermediaire
---

# Influencer Marketing

**Catégorie** : Scale  
**Durée** : 60 min

## Pourquoi

Les micro-influenceurs (1K-100K followers) ont 60% plus d'engagement que les macro. C'est le canal le plus authentique avec un ROI de 5.78$ par dollar investi.

## Objectif

Identifier 20 micro-influenceurs pertinents et créer un plan d'approche.

## Livrable attendu

Liste de 20 influenceurs qualifiés + templates de contact + brief type

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir les critères** — Niche, taille audience, engagement rate, ton, valeurs
2. **Rechercher les candidats** — Hashtags, followers de concurrents, recommandations
   > Prompt: Quels critères pour sélectionner des micro-influenceurs dans le secteur [NICHE] ?
3. **Qualifier les 20 meilleurs** — Engagement rate réel, authenticité, fit avec ta marque
4. **Créer l'approche** — Message personnalisé, value prop pour l'influenceur
5. **Définir le brief** — Objectifs, messages clés, dos/don'ts, tracking

## Pro tips

- L'engagement rate compte plus que le nombre de followers
- Propose de la valeur (produit, contenu exclusif) avant de demander
- Les nano-influenceurs (1K-10K) ont souvent le meilleur ROI

## Erreurs fréquentes

- Se focaliser uniquement sur la taille de l'audience
- Approche trop transactionnelle sans relation
- Pas de tracking des performances par influenceur

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-influencer-marketing.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Passer à l'opérationnel

Cet exercice conçoit la méthode ; pour l'**appliquer aux données réelles** (fiches CRM, pipeline, factures…), passer à **`rapido-marketing:operations-influenceurs`** — il **lit ce livrable forge** (`./rapido-kb/startup/forge/`) comme base, puis agit sur les données MCP. Voir `reference/pont-forge-operations.md`.
