---
name: boost-post-instagram
description: Utiliser quand l'utilisateur veut booster un post ou sponsoriser son meilleur post Instagram. Identifie le top post via les insights CMS puis boost en deux temps — plan (confirmed=false), accord, puis confirmed=true — activation confirmée séparément.
---

# Boost de post Instagram (CMS × Meta)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-meta-ads.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md`.

## Workflow

1. **Identifier le top post** — côté rapidocms : `list_scheduled_posts`
   (période récente) + `post_insights` (lots de 10 max) → le post au meilleur
   engagement. Si l'utilisateur désigne déjà le post, sauter cette étape.
2. **Retrouver le média côté Meta** — `ads_get_ig_accounts` (compte IG lié)
   puis `ads_get_ig_media` : faire correspondre le post CMS au media IG
   (date + visuel). En cas d'ambiguïté, montrer les candidats.
3. **PLAN d'abord** — `ads_boost_ig_post` avec `confirmed: false` : l'outil
   renvoie le plan résolu (budget dans la DEVISE RÉELLE du compte, durée,
   cible, objectif par défaut).
4. **Présenter le plan** — budget/jour, durée, coût maximum, cible, et ce que
   « booster » fera (portée payante sur ce media). Ajuster si demandé
   (re-plan avec les nouveaux paramètres, toujours confirmed=false).
5. **Confirmer** — accord explicite → `ads_boost_ig_post` avec
   `confirmed: true` (le hook demandera confirmation). Le boost est créé
   PAUSED.
6. **Activation séparée** — l'activation (`ads_activate_entity`) est une
   SECONDE confirmation distincte : récap final puis activation.
7. **Boucle** — noter le boost dans la campagne CRM/CMS correspondante ;
   suivi via `pilotage-performance-ads`.

## Garde-fous

- Jamais de `confirmed: true` sans que le plan ait été montré ET approuvé.
- Budget du plan comparé au plafond maison (hook `plafond-budget`).
- Booster un post qui performe déjà organiquement : rappeler que le boost
  hérite du post (pas de modification possible du texte après coup).
