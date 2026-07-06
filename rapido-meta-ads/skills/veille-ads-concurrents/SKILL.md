---
name: veille-ads-concurrents
description: Utiliser quand l'utilisateur demande ce que font ses concurrents en pub ou une veille publicitaire. Recherche leurs pubs actives dans l'Ad Library, synthétise les angles et offres, enrichit concurrents.md et propose des contre-angles.
---

# Veille publicitaire concurrents (KB × Meta)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`. KB :
`concurrents.md` (la liste de départ) — si absente, demander les 2-3
concurrents principaux (et proposer l'onboarding).

## Workflow

1. **Lire la KB** — `./rapido-kb/concurrents.md` : concurrents, leur
   positionnement, nos parades actuelles.
2. **Rechercher leurs pubs** — `ads_library_search` (Ad Library publique) :
   par nom de page et/ou mots-clés du secteur, pays FR. Itérer par concurrent.
3. **Synthétiser** — par concurrent : ANGLES utilisés (prix, qualité,
   nouveauté, preuve sociale), OFFRES mises en avant (promos, menus,
   garanties), FORMATS actifs (image/vidéo/carrousel), volume apparent de
   pubs actives. Constats factuels — l'Ad Library ne donne ni budgets ni
   performances : ne pas extrapoler.
4. **Enrichir concurrents.md — AVEC ACCORD** — proposer la mise à jour via le
   skill `mise-a-jour-kb` (plugin rapido-suite) ou l'édition directe :
   section « Publicité » par concurrent (angles, offres, formats, date de la
   veille). Rien n'est écrit dans la KB sans accord.
5. **Contre-angles** — 2-3 idées de créatifs qui prennent le contre-pied
   (leur angle prix → notre angle qualité sourcée par `propositions-valeur.md`),
   à brancher sur `creatifs-publicitaires`. Jamais de copie d'un créatif
   concurrent, jamais de dénigrement nominatif dans une pub.

## Garde-fous

- Ad Library = données publiques Meta ; pas de scraping au-delà de l'outil.
- Différencier constat (« ils poussent une offre à -30 % ») et hypothèse
  (« ça doit marcher ») — l'hypothèse est marquée comme telle.
- Refaire la veille à cadence raisonnable (mensuelle) — la dater dans la KB.
