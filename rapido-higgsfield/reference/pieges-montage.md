# Pièges du montage local (par OS)

> Le montage local (ffmpeg + transcription) est **auto-amorcé** par
> `scripts/bootstrap_video.py` (zéro installation utilisateur). Les **chemins des
> binaires** sont lus dans `rapido-kb/outils-locaux.md` — **jamais codés en dur**,
> résolus via **`pathlib`**, **aucun antislash Windows en dur**. Détail des chronos
> et de l'install par OS : `docs/ENV-VIDEO.md`.

## Règle de chemins (tous OS)
- Lire `ffmpeg`/`ffprobe` depuis `rapido-kb/outils-locaux.md` (écrit par le bootstrap).
- Construire tout chemin avec `pathlib.Path` (jamais de `\` littéral ni de séparateur
  en dur) — un même skill doit tourner Windows/macOS/Linux sans branche par OS.
- `ffprobe` peut être **absent** (repli PyPI `imageio-ffmpeg` = ffmpeg seul) → faire
  le probing via `ffmpeg -i` dans ce cas.

## Conteneur Linux — **MESURÉ** (2026-07-15)
- npm/PyPI/HuggingFace accessibles ; **assets github (releases) = 403 (proxy)** →
  `ffmpeg-static` (binaire github) **échoue** ; **repli `imageio-ffmpeg` (wheel
  PyPI) réussit** (le bootstrap bascule seul). Chronos e2e (clips 3 s) : xfade
  0,36 s · burn-in 0,77 s · 9:16 2,33 s · transcription tiny 0,56 s.

## Windows (PowerShell) — **THÉORIQUE** (à mesurer en session locale ~5 min)
- Bootstrap n'exige que **node + python** ; il installe ffmpeg/whisper lui-même
  (**aucun `winget install ffmpeg`**). Binaire : `ffmpeg.exe` sous
  `.video-tools\node_modules\ffmpeg-static\` ou wheel `imageio_ffmpeg\binaries\`.
- Pièges : chemins avec espaces → **quoter** (ou passer par le script Python) ;
  `MAX_PATH` 260 → activer *long paths* ; SmartScreen/antivirus peut bloquer un
  `.exe` neuf (autoriser) ; filtres ffmpeg (`:` et `,`) → **quoting PowerShell**
  délicat, préférer l'appel via `bootstrap_video.py`/un fichier d'args.
- **Temps de rendu : à mesurer localement** (varie selon l'environnement) — ne jamais
  transposer les chronos Linux.

## macOS — **THÉORIQUE**
- Node/Python via `brew` ou déjà présents ; bootstrap identique. `imageio-ffmpeg`
  fournit un binaire macOS (vérifier arm64 vs x86_64) ; Gatekeeper peut demander une
  autorisation. **Temps de rendu à mesurer localement.**

## Mode secours 100 % distant
Si l'exécution locale est interdite : bascule MCP distant — **Higgsfield**
(`reframe`/`upscale_video`/`shorts_studio`/`explainer_video`) + **ElevenLabs Scribe**
(sous-titres). Aucun binaire local requis.
