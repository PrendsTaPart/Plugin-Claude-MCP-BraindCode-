# Recette rapido-higgsfield — état & preuve live

> Clôture H10. Décision : **release v1.0.0 sans recette vidéo live** (le solde de
> crédits ne couvre pas la recette complète — voir budget ci-dessous). La **preuve
> de bout en bout** est fournie par le **test de plomberie H0** (réel, réussi).
> La recette vidéo est **différée** jusqu'à un solde suffisant.

## Preuve live déjà réalisée (H0, 2026-07-15)
Chaîne inter-MCP **exécutée pour de vrai** (2 crédits) :
`list_all_files` (CMS, asset `braind_robot_ai` id 166) → `media_import_url`
(media_id `b6e9d941…`) → `generate_image` `nano_banana_pro` 1k (job `640c63cc…`,
**coût réel 2 cr** = préflight exact) → `upload_file_tool` → fichier CMS
`TEST-H0-braind-render`. **Le pont CMS ↔ Higgsfield fonctionne dans les deux sens.**

## Budget (au moment de la release)
- Solde : **80 crédits** (plan basic).
- Recette prévue : (a) packshot 4K ~4 cr · (b) PronoClip Element + clip Kling
  ~10-30 cr · (c) **short 30s ~90 cr** · (d) dubbing 30s (à mesurer).
- **(c) seul dépasse le solde** → recette complète non tenable à 80 crédits.

## Recette différée — à exécuter quand le solde le permet
Chaque étape **chiffrée AVANT** via `gouvernance-credits` (BLOQUÉ = pas de génération) :
1. **(a) FoodEatUp** — 1 packshot de plat 4K (`studio-image-pro`, `ms_image`/`nano_banana_pro`)
   rapatrié dans la carte vitrine (`foodeatup:carte-vitrine`). ~4 cr.
2. **(b) PronoClip** — 1 **Element** depuis un portrait canonique
   (`personnages-univers`) + 1 **clip Kling 3.0 9:16** (start_image + `<<<element_id>>>`)
   → **gate viral** (`analyse-video-virale`) → brouillon rattaché à la campagne **#20**. ~10-30 cr.
3. **(c) Short** — 1 short depuis le top post vidéo du mois (`clips-et-shorts`),
   brouillon planifié (non publié). ~90 cr (nécessite un top-up).
4. **(d) Dubbing** — 30 s d'un extrait **V1 FoodEatUp** en anglais (`voix-et-doublage`).
   Coût à relever (pas de préflight `get_cost` sur `dubbing`).

**À consigner ici après exécution** : coûts réels vs grille (`GRILLE-COUTS-HIGGSFIELD.md`),
qualité, frictions, IDs (jobs/assets), et le nettoyage des données de test.

## Nettoyage en attente
- Fichier CMS `TEST-H0-braind-render` (test H0) — pas d'outil `delete_file` côté
  RapidoCMS → suppression manuelle.
