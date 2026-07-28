---
name: fabrique-contenu-iris
description: Utiliser quand une opportunité Iris validée doit devenir un contenu — « fabrique le visuel du plat du jour », « prépare le post du saumon », « génère la story de lancement ». Fabrique visuel + copy + raison aux couleurs de la maison (gate charte), dépose en brouillon RapidoCMS. Jamais de planification sans validation humaine.
---

# Fabrique de contenu (visuel + copy + raison → brouillon)

## Prérequis

Appairage fait (skill `appairage-marque-iris`) : charte et assets connus dans
`./rapido-kb/iris/marque.md`. Sinon, s'arrêter et appairer d'abord.

## Chaîne de fabrication (pour chaque opportunité retenue)

1. **Charte d'abord** : relire `get_brand` (couleurs hex exactes, police,
   logo). Le prompt visuel intègre la palette — jamais une palette arbitraire.
2. **Visuel** :
   - le plat a des photos réelles (assets `list_all_files`, `file_url`
     publiques) → `images_to_image` (3 références max, URLs http(s) —
     contraintes du hook rapidocms) : le plat RÉEL, aux couleurs de la maison ;
   - pas de photo du plat → visuel d'ambiance/typographique via
     `generate_image` (texte, couleurs, logo) — **jamais un faux plat
     photoréaliste** : représenter un plat servi par une image inventée trompe
     le client ;
   - vidéo → skill `video-virale-plats` (Higgsfield, coûts confirmés).
3. **GATE CHARTE** : vérifier le visuel contre la palette (couleurs, logo,
   zone de protection). Hors charte → régénérer, **2 tentatives maximum**,
   puis marquer l'opportunité en échec. Ne JAMAIS proposer un visuel hors
   charte.
4. **Copy adaptée au canal** (Instagram ≠ SMS ≠ email) : ton de la maison,
   aucun chiffre qui ne vienne pas d'une donnée FoodEatUp lue, pas de
   superlatif invérifiable.
5. **La RAISON en une phrase** : « Parce que… » + la donnée déclencheuse.
   Obligatoire — sans elle, la proposition n'existe pas.
6. **Brouillon CMS** : `create_draft_tool` → noter le `draft_id` dans
   `./rapido-kb/iris/calendrier.md` avec statut `propose`.

## Coûts (annoncés AVANT, jamais après)

Chaque génération consomme des crédits : annoncer le coût estimé avant
`generate_image` / `images_to_image` et s'arrêter si l'utilisateur ne valide
pas. Le compteur ne se découvre pas sur la facture.

## Ce que ce skill NE fait PAS

- Planifier/publier → skill `calendrier-iris` (validation humaine + garde-fou).
- La vidéo → skill `video-virale-plats`.
- Les posts sociaux hors signaux d'exploitation → plugin rapidocms
  (skill `pipeline-contenu-social`).
