---
name: appairage-marque-iris
description: Utiliser quand l'utilisateur configure Iris ou relie son restaurant à sa marque — « installe Iris », « appaire mon restaurant à ma marque », « Iris ne connaît pas mes couleurs », « synchronise ma charte pour les posts ». Crée la liaison établissement FoodEatUp ↔ marque RapidoCMS, prérequis de tout le reste.
---

# Appairage marque (le prérequis bloquant d'Iris)

Sans liaison établissement ↔ marque, rien ne se connecte : ni visuel aux bonnes
couleurs, ni publication sur les bons comptes. C'est le premier chantier,
toujours.

## Enchaînement (lecture d'abord, écriture confirmée)

1. **Côté FoodEatUp** : identifier l'`establishment_id` (le demander si absent).
2. **Côté RapidoCMS** :
   - `get_brand` : couleurs hex, police, logo. **INTERDIT de coder une couleur
     en dur — tout vient de `get_brand`.**
   - `list_all_files` : inventaire des assets de marque disponibles (logos,
     photos de plats déjà uploadées, avec leur `file_url` publique).
   - `list_connected_accounts` : réseaux réellement branchés (Instagram,
     Facebook, LinkedIn, TikTok) et leur statut.
3. **Aucune marque côté CMS ?** Proposer `create_brand` à partir des
   informations de l'établissement — le hook de charte du plugin rapidocms
   exige la confirmation humaine (une charte engage tous les contenus).
4. **Écrire le mapping** dans `./rapido-kb/iris/marque.md` : establishment_id,
   marque CMS, couleurs relevées, police, URL du logo, comptes connectés,
   date de synchronisation. C'est l'équivalent plugin de la table
   `establishment_brand_map` du cahier des charges — la table serveur reste à
   construire côté produit (voir docs/FAISABILITE-IRIS.md).
5. **Restituer pour confirmation visuelle** : couleurs, logo, comptes — le
   restaurateur confirme que c'est bien SA maison.

## Resynchronisation

À chaque session Iris, si `charte_synced_at` date de plus de 24 h : relire
`get_brand` et `list_connected_accounts`, mettre à jour le fichier, signaler
tout écart (couleur changée, compte déconnecté). Non bloquant : un échec de
synchronisation se dit, il n'empêche pas de travailler sur la dernière charte
connue.

## Sortie attendue

Un récapitulatif : marque appairée, palette exacte (codes hex), comptes actifs,
assets photo disponibles pour les plats — et ce qui manque (ex. « aucune photo
du plat X : en fournir une avant toute vidéo »).

## Ce que ce skill NE fait PAS

- Créer ou modifier la charte en détail → skill `gestion-marques` (plugin
  rapidocms).
- Détecter les raisons de publier → skill `moteur-opportunites-iris`.
