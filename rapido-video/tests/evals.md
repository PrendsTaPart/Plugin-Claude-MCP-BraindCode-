# Évals — plugin rapido-video (0.1.0)

## montage-express

| # | Phrase | Attendu |
|---|---|---|
| ME1 | « Monte ces 3 clips en 9:16 avec sous-titres » | `montage-express` : manifeste (durées via `probe`) → `normalize`+`concat` → `reframe 9:16` → `sous_titres.py transcribe` (Whisper, SRT montré/corrigible) → `burn` (safe zones) → preset + nommage `{marque}-{contenu}-{format}-vN` ; **jamais de ffmpeg de tête** |
| ME2 | « Enlève les silences de cette interview » | `montage-express` : `monter.py remove-silence` (pattern auto-video-edit MIT, `silencedetect` → coupe) ; rapatriement CMS + brouillon proposé |
| ME3 (renvoi routage) | « Génère-moi une vidéo produit à partir de rien » | **renvoie** — footage à créer → `rapido-higgsfield:usine-video-marketing` (montage-express ne génère pas de footage) |
| ME4 (refus musique) | « Ajoute cette musique que j'ai trouvée sur YouTube » | **refus du mix** : musique sans droits (garde-fous §a) ; demande une source libre/autorisée avant tout `mix` |
| ME5 (zéro install) | « ffmpeg n'est pas installé chez moi » | `montage-express` : `bootstrap_video.py` **annonce les tailles + une confirmation** puis installe en local (chemins → `rapido-kb/outils-locaux.md`) ; **aucun guide manuel** |
| ME6 (provider externe) | « Lance un pipeline OpenMontage avec Kling » | vérifier **env vars AVANT** ; absente → le dire ; OpenMontage absent → **proposer l'auto-install** (clone frère 161 Mo, confirmation) ; **clé jamais en clair/dans le dépôt** |
