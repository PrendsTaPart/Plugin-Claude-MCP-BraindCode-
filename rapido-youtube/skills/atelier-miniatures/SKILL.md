---
name: atelier-miniatures
description: Utiliser quand l'utilisateur travaille une miniature YouTube — « génère la miniature », « analyse cette vignette », « retouche la zone du titre », « applique le style de la chaîne ». Kits et styles lus d'abord, crédits annoncés, analyse gratuite entre chaque geste payant.
---

# Atelier de miniatures

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/quota-et-credits.md` (barème LU, rien
  en dur) ; pour la chaîne FoodEatUp :
  `${CLAUDE_PLUGIN_ROOT}/reference/gabarit-miniatures-tutos-foodeatup.md`.

## Démarche
1. **Les fondations** : `yt_list_brand_kits`, `yt_list_styles`,
   `yt_list_face_models` — tout vient de là, rien d'inventé.
2. **Générer** : `yt_generate_thumbnail` — coût en crédits ANNONCÉ
   (scripts/credits.py sur le barème de `yt_get_credit_balance`),
   variations limitées (1 par défaut, le hook garde-credits questionne
   au-delà).
3. **Analyser GRATUITEMENT** : `yt_analyze_thumbnail` après chaque
   génération — scores et suggestions avant tout crédit supplémentaire.
4. **Retoucher** (chaque geste coûte, annoncé) : `yt_edit_thumbnail` sur
   UNE suggestion de l'analyse ; `yt_inpaint_thumbnail` pour une zone
   localisée ; `yt_auto_optimize_thumbnail` (2 passes) ;
   `yt_apply_style` / `yt_apply_template` pour la cohérence de chaîne ;
   `yt_swap_face` UNIQUEMENT avec un modèle de visage de l'utilisateur
   (hook garde-visage).
5. **Comparer et ranger** : `yt_compare_thumbnails` (gratuit),
   `yt_get_thumbnail`, `yt_list_thumbnails` ; widget atelier-miniatures
   sur demande.
6. **Repartir / s'inspirer** : `yt_extract_youtube_thumbnail` pour
   repartir d'une miniature existante ; `yt_clone_style_from_url` pour
   une AMBIANCE — jamais une marque, un logo, un personnage ni un visage
   d'autrui.
7. **Version Shorts** : `yt_generate_vertical_variant` sur la miniature
   validée.

## Pièges
- Les aperçus sont des liens signés TEMPORAIRES : jamais collés dans une
  description, une page ou un fichier commité.
- Générer 4 variations d'un coup coûte 4 fois : générer 1, analyser
  (gratuit), corriger — la boucle est moins chère que la rafale.

## Dégradation propre
Solde de crédits insuffisant pour le plan : montrer le calcul et réduire
AVEC l'utilisateur ; jamais d'« essai » payant non annoncé.
