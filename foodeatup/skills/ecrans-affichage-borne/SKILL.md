---
name: ecrans-affichage-borne
description: Utiliser quand l'utilisateur parle des écrans du restaurant (télé, affichage dynamique, menu board), d'affiches à diffuser, de playlists, de programmation d'écran, d'appairer une nouvelle télé, ou des bornes de commande et tablettes de table. Pilote l'offre Écrans & Borne FoodEatUp — bibliothèque d'affiches, affiches IA, diffusion programmée ou immédiate, menu board synchronisé avec la carte, état du parc et des bornes.
---

# Écrans d'affichage & bornes de commande

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — si `ambiguous=true`,
   présenter les candidats et DEMANDER confirmation. Jamais d'ID deviné.
4. Les outils exigent l'offre **Écrans** (bornes : pack **Écrans & Borne**) :
   si le serveur refuse pour cause d'offre, le dire tel quel, sans contourner.

## 1. État des lieux (lecture)

- `etat_parc` : écrans en ligne / hors ligne / pas encore branchés, écrans
  muets depuis quand, diffusions immédiates en cours, quota de l'offre et
  **crédits d'affiches** restants.
- `lister_ecrans` : nom, zone, groupes, orientation, ce que chaque écran joue
  maintenant ; `obtenir_ecran` (`ecran_id`) : programme, prochain changement,
  10 derniers événements (pertes réseau, appairage).
- `rapport_diffusion` (`du`/`au`, `ecran_id` optionnel) : ce qui passe
  maintenant et ce qui a réellement été joué (passages, durées, affiches les
  plus diffusées).

## 2. Brancher un nouvel écran

`creer_code_appairage` (`nom` unique, `zone`, `orientation` ∈ paysage |
portrait) → code à 6 caractères (7 jours) et adresse `/play/CODE` à ouvrir sur
le téléviseur. **Compte dans le quota** même jamais branché : confirmer avant.

## 3. Bibliothèque d'affiches

- `lister_medias` : affiches disponibles + affiches IA en fabrication / en échec.
- `importer_media` (`image_url` HTTPS **directe** vers un JPEG/PNG/WebP ≤ 8 Mo,
  `nom`) : ajoute sans diffuser.
- `generer_affiche` : affiche IA à partir de **plats de la carte** (`plat_ids`
  issus de `list_dishes` — nom, photo et prix TTC relus par le serveur, jamais
  saisis). `format` ∈ `16:9` | `9:16` ; `modele` selon le nombre de plats :
  `hero` (1), `vitrine` (2–4), `menu_board` (5–20). **Coûte des crédits**
  (débités si réussie) → annoncer le solde (`etat_parc`) et confirmer. Puis
  `lister_medias` (1–2 min) termine la fabrication ; **faire relire
  l'affiche** avant toute diffusion.

## 4. Diffuser

- **Programmé** : `creer_playlist` (`nom`, `media_ids` dans l'ordre, `duree_s`
  5–300, `message`) puis `planifier_diffusion` (`playlist_id`, `ecran_id` OU
  `groupe_id`, `jours`, `debut`/`fin` HH:MM, `date_debut`/`date_fin`). Un
  chevauchement est refusé par le serveur en nommant le créneau en conflit :
  le relayer. `lister_playlists` montre playlists et créneaux existants.
- **Immédiat** : `diffuser_maintenant` (`media_ids` ou `playlist_id`, cible
  `ecran_ids` / `groupe_ids` / `zone` / `tous`, `minutes` ≤ 720). Appeler
  d'abord **sans `confirm`** : l'outil renvoie la liste exacte des écrans et
  affiches → la relire au restaurateur, puis `confirm: true`.
- **Arrêter** : `arreter_diffusion`, même protocole aperçu → confirmation.

## 5. Menu board (carte en direct)

`synchroniser_carte` : avec `activer: true/false` pose ou retire la carte
(`category_ids` de `list_dish_categories`, vide = toute la carte) sur les
écrans visés ; sans `activer`, force le rafraîchissement. Les plats épuisés du
jour (`set_dish_sold_out`, skill `carte-caisse-options`) s'y affichent
« Épuisé ». Aucun crédit consommé.

## 6. Bornes de commande & tablettes

- `lister_bornes` : bornes, mode, table, en ligne, commandes du jour, quota.
- `etat_borne` (`borne_id`) : dernier signal, version, TPE, chiffres du jour
  (commandes payées, panier moyen, abandons).
- `lister_commandes_borne` (`borne_id`, `date`, `statut`) : 50 dernières
  commandes. Le suivi en cuisine reste dans `gestion-commandes` /
  `coordination-cuisine`.

## Garde-fous

- `diffuser_maintenant` / `arreter_diffusion` : **jamais `confirm: true`
  d'office** — aperçu relu d'abord (hook `garde-destructif` en filet).
- Aucune affiche IA diffusée sans relecture humaine ; aucun prix saisi à la main.
- Récapituler : écrans appairés, affiches importées/générées (IDs), playlists
  et créneaux créés, diffusions lancées/arrêtées.
