---
name: scale-google-analytics-4
description: "Utiliser quand l'utilisateur veut installer et configurer GA4 pour tracker son site web avec les événements clés (parcours scale StartupsForge)."
tags: [data]
niveau: intermediaire
---

# Google Analytics 4

**Catégorie** : Scale  
**Durée** : 60 min

## Pourquoi

Google Analytics 4 est la nouvelle norme pour mesurer ton trafic web. Sans GA4, tu es aveugle sur tes visiteurs, leurs sources et leurs comportements. C'est la base de toute stratégie SEO/Ads data-driven.

## Objectif

Installer et configurer GA4 pour tracker ton site web avec les événements clés.

## Livrable attendu

GA4 installé + événements de conversion configurés + premier rapport

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Créer la propriété GA4** — Dans Google Analytics, crée une nouvelle propriété GA4
2. **Installer le tag** — Via Google Tag Manager ou directement dans le code HTML
   > Prompt: Comment installer GA4 sur un site [TECHNOLOGIE] ?
3. **Configurer les événements** — Définis les events clés : page_view, scroll, click, form_submit, purchase
4. **Créer les conversions** — Marque les événements importants comme conversions (signup, achat)
5. **Configurer les audiences** — Crée des audiences pour le remarketing

## Pro tips

- Active le mode Debug pour tester avant le déploiement
- Utilise Google Tag Manager pour plus de flexibilité
- Configure les événements e-commerce si tu vends
- Lie GA4 à Google Ads pour optimiser les campagnes

## Erreurs fréquentes

- Oublier de vérifier que le tag se déclenche
- Ne pas configurer les conversions
- Ignorer les filtres pour exclure le trafic interne

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-google-analytics-4.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
