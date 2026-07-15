---
name: voix-et-doublage
description: Utiliser quand l'utilisateur veut une « voix off », « doubler cette vidéo en anglais », « cloner ma voix », ou « changer la voix ». Voix off TTS, doublage 18 langues (dont la série FoodEatUp), changement de voix et clonage — uniquement sur des voix dont l'utilisateur détient les droits, avec confirmation du consentement.
---

# Voix & doublage (Higgsfield)

Voix off, localisation multilingue et clonage — sur **médias Higgsfield**.
**Droits/consentement obligatoires** sur toute voix clonée/doublée (hook `garde-voix`).

## Routage (à confirmer en tête)
- **Avatar présentateur parlant (Mika)** → HeyGen, pas ici (clonage sans droits interdit).
- **Composition éditoriale** (typo, presets) → HyperFrames.
- **Ici** = voix off / doublage / revoicing sur des vidéos et médias.

## Étape 0 — Charger
- `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-media.md` (§b voix) + `routage-media.md`.
- `gouvernance-credits` (TTS ≈ 0,4 cr ; **dubbing/clone sans préflight** → estimer
  via grille et signaler).

## Chaînes
### Voix off (TTS)
- Choisir une voix (lister les voix disponibles via list_voices, preset ou element)
  → génération audio `seed_audio` (ou `text2speech_v2` variant elevenlabs/minimax…).
  Réglages : format, débit, hauteur.

### Doublage (18 langues)
- `dubbing` (`video_id` + `target_language` ∈ eng, fra, ara, spa, deu, por, jpn,
  kor, hin, ita, rus, tur, pol, ind, fil, swe, fin, cmn) : traduit, resynthétise,
  **relippe** la vidéo. **Cas phare** : localiser la série **FoodEatUp V1-V6**
  fra → eng/ara/spa (marchés touristiques). Coût **à mesurer** (pas de préflight) →
  confirmer avant.

### Changement de voix
- `voice_change` (`video_id` + `voice_id`/`voice_type`) : remplace la voix en
  gardant timing et visuels.

### Clonage (encadré)
- Créer une voix (create_voice / clone depuis un audio confirmé) **UNIQUEMENT** sur
  une voix **propre ou autorisée** (la vôtre, un collaborateur consentant, une
  licence). **Confirmation du consentement dans le flux** ; le hook `garde-voix`
  force la question. Clonage **asynchrone** : réutilisable une fois `status=completed`
  et `is_audio_eligible=true` (revérifier via list_voices, ne pas générer trop tôt).

## Capitalisation
Chaque audio réutilisable → bibliothèque **CMS** (`upload_file_tool`) pour réemploi.

## Garde-fous
Voix clonée/doublée/changée = **droits/consentement confirmés** (hook `garde-voix`) ;
Mika = HeyGen (jamais cloné sans droits) ; coûts non préflightables **signalés comme
estimation** ; aucune diffusion automatique.
