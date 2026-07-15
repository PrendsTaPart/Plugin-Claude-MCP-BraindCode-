---
name: videos-explicatives
description: Utiliser quand l'utilisateur veut une « vidéo explicative », un « tuto vidéo », une « vidéo d'onboarding » ou un « épisode Academy ». Assemble une vidéo pédagogique par blocs (script → clips → voix par bloc → montage explainer avec sous-titres), chiffrée et confirmée avant assemblage.
---

# Vidéos explicatives (Higgsfield)

Vidéo pédagogique **structurée par blocs**, montée sans logiciel. **Coût total
chiffré et confirmé avant l'assemblage.**

## Étape 0 — Charger & router
- `${CLAUDE_PLUGIN_ROOT}/reference/routage-media.md` (explainer animé narré → aussi
  le workflow bundlé `video-explainer` de Higgsfield, à orchestrer) + `garde-fous-media.md`.
- `gouvernance-credits` : **chiffrer le total** (N clips + voix + assemblage) AVANT.

## Pipeline
1. **Script par blocs** : déléguer la **méthode** à `rapidocms:content-creation-methodo`
   (structure, angle, message par bloc). Un bloc = un plan + une prise de voix.
2. **Clips par bloc** : vidéo générée par bloc (voie `usine-video-marketing` /
   `personnages-univers` selon le besoin) ou images animées.
3. **Voix par bloc** : `voix-et-doublage` (TTS `seed_audio`, ou doublage si multilingue).
4. **Assemblage** — **par défaut : local, 0 crédit** via `rapido-video:montage-express`
   (concat des blocs + sous-titres burn-in) + habillage `rapido-video:motion-design-remotion`
   (intro/outro/lower-third ; en **mode aperçu** tant que la licence Remotion n'est pas
   tranchée). Le modèle `explainer_video` Higgsfield n'est utilisé **que si tout est
   génératif** (aucun média réel à assembler) — préflight/chiffrage puis confirmation.
5. **Rapatriement** : `upload_file_tool` (CMS) → brouillon via
   `rapidocms:pipeline-contenu-social` (jamais publié directement).

## Croisements
- **Onboarding RH** : vidéo d'accueil J1 → `rapidorh:onboarding-rh-methodo`.
- **FoodEatUp Academy** : épisodes de formation (série).
- **Synthèse de webinar/RDV** : depuis un transcript Fireflies
  (`fireflies_get_summary`, connecteur optionnel) → script → explainer.

## Garde-fous
**Coût total confirmé avant assemblage** (BLOQUÉ = on n'assemble pas) ; script
délégué à la méthode maison (pas de doublon) ; **aucune publication directe**
(brouillon) ; sous-titres burn-in vérifiés ; voix soumises au consentement
(`voix-et-doublage`).
