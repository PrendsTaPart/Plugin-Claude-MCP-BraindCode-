---
name: communication-de-la-semaine
description: Utiliser quand la semaine de communication se planifie, que l'utilisateur dit « prépare la com de la semaine », « planifie les posts FoodEatUp », « quels trous dans le calendrier éditorial ». Déroule la tâche outillée de l'Academy — méthode, calendrier, légendes par réseau, brouillons RapidoCMS après accord, mesure à 48 h.
---

# Communication de la semaine (la tâche outillée, pas l'inspiration)

Familles engagées : **configurer** (calendrier Academy) + **preparer**
(brouillons CMS) + **publier** (programmation, Aperçu).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Cadre du jour en main ; quota `publicationsJour` relu.

## Workflow (étapes de la tâche `communiquer-semaine` de get_capabilities)

1. **`get_communication_skill`** — relire la méthode et les règles maison.
2. **`get_editorial_brief`** et **`get_editorial_gaps`** — ce qui est prévu,
   ce qui manque.
3. **`plan_social_calendar`** — planifier la semaine avec les ressources des
   formations (sujets, formats).
4. **`prepare_social_post`** — adapter CHAQUE légende au réseau ; pour la
   copy fine (banque de hooks, passe anti-voix-IA), DÉLÉGUER aux skills du
   plugin `rapido-copywriter` s'il est installé plutôt que réécrire ses
   règles.
5. **`add_editorial_post`** — inscrire chaque publication au calendrier
   Academy en brouillon (`update_editorial_post` pour corriger).
6. **`create_social_draft`** APRÈS accord — les brouillons RapidoCMS ; la
   PROGRAMMATION (`schedule_draft_tool`, famille publier) se montre et
   attend l'accord, dans le quota du jour (2 actuellement).
7. **À 48 h** : `post_insights` (RapidoCMS) — relever les statistiques et
   les inscrire (`record_kpi` avec source).
8. Option : widget `calendrier-editorial-semaine`.

KPI : `posts-publies`, `engagement-social`.
Formations : `calendrier` (8 missions), `communication-claude`, `viraux`,
`reseaux`.

## Garde-fous

- Rien ne se publie en direct : brouillon → accord → programmation (quota).
- Les visuels passent par le skill `visuels-de-marque` (charte relue) ;
  aucun chiffre non sourcé dans une légende.
- La mesure à 48 h n'est pas optionnelle : un post non mesuré n'apprend
  rien.
