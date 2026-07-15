---
name: lancement-campagne-tiktok
description: Utiliser quand l'utilisateur veut lancer/créer une campagne TikTok Ads, monter un ad group, une pub TikTok. Construit la campagne → ad group → créatif → ad TOUT EN ÉTAT INACTIF, avec récapitulatif du coût maximum ; l'activation est une étape séparée sur confirmation écrite. Verrouillé argent réel.
---

# Lancement de campagne TikTok (100 % inactif)

Monte la structure **entièrement en état inactif** ; **rien n'est activé** sans une
confirmation écrite séparée. Miroir de `rapido-meta-ads:lancement-campagne-meta`,
**plus strict**.

## Étape 0
`reference/garde-fous-tiktok.md`. Budget max et plafonds `./rapido-kb/marketing/`.
Objectif, audience, produit → données réelles (CRM/CMS), jamais inventées.

## Sense
- Contexte : objectif (trafic, conversions, notoriété), audience, budget cible,
  créatifs disponibles (ou à produire — voir Act).

## Plan
- Structure proposée : **campagne → ad group → créatif → ad**, ciblage, budget,
  enchère — **coût maximum estimé affiché AVANT** (devise réelle), dans les **plafonds KB**.
- **Brief créatif** délégué à `rapidocms` / `rapido-video` (le plugin ne fabrique pas
  la vidéo ; il cadre le brief).

## Act (VERROUILLÉ)
- Créer chaque entité **en état INACTIF/brouillon** (l'API doit le permettre — sinon
  **ne pas créer**, seulement lire ; hook `garde-argent-reel-tiktok` **DENY** sur
  création active).
- **Activation = étape séparée, confirmation écrite explicite** (hook **ASK**), coût
  max rappelé.
- **Récapitulatif obligatoire** : IDs, statut (INACTIF), budgets, coût max.

## Anti-collision
- **`rapido-meta-ads:lancement-campagne-meta`** = Meta. Ici = **TikTok**, verrous plus stricts.

## Garde-fous
Création **inactive** obligatoire ; **activation séparée confirmée** ; budget **plafonné
KB** ; coût max **annoncé** ; récap IDs/statuts/budgets ; données réelles.
