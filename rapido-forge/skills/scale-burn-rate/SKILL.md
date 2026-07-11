---
name: scale-burn-rate
description: "Utiliser quand l'utilisateur veut calculer son burn rate actuel et projeter son runway (parcours scale StartupsForge)."
tags: [finance]
niveau: expert
prerequis: [ideation-financial-forecast]
---

# Burn Rate

**Catégorie** : Scale  
**Durée** : 30 min

## Pourquoi

Le Burn Rate et le Runway déterminent combien de temps tu peux survivre. Manquer de cash est la cause #1 de mort des startups. Tu dois toujours savoir combien de mois il te reste.

## Objectif

Calculer ton burn rate actuel et projeter ton runway.

## Livrable attendu

Dashboard Burn Rate avec runway, triggers d'alerte et plan de contingence

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Calculer le Gross Burn** — Total dépenses mensuelles (tout inclus)
2. **Calculer le Net Burn** — Gross Burn - Revenus mensuels = cash perdu/mois
   > Prompt: Avec des dépenses de [X]€/mois et des revenus de [Y]€/mois, quel est le net burn ?
3. **Calculer le Runway** — Cash en banque ÷ Net Burn = mois restants
4. **Définir les seuils d'alerte** — 6 mois = alerte, 3 mois = urgence
5. **Préparer le plan de contingence** — Si runway < 6 mois, quelles actions ?

## Pro tips

- Toujours avoir 6+ mois de runway avant de commencer une levée
- Le runway minimum confortable est 12-18 mois
- Revois ton burn mensuellement, pas trimestriellement

## Erreurs fréquentes

- Oublier des dépenses dans le calcul du burn
- Être trop optimiste sur les revenus futurs
- Attendre le dernier moment pour lever (desperation fundraising)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-burn-rate.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-startup:catalogue-kpi` — burn/runway par script sur données Stripe
