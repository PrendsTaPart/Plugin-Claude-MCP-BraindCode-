# Gabarits de marque (Remotion)

5 gabarits paramétrés par la charte (couleurs hex, police mappée, logo depuis
l'URL CMS) : **Intro** (logo + tagline), **Outro** (CTA site + réseaux),
**LowerThird** (nom + fonction), **TitleCard** (écran titre), **StatBar** (barre de
progression + compteur — stats type PronoClip).

## Règles de rendu encodées (`_shared.tsx`)
- **1080×1920 @ 30 fps** par défaut (`Root.tsx`).
- **Safe zones** : 150 px haut · 170 px bas · 60 px côtés (`SAFE`).
- **Tailles de police minimales** : titres ≥ 56 px, corps ≥ 36 px, **jamais < 28 px**
  (`clampFont`).
- **Sobriété** : peu d'éléments animés simultanés (les compositions chargées se
  dégradent) — chaque gabarit anime 1-2 éléments.
- **Gate licence** : prop `licence` = `apercu` (défaut, non commercial → bandeau
  « APERÇU ») tant que la décision Remotion n'est pas tranchée (V0) ; `commercial`
  une fois la licence validée.

## Câblage (par le skill)
1. Le skill crée un projet Remotion au workspace et **copie ce `templates/`** dedans.
2. Résout la charte (`get_brand` + `./rapido-kb/charte-graphique.md`) → props.
3. Rend via la **CLI Remotion** (`npx remotion render <id> out.mp4 --props='{…}'`),
   en surchargeant `primary`/`secondary`/`textColor`/`fontFamily`/`logoUrl`/`licence`
   et les textes du gabarit.
4. Le MP4 est **assemblé** par `montage-express` (concat avec le contenu) puis
   rapatrié en CMS.
