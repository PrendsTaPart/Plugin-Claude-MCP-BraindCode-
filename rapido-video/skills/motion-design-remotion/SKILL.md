---
name: motion-design-remotion
description: Utiliser quand l'utilisateur veut une « intro animée », une « outro », un « lower third », un « générique », du « motion design », une « animation de logo » ou une « vidéo explicative animée type motion ». Motion design programmatique (Remotion) aux couleurs de la marque, à partir de 5 gabarits maison paramétrés par la charte, rendus en MP4 et assemblés par montage-express.
---

# Motion design de marque (Remotion)

Compositions animées **paramétrées par la charte** (couleurs hex, police mappée,
logo CMS), rendues via Remotion puis assemblées par `montage-express`.

## Étape 0 — Licence, skills, charte (obligatoire)

### Gate licence (V0) — **prioritaire**
- Lire l'état de la **décision licence Remotine** (`./rapido-kb/licences-video.md`,
  ou la validation V0 de `docs/DECISION-LICENCES-VIDEO.md`).
- **Non tranchée / licence entreprise refusée → mode `aperçu non commercial`** :
  rendre en `licence: apercu` (bandeau « APERÇU » sur chaque gabarit), **le dire
  explicitement** à l'utilisateur, et **interdire tout usage commercial/publié**
  jusqu'à validation. Remotion est gratuit ≤ 3 employés ; au-delà = licence Company
  (voir la décision licences).
- **Tranchée (commercial validé) → mode `commercial`** (sans bandeau).

### Skills & projet Remotion (DELTA V4 — zéro install utilisateur)
- **Skills Remotion absents** → l'agent exécute `npx skills add remotion-dev/skills`.
- **Créer un projet Remotion au workspace** (`npm i` local) et **copier
  `${CLAUDE_PLUGIN_ROOT}/skills/motion-design-remotion/templates/`** dedans.
- **Chromium headless** (moteur de rendu Remotion) : **annoncer le téléchargement
  (~400 Mo) et le CONFIRMER** avant. Aucun guide manuel.

### Charte
- `rapidocms:contenu-conforme-marque` (charte KB **prioritaire**) + `get_brand` /
  `list_all_files` (couleurs hex, logo réel) → props des gabarits.

## 1. Bibliothèque de gabarits (`templates/`)
5 gabarits paramétrés par la charte : **Intro** (logo + tagline, 3-5 s), **Outro**
(CTA site + réseaux), **LowerThird** (nom + fonction), **TitleCard** (écran titre),
**StatBar** (barre de progression + compteur — stats **PronoClip**). Props :
`primary`/`secondary`/`textColor`/`fontFamily`/`logoUrl`/`licence` + textes du gabarit.

## 2. Règles de rendu encodées (`templates/_shared.tsx`)
- **1080×1920 @ 30 fps** par défaut ; **safe zones** 150 haut / 170 bas / 60 côtés ;
  **polices** titres ≥ 56 px, corps ≥ 36 px, **jamais < 28 px** ; **sobriété** (peu
  d'éléments animés simultanés — les compositions chargées se dégradent).

## 3. Rendu & intégration
- Rendu **CLI Remotion** : `npx remotion render <id> out.mp4 --props='{…charte…}'`.
- Sortie MP4 → **assemblage par `montage-express`** (concat avec le contenu) →
  **rapatriement CMS** (`upload_file_tool`, nommage `{marque}-{contenu}-{format}-vN`)
  + brouillon proposé — **jamais de publication directe**.

## 4. Capitalisation
- Gabarit validé → `add_prompt` RapidoCMS (`type: "visuel"`) + entrée dans
  `./rapido-kb/marketing/gabarits-video.md` (nom, gabarit, props de marque, IDs).

## Garde-fous
**Gate licence** (aperçu non commercial si non tranchée, dit explicitement) ;
skills/projet/Chromium **auto-installés + confirmés** (aucun guide manuel) ; charte
KB **prioritaire** ; safe zones + tailles mini respectées ; **aucune publication
directe** ; temps de rendu **selon l'environnement**.
