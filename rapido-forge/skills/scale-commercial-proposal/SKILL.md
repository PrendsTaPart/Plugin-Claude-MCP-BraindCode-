---
name: scale-commercial-proposal
description: "Utiliser quand l'utilisateur veut créer un template de proposition commerciale B2B convaincant et professionnel (parcours scale StartupsForge)."
tags: [vente]
niveau: intermediaire
---

# Commercial Proposal

**Catégorie** : Scale  
**Durée** : 90 min

## Pourquoi

Une proposition commerciale professionnelle augmente la confiance et réduit le cycle de vente. Les propales bien structurées ont 65% de chances de plus d'être acceptées.

## Objectif

Créer un template de proposition commerciale B2B convaincant et professionnel.

## Livrable attendu

Template de proposition avec sections clés + version personnalisable

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Structurer les sections** — Exec summary, contexte, solution, pricing, timeline, about us
2. **Écrire l'Executive Summary** — 1 page max, résumé du problème et de ta proposition
   > Prompt: Écris un Executive Summary pour une proposition de [SOLUTION] à [ENTREPRISE]
3. **Détailler la solution** — Fonctionnalités → bénéfices → preuves (cas clients, ROI)
4. **Présenter le pricing** — Options de pricing, breakdown clair, conditions
5. **Ajouter la crédibilité** — Logos clients, témoignages, certifications

## Pro tips

- L'Exec Summary est lu par les décideurs - soigne-le particulièrement
- Propose 3 options de pricing (le middle gagne souvent)
- Inclus une deadline pour créer l'urgence

## Erreurs fréquentes

- Proposition générique non personnalisée
- Trop de features, pas assez de bénéfices
- Oublier le call-to-action et les prochaines étapes

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-commercial-proposal.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-canva:supports-commerciaux` — proposition générée dans Canva, liée au deal CRM
