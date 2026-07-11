---
name: ideation-retargeting-setup
description: "Utiliser quand l'utilisateur veut configurer le retargeting pour récupérer les visiteurs (parcours idéation StartupsForge)."
tags: [acquisition]
niveau: intermediaire
prerequis: [ideation-landing-page, ideation-persona-maker]
---

# Retargeting Setup

**Catégorie** : Idéation  
**Durée** : 45-60 min

## Pourquoi

97% des visiteurs ne convertissent pas à la première visite. Le retargeting les ramène avec un message personnalisé.

## Objectif

Configurer le retargeting pour récupérer les visiteurs.

## Livrable attendu

Campagne retargeting active

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Installer le pixel** — Meta, Google, LinkedIn
2. **Créer les audiences** — Visiteurs page, abandon panier
3. **Designer les créatives** — Message spécifique à l'étape
4. **Configurer les exclusions** — Exclure les clients actuels
5. **Lancer et optimiser** — Ajuster selon les résultats

## Pro tips

- Segmente par étape du funnel
- Limite la fréquence pour ne pas spammer
- Offre un incentive (remise, bonus)

## Erreurs fréquentes

- Audience trop petite
- Même message pour tout le monde
- Pas d'exclusion des convertis

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Facebook ads** (`facebook-ads`, via le plugin `rapido-meta-ads`) — ⚠️ argent réel : tout se crée en PAUSED, activation après accord explicite

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-retargeting-setup.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-meta-ads:pixel-et-retargeting` — pixel + audience WEBSITE + campagne
