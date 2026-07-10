---
name: gestion-marques
description: Utiliser quand l'utilisateur veut créer ou modifier une marque, gérer plusieurs marques (multi-enseignes), ajouter un logo ou un asset de marque, ou parle de la charte d'une de ses marques. Crée/édite/supprime les marques, gère la bibliothèque d'assets officiels par marque, et impose une marque cible avant toute génération de contenu.
---

# Gestion des marques

Ce skill pilote le **cluster marques** de RapidoCMS : création, édition, suppression d'une
marque, et sa **bibliothèque d'assets officiels** (logos, visuels clés). C'est la brique qui
garantit qu'un contenu part toujours à la **bonne charte, pour la bonne enseigne**.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes) et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-outils.md` (pièges des tools). Pour toute couleur/typo,
**ordre de priorité des sources** (identique au reste du plugin) :
`./rapido-kb/charte-graphique.md` (KB client, source de vérité) → `get_brand` + `get_company`
(valeurs live) → `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` (repli générique — à
**SIGNALER** si utilisé). Ne **jamais inventer** une couleur : si aucune source ne la donne, la demander.

> **Schéma vivant.** Les schémas ci-dessous reflètent le contrat live au moment de la rédaction.
> **Avant chaque écriture, ré-introspecte le tool** (surtout l'enum `font_family` et les champs
> requis de `create_brand`) : si le serveur a changé, le serveur fait foi — adapte-toi et signale l'écart.

## 0 bis — Multi-marques : jamais de défaut silencieux

BraindCode opère **plusieurs enseignes** (BraindCode, FoodEatUp, PronoClip, PrendsTaPart,
RapidoSoftware…). Dès qu'une action porte sur « la marque » (créer un contenu, un post, un
visuel, une vidéo…) et que **plusieurs marques existent**, **DEMANDER toujours pour quelle
marque** — jamais de défaut implicite. Puis **charger ses couleurs / ton / logo** (`get_brand`
+ assets de la marque) **avant** de générer. Nouveau projet sans marque → **proposer de créer
la marque manquante** plutôt qu'inventer une identité.

## 1. Créer une marque — `create_brand`

Contrat live : **requis** `nom`, `langue`, `slogan`. Optionnels `couleurs`, `font_family`,
`logo`, `site_web`.

- **`couleurs`** : hex séparés par des virgules, sans espaces (`#1B2A41,#00A8F0,#48A850`),
  **depuis la charte** (ordre de priorité §Étape 0), jamais inventées.
- **`font_family`** : ENUM de piles web-safe. Au moment de la rédaction :
  `Arial, sans-serif` · `Verdana, sans-serif` · `Tahoma, sans-serif` · `Trebuchet MS, sans-serif`
  · `Georgia, serif` · `Times New Roman, serif` · `Garamond, serif` · `Courier New, monospace`
  · `Lucida Console, monospace`. **Introspecter l'enum**, choisir la pile **la plus proche** de la
  typo de la charte, et **le dire à l'utilisateur** (ex. « ta charte utilise *Poppins* ; la police
  web-safe la plus proche disponible est *Trebuchet MS* — je pars là-dessus, OK ? »).
  Aide (indicative) : Poppins/Montserrat/Futura → `Trebuchet MS` ; Inter/Helvetica/Roboto →
  `Arial` ; Open Sans/Segoe → `Verdana` ; serif éditorial → `Georgia` ; serif classique →
  `Times New Roman` ; mono → `Courier New`.
- **`logo`** : **URL PUBLIQUE** obligatoire. Fichier local / image non hébergée → `upload_file_tool`
  (type `image`) d'abord, récupérer la `file_url` retournée, **puis** l'utiliser dans `logo`.

**Confirmation — NIVEAU 2** : toute écriture de marque (`create_brand`/`edit_brand`) exige un
**récapitulatif complet** (nom, langue, slogan, couleurs exactes, font_family choisie + justif,
URL logo, site) et **l'accord explicite** de l'utilisateur avant l'appel.

## 2. Modifier une marque — `edit_brand`

Requis `brand_id`. Ne passer **que** les champs à changer. Récupérer l'état courant via
`get_brand` pour montrer le diff. Mêmes règles couleurs/font/logo. **Confirmation niveau 2**.

## 3. Supprimer une marque — `delete_brand` (GARDE-DESTRUCTIF)

Requis `brand_id`. **Irréversible.** Garde-fou : demander à l'utilisateur de **retaper le nom
EXACT** de la marque ; ne procéder que si la saisie correspond au champ `nom` de la marque
ciblée. Rappeler ce qui sera perdu (assets liés, références).

## 4. Bibliothèque d'assets par marque — `add_asset` / `remove_asset`

Chaque marque a une bibliothèque d'assets officiels (logos fond transparent, déclinaisons,
visuels clés réutilisables par le pipeline vidéo, les posts, les cartes).

- `add_asset(asset_id, brand_id)` — lie un fichier **déjà présent dans la bibliothèque** à la
  marque (uploader via `upload_file_tool` si besoin, récupérer l'`id` via `list_all_files`).
- `remove_asset(asset_id)` — délie l'asset.

**Convention de nommage** (au moment de l'upload, champ `name` de `upload_file_tool`) :
`"<Marque> — <type> — <variante>"` — ex. `FoodEatUp — logo — fond transparent`,
`BraindCode — logo — monochrome blanc`, `RapidoSoftware — visuel clé — hub MCP`. Cette
convention rend les assets **retrouvables par nom** (les routines et le pipeline vidéo s'appuient dessus).

**Flux « ajouter un logo »** : `upload_file_tool(type=image, name="<Marque> — logo — fond transparent", file_url=<url publique>)`
→ `list_all_files(type=image, search="<Marque> — logo")` → `add_asset(asset_id, brand_id)`.

## 5. Lecture — `get_brand`

Renvoie l'état **serveur** d'une marque (couleurs, font, logo, slogan) : référence pour le diff
avant `edit_brand` et pour charger l'identité avant de générer un contenu (§0 bis).

## Intégrations
- **contenu-conforme-marque** : l'étape 0 lit désormais `get_brand` **+ les assets de la marque
  cible**. KB = source de vérité ; écart KB ↔ serveur → le signaler et proposer la synchro via
  `mise-a-jour-kb`.
- **video-marketing** + **prompts-visuels-pro** : les **logos viennent des assets de marque**
  (URL publique via `get_brand`/`list_all_files`), plus des « logos GitHub ».

## Garde-fous (résumé)
- Multi-marques → **toujours demander la marque cible** (jamais de défaut silencieux).
- Écriture marque → **confirmation niveau 2** (récap complet).
- `delete_brand` → **nom exact retapé**.
- Couleurs → **depuis la charte** (ordre de priorité), jamais inventées.
- `font_family` → **ENUM introspecté**, choix expliqué à l'utilisateur.
- `logo` / assets → **URL publique** via `upload_file_tool` d'abord.

Agent dédié : **gestionnaire-marques** (gardien de la cohérence multi-enseignes).
