---
name: campagne-mot-cle
description: Utiliser quand une campagne de commentaires à mot-clé se conçoit, que l'utilisateur dit « monte une campagne commente FOOD », « prépare une mécanique de mot-clé en commentaire », « design la campagne d'engagement ». Relit les règles maison puis conçoit la mécanique — rien n'est publié par ce skill.
---

# Campagne mot-clé (concevoir, jamais publier)

Famille engagée : **configurer** (conception Academy) — AUCUNE publication.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`get_comment_campaign_rules`** — les règles maison des campagnes à
   mot-clé (ce qui se promet, ce qui ne se promet pas, les plateformes, la
   mécanique de réponse).
2. **`design_comment_campaign`** — concevoir la campagne : le mot-clé,
   le post d'appel, la réponse automatique prévue, le lot ou le contenu
   remis, la durée, la mesure.
3. **Livrer la conception** au responsable : mécanique complète + ce qu'il
   reste à faire HUMAINEMENT (publier le post via la chaîne normale — skill
   `communication-de-la-semaine` —, armer la réponse dans l'outil social).
4. **Rien n'est publié ici** : ce skill s'arrête à la conception, c'est sa
   définition.

KPI : `engagement-social`, `demandes-entrantes`.
Formations : `viraux`, `calendrier`.

## Garde-fous

- La mécanique respecte les règles renvoyées — pas de promesse de gain
  déguisée, pas de condition cachée.
- Si la conception appelle un visuel ou un lot payant : skills
  `visuels-de-marque` et garde-depense s'appliquent — toujours rien de
  publié.
