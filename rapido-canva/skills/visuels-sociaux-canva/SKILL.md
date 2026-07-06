---
name: visuels-sociaux-canva
description: Utiliser quand l'utilisateur veut un visuel Canva, un design pour Instagram/LinkedIn/Facebook ou un template de post. Génère le design au format natif du réseau, l'exporte en PNG et l'enchaîne dans le pipeline RapidoCMS (brouillon, planification).
---

# Visuels sociaux (RapidoCMS × Canva)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-canva.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md`. KB : `ton-et-accroches.md` +
`charte-graphique.md` si `./rapido-kb/` existe.

## Workflow

1. **Brief** — objectif (notoriété/trafic/leads/ventes) et réseau cible. Sans
   objectif clair, le demander (règle du responsable-marketing).
2. **Charte** — brand kit via `list-brand-kits` si l'utilisateur veut de
   l'on-brand ; sinon palette de `./rapido-kb/charte-graphique.md` injectée
   dans la query.
3. **Générer au format NATIF du réseau** — `generate-design` avec le bon
   `design_type` : `instagram_post` (1080×1350), `your_story` (story IG/FB),
   `facebook_post`, `facebook_cover`, `pinterest_pin`, `twitter_post`,
   `youtube_thumbnail`… Query détaillée : message, accroche (de
   `ton-et-accroches.md` si dispo), palette, ambiance — contexte complet à
   chaque itération.
4. **Candidats → design** — présenter, faire choisir,
   `create-design-from-candidate`.
5. **Export PNG** — `get-export-formats` puis `export-design`
   (`format.type: "png"`) ; afficher l'URL de téléchargement.
6. **Pipeline CMS** — enchaîner côté rapidocms :
   a. `upload_file_tool` (`type: "image"`, `file_url` = URL d'export Canva,
      `name` descriptif) → bibliothèque ;
   b. `create_draft_tool` (caption adaptée nativement au réseau,
      `media_source: "biblio"`, `account_id` via `list_connected_accounts`) ;
   c. `schedule_draft_tool` (`post_date` `Y-m-d`, `post_heure` `H-i-s`) après
      confirmation de la date/heure.

## Mode récurrent (formats répétitifs : promo hebdo, citation, offre du jour)

1. `search-brand-templates` (`dataset: "non_empty"`, query éventuelle) :
   trouver le template auto-remplissable ; `get-brand-template-dataset` pour
   les champs disponibles.
2. `create-design-from-brand-template` (`brand_template_id` « BTM... »), puis
   remplir les champs via une transaction d'édition (start → `replace_text`/
   `update_fill` → preview → accord → commit) — l'outil `autofill-design`
   n'est pas exposé sur cette connexion (pieges-canva.md §6).
3. Export + pipeline CMS comme ci-dessus. Proposer de sauvegarder la recette
   (template + champs) pour la prochaine itération.

## Garde-fous

- Un design par réseau (formats natifs) — pas de recadrage aveugle.
- Visuel exporté montré et validé AVANT `create_draft_tool`/`schedule_draft_tool`.
- Pas de données personnelles clients dans un visuel public (CONFORMITE.md) ;
  chiffres avec source uniquement.
