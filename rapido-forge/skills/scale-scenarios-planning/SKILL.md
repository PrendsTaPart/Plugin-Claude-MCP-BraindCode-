---
name: scale-scenarios-planning
description: "Utiliser quand l'utilisateur veut créer 3 scénarios de croissance : pessimiste, réaliste, optimiste (parcours scale StartupsForge)."
tags: [strategie]
niveau: expert
---

# Scenarios Planning

**Catégorie** : Scale  
**Durée** : 90 min

## Pourquoi

Modéliser plusieurs scénarios prépare aux imprévus et rassure les investisseurs sur ta maturité. Les fondateurs avec scénarios pivotent 3x plus vite en cas de crise.

## Objectif

Créer 3 scénarios de croissance : pessimiste, réaliste, optimiste.

## Livrable attendu

Modèle financier avec 3 scénarios + triggers de passage + actions

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir le scénario réaliste** — Base case avec tes hypothèses actuelles
2. **Modéliser le pessimiste** — -30% croissance, +20% churn, -20% ARPU
   > Prompt: Quels facteurs dégrader pour créer un scénario pessimiste réaliste pour [TYPE DE STARTUP] ?
3. **Modéliser l'optimiste** — +50% croissance, -30% churn, +20% ARPU
4. **Définir les triggers** — À quels signaux passe-t-on d'un scénario à l'autre ?
5. **Préparer les actions** — Plan d'action pour chaque scénario

## Pro tips

- Le scénario pessimiste doit rester survivable (sinon c'est game over)
- Révise les scénarios tous les trimestres
- Partage les scénarios avec l'équipe pour aligner tout le monde

## Erreurs fréquentes

- Scénario pessimiste pas assez pessimiste
- Pas de triggers clairs pour activer les plans B
- Scénarios jamais mis à jour après création

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-scenarios-planning.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-startup:plan-financier-previsionnel` — scénarios financiers chiffrés
