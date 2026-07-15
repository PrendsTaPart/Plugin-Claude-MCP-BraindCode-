---
name: playbook-objections-vivant
description: Utiliser quand l'utilisateur veut un playbook d'objections, savoir quelles objections reviennent, ou comment répondre à une objection (« c'est trop cher », « je réfléchis »). Agrège les objections réelles (transcripts Fireflies si connecté, sinon notes RDV CRM et raisons de deals perdus), les classe par fréquence × étape × produit, et maintient ./rapido-kb/commercial/objections.md avec reformulation, réponse sourcée et preuve.
---

# Playbook d'objections vivant — nourri par les données

Le playbook qui **apprend** des vraies objections rencontrées, au lieu d'une liste figée.

## Étape 0 — Pont forge
- Livrable `scale-objections-playbook` comme structure de départ ; absent → défauts en
  le disant. Voir `reference/pont-forge-operations.md`.

## Sense (objections réelles)
- **Transcripts** via `rapido-marketing:sales-intelligence-fireflies` **si le MCP
  Fireflies est connecté** ; **sinon** : notes de RDV CRM (`get_historique_prospect`)
  et **raisons de deals perdus** (`close_opportunity` / champs de perte). Serveur
  absent = volet sauté en le disant.

## Plan (classer & répondre)
- Classer chaque objection par **fréquence × étape du funnel × produit**
  (Studio / Agence / SaaS / FoodEatUp).
- Pour chacune : **reformulation**, **réponse recommandée** (technique **sourcée** :
  Voss, Challenger…), **preuve à l'appui** (cas client, chiffre réel).

## Act (mise à jour incrémentale)
- Maintenir `./rapido-kb/commercial/objections.md` : **ajout daté incrémental, jamais
  d'écrasement**. Chaque objection nouvelle ou plus fréquente enrichit le playbook.

## Frontière
- **`rapido-meta-ads:hundred-million-offers`** face à « c'est trop cher » **redessine
  l'OFFRE** (valeur, garanties, bonus). **Moi = la RÉPONSE de vente** (reformuler,
  traiter l'objection dans l'échange). Deux réponses complémentaires à « trop cher ».

## Garde-fous
Objections **réelles** (jamais inventées) ; réponses **sourcées** (technique + preuve) ;
mise à jour **incrémentale datée** ; Fireflies optionnel (absence dite).
