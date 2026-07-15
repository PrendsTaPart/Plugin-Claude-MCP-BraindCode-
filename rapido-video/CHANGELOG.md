# Changelog — plugin rapido-video

## 0.1.0 — 2026-07-15

- Nouveau plugin **rapido-video** (15e du marketplace) — montage 100 % libre.
- Skill **`montage-express`** : couteau suisse ffmpeg + Whisper (concat, coupes,
  xfade, overlay logo, reframe 9:16/1:1/16:9 crop/blur, vitesse, extraction audio,
  mix voix/musique sidechain, suppression des silences, sous-titres burn-in, presets
  plateforme). Recettes **scriptées** — jamais de ffmpeg « de tête ».
- Scripts : `monter.py` (13 recettes ffmpeg, testées e2e) et `sous_titres.py`
  (Whisper local → SRT corrigible → burn-in stylé charte, safe zones 9:16).
- `reference/pieges-montage.md` (par OS, chemins via KB + `pathlib`, **zéro install
  utilisateur — agent auto-installe**) ; `reference/garde-fous-video.md` (musique =
  droits ; **providers externes : env vérifiées AVANT, clés jamais en clair/dans le
  dépôt** [DELTA V3] ; pas de publication directe ; temps de rendu selon l'env).
- **OpenMontage** : proposé en **auto-installation par l'agent** (clone frère 161 Mo,
  confirmation) — jamais requis, jamais dans le dépôt (AGPL) [DELTA V3].
- `NOTICE.md` : patterns MIT (`auto-video-edit` suppression des silences, `jianshuo/
  claude-skills`) — mention obligatoire.
