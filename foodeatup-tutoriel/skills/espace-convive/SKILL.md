---
name: espace-convive
description: Utiliser quand la question vient d'un client final de restaurant ou le concerne, dit « comment je commande avec le QR code », « comment j'adhère au programme de fidélité », « où laisser un avis », ou quand un restaurateur demande « qu'est-ce que vivent mes clients avec FoodEatUp ». Déroule le parcours convive geste par geste, avec le module professionnel à activer en face de chacun.
---

# Espace convive (ce que vit le client du restaurant)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **`parcours_client_restaurant`** — filtrer par `section` si la question
   est ciblée (« Commander, payer, réserver », « Le programme de fidélité »,
   « Après le repas »). Chaque geste renvoie son objectif, son astuce, le
   lien de sa fiche et le module professionnel requis.
2. **Répondre au convive** avec le geste précis (trouver la carte, commander
   au QR code, payer, réserver, rejoindre la fidélité, cumuler/utiliser des
   points, gérer ses offres, laisser un avis) et son astuce, telle que
   renvoyée.
3. **Répondre au restaurateur** en miroir : pour chaque geste convive
   évoqué, nommer le module à activer côté pro (champ renvoyé) et proposer
   la formation correspondante (skill `explorer-un-module` ou
   `parcours-sur-mesure`).
4. **Production de contenu convive** (le restaurateur veut ces vidéos) :
   `brief_video_client` (slug, ou tous les briefs) — objectif, plan en cinq
   points, ton, durée visée, vignette déjà produite ; relais au skill
   `studio-production-tutos` pour prioriser.

## Garde-fous

- **Ces vidéos ne sont pas tournées : ne JAMAIS annoncer de lien vidéo** pour
  le parcours convive — les liens de fiches renvoyés suffisent, les briefs
  décrivent ce qui reste à produire.
- Un geste convive qui dépend d'un module non activé chez ce restaurateur se
  dit conditionnel (« si la fidélité est activée… ») — on ne promet pas une
  expérience que le compte ne sert pas.
- Les questions de prix de l'abonnement pro → skill `decouvrir-l-offre`.
