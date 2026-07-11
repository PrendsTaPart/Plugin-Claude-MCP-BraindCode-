---
name: scale-kpi-dashboard
description: "Utiliser quand l'utilisateur veut créer un dashboard des 10 métriques essentielles à suivre chaque semaine (parcours scale StartupsForge)."
---

# Kpi Dashboard

**Catégorie** : Scale  
**Durée** : 60 min

## Pourquoi

Un dashboard KPI te donne une vue temps réel sur la santé de ton business. Les fondateurs data-driven prennent des décisions 5x plus vite et avec 80% moins d'erreurs.

## Objectif

Créer un dashboard des 10 métriques essentielles à suivre chaque semaine.

## Livrable attendu

Dashboard live avec 10 KPIs, alertes automatiques et revue hebdomadaire

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Sélectionner les 10 KPIs** — Revenue, users, activation, retention, NPS, etc.
2. **Définir la fréquence** — Daily (usage), Weekly (growth), Monthly (financial)
   > Prompt: Quels sont les 10 KPIs essentiels pour un SaaS [STAGE] ?
3. **Configurer les sources** — Stripe, Analytics, CRM, Backend
4. **Créer les alertes** — Si KPI < seuil, notification immédiate
5. **Définir la cadence de revue** — Rituels : daily standup, weekly review, monthly board

## Pro tips

- Maximum 10 KPIs sur le dashboard principal (pas de data overload)
- Chaque KPI doit avoir un owner responsable
- Compare toujours aux périodes précédentes (WoW, MoM)

## Erreurs fréquentes

- Trop de métriques = analyse paralysis
- Métriques vanity (followers) au lieu de métriques actionables
- Dashboard non mis à jour (devient inutile)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-kpi-dashboard.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-startup:catalogue-kpi` — formules et calculs par script
