# rapido-design — le studio UX/UI

Orchestre **toute la chaîne** design avec **les mêmes tokens du début à la fin** :
charte CMS → **direction artistique** → **sitemap/flows** (FigJam) → **maquettes hi-fi +
design system** (Figma) → **MVP Lovable** → **animations**. Le fil rouge des tokens
(couleurs/typo) ne diverge jamais.

## État : squelette (0.1.0)

Fondations : `reference/pipeline-design.md` (7 étapes), `passerelles.md` (CMS↔Figma↔Lovable,
outil par outil), `jugement-design.md` (anti-goût-IA), `motifs-animation.md` (sobriété +
`prefers-reduced-motion`), hook `garde-charte`. Skills à venir : `direction-artistique`
(D2), `architecture-info` + `studio-maquette` (D3), `animations-web` + agent `directeur-ux`
(D4). Audit fondateur : `docs/IMPORTS-DESIGN.md`, `docs/PASSERELLES-REELLES.md`.

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
