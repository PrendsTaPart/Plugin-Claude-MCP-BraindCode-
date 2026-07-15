# Évals — plugin rapidocms

## Éval 1 — bibliotheque-prompts (déclenchement)

| Phrase | Attendu |
|---|---|
| « Sauvegarde ce prompt, il a super bien marché » | `bibliotheque-prompts` (add_prompt proposé) |
| « Réutilise le prompt gagnant du plat signature » | `bibliotheque-prompts` (list_prompts → base) |
| « Nettoie ma bibliothèque de prompts » | `bibliotheque-prompts` (edit/delete sur confirmation) |
| « Génère un visuel du burger » | prompt-engineering-visuel / prompts-visuels-pro, qui CONSULTENT la bibliothèque en Étape 0 |

## Éval 2 — bibliotheque-prompts (comportement)

- ATTENDU : list_prompts (type + search) AVANT toute génération d'image —
  prompt proche → proposé comme base avec placeholders remplacés.
- ATTENDU : sauvegarde PROPOSÉE (jamais imposée) après validation du
  visuel ; titre « type — sujet — style » ; content = positif + négatifs ;
  placeholders [entre crochets] ; anti-doublon via list_prompts.
- ATTENDU : type ∈ text | visuel UNIQUEMENT (piège serveur) — un prompt
  vidéo part en type visuel, titre préfixé « vidéo — ».
- ATTENDU : delete_prompt sur confirmation explicite (hook garde-destructif).

## Éval 3 — assets de marque (contenu-conforme-marque)

- « Ajoute ce logo comme logo officiel » → upload_file_tool (type image,
  fond transparent recommandé) → add_asset (brand_id de get_brand) →
  récapitulatif des IDs.
- « Retire l'ancien logo » → remove_asset APRÈS confirmation (matcher hook
  étendu — testé stdin : remove_asset → ask).
- ATTENDU : toute génération référence le logo des assets de marque — jamais
  d'URL improvisée, jamais de logo généré par IA.
- Pipeline vidéo (kit « Mika ») : les logos viennent des assets CMS, plus du
  repo GitHub — une mise à jour de logo = add_asset, le kit suit.

## Éval 4 — gestion-marques (1.3.0)

| Phrase | Attendu |
|---|---|
| « Crée une marque pour ma deuxième enseigne » | `gestion-marques` : `get_brand` d'abord (anti-doublon), récapitulatif complet (nom, langue, slogan, couleurs hex, font web-safe, logo URL publique), confirmation, PUIS `create_brand` |
| « Change les couleurs de la marque en #0F172A et #F59E0B » | `edit_brand` (`brand_id` de `get_brand`, champ `couleurs` seul) — avant/après montré, confirmation (impact sur toutes les productions suivantes) |
| « Supprime la marque de test » | `delete_brand` : hook garde-destructif (ask) + confirmation explicite + rappel que les contenus existants perdent leur référentiel |

- Frontière : « uploade le logo » → `contenu-conforme-marque` (assets),
  pas gestion-marques.

## bibliotheque-assets

| Phrase | Attendu |
|---|---|
| « Importe ce logo et rattache-le à Braindcode » (avec URL publique) | `bibliotheque-assets` : `upload_file_tool` (nom conforme `braindcode-logo-...-vN`, `type=image`) → `list_all_files` pour **résoudre l'asset_id réel** (l'upload n'en renvoie pas) → `get_brand` (confirmer `brand_id`) → `add_asset` ; aucun id inventé |
| « Quels visuels officiels me manquent pour Pronoclip ? » | `bibliotheque-assets` : `get_brand` (noms des assets) → **`audit_assets.py`** (jamais de calcul de tête) → restitue `manquants` + `plan_import` + `non_conformes`, propose l'import |
| « Détache la mascotte de la marque » | `bibliotheque-assets` : `get_brand` → prendre l'**`id` du LIEN** dans `assets[]` (pas l'id du fichier) → **confirmation** → `remove_asset` ; rappelle que le fichier reste dans la bibliothèque |

- Frontière : « crée une nouvelle marque » / « change les couleurs » →
  `gestion-marques` (identité), pas bibliotheque-assets (fichiers).

## studio-visuel-marque

| Phrase | Attendu |
|---|---|
| « Fais-moi un visuel avec notre logo pour la promo » | `studio-visuel-marque` : `get_brand` (marque cible + logo/couleurs) → `list_all_files` (logo + 1-2 assets, ≤3, <5 Mo, URL publique) → prompt décrivant le rôle de chaque image (logo à ne pas déformer) → `images_to_image` size `hd` → critique PASS/FAIL vs charte → capitalisation + brouillon `pipeline-contenu-social` proposés (jamais publié) |
| « Le logo est devenu bleu sur le rendu, corrige » (boucle corrective) | rendu fautif repassé en **1re référence** + références d'origine, prompt correctif chirurgical (« remets le logo blanc d'origine, ne touche à rien d'autre »), re-critique ; **max 2 itérations** puis proposer un changement d'approche |
| « Un visuel aux couleurs de la marque, sans image de base » (routage) | **aucune référence** → `generate_image` via `prompt-engineering-visuel` (le dire), PAS `images_to_image` ; couleurs hex de la charte, pas de logo inventé |
| « Décline ce visuel façon template Canva » (routage) | délégué au plugin **rapido-canva** ; studio-visuel-marque ne force pas `images_to_image` quand l'utilisateur cite Canva |

- Frontière : import/inventaire d'assets → `bibliotheque-assets` ; identité de
  marque → `gestion-marques`.

## coherence-personnage

| Phrase | Attendu |
|---|---|
| « Crée notre mascotte oiseau origami et garde-la cohérente » | `coherence-personnage` : `description_canonique` posée → 1-3 portraits canoniques (`{marque}-{perso}-canon-{angle}-v1`) via upload → `add_asset` (brand_id résolu par `get_brand`) → enregistrement dans `./rapido-kb/personnages.json` (jamais dans le dépôt) |
| « Nouvelle scène avec Origami sur un skate » | lit le registre → passe **1-3 portraits canoniques en référence** à `images_to_image` + prompt « personnage des images 1-2, identique : proportions/couleurs/style » ; **jamais** `generate_image` seul sur un perso récurrent ; critique PASS/FAIL vs canon |
| « Le bec a changé de forme, corrige » (boucle) | rendu fautif en **1re référence** + portraits canoniques, prompt correctif chirurgical, re-critique vs canon, **max 2 itérations** puis proposer un autre portrait/angle |

- Frontière : visuel brandé ponctuel (sans perso récurrent) →
  `studio-visuel-marque` ; import d'assets → `bibliotheque-assets`.

## Branchement couche marque (mises à jour 1.8.0)

| Phrase | Attendu |
|---|---|
| « Prépare un post Insta avec notre logo » | `pipeline-contenu-social` étape visuel → **arbre de décision** : marque a un logo → `studio-visuel-marque` (pas `generate_image`) ; rendu **rattaché au brouillon** (`media_url`) |
| « Un post avec un fond abstrait, sans logo » | `pipeline-contenu-social` → branche (b) `generate_image` (générique, sans référence) |
| « Fais ça dans un template Canva » | `pipeline-contenu-social` / prompting → branche (c) délégation **rapido-canva** |
| « Applique ma marque à ce visuel » (KB dit #0052FF, CMS dit #1A73E8) | `contenu-conforme-marque` : résout les URLs réelles (`get_brand`+`list_all_files`), **signale la divergence** couleur KB↔CMS, propose la sync via `gestion-marques`, applique la KB (prioritaire) en attendant — **jamais d'écrasement silencieux** |
| « Décline ce visuel avec le logo en 3 versions » | `prompt-engineering-visuel` § références : `images_to_image`, **mêmes images**, seul le texte du prompt change ; logo « ne pas déformer/recolorer » |
| « Il y a une faute dans le texte du visuel » | `prompts-visuels-pro` **protocole v2** : rendu fautif repassé en référence `images_to_image`, correction **du texte seul** charte inchangée ; fallback v1 (`generate_image`) si le serveur refuse le rendu en référence |

## Non-régression (comportements existants inchangés)

- **NR1 — « Prépare et planifie un post LinkedIn »** : pipeline-contenu-social
  — `create_draft_tool` un appel par réseau (média : `media_source` toujours
  `"biblio"`), `schedule_draft_tool` avec `post_date` `Y-m-d` et `post_heure`
  STRICT `H-i-s` (tirets), confirmation date/heure avant l'appel.
- **NR2 — « Génère un visuel pour ce post »** : prompt-engineering-visuel —
  Étape 0 (charte + `list_prompts` AVANT de créer), palette hex de la charte
  dans le prompt, pas de texte incrusté, capitalisation PROPOSÉE via
  `add_prompt` (jamais imposée).
