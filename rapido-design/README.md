# rapido-design — le studio UX/UI

Orchestre **toute la chaîne** design avec **les mêmes tokens du début à la fin** :
charte CMS → **direction artistique** → **sitemap/flows** (FigJam) → **maquettes hi-fi +
design system** (Figma) → **MVP Lovable** → **animations**. Le fil rouge des tokens
(couleurs/typo) ne diverge jamais.

## Skills & agent (0.5.0)

Fondations : `reference/pipeline-design.md` (7 étapes), `passerelles.md` (CMS↔Figma↔Lovable,
outil par outil), `jugement-design.md` (anti-goût-IA), `motifs-animation.md` (sobriété +
`prefers-reduced-motion`), hook `garde-charte`.

- **`direction-artistique`** — DA ↔ charte CMS : 3 directions filtrées par le jugement, sync
  CMS confirmé (la charte existante prime).
- **`architecture-info`** — structure d'abord : sitemap + user flows (FigJam) + wireframes
  gris, validés **avant** toute hi-fi.
- **`studio-maquette`** — design system Figma d'abord (variables des tokens) → écrans hi-fi
  qui consomment les variables → gates critique + a11y → handoff Lovable.
- **`animations-web`** — motion sobre : plan, implémentation Figma→code / framer-motion,
  gates perf (60 fps) + `prefers-reduced-motion` **obligatoire**.
- Agent **`directeur-ux`** — orchestre les 7 étapes et tient le fil rouge des tokens (zéro
  divergence), rapporte à `rapido-lovable:architecte-lovable`.

Audit fondateur : `docs/IMPORTS-DESIGN.md`, `docs/PASSERELLES-REELLES.md`. Recette de bout
en bout (runbook, à jouer sur données réelles) : `docs/RECETTE-DESIGN.md`.

## Prérequis MCP

- **Figma MCP** connecté en session (skills `figma-generate-*`, `figma-*-motion`) — serveur
  de session, non déclaré dans le `.mcp.json` du plugin.
- **Lovable** (design system → projet), **RapidoCMS** (charte, source de vérité).
- Serveur non connecté → dégradation propre annoncée.

## Garde-fous

- **`garde-charte`** (hook) : toute création visuelle (Figma/Lovable) → confirmation que la
  charte est chargée (`get_brand`) et que la maquette **consomme les tokens** (jamais de
  valeur en dur).
- **Gates** : jugement/critique (`jugement-design.md`), **accessibilité WCAG**
  (patterns work-with-design-systems), **`prefers-reduced-motion`** sur toute animation.
- **Charte = source de vérité CMS** ; DA → `edit_brand` **confirmé** ; push DS Lovable
  **confirmé**, versionné. Aucune copie de maquettes/shots de designers réels.

## Attribution & portabilité

Principes francisés de 5 dépôts **MIT** (aucun corps copié ; Trystan-SA reverse-engineered
= exclu ; libs d'animation = motifs seuls) : `NOTICE.md`. Slug **immuable**.
