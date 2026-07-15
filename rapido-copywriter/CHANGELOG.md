# Changelog — plugin rapido-copywriter

## 0.4.0 — 2026-07-15 — agent copywriter-social + boucle hooks gagnants

- Agent **`copywriter-social`** — directeur de création : du brief au lot de brouillons
  multi-réseaux (délégations aux 4 skills), exigence (2 itérations max, critique
  argumentée), capitalisation. Interdits (publication directe, stats inventées, hooks
  verbatim, contourner les gates, toucher au profil perso). Rapporte à directeur-marketing.
- `scripts/score_hooks.py` (stdlib) — boucle d'apprentissage : `interactions = liked +
  shares + comments` par réseau (les seules métriques CMS exposées), tag **GAGNANT** si
  moyenne du hook > **médiane du réseau**. Aucun score inventé. Vérifié.
- Patchs cross-plugin : `pipeline-contenu-social` (déclinaison multi-réseaux proposée),
  `calendrier-editorial` (grammaires par réseau référencées), `content-creation-methodo`
  (recentré blog/email/landing, social délégué), `social-selling-linkedin` (commentaires
  semi-auto).
- Évals : +2 cas (agent, boucle de scoring).

## 0.3.0 — 2026-07-15 — copy-tiktok + declinaison-multi-reseaux

- Skill **`copy-tiktok`** — le livrable est un **script de tournage** (hook < 3 s,
  hook→boucle→valeur→payoff→CTA, texte à l'écran horodaté, sous-titres, caption + 3-5
  hashtags). Anti-voix-IA sur le **parlé** (ton créateur). Sortie double : génératif
  (`usine-video-marketing` via `directeur-prompts`) ou tournage réel (+ `montage-express`).
  Déclinaison Reels/Shorts proposée ; brouillon CMS TikTok ou export.
- Skill **`declinaison-multi-reseaux`** — 1 idée-noyau → 4 déclinaisons **natives**
  (délégation aux copy-*), lot de brouillons CMS même campagne + calendrier
  (`calendrier-editorial`). Jamais de copier-coller raccourci.
- Évals : 4 cas (script TikTok, déclinaison complète, anti-collision montage, publication).

## 0.2.0 — 2026-07-15 — copy-linkedin + copy-meta

- Skill **`copy-linkedin`** — copy pour les **pages de marque** (frontière stricte vs
  profil perso `social-selling-linkedin`) : brief funnel/cible/preuve réelle → **3
  variantes** (grammaire LinkedIn, hooks piochés GAGNANT d'abord) → passe anti-voix-IA →
  gate `brand-review` → `create_draft_tool` (bon compte) + hooks consignés. Carrousel →
  structure slide par slide + visuel délégué.
- Skill **`copy-meta`** — Facebook + Instagram (grammaires **distinctes**) : post FB
  (40-120 mots, local), caption IG (hook < 125 car., 3-8 hashtags), carrousel IG (6-10
  slides), Reel (caption courte + texte à l'écran → monteur), Stories. Brouillons CMS par
  compte.
- Évals : 4 cas (chaîne, renvoi profil perso, blocage anti-voix-IA, grammaires distinctes).

## 0.1.0 — 2026-07-15 — Squelette (grammaires 4 réseaux)

- Nouveau plugin **rapido-copywriter** (24e du marketplace) — copywriter LinkedIn /
  Facebook / Instagram / TikTok. Squelette : fondations + garde-fous, skills à venir
  (CW2→CW5).
- `.mcp.json` : rapidocms (brouillons + insights), rapidocrm (preuves), foodeatup (contexte).
- `reference/grammaires-reseaux.md` : 4 fiches **datées** (formats, longueurs, structure
  gagnante, hooks, hashtags, signaux algo, erreurs qui tuent la portée) — **à réviser
  trimestriellement** via `rapido-seo:tendances-marche`.
- `reference/banque-hooks.md` : patterns de hooks **par réseau**, francisés/re-dérivés
  (templates à placeholders, jamais de post réel), tag `GAGNANT`/`NEUTRE` (init NEUTRE) +
  compteur d'usage — mis à jour par `score_hooks.py` (CW4).
- `reference/anti-voix-ia.md` : liste noire des **tics LLM français** + règles de
  réécriture + test « fondateur pressé ». `reference/articulations.md` : frontières
  (perso vs marque, funnel, pipeline, gate).
- **Hook** `garde-voix-marque` (ask à la création de brouillon : anti-voix-IA + brand-review
  passés ?) + `Stop` (récap copies/brouillons/hooks/sources). **Aucune publication directe.**
- `NOTICE.md` (4 sources MIT, anti-verbatim strict, sans-licence exclus). Fondé sur
  l'audit **CW0** (`docs/IMPORTS-COPYWRITER.md`) : métriques d'insights réelles
  (liked/shares/views/comments) figées.
