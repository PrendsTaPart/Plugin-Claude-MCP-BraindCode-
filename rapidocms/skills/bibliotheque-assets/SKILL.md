---
name: bibliotheque-assets
description: Utiliser quand l'utilisateur veut ajouter/importer un fichier ou un asset, gérer sa bibliothèque de fichiers, rattacher un logo ou un visuel à une marque, savoir quels visuels officiels existent, ou faire le point sur les assets manquants d'une marque. Importe (URL publique), inventorie, rattache/détache les assets à la bonne marque, et audite la complétude par script.
---

# Bibliothèque d'assets

Ce skill gère le **stock de fichiers officiels** (logos, mascottes, visuels
produit, textures, templates…) : les importer proprement, les retrouver, les
rattacher à la bonne marque, et repérer ce qui manque. Il s'appuie sur les
outils fichiers/marque de RapidoCMS dont le **contrat live** est décrit dans
`reference/outils-marque.md` — comportements non évidents (upload sans id,
`remove_asset` sur l'id du lien) qu'il faut respecter à la lettre.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/outils-marque.md` (contrat des outils
marque & assets, vérifié en direct) et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-outils.md` (pièges communs des tools).

## Convention de nommage (imposée à l'import)

Tout asset importé est nommé : **`{marque}-{type}-{variante}-v{N}`**
- minuscules, séparateur `-`, suffixe de version `-v1`, `-v2`…
- ex. `braindcode-logo-blanc-v2`, `pronoclip-mascotte-face-v1`.

**Types canoniques** (les seuls admis) : `logo-principal`, `logo-blanc`,
`logo-noir`, `icone`, `mascotte`, `produit`, `texture`, `template`,
`photo-equipe`.

Cette convention rend les assets **retrouvables et audables par script**. Un
nom hors convention est signalé (voir §Audit) et une reprise de nom proposée.

> **Divergence connue.** L'ancien skill `gestion-marques` documentait une
> convention en prose (`"<Marque> — <type> — <variante>"`, espaces/tirets
> longs). Les deux coexistent tant que le parc n'est pas migré : l'audit
> ci-dessous liste les noms non conformes pour piloter la reprise. Pour tout
> NOUVEL import, appliquer la convention machine ci-dessus.

## Importer un fichier — `upload_file_tool`

`upload_file_tool(type=image|video|doc, name="<nom conforme>", file_url=<URL PUBLIQUE>)`.

- Le serveur **télécharge le fichier depuis l'URL** : elle doit être
  **publique et à fetch direct** (S3, CDN…). Un fichier **local** ne marche
  pas → l'expliquer et proposer : héberger via l'UI CMS (bibliothèque), ou
  réutiliser une URL déjà hébergée. Ne jamais inventer d'URL.
- ⚠️ La réponse **ne contient pas d'id** — voir §Résoudre l'asset_id.

## Inventorier — `list_all_files`

`list_all_files(type, search)` → présenter en **tableau** :
`nom | type | asset_id` (l'`asset_id` = le champ `id` du fichier).
⚠️ `search` **ne filtre pas de façon fiable** : filtrer **côté client** sur le
`nom` (ne pas affirmer « aucun résultat » sur la seule base du paramètre).

## Résoudre l'asset_id (toujours avant un rattachement)

`upload_file_tool` ne renvoie pas d'id. Pour obtenir l'`asset_id` réel :
`list_all_files(type=…)` → retrouver l'entrée par son `nom` exact → lire son
`id`. **Jamais d'id inventé ni deviné.**

## Rattacher à une marque — `add_asset`

Séquence obligatoire, dans l'ordre :
1. `get_brand(nom)` → **confirmer le `brand_id`** (le champ `id`, cf. contrat
   live ; plusieurs marques → demander laquelle, jamais de défaut).
2. `list_all_files` → résoudre l'`asset_id` réel du fichier visé.
3. `add_asset(asset_id=<id fichier biblio>, brand_id=<id marque>)`.

## Détacher d'une marque — `remove_asset` (irréversible)

`get_brand(nom)` → dans `assets[]`, repérer l'entrée du fichier → prendre son
**`id` de LIEN** (⚠️ **PAS** `asset_id`/l'id du fichier) →
`remove_asset(asset_id=<id du lien>)`. **Confirmation explicite** exigée
(retrait irréversible du référentiel de la marque ; le fichier reste dans la
bibliothèque — il n'existe pas d'outil pour supprimer un fichier).

## Audit de complétude — `scripts/audit_assets.py`

Pour « quels visuels officiels me manquent ? » ou avant un lancement de marque.
Ne **jamais** calculer l'écart de tête — passer par le script :

1. `get_brand(nom)` → collecter les `file.nom` des `assets[]` de la marque.
2. Exécuter :
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/bibliotheque-assets/scripts/audit_assets.py"`
   avec en entrée (stdin ou fichier JSON) :
   `{"marque": "<marque>", "assets": ["<nom1>", "<nom2>", …]}`.
3. Restituer la sortie : `presents`, `manquants`, `non_conformes` (avec les
   raisons), et **`plan_import`** (nom attendu par type manquant) → proposer
   d'importer les manquants (via `upload_file_tool`) et de renommer les non
   conformes. Aucune écriture sans accord.

## Garde-fous
- Import : **URL publique** obligatoire ; nom **conforme** à la convention.
- Rattachement : `get_brand` + `list_all_files` **avant** `add_asset` — jamais
  d'`asset_id` ni de `brand_id` inventé.
- `remove_asset` : id du **LIEN** (pas du fichier) + **confirmation** ; rappeler
  que le fichier n'est pas supprimé de la bibliothèque.
- Complétude : **toujours** via `audit_assets.py`, jamais de calcul de tête.
- Multi-marques → demander la marque cible.

## Frontières
- Créer/éditer/supprimer une **marque** (identité, couleurs, font) →
  `gestion-marques`. Ce skill-ci gère les **fichiers/assets** et leur
  rattachement, pas l'identité de marque.
- **Appliquer** la charte à un contenu → `contenu-conforme-marque`.
