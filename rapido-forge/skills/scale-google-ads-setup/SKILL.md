---
name: scale-google-ads-setup
description: "Utiliser quand l'utilisateur veut lancer sa première campagne Google Ads Search rentable (parcours scale StartupsForge)."
---

# Google Ads Setup

**Catégorie** : Scale  
**Durée** : 90 min

## Pourquoi

Google Ads est le canal d'acquisition le plus prévisible. Chaque euro investi peut générer 2-10€ de revenus si bien configuré. C'est essentiel pour valider ta demande et scaler rapidement.

## Objectif

Lancer ta première campagne Google Ads Search rentable.

## Livrable attendu

Campagne Search active + tracking conversions + premiers résultats

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Configurer le compte** — Crée ton compte Google Ads et lie GA4
2. **Recherche de mots-clés** — Utilise le Keyword Planner pour trouver tes keywords
   > Prompt: Quels mots-clés Google Ads pour une startup [SECTEUR] avec budget [BUDGET] ?
3. **Créer la structure** — 1 campagne > groupes d'annonces thématiques > mots-clés ciblés
4. **Rédiger les annonces** — 3 headlines, 2 descriptions, extensions d'annonces
5. **Configurer le tracking** — Installe le tag de conversion et définis les actions

## Pro tips

- Commence en exact match pour contrôler les dépenses
- Utilise des mots-clés négatifs dès le début
- Bid sur ta propre marque (défense)
- Le Quality Score réduit ton CPC - optimise-le

## Erreurs fréquentes

- Utiliser Smart Campaign sans contrôle
- Oublier les mots-clés négatifs (gaspillage)
- Ne pas tracker les conversions (impossible d'optimiser)

## Données & serveurs MCP

- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-google-ads-setup.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
