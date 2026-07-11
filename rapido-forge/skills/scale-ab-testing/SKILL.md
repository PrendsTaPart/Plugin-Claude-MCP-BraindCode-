---
name: scale-ab-testing
description: "Utiliser quand l'utilisateur veut définir un plan de 5 tests A/B prioritaires avec hypothèses et métriques (parcours scale StartupsForge)."
---

# Ab Testing

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

L'A/B testing élimine les opinions et décide sur les données. Les équipes qui testent systématiquement améliorent leurs conversions de 37% en moyenne.

## Objectif

Définir un plan de 5 tests A/B prioritaires avec hypothèses et métriques.

## Livrable attendu

Plan de tests A/B avec hypothèses, variations, sample size et success metrics

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Identifier les pages à fort trafic** — Landing page, pricing, checkout = impact maximal
2. **Formuler les hypothèses** — 'Si [changement], alors [résultat] parce que [raison]'
   > Prompt: Génère 5 hypothèses d'A/B tests pour améliorer la conversion de [PAGE]
3. **Définir les variations** — A = contrôle, B = une seule variable modifiée
4. **Calculer le sample size** — Combien de visiteurs pour signification statistique ?
5. **Définir les success metrics** — KPI primaire + KPIs secondaires à surveiller

## Pro tips

- Teste UNE variable à la fois pour des résultats clairs
- Attends la signification statistique avant de conclure (95%+)
- Les gros changements > micro-optimisations

## Erreurs fréquentes

- Arrêter le test trop tôt (pas assez de data)
- Tester plusieurs variables simultanément
- Ignorer les segments (mobile vs desktop)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Facebook ads** (`facebook-ads`, via le plugin `rapido-meta-ads`) — ⚠️ argent réel : tout se crée en PAUSED, activation après accord explicite

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-ab-testing.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-meta-ads:tests-ab-meta` — A/B tests publicitaires réels
