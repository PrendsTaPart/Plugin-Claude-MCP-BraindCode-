---
name: animations-web
description: Utiliser quand l'utilisateur veut animer un site — « anime le site », « micro-interactions », « animations au scroll », « transitions », « rends-le vivant ». Plan de motion sobre (une intention par animation), implémentation Figma→code ou framer-motion, prefers-reduced-motion obligatoire. À NE PAS utiliser pour le montage vidéo (rapido-video) ni les maquettes statiques (studio-maquette).
---

# Animations web (motion sobre)

**Une intention par animation**, jamais de carnaval. `prefers-reduced-motion` partout.
Fil conducteur : `reference/motifs-animation.md` + `reference/jugement-design.md`.

## Étape 0 — contexte

Lire `reference/motifs-animation.md` (barème durées/easings, perf, reduced-motion) et
`reference/jugement-design.md` (sobriété : une intention par animation).

## 1. Audit de l'existant

Repérer les **surfaces qui méritent du motion** : hero, CTA, listes/cartes (apparition),
**feedbacks** de formulaire, transitions de navigation. Le reste **reste statique**.

## 2. Plan de motion

Par surface : **motif choisi** (catalogue), **durée + easing**, **fallback reduced-motion**.
Maximum 2-3 surfaces animées par écran. Écarter toute animation **sans intention**.

## 3. Implémentation

- **(a) Maquette Figma animée** (si demandé) : `figma-use-motion` (keyframes) →
  `figma-implement-motion` (vers le code).
- **(b) Direct code** : prompts Lovable / patchs **framer-motion** depuis les **motifs
  francisés** (`motifs-animation.md` ; motifs génériques, aucun code de lib tiers embarqué —
  cf. `NOTICE.md`).

## 4. Gates (bloquants)

- **Perf** : animer **`transform`/`opacity`** uniquement, viser **60 fps** ; pas
  d'animation sur des layouts coûteux, pas d'ombre animée en boucle.
- **`prefers-reduced-motion: reduce`** : **obligatoire** sur **chaque** animation (fondu
  discret ou état final direct).
- **Recette visuelle** : avant/après vérifié (dont le rendu reduced-motion).

## Passerelles

Maquettes statiques → `studio-maquette`. Build/MVP → `rapido-lovable:mvp-lovable`. Montage
vidéo → `rapido-video:montage-express`.

## Règles

- **Sobriété** (une intention/animation, 2-3 surfaces max) ; **reduced-motion obligatoire**.
- **Perf** (transform/opacity, 60 fps) ; motifs génériques, aucun code de lib tiers embarqué.
