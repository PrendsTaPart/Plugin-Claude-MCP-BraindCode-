# Pièges du montage (par OS) — rapido-video

> **Zéro installation utilisateur.** L'agent auto-installe ffmpeg + Whisper en local
> au workspace via `scripts/bootstrap_video.py` (annonce des tailles + **une**
> confirmation). **Aucun guide d'installation manuel** : ne jamais demander à
> l'utilisateur d'installer ffmpeg. Chemins lus dans `rapido-kb/outils-locaux.md`,
> résolus via **`pathlib`**, **aucun antislash Windows en dur** — un même skill
> tourne Windows/macOS/Linux sans branche par OS.

## Règle de chemins (tous OS)
- ffmpeg/ffprobe : résolus par `monter.py`/`sous_titres.py` (KB → PATH → wheel PyPI) ;
  ne jamais coder un chemin en dur.
- `ffprobe` peut manquer (repli PyPI `imageio-ffmpeg` = ffmpeg seul) → probing via
  `ffmpeg -i`.
- Le modèle **n'écrit jamais** une commande ffmpeg de tête : il passe par les
  **recettes** de `monter.py`.

## Conteneur Linux — **MESURÉ** (2026-07-15)
- npm/PyPI/HuggingFace OK ; **assets github (releases) = 403 (proxy)** →
  `ffmpeg-static` échoue, **repli `imageio-ffmpeg` (wheel PyPI) réussit** (bascule
  auto). Recettes testées : concat (6,06 s), reframe 9:16 blur (1080×1920), preset
  tiktok, remove-silence, burn-srt — **toutes OK**.

## Windows — **THÉORIQUE** (temps de rendu à mesurer localement)
- L'agent installe ffmpeg/whisper lui-même (rien à faire côté utilisateur). Binaire :
  `ffmpeg.exe` sous `.video-tools\...` ou wheel `imageio_ffmpeg\binaries\`.
- Pièges : chemins avec espaces → passer par les scripts (jamais de commande ffmpeg
  tapée à la main) ; `MAX_PATH` 260 (long paths) ; SmartScreen/antivirus peut bloquer
  un `.exe` neuf ; libass utilise les polices système.

## macOS — **THÉORIQUE**
- `imageio-ffmpeg` fournit un binaire macOS (vérifier arm64/x86_64) ; Gatekeeper peut
  demander une autorisation. Temps de rendu à mesurer localement.

## Secours 100 % distant
Si l'exécution locale est interdite : sous-titres via **ElevenLabs Scribe** (MCP) ;
montage génératif via **Higgsfield** (`reframe`/`upscale`/`shorts`). Aucun binaire local.
