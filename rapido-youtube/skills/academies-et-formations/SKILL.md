---
name: academies-et-formations
description: Utiliser quand les vidéos des académies partent sur YouTube — « publie les tutos RapidoCMS et enregistre les liens », « quelles vidéos Plan'It manquent ? », « transforme les BD de l'Academy en Shorts ». Même chaîne de travail, enregistrement en retour sur accord, Shorts sur Formation Braindcode.
---

# Académies et formations (interconnexions)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/chaines.md` — chaînes RapidoCMS,
  RapidoCRM, Formation Braindcode (PAS de chaîne RapidoRH : destination
  décidée par l'humain) ; serveurs optionnels absents = volet sauté dit.

## Démarche
1. **Académies RapidoCMS / RapidoRH** (serveurs rapidocms-tuto /
   rapidorh-tuto) : `tutoriels_incomplets` pour prioriser, fiches par
   `obtenir_tutoriel`, publication par la chaîne de travail YouTube
   habituelle (SEO, miniature, quota), puis ENREGISTREMENT EN RETOUR du
   lien avec `enregistrer_youtube` — SUR ACCORD, après publication
   constatée.
2. **Plan'It** (serveur planit-tutoriel) : `videos_manquantes` dit ce qui
   manque, `tutoriel_spec` et `vignette_spec` cadrent le contenu ;
   après publication, `enregistrer_video` et
   `marketplace_enregistrer_video` sur accord.
3. **Academy (BD et épisodes → Shorts)** : `get_formation_comic` et
   `list_media_resources` fournissent les planches et médias — montage
   vertical délégué à rapido-video / rapido-higgsfield, publication en
   Shorts sur la chaîne FORMATION BRAINDCODE (channel_id explicite).
4. **Traçabilité** : un tableau par source (contenu → vidéo → lien →
   enregistré en retour oui/non).

## Pièges
- enregistrer_youtube écrit dans l'académie : accord explicite, lien
  vérifié (la vidéo répond) avant l'enregistrement.
- Les médias de l'Academy gardent leur charte : le kit de la chaîne
  Formation Braindcode s'applique à la MINIATURE, pas au contenu.

## Dégradation propre
Serveur d'académie absent (URL en variable d'environnement non remplie) :
le dire et livrer le tableau « prêt à enregistrer » pour un passage
manuel.
