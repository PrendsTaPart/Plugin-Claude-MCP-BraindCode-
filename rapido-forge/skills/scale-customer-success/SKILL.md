---
name: scale-customer-success
description: "Utiliser quand l'utilisateur veut définir son playbook Customer Success avec onboarding, check-ins et expansion (parcours scale StartupsForge)."
tags: [vente, organisation]
niveau: intermediaire
---

# Customer Success

**Catégorie** : Scale  
**Durée** : 60 min

## Pourquoi

Le Customer Success détermine ta rétention et ton NPS. Réduire le churn de 5% augmente les profits de 25-95%. Un client satisfait réfère en moyenne 2.6 nouveaux clients.

## Objectif

Définir ton playbook Customer Success avec onboarding, check-ins et expansion.

## Livrable attendu

Playbook CS complet : onboarding checklist, health score, escalation process

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir l'onboarding idéal** — Étapes, milestones, timeline pour activer le client
2. **Créer le Health Score** — Métriques d'engagement + usage + satisfaction
   > Prompt: Crée un Customer Health Score pour un SaaS [TYPE] avec les indicateurs clés
3. **Planifier les touchpoints** — Check-ins réguliers : J+7, J+30, J+90, trimestriel
4. **Définir les playbooks par situation** — Client à risque, opportunité expansion, renouvellement
5. **Créer le processus d'escalade** — Quand alerter ? Qui ? Quelles actions ?

## Pro tips

- Le Time-to-Value (TTV) est LA métrique critique d'onboarding
- Un Health Score doit combiner usage + engagement + business outcomes
- Les clients qui ne se plaignent jamais sont souvent les plus à risque de churn

## Erreurs fréquentes

- Se concentrer uniquement sur les clients bruyants
- Attendre le renouvellement pour s'occuper de la rétention
- Ne pas définir ce qu'est le 'succès' pour chaque client

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-customer-success.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:draft-response` — réponses clients délicates
- `rapidocrm:ticket-triage` — triage des tickets
