---
name: scale-prototype
description: "Utiliser quand l'utilisateur veut créer un prototype interactif navigable de son MVP (parcours scale StartupsForge)."
---

# Prototype

**Catégorie** : Scale  
**Durée** : 60 min

## Pourquoi

Un prototype cliquable permet de tester l'UX sans coder. Les tests sur prototype révèlent 85% des problèmes d'usabilité avant le développement.

## Objectif

Créer un prototype interactif navigable de ton MVP.

## Livrable attendu

Prototype Figma/Framer avec flows principaux cliquables

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Importer les wireframes** — Utilise tes wireframes comme base
2. **Ajouter le style visuel** — Appliquer le Design System V1
   > Prompt: Génère un prototype haute fidélité pour [WIREFRAME] avec un style [VIBE]
3. **Créer les interactions** — Clics, hover, transitions entre pages
4. **Tester le flow principal** — Onboarding → Core action → Success
5. **Partager le lien** — Lien de preview pour tests utilisateurs

## Pro tips

- Commence par le 'happy path' avant les edge cases
- Utilise des smart animate pour un rendu réaliste
- Le prototype doit donner l'illusion d'un vrai produit

## Erreurs fréquentes

- Trop de pages (garde le scope minimal)
- Interactions incomplètes (boutons qui ne font rien)
- Pas de feedback visuel sur les actions

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Lovable** (`lovable`, via le plugin `rapido-lovable`) pour la construction réelle

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-prototype.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-lovable:frontend-design` — prototype Lovable réel
