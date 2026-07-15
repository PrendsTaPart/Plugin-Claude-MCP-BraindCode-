# Changelog — plugin rapido-design

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
