---
name: coherence-personnage
description: Utiliser quand l'utilisateur veut réutiliser le même personnage ou la même mascotte, garder le style d'un personnage récurrent, une nouvelle scène avec un personnage nommé, ou parle de cohérence de personnage. Maintient un registre de portraits canoniques par personnage et génère de nouvelles scènes en passant TOUJOURS ces portraits en référence à images_to_image.
---

# Cohérence de personnage

Garantit qu'un **personnage récurrent** (mascotte oiseau origami BraindCode,
avatar 3D d'une marque Rapido, personnage anime PronoClip…) reste **identique**
d'une image à l'autre. Le principe : un **registre de portraits canoniques** par
personnage + génération **toujours guidée par ces portraits** via
`images_to_image`. Générer un personnage récurrent **sans référence = dérive
garantie** — c'est interdit ici.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/outils-marque.md` (contrat live :
`images_to_image` URLs publiques, **< 5 Mo/image**, **1 à 3 références**,
rendu dans `image_url.original.content` ; `upload_file_tool` sans id → résoudre
via `list_all_files`). S'appuyer sur `bibliotheque-assets` (nommage/rattachement)
et sur `studio-visuel-marque` (critique + boucle corrective, réutilisées ici).

## Le registre — `./rapido-kb/personnages.json`

Créé et maintenu par ce skill, **côté client** (jamais dans le dépôt du
plugin ; il vit dans la KB versionnée de l'utilisateur). Schéma (exemple annoté
dans `${CLAUDE_PLUGIN_ROOT}/skills/coherence-personnage/reference/personnages.exemple.json`) :

```json
{ "personnages": [ {
  "nom": "Origami", "marque": "braindcode", "brand_id": 14,
  "description_canonique": "oiseau origami, papier bleu #0052FF, œil rond noir…",
  "version_active": "v1",
  "portraits": [ { "asset_id": 624, "url": "…", "angle": "face", "version": "v1" } ]
} ] }
```

Registre absent → le créer ; jamais de `brand_id`/`asset_id` inventé (les
résoudre via `get_brand` / `list_all_files`).

## 1. Créer un personnage (poser le canon)

1. Écrire la **`description_canonique`** (traits, proportions, palette hex,
   style) avec l'utilisateur — c'est la référence textuelle.
2. Obtenir **1 à 3 portraits canoniques** — angles utiles : `face`,
   `trois-quarts`, `action`. Soit fournis (URL publique), soit générés
   (`generate_image` puis, pour les vues suivantes, `images_to_image` à partir
   de la 1re vue pour rester cohérent).
3. `upload_file_tool(type=image, name="{marque}-{personnage}-canon-{angle}-v1",
   file_url=<url publique>)` → `list_all_files` pour **résoudre l'`asset_id`** →
   `add_asset(asset_id, brand_id)` (résoudre le `brand_id` via `get_brand`).
4. Enregistrer le personnage dans `./rapido-kb/personnages.json`
   (`version_active: "v1"`, portraits avec `asset_id`/`url`/`angle`).

## 2. Générer une nouvelle scène (le cœur)

1. Lire le personnage dans le registre → récupérer les **portraits de la
   `version_active`** (leurs `url` publiques) et la `description_canonique`.
2. **TOUJOURS** passer **1 à 3 portraits canoniques** en référence :
   `images_to_image(images="url1,url2", prompt=<scène>, size="hd")`.
3. Le prompt de scène rappelle le canon **explicitement** :
   « le personnage des images 1-2, **identique** : mêmes proportions, mêmes
   couleurs (hex), même style ; nouvelle scène : <décor/action> ». Décrire le
   rôle de chaque référence (comme `studio-visuel-marque`).
4. **INTERDIT** : générer le personnage **sans** portrait de référence
   (`generate_image` seul sur un personnage récurrent) — dérive garantie. Si
   aucun portrait n'existe encore → passer par §1 d'abord.

## 3. Critique vs canon (avant livraison)

Verdict **PASS/FAIL argumenté** sur la **cohérence au canon** : traits du
visage/silhouette, **palette** (hex), **style** (line-art, 3D, origami…),
proportions. FAIL → **boucle corrective identique à `studio-visuel-marque`** :
rendu fautif en **1re référence** + portraits canoniques, prompt correctif
chirurgical, **max 2 itérations** puis proposer un autre angle/portrait.

## 4. Faire évoluer le canon (versionner)

Nouveau look → générer les portraits en **`vN+1`** (`{marque}-{personnage}-canon-{angle}-v2`),
les uploader/rattacher, **garder les anciens** dans la bibliothèque, et mettre
`version_active` à jour dans le registre. Les scènes suivantes utilisent la
nouvelle version ; l'historique reste traçable.

## 5. Capitaliser

Rendu validé → `upload_file_tool` (nommage `{marque}-{personnage}-scene-…-vN`) ;
réutilisable comme nouveau portrait → proposer de l'ajouter aux `portraits` du
registre. Prompt de scène efficace → proposer `add_prompt(type="visuel")`
(placeholders `[entre crochets]`). Enchaîner le brouillon via
`pipeline-contenu-social` (jamais de publication directe).

## Garde-fous
- **Jamais** de génération d'un personnage récurrent **sans référence
  canonique** (règle centrale).
- Références : **URL publique**, **< 5 Mo**, **1 à 3** portraits.
- `brand_id`/`asset_id` **résolus** (`get_brand`/`list_all_files`), jamais
  inventés ; registre côté `./rapido-kb/`, pas dans le dépôt.
- Chaque rendu **critiqué vs canon** (PASS/FAIL), correction **chirurgicale**,
  **max 2 boucles**.
- Évolution du canon = **nouvelle version**, l'ancienne conservée.

## Frontières
- Visuel brandé **ponctuel** (logo/produit, sans personnage récurrent) →
  `studio-visuel-marque`.
- Gérer les **fichiers/assets** (import, inventaire) → `bibliotheque-assets` ;
  **identité de marque** → `gestion-marques`.
- **Rédiger le prompt** finement → `prompt-engineering-visuel` /
  `prompts-visuels-pro`.
