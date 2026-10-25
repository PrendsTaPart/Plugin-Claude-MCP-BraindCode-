# Gabarit des miniatures — tutos FoodEatUp

Consigne de composition pour le kit de marque FoodEatUp (chaîne tutos),
donnée par le propriétaire le 2026-10-25. Elle se passe TELLE QUELLE à
`yt_generate_thumbnail` (et sert de grille de lecture à
`yt_analyze_thumbnail`).

## La composition

- **Fond** : clair, quasi blanc.
- **Formes** : formes bleues organiques en haut à droite et en bas à
  gauche.
- **Logo** : logo FoodEatUp bleu, en haut à gauche.
- **Titre** : orange, sur TROIS lignes, aligné à gauche — le mot-clé en
  GRAS sur la ligne du milieu.
- **Personnage** : personne réelle détourée, à droite.
- **Accents** : touches jaunes.
- **Bouton** : orange, « REJOIGNEZ-NOUS », en bas à droite.

## Règles d'application

1. Les couleurs exactes viennent du kit de marque lu par
   `yt_list_brand_kits` — ce gabarit décrit la COMPOSITION, pas des codes
   hexadécimaux à inventer.
2. Le personnage est une photo réelle fournie (détourée), jamais un visage
   généré ni échangé sans modèle de l'utilisateur (hook garde-visage).
3. Le mot-clé en gras est celui du titre retenu (skill
   titre-description-seo), pas un mot décoratif.
4. La variante Shorts se produit par `yt_generate_vertical_variant` à
   partir de la miniature validée.
5. Chaque génération s'analyse (gratuit) avant toute retouche payante.
