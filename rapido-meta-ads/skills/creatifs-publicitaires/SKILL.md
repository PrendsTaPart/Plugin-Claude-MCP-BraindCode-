---
name: creatifs-publicitaires
description: Utiliser quand l'utilisateur veut un créatif pour la pub ou un visuel publicitaire. Génère le visuel (Canva ou image IA CMS) aux couleurs de la charte, crée le créatif Meta avec le bon CTA et propose des variantes A/B.
---

# Créatifs publicitaires (Canva/CMS × Meta)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-meta-ads.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md`. KB : `charte-graphique.md`,
`ton-et-accroches.md`, `propositions-valeur.md`.

## Workflow

1. **Brief** — objectif de la campagne (le CTA en dépend), promesse (KB,
   source citée), format cible (feed carré/4:5, story/reel 9:16).
2. **Générer le visuel** — deux voies :
   - **Canva** (support designé, texte maîtrisé) : `generate-design` au format
     natif (`instagram_post`, `your_story`…) → candidats →
     `create-design-from-candidate` → `get-export-formats` → `export-design`
     PNG → URL publique ;
   - **Image IA CMS** (rapide) : skill `prompt-engineering-visuel`
     (`generate_image` + `upload_file_tool`) — pas de texte dans l'image.
   Règle pub : peu de texte incrusté (meilleure diffusion), le message vit
   dans le texte de l'annonce.
3. **Créer le créatif Meta** — `ads_create_creative` : `page_id` VÉRIFIÉ
   (`ads_get_ad_account_pages`), visuel (URL/image uploadée), texte principal
   (accroche de `ton-et-accroches.md`), titre, **CTA adapté à l'objectif**
   (TRAFFIC → « En savoir plus », SALES → « Réserver »/« Acheter », LEADS →
   « S'inscrire »).
4. **Aperçu par placements** — `ads_get_ad_preview` (feed, story, reels…) :
   montrer à l'utilisateur AVANT toute utilisation dans une ad.
5. **Variantes A/B (proposer)** — 2-3 accroches différentes (angles :
   bénéfice, preuve, urgence datée réelle) sur le même visuel, ou 2 visuels
   sur la même accroche — à brancher sur le skill `tests-ab-meta`. UNE
   variable à la fois (règle du media-buyer).

## Garde-fous

- Chiffres et promesses : sourcés (KB/CRM/FoodEatUp) — une pub mensongère
  engage l'annonceur (CONFORMITE.md) ; pas de PII clients dans les créatifs.
- Charte : hex exacts, bonne variante de logo — validation
  `directeur-artistique` (rapidocms) pour les visuels sensibles.
- Alcool/secteurs réglementés : signaler les contraintes (ciblage d'âge,
  Loi Évin) avant de créer.
