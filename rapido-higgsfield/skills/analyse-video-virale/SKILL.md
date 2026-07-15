---
name: analyse-video-virale
description: Utiliser quand l'utilisateur demande « cette vidéo peut-elle percer », « analyse cette vidéo », « gate viral », ou en invocation par les skills vidéo avant un boost payant. Analyse une vidéo scène par scène (rythme, hook, structure) et prédit son potentiel viral, puis rend un verdict PASS / RETRAVAILLER avec 3 corrections concrètes.
---

# Analyse vidéo virale — le gate avant boost

Le **contrôle qualité** d'une vidéo avant publication/boost : analyse objective +
prédiction de viralité → verdict actionnable.

## Règle (gate, non négociable)
**Aucun boost payant Meta sur une vidéo non passée à ce gate.** Cette règle est
écrite ici **et** appliquée dans `rapido-meta-ads:lancement-campagne-meta` et
`rapido-meta-ads:boost-post-instagram` (patch H6).

## Étape 0 — Charger
- `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-media.md`.
- `gouvernance-credits` si l'analyse consomme des crédits (chiffrer avant).
- `./rapido-kb/marketing/benchmarks.md` (les scores passés priment comme référence).

## Méthode
1. **Analyse scène par scène** : `video_analysis_create` (`video_input_id` d'une
   vidéo uploadée/générée **ou** `youtube_url`) → `video_analysis_status` jusqu'à
   `completed` (3-5 min ; **prévenir** : plus la vidéo est longue, moins l'analyse
   est fiable — les clips courts donnent le meilleur signal). Sortie : rythme, hook,
   structure.
2. **Prédiction de viralité** : `virality_predictor` `action=create` (medias = la
   vidéo) → dashboard (potentiel, hook, rétention, réponse d'audience).
3. **Verdict** : **PASS** ou **RETRAVAILLER** + **3 corrections concrètes**
   (hook plus fort dans les 2 premières secondes, resserrer le rythme, clarifier
   l'appel à l'action…). Un RETRAVAILLER renvoie à `usine-video-marketing` /
   `personnages-univers` pour la reprise.

## Capitalisation
Les scores (hook, rétention, potentiel) alimentent `./rapido-kb/marketing/benchmarks.md`
(daté, source) — pour comparer les prochaines vidéos et objectiver « ce qui marche ».

## Garde-fous
Verdict **argumenté** (jamais « ça a l'air bien ») ; **PASS obligatoire avant tout
boost payant** (gate) ; scores tracés en KB ; analyse chiffrée si elle consomme des
crédits ; aucune publication/boost décidée ici (ce skill **juge**, il ne booste pas).
