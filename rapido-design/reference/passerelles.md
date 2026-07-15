# Passerelles — CMS ↔ Figma ↔ Lovable (outil par outil)

**Révisé le 2026-07-15.** Validées en direct en D0 (`docs/PASSERELLES-REELLES.md`). Fil
rouge : **mêmes tokens du début à la fin**, zéro divergence.

| De → Vers | Mécanique | Réserve |
|---|---|---|
| **Charte CMS → Figma** | `get_brand` (couleurs hex, `font_family`, logo, slogan) → variables/tokens via `figma-generate-library` ; la maquette **consomme** les variables | `font_family` = **9 polices web-safe** (voir § police) |
| **DA validée → Charte CMS** | décisions DA → `edit_brand(brand_id, …)` **après confirmation** + assets (`upload_file_tool`) ; le CMS reste **source de vérité** | idem police |
| **Figma → Lovable** | maquette → `figma-design-to-code` **ou** brief `mvp-lovable` ; DS maison = **projet design system Lovable** → `create_project(design_systems:[{project_id}])` (1ᵉʳ appliqué) | **0 DS dans le workspace aujourd'hui** → à **créer** (D3), poussé sur confirmation |
| **Flows/Sitemap → Spec** | `figma-generate-diagram` (FigJam) → la spec `mvp-lovable` référence le diagramme | — |
| **Motion → Code** | `figma-use-motion` → `figma-implement-motion` ; ou framer-motion depuis `motifs-animation.md` | `prefers-reduced-motion` obligatoire |

## § Police (point de vigilance unique)

`font_family` côté CMS = **liste FERMÉE de 9** (Arial, Verdana, Tahoma, Trebuchet MS,
Georgia, Times New Roman, Garamond, Courier New, Lucida Console). **Arbitrage** : la vraie
police (Google Font/custom) vit dans le **DS Figma/Lovable** ; le CMS stocke la **plus
proche des 9** (tracé dans la charte KB). Les **couleurs** (hex) ne divergent jamais. Spec
police custom au CMS : `docs/OUTILS-MCP-MANQUANTS.md` §12.

> **Figma** est un serveur MCP **de session** (non déclaré dans le `.mcp.json` du plugin) :
> il doit être connecté (voir README). Le plugin déclare `rapidocms` et `lovable`.
