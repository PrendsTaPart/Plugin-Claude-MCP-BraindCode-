---
name: declinaison-multi-reseaux
description: Utiliser quand l'utilisateur veut adapter un contenu à plusieurs réseaux — « décline sur les 4 réseaux », « adapte ce post pour Instagram/TikTok », « repurpose ce contenu ». Une idée-noyau → 4 déclinaisons NATIVES (une par grammaire), via délégation aux skills copy-*. À NE PAS utiliser pour écrire un seul post (copy-linkedin/copy-meta/copy-tiktok directement).
---

# Déclinaison multi-réseaux

Une **idée-noyau** → **4 déclinaisons NATIVES** (LinkedIn, Facebook, Instagram, TikTok),
**jamais** un copier-coller raccourci. Patterns de repurpose (content-repurposer /
linkedin-repurposer, MIT — cf. `NOTICE.md`).

## Étape 0 — contexte

Lire `reference/grammaires-reseaux.md`, `reference/articulations.md`. Charte `get_brand`.

## 1. Source → idée-noyau

Contenu source possible : un **post existant**, un article
(`rapidocms:generation-article-blog`), un **transcript** de vidéo/épisode. En extraire
l'**idée-noyau** (le message, la preuve, le CTA) — le fond commun aux 4 réseaux.

## 2. Quatre déclinaisons natives (délégation)

Pour chaque réseau, **déléguer au skill dédié** (angle ajusté par grammaire, **pas** un
raccourci du même texte) :

- LinkedIn → `copy-linkedin` (storytelling pro, CTA question).
- Facebook → `copy-meta` (court, local).
- Instagram → `copy-meta` (caption hook < 125 car. / carrousel).
- TikTok → `copy-tiktok` (script hook < 3 s).

Chaque déclinaison passe **anti-voix-IA** + **gate `brand-review`** (via son skill).

## 3. Lot + calendrier

`create_draft_tool` : **lot de brouillons CMS** rattachés à la **même campagne** (par
compte/réseau, `list_connected_accounts`). Proposer un **calendrier** de publication
(`rapidocms:calendrier-editorial`) — étalé, adapté aux fenêtres de chaque réseau. **Jamais
de publication directe.**

## Passerelles

Un seul réseau → `copy-linkedin` / `copy-meta` / `copy-tiktok`. Planification →
`rapidocms:pipeline-contenu-social` + `calendrier-editorial`.

## Règles

- **Déclinaisons natives** (une grammaire par réseau), jamais un copier-coller raccourci.
- **Brouillons** (lot, même campagne), jamais de publication ; preuves réelles ; anti-voix-IA
  + gate marque via chaque skill.
