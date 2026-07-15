# Changelog — plugin rapido-copywriter

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
