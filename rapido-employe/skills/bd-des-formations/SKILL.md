---
name: bd-des-formations
description: Utiliser quand les formations se racontent en images, que l'utilisateur dit « sors la BD de la formation prospection », « prépare les planches pour les réseaux », « quelles ressources média pour cette formation ». Récupère la bande dessinée et les médias d'une formation et les pousse en brouillon RapidoCMS — jamais publiés directement.
---

# BD des formations (les planches, en brouillon)

Familles engagées : **apprendre** (lectures) + **preparer** (brouillons CMS).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`get_formation_comic`** sur la formation visée — les planches de la
   bande dessinée maison ; **`list_media_resources`** pour les autres
   médias (couvertures, audio, captures).
2. **Choisir** avec l'utilisateur les planches qui portent le message de la
   semaine (lien avec `get_editorial_gaps` du skill
   `communication-de-la-semaine`).
3. **Pousser en brouillon RapidoCMS** : `upload_file_tool` pour les
   planches, `create_draft_tool` pour le post (légende sobre : ce que la
   formation apprend, à qui, le lien d'inscription officiel) — BROUILLONS
   seulement, la programmation suit la chaîne normale (accord + quota).
4. Mesurer comme tout post : `post_insights` à 48 h.

KPI : `posts-publies`, `engagement-social`, `demandes-entrantes`.
Formations : `communication-claude`, `viraux`.

## Garde-fous

- Les planches sont des fichiers servis par l'Academy — pas de redessin,
  pas de montage qui trahit la charte.
- Jamais publiés directement : brouillon, accord, quota (garde-envois en
  filet sur `schedule_draft_tool`).
