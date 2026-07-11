---
name: scale-fundraising-plan
description: "Utiliser quand l'utilisateur veut définir sa stratégie de financement sur les 24 prochains mois (parcours scale StartupsForge)."
---

# Fundraising Plan

**Catégorie** : Scale  
**Durée** : 60 min

## Pourquoi

Un plan de financement structuré maximise tes chances de lever au bon moment et au bon montant. Lever trop tôt dilue, lever trop tard risque la faillite.

## Objectif

Définir ta stratégie de financement sur les 24 prochains mois.

## Livrable attendu

Plan de financement avec montants, timing, utilisation et milestones

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir les milestones** — Quels objectifs atteindre avant chaque round ?
2. **Calculer les besoins** — Combien pour atteindre chaque milestone + buffer 6 mois
   > Prompt: Combien lever en [STAGE] pour un SaaS visant [MILESTONE] ?
3. **Choisir les sources** — Bootstrap, BA, VC, grants, debt, crowdfunding ?
4. **Définir le timing** — Quand commencer à lever ? (6 mois avant besoin)
5. **Planifier l'utilisation** — Use of funds : % produit, marketing, équipe, etc.

## Pro tips

- Lève pour 18-24 mois de runway minimum
- Les milestones doivent justifier une valorisation 2-3x supérieure
- Garde des options (VC n'est pas la seule voie)

## Erreurs fréquentes

- Lever trop peu et devoir relever 6 mois après
- Pas de milestone clair pour le prochain round
- Lever sans savoir précisément l'utilisation des fonds

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-fundraising-plan.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-startup:interview-business-plan` — dossier de levée complet
