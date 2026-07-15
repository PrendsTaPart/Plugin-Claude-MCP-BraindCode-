# Environnement montage vidéo — par OS

> Le plugin **n'exige AUCUNE installation manuelle** : `scripts/bootstrap_video.py`
> installe tout en local au workspace, après avoir **annoncé les tailles** et obtenu
> **une confirmation globale**. Ce doc décrit l'amorçage et les spécificités par OS.
> Chronos : **mesurés** en conteneur Linux ; **à mesurer en session locale (~5 min)**
> sur Windows/macOS.

## Amorçage (tous OS)
```bash
python3 scripts/bootstrap_video.py --check                       # détection, aucun DL
python3 scripts/bootstrap_video.py --plan ffmpeg,whisper         # annonce les tailles
python3 scripts/bootstrap_video.py --install ffmpeg,whisper --yes --whisper-model small
python3 scripts/bootstrap_video.py --transcription scribe --yes  # OU mode 100 % distant
```
- **ffmpeg** : `ffmpeg-static` + `@ffprobe-installer/ffprobe` (npm, binaires depuis
  github) ; **repli** `imageio-ffmpeg` (wheel PyPI) si github est bloqué.
- **Transcription** : `faster-whisper` (local, modèle téléchargé au 1er usage) **ou**
  `scribe` (MCP ElevenLabs, distant, payant). Choix mémorisé dans
  `rapido-kb/outils-locaux.md`.
- Binaires **appelés en sous-processus** → licences ffmpeg OK commercial
  (`DECISION-LICENCES-VIDEO.md`).

## Conteneur Linux — **MESURÉ** (2026-07-15, indicatif)
- OS : Linux x86_64 · node 22 · Python 3.11 · pip · npm/npx présents.
- **Découverte réseau** : npm/PyPI/HuggingFace **OK** ; **assets github (releases)
  = 403** (politique proxy). → `ffmpeg-static` échoue ; **`imageio-ffmpeg` (PyPI)
  réussit** (ffmpeg 7.0.2 statique). Le bootstrap bascule automatiquement.
- ffprobe : absent du repli PyPI → probing via `ffmpeg -i`.
- **Chronos e2e** (concat+xfade+burn-in+9:16 sur clips 3 s) :
  install ffmpeg ~2,6 s · whisper tiny 1er chargement ~5 s · xfade 0,36 s ·
  burn-in 0,77 s · 9:16 2,33 s · transcription tiny 0,56 s. Sortie 1080×1920 valide.

## Windows (PowerShell) — **THÉORIQUE, à mesurer en session locale**
- **Node/Python** : `winget install OpenJS.NodeJS.LTS` et `winget install Python.Python.3.12`
  (ou déjà présents). Le bootstrap n'a besoin **que de node+python** ; il installe
  ffmpeg/whisper lui-même — **aucun `winget install ffmpeg` requis**.
- **ffmpeg** : `ffmpeg-static` pose un `ffmpeg.exe` sous
  `.video-tools\node_modules\ffmpeg-static\ffmpeg.exe` ; repli
  `imageio-ffmpeg` → `...\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-*.exe`.
- **Pièges Windows** (théoriques) : chemins avec espaces → **toujours quoter** ;
  `MAX_PATH` 260 caractères (activer *long paths* si node_modules profond) ;
  antivirus/SmartScreen peut bloquer un `.exe` fraîchement téléchargé (autoriser) ;
  filtres ffmpeg avec `:` et `,` → attention au **quoting PowerShell** (préférer des
  fichiers d'args ou l'appel via le script Python) ; libass a besoin des polices
  système (OK par défaut).
- **Chronos** : **à mesurer en session locale (~5 min)** — l'exécution disque/CPU
  Windows diffère du conteneur ; ne pas transposer les chiffres Linux.

## macOS — **THÉORIQUE**
- Node/Python via `brew` ou déjà présents. Bootstrap identique.
- ffmpeg : `imageio-ffmpeg` fournit un binaire macOS (arm64/x86_64) ; sur Apple
  Silicon, vérifier l'arch du wheel. Gatekeeper peut demander d'autoriser le binaire.
- **Chronos** : à mesurer en session locale.

## Mode secours 100 % distant (aucune exécution locale)
Si l'environnement interdit toute exécution locale : basculer en **MCP distant** —
**Higgsfield** (`reframe`, `upscale_video`, `shorts_studio`, `explainer_video`) pour
le montage/génératif, **ElevenLabs Scribe** pour les sous-titres. `bootstrap_video.py
--transcription scribe` mémorise ce choix ; aucun binaire local requis.
