# Évals — plugin rapido-design (0.4.0)

## Déclenchement

| Phrase | Skill |
|---|---|
| « direction artistique » / « moodboard » / « quel style pour [projet] » / « identité visuelle du site » | `direction-artistique` |
| « sitemap » / « user flow » / « arborescence » / « wireframes » | `architecture-info` |
| « maquette » / « écrans hi-fi » / « design system » / « maquette Figma de [projet] » | `studio-maquette` |
| « anime le site » / « micro-interactions » / « animations au scroll » / « transitions » / « rends-le vivant » | `animations-web` |

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

## Cas `animations-web` (3)

8. **`prefers-reduced-motion` obligatoire** : chaque animation a un fallback
   `reduce` (fondu discret ou état final direct) — un écran animé sans fallback est **rejeté**.
9. **Perf** : n'animer que `transform`/`opacity` (viser 60 fps) ; une animation d'ombre en
   boucle ou sur un layout coûteux est **écartée**.
10. **Sobriété** : **une intention par animation**, 2-3 surfaces max par écran ; toute
    animation sans intention (carnaval) est **retirée**.

## Orchestration — agent `directeur-ux`

- Déroule les **7 étapes** (`direction-artistique` → `architecture-info` → `studio-maquette`
  gates → handoff → `animations-web`) et **tient le fil rouge des tokens** (charte CMS →
  variables Figma → DS Lovable, **zéro divergence**).
- **Interdits** vérifiés : pixel sans charte ; hi-fi sans structure validée ; valeur en dur ;
  animation sans `prefers-reduced-motion` ; push DS Lovable sans confirmation.
- Arbitre **avec goût** (2 itérations max, critique argumentée) et **rapporte** à
  `rapido-lovable:architecte-lovable` pour le build.

## Anti-déclenchements (à respecter dans les skills)

- « Génère un visuel de post » → `rapidocms:studio-visuel-marque`.
- « Quel style choisir » seul → `rapido-lovable:ui-ux-pro-max`.
- « Audit accessibilité » d'un site existant → gate a11y de `studio-maquette` (pas un skill
  séparé).
- « Monte une vidéo » / « montage » → `rapido-video:montage-express` (pas `animations-web`).
