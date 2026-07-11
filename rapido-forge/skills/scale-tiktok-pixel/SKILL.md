---
name: scale-tiktok-pixel
description: "Utiliser quand l'utilisateur veut préparer son tracking TikTok pour de futures campagnes (parcours scale StartupsForge)."
tags: [acquisition]
niveau: intermediaire
prerequis: [ideation-landing-page, ideation-persona-maker]
---

# Tiktok Pixel

**Catégorie** : Scale  
**Durée** : 30 min

## Pourquoi

Le TikTok Pixel est essentiel si tu cibles les 18-35 ans. Le coût par impression est encore bas comparé à Meta. Installer le pixel maintenant te prépare pour des campagnes rentables.

## Objectif

Préparer ton tracking TikTok pour de futures campagnes.

## Livrable attendu

TikTok Pixel installé + événements configurés + première audience

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Créer le Pixel** — Dans TikTok Ads Manager > Assets > Events > Web Events
2. **Choisir l'installation** — Manual, Partner (Shopify, GTM), ou Events API
3. **Installer le code** — Copie le code base dans le header de ton site
   > Prompt: Comment installer TikTok Pixel sur [TECHNOLOGIE] ?
4. **Configurer les événements** — ViewContent, AddToCart, CompletePayment, SubmitForm
5. **Tester avec Pixel Helper** — Utilise TikTok Pixel Helper pour vérifier

## Pro tips

- Combine Web Pixel + Events API pour plus de précision
- TikTok a besoin de 50 conversions/semaine pour optimiser
- Les audiences Custom peuvent être créées à partir du pixel

## Erreurs fréquentes

- Lancer des campagnes sans pixel (impossible d'optimiser)
- Oublier l'Events API pour iOS
- Ne pas tester avant de lancer des Ads

## Données & serveurs MCP

- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-tiktok-pixel.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
