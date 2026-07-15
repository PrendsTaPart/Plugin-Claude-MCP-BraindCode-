# rapido-higgsfield

L'**usine média IA** de l'écosystème Rapido, branchée sur le MCP **Higgsfield**
(images 4K & packshots, vidéos génératives & pubs, personnages cohérents
Soul/Elements, voix & doublage, sites & jeux) et pontée avec RapidoCMS (marque,
bibliothèque d'assets), RapidoCRM, RapidoRH et FoodEatUp.

> **Version 1.0.0.** Audit live (H0) + 9 skills + 1 agent + garde-fous et hooks
> coûts/voix. Grille de coûts et signatures : `docs/AUDIT-MCP-HIGGSFIELD.md` +
> `docs/GRILLE-COUTS-HIGGSFIELD.md`.

> **Prérequis utilisateur : AUCUN.** `marketplace add` + `install` + MCP connectés.
> Les dépendances de montage (ffmpeg, transcription) sont **auto-installées en local
> au workspace et confirmées à la première utilisation** (`scripts/bootstrap_video.py`,
> voir `reference/pieges-montage.md` et `docs/ENV-VIDEO.md`) — rien à installer à la main.

## Skills (9) & agent (1)

| Skill / agent | Rôle |
|---|---|
| `gouvernance-credits` | gardien budgétaire (verdict OK/CONFIRMATION/BLOQUÉ par script, get_cost) |
| `studio-image-pro` | images premium brandées (4K, packshot, DTC), pont de marque |
| `usine-video-marketing` | Marketing Studio (pub vidéo/UGC, hooks/ad_reference, 9:16) |
| `personnages-univers` ⭐ | cohérence Soul/Elements, pipeline PronoClip (Kling 3.0) |
| `clips-et-shorts` | Personal Clipper / Shorts Studio / reframe-upscale |
| `analyse-video-virale` | gate : `video_analysis` + `virality_predictor` → PASS/RETRAVAILLER |
| `voix-et-doublage` | TTS, doublage 18 langues, clonage encadré (droits) |
| `videos-explicatives` | montage explainer par blocs (script → clips → voix) |
| `sites-et-jeux-express` | microsites jetables & jeux jouables (croisement concours CRM) |
| **agent `producteur-studio`** | exécutant média : route, chiffre, produit, critique, rapatrie, récap |

## Socle
`reference/routage-media.md` (arbre Canva/CMS/Higgsfield/HyperFrames/Lovable) ·
`pieges-outils.md` (règles des schémas + confirmations H0) · `garde-fous-media.md`
(coûts/voix/marque/publication) · hooks `garde-couts`/`garde-voix`/Stop ·
`kb-templates/budget-media.md`.

## Connecteur requis
Le MCP Higgsfield est **requis** (le plugin existe pour lui), déclaré dans
`.mcp.json` sous le namespace **`huggsfield`** via **`HIGGSFIELD_MCP_URL`**.
Authentification à la charge de l'utilisateur (compte Higgsfield) — **aucune clé ni
secret dans le dépôt** (règle du marketplace).

## Garanties
Tout est **payant en crédits** → `get_cost` préflight + plafond KB + confirmation
au-delà du seuil ; **voix** clonées/doublées uniquement avec droits/consentement ;
**aucune publication directe** (brouillons), créatifs IA vers Meta en
`self_ai_disclosure: OPT_IN`, **gate viral avant tout boost**.
