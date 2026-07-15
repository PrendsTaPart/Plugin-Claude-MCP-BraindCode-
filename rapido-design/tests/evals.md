# Évals — plugin rapido-design (0.2.0)

## Déclenchement

| Phrase | Skill |
|---|---|
| « direction artistique » / « moodboard » / « quel style pour [projet] » / « identité visuelle du site » | `direction-artistique` |
| « sitemap » / « user flow » / « arborescence » / « wireframes » | `architecture-info` |
| « maquette » / « écrans hi-fi » / « design system » / « maquette Figma de [projet] » | `studio-maquette` |

## Cas `direction-artistique` (3)

1. **Charte existante s'impose** : le projet a déjà une charte (`get_brand` renvoie une
   marque) → on la **décline**, on ne propose PAS 3 nouvelles directions.
2. **3 directions** (marque neuve) : chacune avec intention + palette (tokens nommés) +
   typo + **un écran de principe Figma** ; filtrées par le jugement anti-goût-IA.
3. **Sync CMS confirmé** : direction retenue → `create_brand`/`edit_brand` **après
   confirmation** + `charte-graphique.md` ; la vraie police vit dans le DS (CMS = 9 web-safe).

## Garde-fous (hook `garde-charte`, testé au testeur)

| Entrée | Décision attendue |
|---|---|
| `mcp__Figma__generate_figma_design` | **ask** (charte chargée ? tokens ?) |
| `mcp__Figma__use_figma` | **ask** |
| `mcp__Lovable__create_project` | **ask** |
| `mcp__RapidoCMS__get_brand` (lecture charte) | **allow** |

## Principes vérifiés

- **Charte d'abord** : toute création visuelle suppose la charte chargée (`get_brand`) ;
  la maquette **consomme les tokens**, jamais de valeur en dur.
- **Fil rouge des tokens** : couleurs identiques CMS → Figma → Lovable (zéro divergence) ;
  police = point de vigilance (9 web-safe au CMS, riche dans le DS).
- **Gates** : jugement anti-goût-IA, accessibilité WCAG, `prefers-reduced-motion`.
- **Provenance** : Trystan-SA (reverse-engineered) exclu ; libs d'animation = motifs seuls.

## Cas `architecture-info` + `studio-maquette` (4)

4. **Structure d'abord** : sitemap + flows (FigJam) + wireframes gris **validés avant**
   toute hi-fi.
5. **Refus hi-fi sans wireframes** : `studio-maquette` appelé sans wireframes validés →
   **renvoyer** à `architecture-info`.
6. **Valeur en dur détectée** : une couleur écrite en dur (hors variable) dans un écran →
   **corrigée** (les écrans consomment les variables du DS).
7. **Push DS Lovable confirmé** : DS maison poussé en projet design system Lovable **après
   confirmation**, versionné (0 DS aujourd'hui → créé ici).

## Anti-déclenchements (à respecter dans les skills)

- « Génère un visuel de post » → `rapidocms:studio-visuel-marque`.
- « Quel style choisir » seul → `rapido-lovable:ui-ux-pro-max`.
- « Audit accessibilité » d'un site existant → gate a11y de `studio-maquette` (pas un skill
  séparé).
