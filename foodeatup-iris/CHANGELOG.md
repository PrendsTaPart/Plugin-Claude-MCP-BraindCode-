# Changelog — plugin foodeatup-iris

## 0.2.0 — 2026-10-25 — nouveaux capteurs et canal écrans

- Moteur : marronniers/événements via `get_marketing_calendar` (serveur, plus
  de calendrier interne), plat star aussi via `get_top_flop_products`.
- Fabrique : affiches pour les écrans de la salle (`generer_affiche`, modèle
  selon le nombre de plats) ; diffusion toujours confirmée (garde foodeatup).

## 0.1.0 — 2026-07-28 — naissance d'Iris (CDC agent communication v1.0)

- Agent `iris` + 6 skills : appairage marque (L1), moteur d'opportunités
  (11 capteurs FoodEatUp, score urgence × valeur × fraîcheur, dédup, raison
  obligatoire), fabrique (gate charte, 2 tentatives max), vidéo virale de
  plats (photos réelles → Higgsfield, virality_predictor, coûts confirmés),
  calendrier 7 jours glissants (valider/modifier/refuser avec motif), mesure
  & apprentissage (insights réels, corrélation commandes 48 h, add_prompt).
- Hook garde-iris : publication/planification → confirmation humaine toujours ;
  génération vidéo sans cout_confirme → refus. Hook Stop : pas de proposition
  sans raison.
- Étude de faisabilité vs CDC : docs/FAISABILITE-IRIS.md (plugin vs backlog
  produit L1-L6).
