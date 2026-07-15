# NOTICE — rapido-prompteur

Le plugin `rapido-prompteur` **orchestre** la conception de prompts. Ses
`assets/patterns/` sont des **structures de prompt francisées et réécrites**,
inspirées de dépôts open source **sous licence MIT**. **Aucun texte n'est repris
verbatim** : seules des **structures/idées** (non protégeables) ont été distillées,
puis rédigées en français maison (cf. l'audit `docs/IMPORTS-PROMPTEUR.md`).

## Patterns repris (licences MIT — mention obligatoire)

| Source | Licence | Ce qui est repris (structure, pas le texte) |
|---|---|---|
| `wshobson/agents` — © 2024 Seth Hobson | MIT | Charpente du rôle « prompt-engineer » (afficher le prompt complet, format de sortie), brief web |
| `Hao0321/ai-media-generator` — © 2026 contributors | MIT | Taxonomie plateforme→reference→template, anatomie packshot/food/portrait/cinématique |
| `rediumvex/ai-video-generator-claude` — © 2026 Roman Knox | MIT | `description` déclenchable, découpe « format × objectif », budget temporel du hook (UGC, viral) |
| `ZeroLu/awesome-nanobanana-pro` — © 2025 ZeroLu | MIT | Format de fiche (titre + intention + bloc structuré) pour le packshot |
| `KingLeoJr/prompts` — © 2025 KingLeoJr | MIT | Structure « 1 brief = rôle / pages / design / data » (web-apps) |

> **Obligation MIT** : conserver la mention de copyright et le texte de licence
> des projets d'origine **si leur code/texte est réutilisé**. Ici, seuls des
> **patterns** (idées) sont repris — cette NOTICE tient lieu de mention. Avant
> toute réutilisation de **texte**, joindre le texte MIT et le titulaire exact.

## Volontairement EXCLU (non francisé)

- **`contains-studio/agents`** : dépôt **SANS fichier LICENSE** → « tous droits
  réservés » par défaut. Aucun fichier ni texte repris (structure d'agent
  seulement évoquée dans l'audit, jamais copiée).
- **`Hao0321/.../director-style-library.md`** (31 réalisateurs vivants nommés),
  patterns `ZeroLu` référençant des marques/franchises (Victoria's Secret, Star
  Wars, iPhone…), mentions « Apple/iPhone-style », grammaire propriétaire
  Midjourney : **exclus** — IP tierces / artistes vivants (cf.
  `reference/regles-de-construction.md` INTERDITS).

## Moteurs pilotés (non redistribués par ce dépôt)

Higgsfield, RapidoCMS, Lovable, Canva — pilotés via leurs serveurs MCP, dont la
grammaire est **lue en direct** à chaque session (aucune spec figée ici).
