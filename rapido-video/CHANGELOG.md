# Changelog — plugin rapido-video

## 1.0.1 — 2026-07-15 — hooks (garde + récap IDs) — série FINITION F2

- hook PreToolUse `garde-video` sur Bash (ask avant installation lourde ffmpeg/Whisper/Remotion, et confirmation musique = registre autorisé) + hook Stop récap-IDs. Testés au testeur.

## 1.0.0 — 2026-07-15 — RELEASE montage 3 étages

- **Release** : 3 étages — montage libre (`montage-express`), motion design
  (`motion-design-remotion`, mode aperçu sous licence [B] différée), auto-bootstrap
  zéro-install.
- **DELTA V5(d) — test vierge RÉUSSI** : environnement vierge → install → 1re
  invocation → bootstrap (repli imageio-ffmpeg anti github-403) → **montage sans
  action manuelle**. Recette (a) (épisode 9:16 : titre+concat+logo+sous-titres FR)
  **prouvée 0 crédit** (≈ 10,7 s, conteneur Linux mesuré).
- **Recette (a/b/c) réelle** : écarts documentés (`docs/RECETTE-VIDEO.md`) — sources
  réelles (clips Kling, extrait V1, transcript Fireflies) + crédits doublage → à
  exécuter en session locale ; aucune donnée fabriquée.
- Nouvelle recette `title-card` (carton titre via **libass**, `drawtext` absent des
  builds statiques imageio). README plugin : 3 étages + **tableau licences**.
- Chronos étiquetés par environnement (Linux mesuré / Windows à mesurer).

## 0.2.0 — 2026-07-15

- Skill **`motion-design-remotion`** : motion design programmatique (Remotion) aux
  couleurs de la marque.
  - **5 gabarits** `templates/` paramétrés par la charte (hex, police, logo CMS) :
    Intro (logo+tagline), Outro (CTA), LowerThird (nom+fonction), TitleCard, StatBar
    (barre + compteur, stats PronoClip). `Root.tsx` (1080×1920 @ 30 fps), `_shared.tsx`
    (safe zones 150/170/60, polices ≥ 56/36, jamais < 28, sobriété).
  - **Gate licence V0** : si la décision Remotion n'est pas tranchée (ou licence
    entreprise refusée) → **mode « aperçu non commercial »** (bandeau APERÇU, dit
    explicitement, usage commercial/publié interdit) ; gratuit ≤ 3 employés sinon Company.
  - **DELTA V4** : skills Remotion absents → `npx skills add remotion-dev/skills`
    exécuté par l'agent ; projet Remotion créé au workspace (npm i local) ; **Chromium
    headless annoncé + confirmé** avant rendu. Aucun guide manuel.
  - Rendu CLI → MP4 → assemblage `montage-express` → rapatriement CMS ; capitalisation
    `add_prompt` + `rapido-kb/marketing/gabarits-video.md`. 3 évals (dont gate licence).

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
