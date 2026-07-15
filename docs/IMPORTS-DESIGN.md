# Imports & audit — rapido-design (D0)

**Date** : 2026-07-15 · **Portée** : audit uniquement — aucune création de skill,
aucune écriture (Figma/Lovable/CMS). 6 dépôts clonés (licences relues), passerelles
sondées en direct. Passerelles détaillées : `docs/PASSERELLES-REELLES.md`.

## 1. Moisson (6 dépôts, licences relues)

Anti-verbatim : on **francise/réimplémente des principes** ; aucun corps copié ; **aucun
exemple citant un designer/marque réel** repris. Attribution `NOTICE.md`.

### 1.a `dominikmartn/hue` (⭐756, **MIT**) — 🥇 ADAPTER (charte → design system)
Apprend une marque (URL/nom/screenshot) → **design system complet** (tokens couleur,
typographie, spacing, composants, **clair/sombre**, hero recipes, icon kit).
- **Verdict** : **ADAPTER** le **pont charte → DS** (exactement la fusion CMS↔design) →
  `direction-artistique` + `studio-maquette`. Le principe « la marque comme input » nourrit
  la DA.

### 1.b `bitjaru/styleseed` (⭐742, **MIT**) — 🥇 ADAPTER (jugement / anti-goût-IA)
Moteur de **jugement design** (« l'output cesse de ressembler à du généré ») : tokens qui
pilotent des skins, presets de restyle. **Note anti-verbatim** : le dépôt lui-même précise
que ses skins sont « inspired-by, not recreations » — même discipline maison.
- **Verdict** : **ADAPTER** en `reference/jugement-design.md` (goût, quand dire non).

### 1.c `joeseesun/qiaomu-design` (⭐388, **MIT**, 中文) — ✅ ADAPTER (francisé)
Conseiller design **anti-goût-IA** (Jobs/Rams) + cabine d'essayage de styles + biblio de
58 design systems.
- **Verdict** : **ADAPTER francisé** — le pendant design de notre `anti-voix-ia`
  (rapido-copywriter) → complète `jugement-design.md`. Chinois **non copié**.

### 1.d `natdexterra/work-with-design-systems` (⭐47, **MIT**, v2) — ✅ ADAPTER (Figma DS + WCAG)
Deux modes : **inspect** (audits **WCAG**, scoring de composants, pause obligatoire) +
**build** (composants, foundations) + Phase 6 export code (`tokens.css`).
- **Verdict** : **ADAPTER** → alimente `studio-maquette` (gate **a11y** + audit DS) ; c'est
  ce qui **remplace** un skill « accessibility-review » inexistant (voir §3).

### 1.e `B3nnyL/figgo` (⭐306, **MIT**) — ✅ PATTERN (tokens sync)
CLI de sync Figma ↔ design tokens locaux.
- **Verdict** : **PATTERN** — la tuyauterie tokens (fil rouge Figma → code), référence,
  non embarquée.

### 1.f `Trystan-SA/claude-design-system-prompt` (⭐1 724, **MIT**) — ⚠️ **ÉVITER**
README explicite : « **Reverse-engineered system prompt of Claude Design from Anthropic** ».
- **Verdict (règle maison)** : le **contenu** est **extrait d'un produit tiers**
  (system prompt propriétaire) → **ÉVITER**. On n'en adapte **rien** ; **benchmark de
  concepts** seulement (les principes anti-goût-IA génériques sont pris de styleseed/qiaomu,
  pas d'ici). La licence MIT de l'extracteur ne lève pas le problème de provenance.

### 1.g Benchmarks & animations
- `Pythoughts-labs/designer-skill` (MIT) : 🟡 s'inspirer (concepts). `plugin87/ux-ui-agent-skills`
  (**sans licence**) : 👁️ benchmark seul, **zéro copie**.
- **Bibliothèques d'animation** (`magicui`, `motion-primitives`, `animata`) : licences
  **non confirmées automatiquement** (proxy). **Sans importance** : le plugin ne référence
  que des **motifs génériques** (durées 150-400 ms, easings, scroll-reveal — savoir web
  générique), **aucun code embarqué**. Toute reprise de code exigerait une confirmation de
  licence — ce qui n'aura pas lieu.

## 2. Inventaire des outils réels (live)

### Figma (skills du plugin figma)
- `figma-generate-library` → **design system** (variables/tokens, **modes clair/sombre**,
  composants, thèmes ; outils `get_variable_defs`, `use_figma`, `create_new_file`).
- `figma-generate-diagram` → **user flows & sitemaps** en **FigJam** (`generate_diagram`).
- `figma-generate-design` → écrans (`generate_figma_design`). `figma-design-to-code`
  (`get_design_context`, `get_code_connect_map`). `figma-use-motion` /
  `figma-implement-motion` (`get_motion_context`, `export_video`).

### Lovable
- `list_design_systems(workspace_id)` → **le workspace `7gbZqk6ls…` a 0 design system
  aujourd'hui**. `create_project(design_systems:[{project_id}])` — **le 1ᵉʳ appliqué** →
  mécanisme **validé** ; le **DS Rapido est à CRÉER** (un projet Lovable désigné DS, D3).

### RapidoCMS (charte = source de vérité)
- `get_brand(nom)` / `edit_brand(brand_id, couleurs, font_family, logo, slogan, site_web,
  langue)`. **⚠️ Limitation majeure** : `font_family` est une **liste FERMÉE de 9 polices
  web-safe** (Arial, Verdana, Tahoma, Trebuchet, Georgia, Times New Roman, Garamond,
  Courier New, Lucida Console). `couleurs` = hex séparés par virgules. → détails et
  arbitrage dans `docs/PASSERELLES-REELLES.md` (§ police).

## 3. Croisement maison — qui fait quoi (le plugin ORCHESTRE)

| Besoin | Existant réel | Rôle |
|---|---|---|
| Styles/palettes/fonts | **`rapido-lovable:ui-ux-pro-max`** (50+ styles, 161 palettes, 57 paires) | **consommé** par `direction-artistique` |
| Rendu front | `rapido-lovable:frontend-design`, kit LV, `mvp-lovable`, `architecte-lovable` | build (D4 patch : consomme le DS) |
| Thèmes | `rapido-canva:theme-factory` | référence |
| Charte source de vérité | **`rapidocms:gestion-marques`** + `get_brand`/`edit_brand` | pivot CMS↔design |
| Sitemap/wireframes/UI (pédagogie) | `rapido-forge:ideation-sitemap-generator`, `ideation-mvp-wireframes`, `bootcamp-visual-identity`, `ideation-ui-guidelines` | **renvois** (apprendre) ; ici on **exécute** |
| Critique design · a11y · handoff · user-research | **N'EXISTENT PAS** (pas de « plugin design ») | **rapido-design les FOURNIT** : critique = `jugement-design.md` ; a11y = patterns WCAG de work-with-design-systems (gate dans `studio-maquette`) ; handoff = `figma-design-to-code` + `mvp-lovable` |

> **Correction au plan** : les skills `design-critique`, `accessibility-review`,
> `design-handoff`, `user-research` supposés n'existent pas dans le dépôt. rapido-design
> **intègre** critique et a11y comme **gates internes** (pas de délégation à des skills
> fantômes).

## 4. STOP — validation avant D1

1. **Trystan-SA = ÉVITER** (reverse-engineered d'un produit tiers) — confirmez la règle ?
2. **Police (font_family) limitée à 9 valeurs côté CMS** : arbitrage — soit le DS se **limite**
   à ces 9 polices web-safe (100 % fidèle CMS), soit le CMS stocke **la plus proche** des 9
   et la **vraie police** (ex. Google Font) vit dans le **DS Figma/Lovable** (le CMS n'est
   alors plus 100 % source de vérité pour la typo). **Recommandation** : police riche dans
   le DS Figma/Lovable + police CMS = la plus proche des 9 (documenté) ; **spec Tunis** pour
   une police custom au CMS (`docs/OUTILS-MCP-MANQUANTS.md`). OK ?
3. **DS Rapido à créer** (0 dans le workspace) : OK pour que `studio-maquette` (D3) crée un
   **projet Lovable désigné design system**, versionné, poussé **sur confirmation** ?

*Sources : 6 dépôts clonés (LICENSE relus, MIT), sondes live Lovable/RapidoCMS + schémas
d'outils Figma. Aucune donnée inventée.*
