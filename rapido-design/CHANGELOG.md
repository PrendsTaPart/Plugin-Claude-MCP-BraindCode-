# Changelog — plugin rapido-design

## 0.5.0 — 2026-07-15 — release studio UX/UI (charte → Figma → Lovable)

- **Pipeline complet** livré : `direction-artistique` → `architecture-info` →
  `studio-maquette` (gates critique + a11y) → handoff → `animations-web`, orchestré par
  l'agent `directeur-ux` avec **le même fil rouge de tokens** du début à la fin.
- **Tests consolidés** (`tests/evals.md`) : déclenchements des 4 skills, cas par skill,
  garde-fous `garde-charte` (testés au testeur), **3 anti-déclenchements** (visuel de post →
  `rapidocms:studio-visuel-marque` ; style seul → `rapido-lovable:ui-ux-pro-max` ; audit a11y →
  gate de `studio-maquette` ; +montage → `rapido-video`).
- **Recette de bout en bout** documentée en runbook : `docs/RECETTE-DESIGN.md` (landing de
  démo charte → wireframes → hi-fi/DS Figma → MVP Lovable animé) — à jouer sur données réelles.
- Marketplace : description « Squelette » retirée (plugin livré). Racine : 25 plugins /
  380 skills / 37 agents.

## 0.4.0 — 2026-07-15 — animations-web + agent directeur-ux

- Skill **`animations-web`** — motion **sobre** : audit des surfaces qui méritent du motion →
  plan (motif + durée/easing + fallback) → implémentation Figma→code (`figma-use-motion` →
  `figma-implement-motion`) **ou** patchs framer-motion (motifs francisés) → **gates**
  perf (`transform`/`opacity`, 60 fps) et **`prefers-reduced-motion` obligatoire** → recette
  avant/après. Une intention par animation, 2-3 surfaces max.
- Agent **`directeur-ux`** — orchestre les **7 étapes** (DA → archi info → maquettes/DS gates →
  handoff → motion), **tient le fil rouge des tokens** (charte CMS → variables Figma → DS
  Lovable, zéro divergence), arbitre avec goût (2 itérations max) et rapporte à
  `rapido-lovable:architecte-lovable`. 5 interdits non négociables.
- Patchs croisés (articulation du pipeline) : `rapido-lovable:mvp-lovable` (le MVP démarre du
  DS Lovable), `rapido-lovable:ui-ux-pro-max` (bibliothèque de styles vs pipeline),
  `rapido-prompteur:prompt-lovable` (tokens du DS), `rapidocms:gestion-marques` (sync DA
  bidirectionnel).
- Évals : +3 cas `animations-web` (reduced-motion, perf, sobriété) + orchestration `directeur-ux`.

## 0.3.0 — 2026-07-15 — architecture-info + studio-maquette (DS Figma ↔ Lovable)

- Skill **`architecture-info`** — structure d'abord : sitemap + user flows (FigJam,
  `figma-generate-diagram`) + wireframes **gris** (`figma-generate-design`), **validés
  AVANT toute hi-fi** (règle bloquante). Renvoi pédagogie `rapido-forge:ideation-sitemap-generator`.
- Skill **`studio-maquette`** — prérequis DA + wireframes (sinon renvoyer) → **design
  system Figma d'abord** (`figma-generate-library`, variables des tokens, clair/sombre,
  audits WCAG) → écrans hi-fi qui **consomment les variables** (zéro valeur en dur) →
  **gates** critique (jugement) + a11y (WCAG) → publication (fichier Figma organisé ; DS
  poussé en **projet design system Lovable** confirmé/versionné ; handoff `figma-design-to-code`
  ou brief `rapido-lovable:mvp-lovable` enrichi).
- Évals : 4 cas (structure d'abord, refus hi-fi sans wireframes, valeur en dur, push DS confirmé).

## 0.2.0 — 2026-07-15 — direction-artistique (DA ↔ charte CMS)

- Skill **`direction-artistique`** — Étape 0 (jugement + **charte existante qui s'impose**),
  3 directions via `rapido-lovable:ui-ux-pro-max` filtrées par le jugement anti-goût-IA
  (intention + palette tokens + typo + un écran de principe Figma), formalisation en
  mini-charte (page Fondations), **sync CMS confirmé** (`create_brand`/`edit_brand` +
  charte KB ; vraie police dans le DS, CMS = 9 web-safe).
- Évals : 3 cas (charte existante, 3 directions, sync CMS).

## 0.1.0 — 2026-07-15 — Squelette (pipeline + jugement)

- Nouveau plugin **rapido-design** (25e du marketplace) — studio UX/UI qui orchestre la
  chaîne charte → Figma → Lovable avec les mêmes tokens. Squelette : fondations +
  garde-fous, skills à venir (D2→D5).
- `.mcp.json` : rapidocms (charte), lovable (design system). Figma = serveur de session.
- `reference/pipeline-design.md` : **7 étapes** (brief → DA+charte → archi info → wireframes
  → maquettes hi-fi + DS Figma → handoff Lovable → motion) avec livrable/skill/outils/done/
  gate. `reference/passerelles.md` : CMS↔Figma↔Lovable outil par outil (⚠️ font_family = 9
  web-safe ; DS Rapido à créer).
- `reference/jugement-design.md` : principes de goût + **liste anti-goût-IA** (gradients
  violets, glassmorphism, emojis en puces, cartes clonées…) + quand dire non (styleseed +
  qiaomu francisés). `reference/motifs-animation.md` : catalogue sobre (durées 120-400 ms,
  easings, perf transform/opacity, **prefers-reduced-motion obligatoire**).
- **Hook** `garde-charte` (ask sur création visuelle Figma/Lovable : charte chargée ?
  tokens consommés ?) + `Stop` (récap fichiers/tokens/gates/liens). Tests au testeur.
- `NOTICE.md` (5 sources MIT ; Trystan-SA reverse-engineered EXCLU ; libs anim = motifs
  seuls). Fondé sur l'audit **D0** (`docs/IMPORTS-DESIGN.md` + `docs/PASSERELLES-REELLES.md`).
