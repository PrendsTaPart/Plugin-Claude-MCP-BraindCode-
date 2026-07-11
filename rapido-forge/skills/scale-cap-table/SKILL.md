---
name: scale-cap-table
description: "Utiliser quand l'utilisateur veut créer et simuler sa table de capitalisation avant/après levée (parcours scale StartupsForge)."
---

# Cap Table

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

La Cap Table montre la répartition du capital entre fondateurs, investisseurs, et pool BSPC/Stock Options. Une cap table mal gérée crée des conflits et bloque les futures levées.

## Objectif

Créer et simuler ta table de capitalisation avant/après levée.

## Livrable attendu

Cap Table V1 avec simulation de dilution sur 3 rounds

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister les actionnaires actuels** — Fondateurs, parts, valorisation implicite
2. **Définir le pool BSPC** — Typiquement 10-15% pour futurs recrutements clés
   > Prompt: Quel pool de BSPC prévoir pour une startup en seed dans [SECTEUR] ?
3. **Simuler le premier round** — Montant levé, valorisation pre-money, dilution
4. **Simuler les rounds suivants** — Seed, Serie A, Serie B - dilution cumulée
5. **Analyser la détention finale** — % fondateurs après Series B, seuils critiques

## Pro tips

- Garde au moins 50%+ après le seed pour garder le contrôle
- Le pool BSPC dilue AVANT les investisseurs (pre-money)
- Anticipe les clauses de liquidation préférentielle

## Erreurs fréquentes

- Donner trop d'equity trop tôt (advisors, premiers employés)
- Pool BSPC trop petit = dilution fondateurs au prochain round
- Ignorer les préférences de liquidation

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-cap-table.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
