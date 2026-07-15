# NOTICE — rapido-video

Le plugin `rapido-video` est **100 % libre** : il pilote **ffmpeg** et **Whisper**
(via `faster-whisper`), tous deux appelés **en sous-processus** (usage-outil, pas de
code lié) — **embarquable en SaaS sans contrainte de licence** (voir
`docs/DECISION-LICENCES-VIDEO.md`).

## Patterns repris (licences MIT — mention obligatoire)
- **`auto-video-edit`** (MIT) — pattern de **suppression des silences** (détection
  `silencedetect` puis coupe des segments). Reformulé/réimplémenté en Python+ffmpeg ;
  aucun code copié verbatim.
- **`jianshuo/claude-skills`** (MIT) — inspirations de structuration des recettes de
  montage. Reformulé.

> Obligation MIT : conserver la mention de copyright et le texte de licence des
> projets d'origine si leur code est réutilisé. Ici, seuls des **patterns** (idées,
> pas de code) sont repris — cette NOTICE tient lieu de mention. Avant toute
> réutilisation de code, joindre le texte MIT et le titulaire du copyright exacts.

## Outils appelés (non redistribués par ce dépôt)
- **ffmpeg** (GPL/LGPL selon build) — installé localement par l'agent
  (`scripts/bootstrap_video.py`), appelé en sous-processus.
- **faster-whisper** (MIT) + modèles Whisper (MIT, OpenAI) — installés à la demande.
