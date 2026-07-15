---
name: scale-spin-selling
description: "Utiliser quand l'utilisateur veut maîtriser les 4 types de questions SPIN pour qualifier et convertir efficacement (parcours scale StartupsForge)."
tags: [vente]
niveau: intermediaire
---

# Spin Selling

**Catégorie** : Scale  
**Durée** : 60 min

## Pourquoi

SPIN Selling est LA méthode pour ventes complexes B2B. Au lieu de 'pousser' ton produit, tu guides le client à découvrir lui-même pourquoi il a besoin de toi. Les commerciaux SPIN closent 20% plus de deals.

## Objectif

Maîtriser les 4 types de questions SPIN pour qualifier et convertir efficacement.

## Livrable attendu

Script de découverte SPIN complet avec questions par type + transitions

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Préparer les questions Situation** — Contexte actuel du client (attention : pas trop !)
2. **Développer les questions Problème** — Douleurs, difficultés, insatisfactions
   > Prompt: Génère 10 questions 'Problème' pour découvrir les douleurs d'un [PERSONA] concernant [DOMAINE]
3. **Créer les questions Implication** — Conséquences et coûts du problème non résolu
4. **Formuler les questions Need-payoff** — Faire imaginer la valeur de la solution au client
5. **Assembler le script complet** — Enchaînement naturel avec transitions

## Pro tips

- Les questions Implication et Need-payoff sont les plus puissantes
- Limite les questions Situation (le client s'ennuie)
- Laisse le client conclure lui-même qu'il a besoin de toi

## Erreurs fréquentes

- Poser trop de questions Situation (interrogatoire)
- Sauter directement à la solution sans Implication
- Donner les réponses au lieu de laisser le client les trouver

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-spin-selling.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Enrichissement — besoin implicite→explicite & Advance

Compléments issus de la recherche de Rackham, au-delà des 4 types de questions :

- **Implicite → explicite** : dans les ventes importantes, seuls les besoins
  **explicites** (le client énonce lui-même le manque) prédisent l'achat. Le rôle
  des questions Implication est de faire passer un problème mineur au rang de
  besoin explicite.
- **Les 4 issues d'un entretien** : Commande / **Advance** (étape suivante
  concrète) / Continuation / Sans-suite. Viser un **Advance**, pas « demander la
  vente » ; juger au **comportement**, jamais aux compliments.
- **Bénéfice recadré (FAB)** : un vrai bénéfice répond à un besoin **explicite
  déjà exprimé** ; sinon ce n'est qu'un « avantage ». Ne pas déballer les
  fonctionnalités avant le besoin.
- **Articulation** : complète `scale-bant-qualification` — SPIN **construit** le
  « Need » (Implication → coût du statu quo) là où BANT ne fait que le cocher.

> Idées : Neil Rackham, *SPIN Selling* — distillation founder-playbook
> (MIT © 2026 AgentSeal). Reformulé.

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:coaching-pipeline` — application aux deals réels
- `rapido-forge:scale-bant-qualification` — grille de qualification complémentaire

## Passer à l'opérationnel

Cet exercice conçoit la méthode ; pour l'**appliquer aux données réelles** (fiches CRM, pipeline, factures…), passer à **`rapidocrm:coach-de-vente`** — il **lit ce livrable forge** (`./rapido-kb/startup/forge/`) comme base, puis agit sur les données MCP. Voir `reference/pont-forge-operations.md`.
