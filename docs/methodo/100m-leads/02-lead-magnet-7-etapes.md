# Lead magnet — les 7 étapes (et les 3 types)

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation source** :
> founder-playbook (MIT © 2026 AgentSeal). Reformulation FR — voir `NOTICE.md`.

## Ce qu'est un lead magnet

Une **solution complète à un problème étroit**, gratuite ou peu chère, qui
**révèle un problème plus large** que votre offre principale résout. Il
transforme un lead brut en **lead engagé**.

## Les 7 étapes de création

1. **Choisir le problème** — étroit, réel, qui mène naturellement à votre offre.
2. **Trouver la solution** — l'un des 3 types ci-dessous.
3. **Choisir le format de livraison** — PDF, vidéo, outil, essai.
4. **Tester le NOM** — le nom compte plus que le contenu (voir plus bas).
5. **Le rendre facile à consommer** — idéalement < 10 minutes.
6. **Le rendre vraiment bon** — assez bon pour être vendu.
7. **Rendre l'étape suivante évidente** — un CTA clair vers l'offre.

## Les 3 types de lead magnet

| Type | Mécanique | Exemple restaurant |
|---|---|---|
| **Révéler un problème** | un diagnostic montre un problème ignoré | « Audit gratuit de votre food cost en 5 min » |
| **Échantillon / essai** | accès limité à l'offre | un dessert offert à la 1re résa en ligne |
| **1 étape d'un processus** | résoudre l'étape 1 sur 5 | « Le calibrage de 10 portions anti-gaspi » (modèle) |

Le lead magnet résout **un** problème, qui en révèle **un suivant** que votre
offre traite.

## Le nom (le levier n°1)

**Formule** : promettre un **résultat précis**, dans un **délai précis**, pour un
**public précis**.

| Faible | Fort |
|---|---|
| « Guide marketing » | « Le playbook cold email en 5 jours pour freelances » |
| « Checklist gratuite » | « La checklist pré-lancement en 10 points pour SaaS » |

**Distribution** : ne pas le cacher derrière un seul canal — le mettre PARTOUT
(signature email, CTA de chaque post, bio, bas d'article). Le goulot, c'est
presque toujours la distribution, pas la qualité.

## Exemple Rapido / FoodEatUp
« Le calculateur de marge par plat (Excel) » en lead magnet → révèle que le menu
n'est pas optimisé → mène à l'offre d'accompagnement Rapido.

## Outils MCP Rapido pressentis

| Étape | Outils MCP Rapido |
|---|---|
| Héberger / diffuser le magnet | rapidocms `upload_file_tool`, `create_draft_tool` (CTA), carte digitale `add_digital_card` |
| Capturer les leads | rapidocrm `list_formulaires`/`get_formulaire_soumissions`, `enregistrer_prospect`, `list_cta` |
| Router vers l'offre | rapidocrm `ajouter_prospect_pipeline`, `create_devis` ; rapido-suite `invoice-chase` en aval |
| Générer le visuel du magnet | rapidocms `generate_image` / `studio-visuel-marque` |

## Frontières
- **Diffuser** le magnet dans les canaux → `01-core-four.md`.
- **Qualité de l'offre** derrière le magnet → benchmark `100m-offers`
  (`docs/BENCHMARK-FOUNDER-PLAYBOOK.md`).
