---
name: scale-linkedin-pixel
description: "Utiliser quand l'utilisateur veut installer le Insight Tag et configurer le tracking B2B (parcours scale StartupsForge)."
tags: [acquisition]
niveau: intermediaire
prerequis: [ideation-landing-page, ideation-persona-maker]
---

# Linkedin Pixel

**Catégorie** : Scale  
**Durée** : 30 min

## Pourquoi

Le LinkedIn Insight Tag est indispensable pour le B2B. Il te permet de tracker les décideurs qui visitent ton site et de les cibler avec des campagnes ultra-précises par entreprise, poste et secteur.

## Objectif

Installer le Insight Tag et configurer le tracking B2B.

## Livrable attendu

Insight Tag actif + audiences B2B créées + données entreprises

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Accéder à Campaign Manager** — Dans LinkedIn Campaign Manager, va dans Account Assets > Insight Tag
2. **Copier le tag** — Copie le code JavaScript du Insight Tag
3. **Installer sur le site** — Colle dans le header ou via Google Tag Manager
   > Prompt: Comment installer LinkedIn Insight Tag avec GTM ?
4. **Définir les conversions** — Crée des conversions : demo request, contact form, signup
5. **Analyser les Demographics** — Utilise Website Demographics pour voir qui visite

## Pro tips

- Website Demographics révèle les entreprises qui te visitent (gratuit!)
- Crée des audiences par taille d'entreprise et fonction
- Le retargeting LinkedIn a un CPM élevé mais un ROI B2B supérieur

## Erreurs fréquentes

- Attendre trop longtemps avant d'installer (perte de data)
- Ne pas définir de conversions
- Ignorer les Website Demographics (pépite gratuite)

## Données & serveurs MCP

- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-linkedin-pixel.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
