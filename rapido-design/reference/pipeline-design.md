# Pipeline design — les 7 étapes

**Révisé le 2026-07-15.** De la charte au MVP animé, **mêmes tokens du début à la fin**.
Chaque étape : livrable · skill responsable · outils · critère de done · gate.

| # | Étape | Skill | Outils / délégations | Livrable | Done / gate |
|---|---|---|---|---|---|
| 1 | **Brief & recherche** | (cadrage) | brief + personas (renvoi `rapido-forge` si pédagogie) | Brief validé (cible, objectif, contraintes) | Brief signé |
| 2 | **Direction artistique + charte** | `direction-artistique` (D2) | `ui-ux-pro-max`, `get_brand`/`edit_brand` (CMS), Figma écran de principe | 3 directions → 1 retenue → mini-charte projet | **Charte existante s'impose** ; sync CMS confirmé |
| 3 | **Architecture de l'info** | `architecture-info` (D3) | `figma-generate-diagram` (FigJam) | Sitemap + user flows des parcours critiques | — |
| 4 | **Wireframes basse-fi** | `architecture-info` (D3) | `figma-generate-design` (gris, sans style) | Wireframes des écrans clés | **Validation AVANT hi-fi** (jamais de joli sur structure non validée) |
| 5 | **Maquettes hi-fi + design system** | `studio-maquette` (D3) | `figma-generate-library` (variables des tokens, clair/sombre) + `figma-generate-design` | DS Figma (Fondations/Composants/Écrans) + écrans hi-fi | **Gate critique** (jugement-design) + **gate a11y** (WCAG) ; zéro valeur en dur |
| 6 | **Handoff → Lovable / code** | `studio-maquette` (D3) | `figma-design-to-code` **ou** brief `rapido-lovable:mvp-lovable` ; DS poussé en **projet design system Lovable** (`create_project(design_systems)`) | Code/brief + DS Lovable | Push DS **confirmé**, versionné |
| 7 | **Motion** | `animations-web` (D4) | `figma-use-motion` → `figma-implement-motion` ; motifs framer-motion | Animations (hero, scroll-reveal, micro-interactions) | **`prefers-reduced-motion` obligatoire** + gate perfs (60 fps) |

**Agent** `directeur-ux` (D4) orchestre les 7 étapes, tient le **fil rouge des tokens**
(charte CMS → Figma → Lovable, **zéro divergence**) et arbitre avec goût (2 itérations max).

> Passerelles détaillées (outil par outil, limites) : `reference/passerelles.md`. Jugement
> et anti-goût-IA : `reference/jugement-design.md`. Motifs d'animation :
> `reference/motifs-animation.md`.
