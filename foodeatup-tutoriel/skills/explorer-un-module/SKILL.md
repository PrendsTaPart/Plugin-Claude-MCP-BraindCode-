---
name: explorer-un-module
description: Utiliser quand on part du logiciel plutôt que d'un sujet, que l'utilisateur dit « quels sujets couvrez-vous », « le sommaire de la formation », « toutes les vidéos du module caisse », « qu'est-ce qu'on apprend sur l'écran températures ». Donne le plan du catalogue, le contenu d'un module et les tutoriels d'un écran précis.
---

# Explorer un module (le catalogue par la carte du logiciel)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **Vue d'ensemble** : `lister_modules` — catégories, modules, sections et
   compteurs. Présenter par catégorie, avec `videosEnLigne` tel que renvoyé.
2. **Un module entier, dans l'ordre du parcours** : `lister_tutoriels`
   (`moduleSlug`, ou `categorieSlug` ; `limite` si le module est gros).
3. **Depuis un écran du logiciel** : `tutoriels_du_module` (`module` du hub,
   et `ecran` pour cibler — ex. `haccp` + `temperatures`). Le vocabulaire
   module/écran vient des `ecrans_logiciel` portés par les fiches, pas d'un
   slug deviné (piège vérifié : hub ≠ catalogue).
4. Fiche repérée → la montrer avec le skill `trouver-un-tuto` (carte, lien)
   ou la suivre avec `lecon-guidee`.
5. L'utilisateur veut un programme plutôt qu'une liste → basculer sur
   `parcours-sur-mesure` (`moduleSlug` thématique).

## Garde-fous

- `videosEnLigne` ≠ `videosPrevues` sur plusieurs modules : annoncer ce qui
  est EN LIGNE ; ce qui est prévu mais pas filmé se dit « à venir », jamais
  promis avec un lien (relevé du 2026-10-25 en référence pièges — relire la
  réponse du jour, ça bouge).
- Les compteurs cités viennent de la réponse en cours, pas d'un souvenir.
