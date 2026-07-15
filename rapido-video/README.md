# rapido-video

Montage vidéo **100 % libre** (ffmpeg + Whisper) : le couteau suisse **zéro crédit**,
**embarquable en SaaS sans contrainte** de licence (binaires appelés en sous-processus,
voir `NOTICE.md` et `docs/DECISION-LICENCES-VIDEO.md`).

> **Prérequis utilisateur : AUCUN.** `marketplace add` + `install` + MCP connectés.
> Les dépendances (ffmpeg, Whisper) sont **auto-installées en local au workspace et
> confirmées à la première utilisation** (`scripts/bootstrap_video.py`) — rien à
> installer à la main.

## Skill
| Skill | Rôle |
|---|---|
| `montage-express` | concat · coupes · xfade · overlay logo · reframe 9:16/1:1/16:9 (crop/blur) · vitesse · extraction audio · mix voix/musique (sidechain) · suppression des silences · sous-titres Whisper→SRT→burn-in · presets plateforme |

## Scripts (recettes — le modèle n'écrit jamais ffmpeg de tête)
- `skills/montage-express/scripts/monter.py` — wrapper ffmpeg (13 recettes).
- `skills/montage-express/scripts/sous_titres.py` — Whisper local → SRT corrigible → burn-in.

## Socle
`reference/pieges-montage.md` (par OS, chemins via `rapido-kb/outils-locaux.md` +
`pathlib`) · `reference/garde-fous-video.md` (musique = droits, providers = env
vérifiées & clés jamais dans le dépôt, pas de publication directe).

## Sourcing & sortie
Médias **locaux**, **RapidoCMS** (`list_all_files`) ou **rendus Higgsfield**
(`show_generations`). Sortie : preset plateforme, nommage `{marque}-{contenu}-{format}-vN`,
rapatriement CMS (`upload_file_tool`) + brouillon proposé — **jamais de publication directe**.

## Garanties
Zéro crédit · musique/médias **avec droits uniquement** · dépendances **auto-installées
et confirmées** · providers externes **env vérifiées, clés jamais en clair/dans le dépôt**
· temps de rendu **selon l'environnement**.
