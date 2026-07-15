# Passerelles réelles — CMS ↔ Figma ↔ Lovable (D0)

**Date** : 2026-07-15.** Chaque flèche du pipeline design, **validée en direct** ou
**marquée avec son manque**. Fil rouge : **les mêmes tokens du début à la fin** (zéro
divergence).

## 1. Charte CMS → Figma — ✅ (avec limite police)

- **Mécanique** : `get_brand(nom)` → `couleurs` (hex, séparés par virgules), `font_family`,
  `logo` (URL publique), `slogan`, `site_web`, `langue`, `assets[]` → **variables/tokens
  Figma** via `figma-generate-library`. La maquette **consomme les variables**, jamais de
  valeur en dur.
- **⚠️ Limite — police** : `font_family` côté CMS est une **liste FERMÉE de 9 polices
  web-safe** (Arial, Verdana, Tahoma, Trebuchet MS, Georgia, Times New Roman, Garamond,
  Courier New, Lucida Console). Figma/Lovable peuvent utiliser une police **riche** (Google
  Font, custom) ; le CMS ne peut en stocker qu'**une des 9**.
  - **Arbitrage retenu (à confirmer, D0 §STOP)** : la **vraie police** vit dans le **DS
    Figma/Lovable** ; le CMS stocke **la plus proche des 9** (documenté dans la charte KB).
    → **spec Tunis** pour une police custom au CMS (`OUTILS-MCP-MANQUANTS.md` §12).

## 2. DA validée → Charte CMS — ✅ (source de vérité)

- **Mécanique** : décisions de direction artistique → `edit_brand(brand_id, couleurs,
  font_family[9], logo, slogan, site_web, langue)` **après confirmation** ; assets officiels
  dans la bibliothèque CMS (`upload_file_tool`). **Le CMS reste LA source de vérité** pour
  tous les autres plugins.
- **Limite** : même contrainte 9 polices qu'au §1. `couleurs` illimitées (hex).

## 3. Figma → Lovable — ✅ mécanisme, ⚠️ DS à créer

- **Mécanique** : maquette validée → `figma-design-to-code` **ou** brief `mvp-lovable`
  enrichi des tokens ; le DS maison publié comme **projet design system Lovable** →
  `create_project(design_systems: [{project_id: <DS Rapido>}])` (**le 1ᵉʳ appliqué**).
- **État live** : `list_design_systems(7gbZqk6ls…)` → **0 design system**. Donc le **DS
  Rapido n'existe pas encore** — `studio-maquette` (D3) doit **créer** un projet Lovable
  désigné DS (versionné, poussé **sur confirmation**). Mécanisme du paramètre `design_systems`
  **validé par schéma** ; contenu à produire.

## 4. Flows / Sitemap → Spec MVP — ✅

- **Mécanique** : `figma-generate-diagram` (`generate_diagram`, **FigJam**) → user flows +
  sitemap → la **spec de `mvp-lovable`** (LV3) **référence le diagramme** (lien FigJam dans
  `docs/specs/{projet}.md`).

## 5. Motion Figma → Code — ✅

- **Mécanique** : `figma-use-motion` (keyframes dans la maquette) → `figma-implement-motion`
  (`get_motion_context`) → composants animés du MVP. Alternative directe : patterns
  framer-motion depuis `reference/motifs-animation.md` (motifs francisés, `prefers-reduced-motion`
  obligatoire).

## Synthèse

| Passerelle | État | Réserve |
|---|---|---|
| Charte CMS → Figma | ✅ | police limitée à 9 (§1) |
| DA → Charte CMS | ✅ | idem police |
| Figma → Lovable (DS) | ✅ mécanisme | **DS Rapido à créer** (0 aujourd'hui) |
| Flows/Sitemap → Spec | ✅ | — |
| Motion → Code | ✅ | `prefers-reduced-motion` obligatoire |

> **Fil rouge des tokens** : couleurs = hex identiques CMS → Figma → Lovable (aucune
> divergence). Police = point de vigilance unique (§1) — tracé dans la charte KB.
