---
name: ideation-analytics-setup
description: "Utiliser quand l'utilisateur veut configurer GA4, Mixpanel ou équivalent (parcours idéation StartupsForge)."
tags: [data]
niveau: intermediaire
---

# Analytics Setup

**Catégorie** : Idéation  
**Durée** : 45-60 min

## Pourquoi

Sans analytics, tu navigues à l'aveugle. Mesurer c'est pouvoir améliorer.

## Objectif

Configurer GA4, Mixpanel ou équivalent.

## Livrable attendu

Analytics opérationnel avec events clés

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Choisir l'outil** — GA4 (gratuit) ou Mixpanel (freemium)
2. **Installer le tracking** — Via GTM ou code direct
3. **Configurer les events** — Signup, login, conversion clés
4. **Créer les dashboards** — Métriques principales visibles
5. **Tester le tracking** — Vérifier chaque event

## Pro tips

- Track les actions, pas juste les pages vues
- Utilise les funnels pour identifier les drop-offs
- Configure des alertes pour les anomalies

## Erreurs fréquentes

- Ne tracker que les pages vues
- Pas de test avant go-live
- Trop d'events qui diluent les insights

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-analytics-setup.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-forge:scale-google-analytics-4` — setup GA4 détaillé
