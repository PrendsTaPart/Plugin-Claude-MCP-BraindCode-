# Cluster marque & assets — contrat live des outils

> Comportements **vérifiés en direct** sur le serveur RapidoCMS (introspection +
> appels réels non destructifs). Le serveur fait foi : si un schéma a changé,
> ré-introspecte l'outil et signale l'écart. À charger en Étape 0 des skills du
> cluster marque (`gestion-marques`, `bibliotheque-assets`,
> `contenu-conforme-marque`).

## Lecture d'une marque — `get_brand(nom)`

- Recherche par **nom** (pas d'id, pas de « lister toutes les marques »).
- Renvoie un **tableau** : `{"brand": [ { … } ]}` (filtré par nom).
- L'`id` de l'objet marque **EST le `brand_id`** (il n'y a pas de champ
  nommé `brand_id`).
- Chaque marque porte un tableau `assets` :
  `assets: [ { "id": <id du LIEN>, "asset_id": <id du fichier biblio>,
  "marque_id": <brand_id>, "file": { "id", "nom", "type", "file_url", … } } ]`.
  Marque sans asset → `assets: []`.

## Création / édition — `create_brand`, `edit_brand`

- `create_brand` **requis** : `nom`, `langue`, `slogan`. Optionnels :
  `couleurs`, `font_family`, `logo`, `site_web`.
- La réponse de `create_brand` **contient l'`id` de la marque créée** (le
  `brand_id`) — le lire directement, ne pas ré-appeler `get_brand` pour le
  retrouver.
- `edit_brand` **requis** : `brand_id`. Ne passer que les champs à changer.
- **`couleurs`** : hex séparés par des virgules, sans espaces
  (`#0052FF,#FFFFFF`). ⚠️ **Le serveur ne valide PAS le format** : une valeur
  invalide (`#ZZZ,bleu`) est **stockée telle quelle**. C'est au skill de
  valider l'hex AVANT l'écriture — jamais de couleur inventée ni malformée.
- **`font_family`** : ENUM de piles web-safe (voir `gestion-marques`).
- **`logo`** : URL **publique** obligatoire (uploader d'abord si besoin).

## Bibliothèque de fichiers — `upload_file_tool`, `list_all_files`

- `upload_file_tool(type, name, file_url)` : `type` ∈ `image|video|doc`,
  `file_url` **publique**. Le serveur **télécharge le fichier côté serveur** —
  certains hôtes refusent ce fetch (ex. Wikimedia → HTTP 403). Préférer un
  hébergement à fetch direct (S3, CDN, `gstatic`).
- ⚠️ La réponse de `upload_file_tool` = `{message, file_url}` **SANS id**.
  Pour obtenir l'`asset_id`, il faut **ensuite** `list_all_files` et retrouver
  le fichier par son `nom`.
- `list_all_files(type, search)` : renvoie `{files: [ {id, file, nom, type,
  taille, file_url} ]}`. L'`id` (entier) est l'**asset_id** utilisé par
  `add_asset`. ⚠️ Le paramètre `search` **ne filtre pas de façon fiable**
  (peut renvoyer toute la liste) — filtrer **côté client** sur `nom`.
- `taille` peut valoir `"0"` juste après un upload (métadonnée non recalculée) :
  ne pas s'y fier pour un contrôle de poids.

## Rattacher / détacher un asset — `add_asset`, `remove_asset`

- `add_asset(asset_id, brand_id)` : `asset_id` = l'**`id` du fichier
  bibliothèque** (celui de `list_all_files`). Crée un **lien** dont la réponse
  porte un `id` propre (l'id du LIEN, ≠ id du fichier).
- ⚠️ `remove_asset(asset_id)` attend l'**`id` du LIEN** — c'est-à-dire le champ
  `id` d'une entrée de `brand.assets[]` renvoyée par `get_brand`, **PAS** l'id
  du fichier bibliothèque. Toujours résoudre le bon id via `get_brand` avant de
  détacher. Opération **irréversible** côté marque (hook `garde-destructif`).

## Génération d'image à partir de références — `images_to_image`

- `images_to_image(prompt, size, images)` : `images` = URLs **publiques**
  séparées par des virgules, **< 5 Mo chacune** ; `size` ∈ `hd|standard`.
- Réponse : `{"image_url": {"original": {"success": true, "content":
  "<URL S3 du rendu>"}}}` — l'URL du rendu est dans `original.content`.
- Vérifié fonctionnel de **1 à 3 images de référence**. Consomme des crédits :
  ne pas multiplier les appels de test.

## Nettoyage / suppression de fichier

- Il **n'existe aucun outil de suppression d'un fichier de la bibliothèque**
  parmi les outils exposés (on peut `remove_asset` le lien à une marque, pas
  supprimer le fichier lui-même). Le dire à l'utilisateur : un fichier importé
  par erreur se détache d'une marque mais reste dans la bibliothèque (retrait
  via l'UI CMS).
