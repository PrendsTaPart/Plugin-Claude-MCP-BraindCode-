---
name: scale-meta-pixel
description: "Utiliser quand l'utilisateur veut installer le Meta Pixel avec les événements de conversion clés (parcours scale StartupsForge)."
tags: [acquisition]
niveau: intermediaire
prerequis: [ideation-landing-page, ideation-persona-maker]
---

# Meta Pixel

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

Le Meta Pixel permet de tracker les visiteurs de ton site et de les retargeter sur Facebook/Instagram. Sans pixel, tu paies pour du trafic sans pouvoir le reconvertir. C'est obligatoire pour des Ads rentables.

## Objectif

Installer le Meta Pixel avec les événements de conversion clés.

## Livrable attendu

Pixel installé + événements configurés + audience de retargeting créée

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Créer le Pixel** — Dans Meta Events Manager, crée un nouveau pixel
2. **Installer le code** — Via Google Tag Manager ou directement dans le header
   > Prompt: Comment installer Meta Pixel sur [TECHNOLOGIE] ?
3. **Configurer les événements** — PageView, ViewContent, AddToCart, Lead, Purchase
4. **Tester avec Pixel Helper** — Utilise l'extension Chrome pour vérifier
5. **Créer les audiences** — Visiteurs 7j, 30j, abandon panier, acheteurs

## Pro tips

- Active la Conversions API pour plus de précision (iOS 14+)
- Crée des Lookalike audiences sur tes meilleurs clients
- L'événement Purchase doit inclure la valeur

## Erreurs fréquentes

- Installer sans tester (Pixel Helper)
- Oublier les événements côté serveur (CAPI)
- Ne pas créer d'audiences avant de lancer les Ads

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Facebook ads** (`facebook-ads`, via le plugin `rapido-meta-ads`) — ⚠️ argent réel : tout se crée en PAUSED, activation après accord explicite

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-meta-pixel.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-meta-ads:pixel-et-retargeting` — pose du pixel + Test Events + audience
