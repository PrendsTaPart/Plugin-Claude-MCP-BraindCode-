---
name: bootcamp-financial-projections
description: "Utiliser quand l'utilisateur veut créer ses projections sur 3 ans (bootcamp 5 jours StartupsForge — Jour 5)."
tags: [finance]
niveau: debutant
---

# Prévisions Financières

**Bootcamp 5 jours — Jour 5**  
**Catégorie** : Finance  
**Framework** : Financial Modeling  
**Durée** : 50 min

## Objectif

Crée tes projections sur 3 ans

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Récupérer les hypothèses sourcées** — prix, conversion, coûts : depuis la KB, chaque chiffre a une source ou la mention « confiance faible »
2. **Construire le bottom-up** — capacité commerciale réelle → clients/mois → CA ; pas de courbe en crosse de hockey
3. **3 scénarios** — bas (hypothèses faibles dégradées), central, haut ; le bas doit rester survivable
4. **Calculs par script** — point mort, runway, besoin de financement : jamais de tête
5. **Restituer** — tableau 36 mois + les 3 hypothèses qui changent tout, daté en KB

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/bootcamp/bootcamp-financial-projections.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-startup:plan-financier-previsionnel` — prévisionnel 3 ans, point mort, scénarios — calculs par script
