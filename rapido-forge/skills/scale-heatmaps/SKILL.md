---
name: scale-heatmaps
description: "Utiliser quand l'utilisateur veut installer et analyser les heatmaps et session recordings sur son site (parcours scale StartupsForge)."
tags: [data]
niveau: intermediaire
---

# Heatmaps

**Catégorie** : Scale  
**Durée** : 30 min

## Pourquoi

Les heatmaps révèlent où cliquent vraiment tes utilisateurs. Souvent très différent de ce que tu imagines. C'est de la data comportementale pure, sans biais déclaratif.

## Objectif

Installer et analyser les heatmaps et session recordings sur ton site.

## Livrable attendu

Setup Hotjar/Clarity + premiers insights + améliorations identifiées

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Installer le tracking** — Script Hotjar ou Microsoft Clarity (gratuit)
2. **Configurer les pages clés** — Homepage, pricing, signup, core feature
3. **Attendre les données** — Minimum 100 sessions pour des patterns valides
   > Prompt: Quelles pages analyser en priorité pour une startup SaaS [STAGE] ?
4. **Analyser les heatmaps** — Clics, scroll depth, rage clicks
5. **Regarder les recordings** — Sessions complètes pour comprendre le contexte

## Pro tips

- Microsoft Clarity est gratuit et suffisant pour démarrer
- Les rage clicks indiquent une frustration à adresser
- La scroll depth révèle si ton contenu est lu

## Erreurs fréquentes

- Tirer des conclusions avec trop peu de data
- Se focaliser sur les anomalies au lieu des patterns
- Installer mais ne jamais regarder les données

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-heatmaps.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
