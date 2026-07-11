---
name: scale-meta-ads-campaign
description: "Utiliser quand l'utilisateur veut créer et lancer une campagne Meta Ads complète (parcours scale StartupsForge)."
tags: [acquisition]
niveau: intermediaire
prerequis: [ideation-landing-page, ideation-persona-maker]
---

# Meta Ads Campaign

**Catégorie** : Scale  
**Durée** : 120 min

## Pourquoi

Meta Ads (Facebook/Instagram) reste le canal social #1 avec 3 milliards d'utilisateurs. Le ciblage et le machine learning de Meta peuvent générer des ROAS de 3-10x si bien configuré.

## Objectif

Créer et lancer une campagne Meta Ads complète.

## Livrable attendu

Campagne active + 3 audiences + 3 créatives + tracking

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Choisir l'objectif** — Conversions, Traffic, Leads selon ton funnel
2. **Créer les audiences** — Lookalike 1%, Retargeting, Intérêts larges
   > Prompt: Quelle structure d'audiences Meta Ads pour une startup [SECTEUR] ?
3. **Créer les visuels** — 3 formats : Image, Vidéo courte, Carrousel
4. **Rédiger les copies** — Hook + Pain + Solution + CTA. Test 3 variations
5. **Configurer le tracking** — Vérifie le pixel, configure CAPI, active les Advantage+
6. **Lancer et monitorer** — Budget test, puis scale les winners

## Pro tips

- Advantage+ Shopping est très performant pour l'e-commerce
- 3 audiences min pour laisser l'algo optimiser
- La créative compte pour 70% du succès
- Teste les UGC (User Generated Content)

## Erreurs fréquentes

- Budget trop faible pour sortir du learning phase
- Trop d'audiences/adsets (dilution)
- Ignorer les placements automatiques

## Données & serveurs MCP

- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord
- **Facebook ads** (`facebook-ads`, via le plugin `rapido-meta-ads`) — ⚠️ argent réel : tout se crée en PAUSED, activation après accord explicite

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-meta-ads-campaign.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-meta-ads:lancement-campagne-meta` — exécution réelle, garde-fous argent réel
