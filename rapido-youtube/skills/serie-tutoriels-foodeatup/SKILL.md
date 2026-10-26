---
name: serie-tutoriels-foodeatup
description: Utiliser quand l'utilisateur publie la série des tutos FoodEatUp sur YouTube — « mets les tutoriels du module caisse sur la chaîne », « prépare la série FoodEatUp », « quelles vidéos tuto manquent sur YouTube ? ». Fiches et transcriptions lues au serveur tutoriel, gabarit de miniature appliqué, liens rendus en tableau.
---

# Série tutoriels FoodEatUp (interconnexion)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/gabarit-miniatures-tutos-foodeatup.md` ;
- serveur foodeatup-tutoriel ABSENT de la session : volet sauté en le
  disant (il est en LECTURE SEULE quand il est là).

## Démarche
1. **Lister** : `lister_modules` puis `tutoriels_du_module` (ou
   `lister_tutoriels`) — la série se construit module par module.
2. **Par tutoriel** : `obtenir_tutoriel` (fiche), `transcription_tutoriel`
   (chapitres via scripts/chapitres.py), `obtenir_vignette_tutoriel`
   (visuel source), `obtenir_lien_tutoriel` (lien de la page).
3. **Écrire** : titre (mot-clé du tutoriel), description chaptée + lien
   vers tutoriel.foodeatup.com, SEO noté (`yt_score_video_seo`).
4. **Miniatures** : gabarit tutos FoodEatUp appliqué via l'atelier
   (`yt_generate_thumbnail` sur le kit FoodEatUp, analyse gratuite).
5. **Planifier** : sur la chaîne FoodEatUp (channel_id explicite), grille
   et quota respectés (skills `planifier-et-grille`, hook garde-quota).
6. **Rendre les liens** : le serveur tutoriel est en LECTURE SEULE — les
   liens YouTube obtenus sont rendus à l'HUMAIN dans un TABLEAU
   (tutoriel → lien YouTube → statut), pour report dans l'administration
   du site tutoriel.

## Pièges
- Ne publier que des tutoriels dont la vidéo EXISTE (fiche vidéo servie)
  — un tutoriel sans vidéo se signale, ne s'improvise pas.
- Le lien de la description pointe la PAGE du tutoriel, pas un lien
  signé temporaire.

## Dégradation propre
Serveur tutoriel absent : préparer la trame (titres/descriptions) depuis
les données fournies par l'humain, en marquant ce qui reste à vérifier.
