# Routage média — l'arbre de décision unique de l'écosystème

Quel outil pour quel média ? Ce fichier est **la** référence : tout skill média
des autres plugins (RapidoCMS, meta-ads, marketing…) doit s'y rapporter avant de
produire, pour éviter les doublons et router au bon endroit.

## Arbre de décision

| Besoin | Voie | Skill responsable |
|---|---|---|
| Visuel avec **texte / layout / print** (menu, affiche, slide, flyer) | **rapido-canva** | `rapido-canva:*` |
| Visuel **brandé courant** (logo + assets, déclinaison sociale) | **RapidoCMS** `images_to_image` | `rapidocms:studio-visuel-marque` |
| **Photo réaliste / 4K / packshot pub / texte incrusté complexe** | **Higgsfield** (nano_banana_pro, ms_image, soul_2) | `studio-image-pro` (H3) |
| **Vidéo générative / pub produit / shorts** | **Higgsfield** (kling3_0, marketing_studio_video, shorts) | `usine-video-marketing` (H4), `clips-et-shorts` (H6) |
| **Personnage récurrent** (mascotte, anime PronoClip, humain récurrent) | **Higgsfield** Soul / Elements | `personnages-univers` (H5) |
| **Vidéo éditoriale maquettée** (presets design, typographie animée) | **HyperFrames (HeyGen)** | `rapidocms:video-marketing` |
| **Avatar présentateur Mika** (visage parlant) | **HeyGen** | (HeyGen, hors Higgsfield) |
| **App / landing connectée au CRM** (formulaires, prospects) | **Lovable** (PRIORITAIRE) | `rapido-lovable:usine-a-landing` |
| **Microsite jetable / page événement / JEU jouable** | **Higgsfield** websites/games | `sites-et-jeux-express` (H8) |
| **Voix off / doublage / clonage** (sur médias Higgsfield) | **Higgsfield** audio | `voix-et-doublage` (H7) |

## Règles de tranchage
- **Brandé simple** (logo + variante) → **reste sur CMS** `images_to_image`, ne
  PAS aller sur Higgsfield (coût crédits inutile).
- **Landing CRM** → **Lovable**, jamais un site Higgsfield (qui est jetable).
- **Avatar Mika** → **HeyGen**, jamais un clonage Higgsfield sans droits.
- **Éditorial maquetté** (typo animée, presets) → **HyperFrames**, pas de vidéo
  générative Higgsfield.
- Higgsfield = **la voie premium** : photo réaliste, 4K, vidéo générative, pubs,
  personnages cohérents, sites/jeux express.

> Les branches ci-dessus renvoient à des skills livrés en H2+ ; en H1 seul le
> routage et les garde-fous existent. Un critère ambigu → trancher par le **coût**
> (le moins cher qui atteint la qualité voulue) et par la **charte** (marque d'abord).
