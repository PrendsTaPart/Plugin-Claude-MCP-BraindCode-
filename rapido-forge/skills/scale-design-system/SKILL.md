---
name: scale-design-system
description: "Utiliser quand l'utilisateur veut créer un Design System V1 avec les composants essentiels (parcours scale StartupsForge)."
tags: [produit]
niveau: intermediaire
---

# Design System

**Catégorie** : Scale  
**Durée** : 90 min

## Pourquoi

Un Design System assure cohérence et rapidité de développement. Les équipes avec DS développent les UI 30% plus vite et avec 5x moins d'incohérences visuelles.

## Objectif

Créer un Design System V1 avec les composants essentiels.

## Livrable attendu

Figma Design System avec tokens, composants et guidelines

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir les tokens** — Couleurs, typographies, espacements, ombres
2. **Créer les composants atomiques** — Boutons, inputs, labels, icônes, badges
   > Prompt: Quels sont les composants essentiels pour un Design System MVP ?
3. **Construire les molécules** — Cards, form groups, navigation items
4. **Assembler les organismes** — Headers, footers, sidebars, modals
5. **Documenter les guidelines** — Usage, dos/don'ts, accessibilité

## Pro tips

- Commence par les composants que tu utilises le plus
- Prévois les états : hover, focus, disabled, error
- Pense accessibilité dès le début (contraste, focus visible)

## Erreurs fréquentes

- DS trop complexe pour commencer (MVP d'abord)
- Pas de documentation (les devs ne l'utilisent pas)
- Composants trop spécifiques (pas réutilisables)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Lovable** (`lovable`, via le plugin `rapido-lovable`) pour la construction réelle
- **Canva** (`canva`, via le plugin `rapido-canva`) pour la production graphique

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-design-system.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-lovable:ui-styling` — design system shadcn/ui
- `rapido-lovable:frontend-design` — audit et documentation
