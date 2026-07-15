---
name: scale-bant-qualification
description: "Utiliser quand l'utilisateur veut créer une grille de qualification BANT pour prioriser ses opportunités (parcours scale StartupsForge)."
tags: [vente]
niveau: intermediaire
---

# Bant Qualification

**Catégorie** : Scale  
**Durée** : 30 min

## Pourquoi

BANT te permet de qualifier rapidement si un prospect vaut ton temps. Les commerciaux qui qualifient bien passent 45% moins de temps sur des deals perdants.

## Objectif

Créer une grille de qualification BANT pour prioriser tes opportunités.

## Livrable attendu

Grille BANT avec questions par critère + système de scoring

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir les critères Budget** — A-t-il le budget ? Montant, ligne budgétaire, timing
2. **Définir les critères Authority** — Est-ce le décisionnaire ? Qui d'autre impliqué ?
   > Prompt: Quelles questions poser pour identifier le décisionnaire dans un deal B2B [SECTEUR] ?
3. **Définir les critères Need** — Le besoin est-il réel et urgent ? Pain point identifié ?
4. **Définir les critères Timing** — Quand veut-il acheter ? Y a-t-il un événement déclencheur ?
5. **Créer le système de scoring** — Score 1-3 par critère, seuil minimum pour poursuivre

## Pro tips

- Le Budget est souvent le dernier à être qualifié (ne commence pas par là)
- Un champion interne est plus important qu'un simple décisionnaire
- Le timing est souvent le facteur le plus déterminant

## Erreurs fréquentes

- Demander le budget trop directement et trop tôt
- Confondre utilisateur et acheteur
- Ignorer les signaux de faible timing

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-bant-qualification.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:prospection-pipeline` — qualification dans le pipeline réel

## Passer à l'opérationnel

Cet exercice conçoit la méthode ; pour l'**appliquer aux données réelles** (fiches CRM, pipeline, factures…), passer à **`rapidocrm:qualification-deals`** — il **lit ce livrable forge** (`./rapido-kb/startup/forge/`) comme base, puis agit sur les données MCP. Voir `reference/pont-forge-operations.md`.
