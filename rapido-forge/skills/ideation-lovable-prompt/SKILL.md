---
name: ideation-lovable-prompt
description: "Utiliser quand l'utilisateur veut générer le code de son site web avec Lovable.dev (parcours idéation StartupsForge)."
tags: [produit]
niveau: debutant
---

# Lovable Prompt

**Catégorie** : Idéation  
**Durée** : 60-90 min

## Pourquoi

Lovable.dev te permet de créer un site web complet sans coder. En 2024, les fondateurs non-techniques peuvent lancer leur MVP en quelques heures grâce aux outils no-code/low-code.

## Objectif

Générer le code de ton site web avec Lovable.dev.

## Livrable attendu

Site web fonctionnel déployé avec toutes les pages essentielles

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Préparer le brief complet** — Nom, description, couleurs, structure, contenu
2. **Générer la V1** — Prompt initial décrivant tout le site
   > Prompt: Crée un site web moderne pour [STARTUP]. Page d'accueil avec Hero, Problème/Solution, Témoignages, Pricing, Footer. Style: [VIBE]. Couleurs: [PALETTE]
3. **Itérer sur le design** — Affine chaque section avec des prompts ciblés
4. **Ajouter les fonctionnalités** — Formulaires, authentification, paiement
5. **Déployer** — Publie sur le domaine personnalisé

## Pro tips

- Sois très précis dans tes prompts - donne des exemples
- Itère section par section plutôt que tout d'un coup
- Sauvegarde des versions régulièrement

## Erreurs fréquentes

- Prompts trop vagues ('fais un beau site')
- Vouloir tout parfait du premier coup
- Ignorer le responsive mobile

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Lovable** (`lovable`, via le plugin `rapido-lovable`) pour la construction réelle

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-lovable-prompt.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-lovable:frontend-design` — direction visuelle
- `rapido-lovable:ui-ux-pro-max` — styles, palettes, typos
