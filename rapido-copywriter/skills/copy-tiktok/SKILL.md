---
name: copy-tiktok
description: Utiliser quand l'utilisateur veut un script TikTok pour une page de marque — « script TikTok », « vidéo TikTok pour [marque] », « hook TikTok », « contenu TikTok ». Le livrable est un SCRIPT DE TOURNAGE (pas une caption) : hook < 3 s, structure hook→boucle→valeur→payoff→CTA. À NE PAS utiliser pour LinkedIn/Meta (copy-linkedin, copy-meta) ni le montage lui-même (montage-express).
---

# Copy TikTok — le script prime

Le livrable est un **script de tournage/production**, **pas** une caption. Ton
**créateur** (jamais corporate).

## Étape 0 — contexte

Lire `reference/grammaires-reseaux.md` (fiche **TikTok**), `reference/banque-hooks.md`
(hooks TikTok **GAGNANT d'abord**), `reference/anti-voix-ia.md`, `reference/articulations.md`.
Charte `get_brand` + `rapido-kb/`.

## 1. Brief

Objectif (quasi tout **TOFU** découverte), cible, **angle réel** (fait/coulisse/chiffre
CRM/CMS — jamais inventé), durée cible **15-45 s**.

## 2. Le script (livrable)

- **Hook verbal + visuel < 3 s** (écrit **tel quel**, la rétention se joue là).
- **Structure** : hook → **boucle ouverte** → valeur → **payoff** → **CTA**.
- **Texte à l'écran horodaté** (00:00–00:03 : « … »), **indications sous-titres**
  (obligatoires), **son natif** suggéré.
- **Caption** courte + **3-5 hashtags** (dont un niche).

## 3. Passe anti-voix-IA sur le PARLÉ

`reference/anti-voix-ia.md` appliqué au **texte parlé** : ton créateur, phrases orales,
pas de « bonjour à tous », pas de corporate.

## 4. Sortie double

- **(a) Production générative** → brief vers `rapido-higgsfield:usine-video-marketing`
  (9:16, `self_ai_disclosure` si diffusé sur Meta) via l'agent
  `rapido-prompteur:directeur-prompts`.
- **(b) Tournage réel** (fondateur face caméra) → **script prêt à tourner** +
  `rapido-video:montage-express` pour la post-prod (sous-titres burn-in, coupes).

## 5. Déclinaison + publication

Proposer la **déclinaison** : le même script sert les **Reels IG** et **Shorts** (grammaire
ajustée). Publication : `create_draft_tool` (brouillon CMS **TikTok** si compte connecté,
`list_connected_accounts`), sinon **export du script**. **Jamais de publication directe.**
Hooks consignés (compteur `banque-hooks.md`).

## Passerelles

Décliner sur les 4 réseaux → `declinaison-multi-reseaux`. Montage → `rapido-video:montage-express`.
Vidéo générative → `rapido-higgsfield:usine-video-marketing`.

## Règles

- **Script**, pas caption ; ton créateur ; **brouillon/export**, jamais de publication.
- Angle **réel**, anti-clickbait (payoff tient la promesse), hooks re-dérivés ; anti-voix-IA
  sur le parlé.
