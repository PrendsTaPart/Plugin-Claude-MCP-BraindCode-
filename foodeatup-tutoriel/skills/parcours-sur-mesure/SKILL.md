---
name: parcours-sur-mesure
description: Utiliser quand l'utilisateur veut un programme de formation adapté, dit « fais-moi un programme », « je veux maîtriser le HACCP », « forme-moi en 30 minutes par jour », « quelle est la prochaine leçon ». Construit une suite ordonnée de leçons par poste, module ou objectif, avec la durée par séance, et enchaîne leçon par leçon.
---

# Parcours sur mesure (programme puis leçon suivante)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
   `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.
2. Secteur et métier non cadrés → passer d'abord par le skill
   `demarrer-academie`. Un code de reprise fourni → skill `carnet-de-reprise`.

## Workflow

1. **Fixer le niveau** (obligatoire pour l'outil) : `debutant` = compte non
   configuré, `intermediaire` = utilise déjà les bases, `avance` = cherche
   l'automatisation et les prompts. Le demander si rien ne permet de le
   déduire.
2. **`parcours_apprentissage`** — passer `niveau`, et selon la demande
   `metierSlug` (parcours de poste), `moduleSlug` (parcours thématique,
   ex. « haccp »), `minutesParSeance` (défaut 15), `dejaVus` (slugs déjà
   vus, à exclure).
3. Présenter le programme : ordre des leçons, durée totale renvoyée,
   objectif de chacune. Proposer d'afficher la progression avec le widget
   `progression-parcours` (`${CLAUDE_PLUGIN_ROOT}/scripts/render_widget.py`).
4. Dérouler la première leçon avec le skill `lecon-guidee`.
5. Pour continuer en cours de route : **`lecon_suivante`** (avec `dejaVus`
   dans l'ordre, `niveau`, et le `metierSlug`/`moduleSlug` du parcours) —
   pas un nouveau `parcours_apprentissage` à chaque fois.
6. En fin de séance : encoder la progression (skill `carnet-de-reprise`).

## Garde-fous

- **Une leçon à la fois** — jamais deux vidéos d'affilée sans confirmation
  explicite.
- Les leçons viennent du serveur : ne jamais insérer dans le programme un
  sujet sans fiche (sujet manquant → le dire, et le skill
  `studio-production-tutos` sait le consigner).
- La durée totale est celle renvoyée par le serveur ; si on additionne des
  séances soi-même, le calcul passe par un script Python stdlib avec la
  formule affichée.
