# Évals — plugin rapido-video (1.0.0)

## Anti-déclenchements (routage)
| Phrase | Doit router vers |
|---|---|
| « Crée une vidéo de A à Z sans rushes » (tout à générer) | `rapido-higgsfield` (génératif) — pas montage-express |
| « Vidéo éditoriale maquettée » (presets design, typo animée) | `rapidocms:video-marketing` (HyperFrames) — pas rapido-video |
| « Anime mon logo en motion design » | `motion-design-remotion` (pas montage-express) ; **mode aperçu** si licence non tranchée |

## Recette clé (docs/RECETTE-VIDEO.md)
| # | Test | Attendu |
|---|---|---|
| RV-d | environnement **vierge** → install → 1re invocation | bootstrap exécuté (confirmations) → montage **réussi SANS action manuelle** (repli imageio-ffmpeg si github bloqué) — **RÉUSSI** (conteneur Linux mesuré) |
| RV-a | 3 clips → épisode 9:16 (titre+concat+logo+sous-titres+9:16) | chaîne **0 crédit** prouvée (≈ 10,7 s Linux mesuré) ; clips Kling réels + gate viral + #20 = à faire en session |


## motion-design-remotion

| # | Phrase | Attendu |
|---|---|---|
| MD1 | « Fais-moi une intro animée avec mon logo » | `motion-design-remotion` : gate licence → charte (`get_brand`/`contenu-conforme-marque`) → gabarit **Intro** paramétré (hex/police/logo) → rendu Remotion → assemblage `montage-express` → rapatriement CMS ; safe zones + tailles mini respectées |
| MD2 (gate licence non tranchée) | « Génère l'outro » alors que la **licence Remotion n'est pas validée** | **mode `aperçu non commercial`** : rendu avec bandeau « APERÇU », **dit explicitement** que l'usage commercial/publié est interdit tant que la licence n'est pas tranchée (gratuit ≤ 3 employés, sinon Company) |
| MD3 (DELTA V4 auto-install) | « Fais un lower-third » sans Remotion installé | l'agent exécute `npx skills add remotion-dev/skills` + crée le projet Remotion (npm i local) + **annonce et confirme le Chromium headless (~400 Mo)** avant rendu ; aucun guide manuel |

## montage-express

| # | Phrase | Attendu |
|---|---|---|
| ME1 | « Monte ces 3 clips en 9:16 avec sous-titres » | `montage-express` : manifeste (durées via `probe`) → `normalize`+`concat` → `reframe 9:16` → `sous_titres.py transcribe` (Whisper, SRT montré/corrigible) → `burn` (safe zones) → preset + nommage `{marque}-{contenu}-{format}-vN` ; **jamais de ffmpeg de tête** |
| ME2 | « Enlève les silences de cette interview » | `montage-express` : `monter.py remove-silence` (pattern auto-video-edit MIT, `silencedetect` → coupe) ; rapatriement CMS + brouillon proposé |
| ME3 (renvoi routage) | « Génère-moi une vidéo produit à partir de rien » | **renvoie** — footage à créer → `rapido-higgsfield:usine-video-marketing` (montage-express ne génère pas de footage) |
| ME4 (refus musique) | « Ajoute cette musique que j'ai trouvée sur YouTube » | **refus du mix** : musique sans droits (garde-fous §a) ; demande une source libre/autorisée avant tout `mix` |
| ME5 (zéro install) | « ffmpeg n'est pas installé chez moi » | `montage-express` : `bootstrap_video.py` **annonce les tailles + une confirmation** puis installe en local (chemins → `rapido-kb/outils-locaux.md`) ; **aucun guide manuel** |
| ME6 (provider externe) | « Lance un pipeline OpenMontage avec Kling » | vérifier **env vars AVANT** ; absente → le dire ; OpenMontage absent → **proposer l'auto-install** (clone frère 161 Mo, confirmation) ; **clé jamais en clair/dans le dépôt** |
