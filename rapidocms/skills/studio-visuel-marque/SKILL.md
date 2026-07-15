---
name: studio-visuel-marque
description: Utiliser quand l'utilisateur veut un visuel avec son logo, une image aux couleurs de la marque, un visuel brandé, intégrer le logo ou la mascotte dans une image, ou décliner un visuel existant. Génère des visuels qui intègrent les VRAIS assets de la marque (logo, mascotte, produit) via images_to_image, avec critique charte et boucle corrective, puis enchaîne le brouillon.
---

# Studio visuel de marque

Le skill **vitrine** de la production visuelle brandée : au lieu d'une image
générique, il génère un visuel qui **intègre le vrai logo et les vrais assets**
de la marque via `images_to_image`, le **critique contre la charte**, corrige
si besoin, puis capitalise et enchaîne le brouillon. Il n'invente ni logo, ni
couleur, ni asset : tout vient du serveur et de la KB.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/outils-marque.md` (contrat live des
outils marque & assets, dont `images_to_image` : URLs publiques, **< 5 Mo par
image**, `size` ∈ `hd|standard`, réponse dans `image_url.original.content`) et
appliquer `contenu-conforme-marque` : **la charte de `./rapido-kb/` prime**
(KB → `get_brand`/`get_company` → repli générique signalé), couleurs et
interdits jamais inventés.

## Routage (à décider en premier)

- Des **références disponibles** (logo/assets de la marque) → `images_to_image`
  (ce pipeline).
- **Aucune référence** exploitable → `generate_image` (via
  `prompt-engineering-visuel`), en le disant.
- L'utilisateur **cite Canva** (template, gabarit précis) → déléguer au plugin
  **rapido-canva**.

## Pipeline (chaque étape annoncée à l'utilisateur)

### 1. Résoudre la marque cible
`get_brand(nom)` → si **plusieurs marques**, DEMANDER laquelle (jamais de
défaut). Extraire de la marque : **logo** (URL), **couleurs** (hex), **font**.
Pas de marque/logo → proposer `bibliotheque-assets` (import) plutôt qu'inventer.

### 2. Collecter les références (sélection minimale)
`list_all_files(type=image)` → filtrer **côté client** (le param `search` ne
filtre pas) sur la convention `{marque}-…` pour retrouver logo + assets utiles.
- **Ne passer QUE les références utiles au rendu** : en général **logo + 1-2
  assets max**.
- Respecter la **limite d'images de `images_to_image`** : contrat vérifié pour
  **1 à 3 références** ; la borne haute exacte n'est pas garantie, donc **ne pas
  dépasser 3** — la sélection minimale y suffit. **< 5 Mo** et **URL publique**
  par image (contrôler `taille`/`file_url` via `list_all_files`).

### 3. Construire le prompt (méthode déléguée)
Déléguer la rédaction à `prompt-engineering-visuel` (et `prompts-visuels-pro`
si **texte incrusté** — orthographe stricte). Dans le prompt, **décrire
explicitement le rôle de chaque référence**, dans l'ordre où elles sont
passées :
- ex. « image 1 = logo officiel, à intégrer en [position], **ne pas déformer ni
  recolorer**, respecter une zone de protection ; image 2 = produit, sujet
  principal ».
Rappeler les **couleurs hex** de la charte et les **interdits** (mots/éléments
bannis de `ton-et-accroches.md`).

### 4. Générer
`images_to_image(images="url1,url2", prompt=<construit>, size="hd")` — **hd par
défaut** pour une publication (`standard` pour un test rapide). Lire l'URL du
rendu dans `image_url.original.content`.

### 5. Critique automatique vs charte
Vérifier et **annoncer un verdict PASS/FAIL argumenté** sur :
- **logo intact** (non déformé, non recoloré, lisible, zone de protection) ;
- **couleurs conformes** à la charte (hex) ;
- **texte sans faute** (si texte incrusté) ;
- **composition adaptée au format cible** (carré/story/bannière).

### 6. Boucle corrective (si FAIL — max 2 itérations)
Repasser le **RENDU FAUTIF en première référence** + les références d'origine,
avec un prompt **correctif chirurgical** : « corrige uniquement X (ex. le logo
est recoloré → le remettre en blanc d'origine), **ne touche à rien d'autre** ».
Après **2 itérations** sans PASS → **arrêter** et proposer un changement
d'approche (autre asset, `generate_image`, ou Canva) plutôt que de boucler.

### 7. Capitaliser
- **Rendu validé** → `upload_file_tool(type=image, name="{marque}-…-vN",
  file_url=<URL du rendu>)` (nommage conforme, cf. `bibliotheque-assets`).
- Réutilisable → proposer `add_asset` (rattacher à la marque).
- Prompt efficace → proposer `add_prompt(type="visuel", …)` avec les valeurs
  spécifiques généralisées en **placeholders `[entre crochets]`**.

### 8. Enchaîner
Proposer le brouillon via `pipeline-contenu-social` — **jamais de publication
directe** (planification confirmée séparément).

## Garde-fous
- Aucun logo/couleur/asset **inventé** : tout vient de `get_brand` +
  `list_all_files` + KB.
- Références : **URL publique**, **< 5 Mo**, **≤ 3** (sélection minimale).
- Chaque rendu **critiqué vs charte** (PASS/FAIL) ; correction **chirurgicale**,
  **max 2 boucles**.
- Capitalisation et brouillon **proposés**, jamais exécutés sans accord ;
  **pas de publication directe**.

## Frontières
- Définir l'**identité** (couleurs, font) → `gestion-marques` ; gérer les
  **fichiers/assets** (import, inventaire, rattachement) → `bibliotheque-assets`.
- **Sans référence** → `generate_image` (`prompt-engineering-visuel`) ;
  **template Canva** → plugin `rapido-canva`.
