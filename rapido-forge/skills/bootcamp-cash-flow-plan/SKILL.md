---
name: bootcamp-cash-flow-plan
description: "Utiliser quand l'utilisateur veut prévois ses flux de trésorerie (bootcamp 5 jours StartupsForge — Jour 5)."
tags: [finance]
niveau: debutant
---

# Plan de Trésorerie

**Bootcamp 5 jours — Jour 5**  
**Catégorie** : Finance  
**Framework** : Cash Flow Forecasting  
**Durée** : 40 min

## Objectif

Prévois tes flux de trésorerie

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister les encaissements** — quand l'argent ARRIVE vraiment (délais de paiement, pas la facturation)
2. **Lister les décaissements** — salaires, loyer, outils, TVA, charges sociales avec leurs vraies échéances
3. **Construire le plan mensuel 12 mois** — solde de départ + entrées − sorties, mois par mois
4. **Identifier le point bas** — le mois où la trésorerie est minimale : c'est LE chiffre à surveiller
5. **Plan B** — si le point bas passe sous le seuil : quelles dépenses coupables, quel financement relais

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/bootcamp/bootcamp-cash-flow-plan.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-suite:cash-flow-snapshot` — projection 30/60/90 j sur données réelles
- `rapido-startup:plan-financier-previsionnel` — plan de trésorerie prévisionnel complet
