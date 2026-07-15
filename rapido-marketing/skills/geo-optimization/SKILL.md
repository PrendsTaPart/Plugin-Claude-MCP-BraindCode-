---
name: geo-optimization
description: Utiliser quand l'utilisateur parle de GEO, veut être cité par ChatGPT/Claude/Perplexity/AI Overviews, ou d'optimisation pour les moteurs génératifs. Audite un contenu contre une checklist GEO déterministe (script), propose les corrections, et met à jour le contenu via les outils CMS après confirmation.
---

# GEO Optimization — être cité par les moteurs génératifs

> **Sourcé** de `docs/methodo/etat-de-lart-2026.md` §8 (pratiques 2025-2026,
> sources datées). Complète le skill `generation-article-blog` (rapidocms) qui a
> déjà E-E-A-T/GEO — ici on **audite et corrige** contre une checklist mesurable.

## Étape 0 — Charger (obligatoire)
- `docs/methodo/etat-de-lart-2026.md` (§8 GEO) et
  `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-marketing.md`.
- `./rapido-kb/charte-graphique.md` + `ton-et-accroches.md` (le contenu corrigé
  reste conforme à la marque).

## La checklist GEO (mesurée par script)
Critères tirés de l'état de l'art (2025-2026) :
1. **Réponse directe** dans les 40-60 premiers mots.
2. **Densité de faits** : une statistique toutes les ~150-200 mots.
3. **Sources autoritaires** citées (liens).
4. **Schema markup** présent.
5. **Ancres `id`** sur les blocs (citations précises par les IA).
6. **Blocs FAQ / définition** (formats extraits par les moteurs).
7. **Auteur** présent (autorité E-E-A-T).
8. **Style déclaratif** (supprimer « je pense », « à mon avis » → baisse la
   perplexité, hausse la citabilité).
9. **Fraîcheur** (mise à jour récente favorisée).

## Méthode

1. **Auditer** un contenu existant (ou un brouillon `generation-article-blog`) :
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/geo-optimization/scripts/audit_geo.py"`
   avec `{"contenu": "<markdown>", "meta": {date_maj, date_reference, auteur,
   schema}}` → **score GEO** + critère par critère (ok/detail) + liste des
   corrections. Le modèle ne score **jamais** de tête.
2. **Proposer les corrections** ciblées (par critère échoué) : ajouter la
   réponse en 40-60 mots, densifier les stats sourcées, poser des ancres, ajouter
   un bloc FAQ/définition, retirer les tournures subjectives, dater.
3. **Mettre à jour le contenu via les outils CMS APRÈS confirmation** : le
   contenu se (re)génère via le skill `generation-article-blog`, le brouillon se
   met à jour via `create_draft_tool`/`edit_draft_tool` (rapidocms) — publication
   **confirmée**.
4. **Nuances par moteur** (état de l'art) : ChatGPT = encyclopédique, Perplexity
   = récence, AI Overviews = contenu déjà bien classé — adapter l'angle.

## Livrable type
Rapport d'audit GEO (score + critères + corrections priorisées) et, après
accord, le contenu corrigé prêt à publier.

## Cas d'usage croisés
- Produire le contenu à optimiser → skill `generation-article-blog`.
- Conformité à la marque du contenu corrigé → skill `contenu-conforme-marque`.
- Angle éditorial / calendrier → skill `calendrier-editorial`.

## Anti-collision avec `rapido-seo:recherche-mots-cles`
Ce skill = optimisation pour **moteurs GÉNÉRATIFS** (être cité/repris par les
réponses LLM — GEO). **`rapido-seo:recherche-mots-cles`** = **search classique**
(volumes Google, difficulté, SERP, contenu). Un besoin « être cité par ChatGPT » →
ici ; « me positionner sur Google » → rapido-seo. Règle miroir des deux côtés.

## Garde-fous
Score **par script** (checklist déterministe), jamais de tête ; chiffres et
sources **réels** (pas de stat inventée pour « densifier ») ; mise à jour du
contenu et publication **confirmées** ; conforme à la charte.
