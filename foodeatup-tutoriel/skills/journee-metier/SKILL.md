---
name: journee-metier
description: Utiliser quand on raisonne par poste, que l'utilisateur dit « à quoi ressemble la journée d'un manager avec FoodEatUp », « le quotidien de mon chef de rang », « cette vidéo est pour quel poste ? », « je tiens une boulangerie, c'est adapté ? ». Raconte la journée type d'un métier, situe un tutoriel dans les parcours de poste et ancre le tout dans le bon secteur.
---

# Journée métier (le logiciel vu d'un poste)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **Le secteur d'abord** si doute : `secteur_foodeatup` (`restaurant`,
   `boulangerie`, `reseau`) — les postes proposés en dépendent.
2. **La journée d'un poste** : `journee_type` (`metierSlug` précis, ex.
   « chef-de-cuisine », ou `journeeSlug` socle : `cuisine`, `serveur`,
   `directeur`) — moments clés, gestes FoodEatUp, temps gagné TEL QUE
   RENVOYÉ (jamais un gain estimé de tête).
3. **Situer une vidéo dans un poste** : `parcours_metier_tutoriel` (slug de
   la fiche, `metierSlug` pour l'étape précédente/suivante) — répond à
   « qui doit voir ça ? » et « ça vient avant ou après quoi ? ».
4. Transformer l'intérêt en formation : proposer le programme du poste
   (skill `parcours-sur-mesure` avec `metierSlug`) ou, pour toute une
   équipe, le skill `former-mon-equipe`.

## Garde-fous

- Un métier hors des slugs proposés par le serveur ne s'invente pas : lister
  les postes du secteur (réponse de `secteur_foodeatup`) et faire choisir.
- Les minutes « gagnées » viennent de `journee_type` ; aucun chiffre ajouté.
