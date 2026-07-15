# Évals — plugin rapido-design (0.1.0, squelette)

Stade squelette : pipeline + jugement + garde-fous. Les évals de déclenchement des skills
arrivent avec eux (D2→D5).

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

## Anti-déclenchements (à respecter dans les skills)

- « Génère un visuel de post » → `rapidocms:studio-visuel-marque`.
- « Quel style choisir » seul → `rapido-lovable:ui-ux-pro-max`.
- « Audit accessibilité » d'un site existant → gate a11y de `studio-maquette` (pas un skill
  séparé).
