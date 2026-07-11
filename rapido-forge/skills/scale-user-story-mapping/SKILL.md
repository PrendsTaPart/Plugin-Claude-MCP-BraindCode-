---
name: scale-user-story-mapping
description: "Utiliser quand l'utilisateur veut cartographier les parcours utilisateurs en user stories prioritisées (parcours scale StartupsForge)."
---

# User Story Mapping

**Catégorie** : Scale  
**Durée** : 60 min

## Pourquoi

Le User Story Mapping structure ton backlog par parcours utilisateur. Ça évite de construire des features isolées et assure une expérience cohérente. Les équipes qui l'utilisent livrent 40% plus de valeur.

## Objectif

Cartographier les parcours utilisateurs en user stories prioritisées.

## Livrable attendu

User Story Map complet avec backbone, walking skeleton et releases

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir le backbone** — Grandes activités utilisateur de gauche à droite
2. **Ajouter les user tasks** — Sous chaque activité, les actions détaillées
   > Prompt: Liste les tâches utilisateur pour l'activité '[ACTIVITÉ]' dans [PRODUIT]
3. **Écrire les user stories** — Pour chaque tâche : 'En tant que X, je veux Y pour Z'
4. **Prioriser verticalement** — En haut = essentiel, en bas = nice-to-have
5. **Tracer les releases** — Lignes horizontales séparant MVP, V1, V2

## Pro tips

- Le 'walking skeleton' en haut = le minimum pour un parcours complet
- Implique les utilisateurs dans la création de la map
- La largeur de la map montre l'étendue du produit

## Erreurs fréquentes

- Trop de détails dès le début (reste high-level d'abord)
- Stories techniques au lieu de stories utilisateur
- Oublier les edge cases et parcours d'erreur

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-user-story-mapping.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
