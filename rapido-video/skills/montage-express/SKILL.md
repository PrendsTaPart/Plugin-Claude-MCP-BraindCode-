---
name: montage-express
description: Utiliser quand l'utilisateur veut « monter ces clips », « couper cette vidéo », « assembler », « sous-titrer cette vidéo », « passer en 9:16 », « ajouter l'intro/le logo » ou « enlever les silences ». Couteau suisse de montage 100 % libre (ffmpeg + Whisper) : concat, coupes, transitions, reframe, overlay logo, sous-titres burn-in, suppression des silences — zéro crédit, via des recettes scriptées.
---

# Montage express — ffmpeg + Whisper (0 crédit)

Le montage **100 % libre** : rien de génératif, rien de payant. Le modèle **ne tape
jamais** de commande ffmpeg de tête — il appelle les **recettes** de
`scripts/monter.py` et `scripts/sous_titres.py`.

## Étape 0 — Charger, router, amorcer (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/pieges-montage.md` (chemins via KB + `pathlib`,
  par OS) et `garde-fous-video.md` (musique = droits, jamais de clé en clair, pas
  de publication directe).
- **Routage** : besoin de **créer du footage** (générer de la vidéo/des plans) →
  renvoyer à `rapido-higgsfield:usine-video-marketing` / `studio-image-pro` ; **motion
  design** (typo animée, data-viz) → voie V4 (à venir). **Ici** = montage de médias
  **existants**.
- **Amorçage (zéro install utilisateur)** : si ffmpeg/Whisper absents → le script
  d'amorçage du dépôt (scripts/bootstrap_video.py) **annonce les tailles + une
  confirmation** puis installe en local (chemins écrits dans
  `rapido-kb/outils-locaux.md`). **Aucun guide manuel.**
- **OpenMontage absent** (pipelines avancés multi-providers) : **PROPOSER
  l'auto-installation par l'agent** — clone en **dossier frère** (~161 Mo + prérequis),
  **sur confirmation** ; jamais requis, jamais dans le dépôt (AGPL).
- **Voie à provider externe** : **vérifier les variables d'environnement AVANT**
  lancement ; **jamais** de clé demandée en clair ni écrite dans le dépôt.

## 1. Sourcing des médias → manifeste (avant toute action)
- Sources : fichiers **locaux**, **RapidoCMS** (`list_all_files` → téléchargement),
  ou **rendus Higgsfield** (`show_generations` → URLs). Résoudre logo/assets de marque
  via `get_brand` / `list_all_files`.
- **Écrire un manifeste de travail** : liste des fichiers, **durées via ffprobe**
  (`monter.py probe`), formats. Rien ne se coupe avant le manifeste.

## 2. Opérations (chacune = une recette `monter.py`)
- **concat** (normaliser d'abord si formats hétérogènes : `normalize` puis `concat`).
- **coupes** par timecodes (`cut --start --end`).
- **transitions** simples (`xfade`, fondu + acrossfade).
- **overlay logo/watermark** depuis les assets de marque (`overlay-logo --pos --scale`,
  zone de protection = marge respectée).
- **reframe** `9:16`/`1:1`/`16:9` (`reframe --mode crop` intelligent **ou** `blur` fill).
- **vitesse** (`speed --factor`).
- **extraction audio** (`extract-audio`).
- **mix voix/musique** (`mix --music [--sidechain]`) — **musique autorisée seulement**
  (garde-fous §a).
- **suppression des silences** (recette remove-silence de `monter.py` — pattern
  `auto-video-edit` MIT, voir `NOTICE.md`).
- **burn-in de sous-titres** (`monter.py burn-srt` ou `sous_titres.py burn`).

## 3. Sous-titres (`scripts/sous_titres.py`)
- **Whisper local** : `transcribe --language auto|fr|… --model tiny|base|small` → **SRT
  corrigible par l'utilisateur** (le montrer, permettre l'édition avant burn-in).
- **Burn-in stylé charte** : `burn --font --size` (**min ≈ 28 px éq.**) **safe zones
  9:16** : marge **haut 150 px / bas 170 px** (`--margin-v 170`). OU **SRT séparé**
  livré pour les plateformes qui le gèrent (YouTube, LinkedIn).

## 4. Sortie
- **Preset plateforme** choisi (`monter.py preset --platform reels|tiktok|shorts|
  linkedin|youtube`).
- **Nommage** `{marque}-{contenu}-{format}-vN`.
- **Rapatriement CMS** (`upload_file_tool`) + **proposition de brouillon**
  (`rapidocms:pipeline-contenu-social`) — **jamais de publication directe**.

## Garde-fous
Recettes **scriptées** (jamais de ffmpeg de tête) ; **musique = droits** (refus
sinon) ; dépendances **auto-installées + confirmées** ; providers externes = **env
vérifiées, clés jamais en clair/dans le dépôt** ; chemins via KB + `pathlib` ;
**aucune publication directe** ; temps de rendu **selon l'environnement**.
