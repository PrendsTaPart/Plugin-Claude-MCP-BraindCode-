# Audit montage vidéo — OpenMontage, Remotion, chaîne locale

> 2026-07-15. Audit **lecture + tests réels** (conteneur Linux). Aucune création de
> skill. Compagnons : `DECISION-LICENCES-VIDEO.md`, `ENV-VIDEO.md`. **STOP validation.**

## 1. OpenMontage — 12 pipelines (AGPL-3.0, cloné en dossier frère)
Système **instruction-driven** : l'agent lit un manifeste YAML (`pipeline_defs/`) +
des skills « director » par étape, et pilote des **tools** (transcriber, subtitle_gen,
video_compose, tts_selector, lip_sync, audio_mixer…) qui appellent des **providers**.

| Pipeline | Usage | Entrées → sorties | Providers requis | Offline ? |
|---|---|---|---|---|
| `animated-explainer` (prod) | explainer généré depuis un sujet | idée → narration+visuels+musique → MP4 | image+vidéo+TTS+musique (FAL/Google/ElevenLabs…) | ❌ (génératif) |
| `animation` (prod) | motion-graphics / typo cinétique | script → anim → MP4 | Remotion/ffmpeg (+ image gen optionnelle) | ~partiel |
| `cinematic` (prod) | trailer / brand film | brief → montage mood → MP4 | vidéo gen + stock + musique | ❌ |
| `screen-demo` (prod) | captures d'écran / walkthrough | enregistrement → montage | ffmpeg (+ TTS optionnel) | ✅ (montage) |
| `hybrid` (prod) | footage + visuels de support | footage → montage+overlays | ffmpeg + gen optionnelle | ~partiel |
| `avatar-spokesperson` (prod) | présentateur avatar / lip-sync | script → avatar parlant | HeyGen/Kling + TTS + lip_sync | ❌ |
| `talking-head` (beta) | vidéos de speaker (footage) | footage parlant → montage | ffmpeg + transcriber (+ lip_sync opt.) | ~partiel |
| `clip-factory` (beta) | N shorts depuis 1 source longue | webinar/stream → N clips 9:16 sous-titrés | transcriber + ffmpeg (+ audio_enhance) | ✅ (montage) |
| `podcast-repurpose` (beta) | dérivés depuis un podcast | audio/vidéo → highlights | transcriber + ffmpeg | ✅ (montage) |
| `documentary-montage` (beta) | montage thématique retrieval-first | corpus réel → montage | stock (Pexels/Pixabay) + ffmpeg | ~partiel |
| `character-animation` (beta) | perso cartoon riggé réutilisable | perso → acting animé | rig local / gen | ~partiel |
| `localization-dub` (beta) | sous-titres + doublage + variantes | vidéo source → variantes langues | transcriber + TTS + lip_sync opt. | ~partiel (sous-titres ✅, dub ❌) |
| *(framework-smoke = test 2 étapes, non compté)* | | | | |

**Recouvrement avec nos besoins** : `clip-factory` ↔ notre `clips-et-shorts` ;
`localization-dub` ↔ `voix-et-doublage` ; `animated-explainer`/`animation` ↔
`videos-explicatives` ; `avatar-spokesperson`/`talking-head` ↔ HeyGen/Higgsfield.
**Exigent des clés API externes** (payantes) : tous les pipelines **génératifs**
(FAL, Kling, Higgsfield, ElevenLabs, HeyGen, Google, OpenAI, Runway…). **Montage
pur** (`clip-factory`, `podcast-repurpose`, `screen-demo`, sous-titres de
`localization-dub`) tourne **offline** avec ffmpeg + Whisper.

**Verdict OpenMontage** : puissant mais **lourd en dépendances payantes + AGPL** →
**OPTIONNEL avancé**, jamais un socle. Réutiliser ses **idées de pipeline** (nos
skills couvrent déjà l'essentiel), pas son code.

## 2. Skills Remotion officiels (`remotion-dev/skills`, cloné)
8 groupes : `remotion-create`, `remotion-render`, `remotion-captions`,
`remotion-best-practices`, `remotion-interactivity`, `remotion-markup`,
`remotion-saas`, `mediabunny` — déclinés en dizaines de sous-skills utiles au
montage : `transitions`, `voiceover`, `captions`/`silence-detection`, `sequencing`,
`trimming`, `audio-visualization`, `gif`, `sfx`, `3d`, `calculate-metadata`…
Installation prévue : `npx skills add remotion-dev/skills` (npm). **Rendu** =
Chromium headless **auto-téléchargé par Remotion (~400 Mo) — confirmer avant**, et
**susceptible d'être bloqué** par le proxy (téléchargement type github, voir §4).
Licence : voir `DECISION-LICENCES-VIDEO.md` (gratuit ≤ 3 employés).

## 3. Chaîne locale — testée de bout en bout (conteneur Linux, indicatif)
`concat + xfade + transcription FR + sous-titres burn-in + 9:16`, **réussie** :
| Étape | Outil | Chrono (Linux, indicatif) |
|---|---|---|
| install ffmpeg (wheel PyPI) | `imageio-ffmpeg` | ~2,6 s |
| install faster-whisper + modèle tiny | pip + HF | ~5 s (1er usage) |
| xfade + acrossfade | ffmpeg | 0,36 s |
| burn-in sous-titres (libass) | ffmpeg | 0,77 s |
| recadrage 9:16 (1080×1920) | ffmpeg | 2,33 s |
| transcription (tiny, clip 3 s) | faster-whisper | 0,56 s |
Sortie : `final_9x16.mp4` 1080×1920, h264+aac, sous-titres incrustés. Chronos
**non transposables tels quels** à Windows/macOS — voir `ENV-VIDEO.md`.

## 4. Découverte réseau (importante pour la distribution)
- Registres **npm / PyPI / HuggingFace** : **accessibles**.
- **Téléchargements d'assets github (releases)** : **403 (politique org du proxy)**
  → `ffmpeg-static` (binaire depuis github) **échoue ici**. **Repli robuste** :
  `imageio-ffmpeg` (binaire **embarqué dans le wheel PyPI**) → **fonctionne**. Le
  bootstrap encode ce repli automatiquement. (Chromium de Remotion pourrait subir le
  même blocage → à vérifier en session locale.)

## 5. Modèle de distribution — ZÉRO installation utilisateur
- **Prérequis utilisateur : AUCUN.** `marketplace add` → `install` → connecter les
  MCP. Rien d'autre à installer à la main.
- **Tout le reste = auto-bootstrap confirmé** : `scripts/bootstrap_video.py` détecte,
  **annonce les tailles**, demande **UNE confirmation globale**, installe **en local
  au workspace** (ffmpeg via wheel PyPI ; faster-whisper via pip). Chemins écrits dans
  `rapido-kb/outils-locaux.md` (KB client, gitignoré).
- **Mode secours 100 % MCP distant** (si l'environnement interdit toute exécution
  locale) : **Higgsfield** (`reframe`, `upscale_video`, `shorts_studio`, `explainer_video`)
  pour le montage génératif, et **ElevenLabs Scribe** (MCP) pour les sous-titres —
  aucune dépendance locale requise.

## GO / NO-GO par étage
| Étage | Verdict | Note |
|---|---|---|
| Montage ffmpeg (concat/xfade/burn-in/9:16/upscale) | ✅ **GO** | testé e2e ; repli PyPI anti github-403 |
| Transcription locale (faster-whisper) | ✅ **GO** | HF accessible ; modèle confirmé avant (poids annoncé) |
| Transcription distante (Scribe MCP) | ✅ **GO** | mode zéro-local, payant |
| Remotion (compositions React) | ⚠️ **GO conditionnel** | licence si >3 empl. + Chromium ~400 Mo (confirmer, risque proxy) |
| OpenMontage (pipelines complets) | ⛔ **NO-GO comme socle** | AGPL + providers payants → **optionnel avancé** seulement |
| Mode 100 % MCP distant | ✅ **GO** | Higgsfield + Scribe, aucune install locale |
