# Garde-fous média (non négociables)

Règles de tout skill/agent du plugin. Les hooks (`hooks/`) en appliquent une
partie ; le reste est contractuel.

## (a) Coûts — tout est payant en crédits
- **Plafond mensuel** défini dans `./rapido-kb/budget-media.md` (crédits + seuil de
  confirmation + compteur). En début de session de production : lire `balance`.
- **`get_cost: true` en préflight systématique** avant toute génération payante
  (jamais d'estimation « de tête »). Le devis préflight ne facture pas.
- **Toute génération au-dessus du seuil KB = confirmation explicite** de
  l'utilisateur avant lancement. Hook en filet : `garde-couts` (refus tant que le
  coût n'est pas confirmé — marqueur `get_cost:true` ou `cout_confirme:true`).
- `select_workspace` engage la **facturation** : vérifier le workspace actif d'abord.

## (b) Voix — droits & consentement obligatoires
- `create_voice*`, `voice_change`, `dubbing` **uniquement** sur des voix dont
  l'utilisateur détient les **droits** (la sienne, un collaborateur consentant, une
  licence). **Mika / HeyGen** : statut de licence **à clarifier** avant tout clonage.
- **Confirmation explicite + mention du consentement à chaque clonage/doublage.**
  Hook en filet : `garde-voix` (force la question).

## (c) Marque — charte avant publication
- Tout rendu destiné à publication passe par la **critique charte** (grille de
  `rapidocms:studio-visuel-marque`) **avant** tout brouillon. Écart charte → remonter
  à `rapidocms:gardien-de-marque`.
- Les assets entrent dans la **bibliothèque de marque** RapidoCMS
  (`upload_file_tool`, nommage `{marque}-{type}-{variante}-vN`).

## (d) Publication & publicité — jamais directe
- **Aucune publication directe** : les rendus deviennent des **brouillons** (CMS),
  la planification/publication reste sous le garde-fou d'envoi du plugin concerné.
- Créatifs IA envoyés à Meta → **`self_ai_disclosure: "OPT_IN"`** (déclaration Meta
  d'un créatif généré par IA), campagne en **PAUSED**, budget confirmé.
- **Gate viral** (`analyse-video-virale`, H6) **avant tout boost payant** : aucune
  vidéo non passée au gate n'est boostée.

## (e) Montage local — temps & chemins
- **Temps de rendu variable selon l'environnement** : annoncer que la durée dépend
  de la machine (à mesurer localement), **jamais** de chiffre présenté comme absolu.
- **Dépendances auto-installées** (ffmpeg, transcription) : **annoncer les tailles
  et confirmer une fois** avant tout téléchargement (`scripts/bootstrap_video.py`).
- **Chemins d'outils** : toujours lus depuis `rapido-kb/outils-locaux.md` (résolus
  par le bootstrap), via `pathlib` — **aucun antislash Windows en dur**.
