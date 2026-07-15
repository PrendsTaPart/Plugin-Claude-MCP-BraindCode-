---
name: scale-soncas
description: "Utiliser quand l'utilisateur veut identifier le profil SONCAS de ses clients types et adapter ses argumentaires (parcours scale StartupsForge)."
tags: [vente]
niveau: intermediaire
---

# Soncas

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

SONCAS est la clé pour adapter ton discours aux motivations profondes de chaque client. Les commerciaux qui maîtrisent SONCAS convertissent 35% de plus car ils parlent le langage de leur client.

## Objectif

Identifier le profil SONCAS de tes clients types et adapter tes argumentaires.

## Livrable attendu

Matrice SONCAS par segment client + scripts adaptés par motivation

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Comprendre les 6 motivations** — S(écurité), O(rgueil), N(ouveauté), C(onfort), A(rgent), S(ympathie)
2. **Profiler tes segments** — Quel SONCAS dominant pour chaque persona ?
   > Prompt: Pour un [PERSONA], classe les motivations SONCAS par ordre d'importance
3. **Créer les arguments par motivation** — Sécurité → garanties, Orgueil → exclusivité, etc.
4. **Préparer les questions de découverte** — Questions pour identifier le SONCAS dominant en RDV
5. **Adapter ton pitch** — Version du pitch pour chaque profil SONCAS

## Pro tips

- Pose des questions ouvertes pour identifier le SONCAS dominant
- Un client a souvent 2 SONCAS dominants
- La Sympathie est rarement la seule motivation - creuse plus

## Erreurs fréquentes

- Projeter son propre SONCAS sur le client
- Argumenter uniquement sur l'Argent (erreur classique)
- Oublier que le SONCAS peut changer selon le contexte

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-soncas.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:redaction-commerciale` — adaptation du copy au profil

## Passer à l'opérationnel

Cet exercice conçoit la méthode ; pour l'**appliquer aux données réelles** (fiches CRM, pipeline, factures…), passer à **`rapidocrm:preparation-rdv`** — il **lit ce livrable forge** (`./rapido-kb/startup/forge/`) comme base, puis agit sur les données MCP. Voir `reference/pont-forge-operations.md`.
