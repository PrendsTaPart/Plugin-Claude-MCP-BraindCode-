# rapido-video

Montage vidéo **100 % libre** (ffmpeg + Whisper) : le couteau suisse **zéro crédit**,
**embarquable en SaaS sans contrainte** de licence (binaires appelés en sous-processus,
voir `NOTICE.md` et `docs/DECISION-LICENCES-VIDEO.md`).

> **Prérequis utilisateur : AUCUN.** `marketplace add` + `install` + MCP connectés.
> Les dépendances (ffmpeg, Whisper) sont **auto-installées en local au workspace et
> confirmées à la première utilisation** (`scripts/bootstrap_video.py`) — rien à
> installer à la main.

## Les 3 étages
| Étage | Skill / mécanisme | Licence |
|---|---|---|
| **1. Montage** (libre) | `montage-express` — concat · coupes · xfade · overlay logo · reframe 9:16/1:1/16:9 · carton titre · vitesse · mix voix/musique (sidechain) · suppression des silences · sous-titres Whisper→SRT→burn-in · presets plateforme | **ffmpeg (GPL/LGPL) + Whisper (MIT)** en sous-processus → **embarquable SaaS sans contrainte** |
| **2. Motion design** | `motion-design-remotion` — 5 gabarits de marque (intro/outro/lower-third/title-card/stat-bar) | **Remotion** : gratuit ≤ 3 employés ; au-delà = Company. **Mode aperçu non commercial tant que la licence n'est pas tranchée** |
| **3. Auto-bootstrap** | `scripts/bootstrap_video.py` — installe ffmpeg/Whisper (et Remotion sur demande) en local, **annonce + confirme** les tailles | binaires appelés en sous-processus |

### Tableau licences (résumé — détail `docs/DECISION-LICENCES-VIDEO.md`)
| Composant | Licence | Usage commercial |
|---|---|---|
| ffmpeg (sous-processus) | GPL/LGPL | ✅ (agrégation, pas de code lié) |
| Whisper / faster-whisper | MIT | ✅ |
| Remotion | Remotion License | ✅ ≤ 3 empl. ; sinon Company (Creators 25 $/siège, Automators ~100 $/mois) |
| OpenMontage (optionnel) | **AGPL-3.0** | outil séparé seult (jamais fusionné, clause réseau SaaS) |

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
