---
name: ideation-hero-image
description: "Utiliser quand l'utilisateur veut générer des visuels professionnels pour son site web (parcours idéation StartupsForge)."
tags: [contenu]
niveau: debutant
---

# Hero Image

**Catégorie** : Idéation  
**Durée** : 30-45 min

## Pourquoi

Les visuels captent l'attention 60 000x plus vite que le texte. Une image Hero de qualité augmente le temps passé sur la page et le taux de conversion de 40%.

## Objectif

Générer des visuels professionnels pour ton site web.

## Livrable attendu

Image Hero + 3-5 visuels pour les sections du site

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir le brief visuel** — Style, ambiance, couleurs, sujets
2. **Rédiger le prompt Hero** — Image principale représentant ta marque
   > Prompt: [SUJET], [STYLE], [COULEURS], professional photography, 16:9 aspect ratio --v 6 --ar 16:9
3. **Générer les images sections** — Visuels pour chaque partie du site
4. **Éditer si nécessaire** — Retouches avec Canva ou Photoshop
5. **Optimiser pour le web** — Compression, formats WebP

## Pro tips

- Maintiens une cohérence visuelle entre toutes les images
- Évite les visages générés (uncanny valley)
- Compresse les images pour le chargement rapide

## Erreurs fréquentes

- Images génériques de type 'stock photo'
- Incohérence de style entre les visuels
- Images trop lourdes ralentissant le site

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Lovable** (`lovable`, via le plugin `rapido-lovable`) pour la construction réelle

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-hero-image.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocms:prompt-engineering-visuel` — génération d'image méthodique
