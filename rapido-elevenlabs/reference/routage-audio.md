# Routage audio — la branche « son » de l'écosystème

> Complète l'arbre unique `rapido-higgsfield/reference/routage-media.md` (patché en
> parallèle). Ce fichier tranche : **quel outil pour quel besoin audio ?**

## Arbre de décision audio

| Besoin | Voie | Skill responsable (E2+) |
|---|---|---|
| **Voix off / narration** (post, article, épisode) | **ElevenLabs** TTS | `studio-voix` (E2) |
| **Identité vocale de marque** (une voix par marque) | **ElevenLabs** voice design | `identite-vocale-marque` (E3) |
| **Clonage de voix** (voix propre / consentie) | **ElevenLabs** clonage | `clonage-voix` (E3) |
| **Effets sonores / ambiances / jingle / musique** | **ElevenLabs** SFX/musique (outil retenu en E0) | `sound-design` (E4) |
| **Agent vocal téléphonique** (Jarvis : accueil, résa, rappels) | **ElevenLabs** agents + pont Twilio/n8n | `agent-vocal-jarvis` (E5) |
| **Audio DANS un pipeline vidéo Higgsfield** (voix d'un rendu Higgsfield) | **Higgsfield** `generate_audio` | `rapido-higgsfield:voix-et-doublage` (H7) |
| **Avatar présentateur parlant (Mika)** | **HeyGen** | (HeyGen, hors ElevenLabs) |

## Transcription — 3 étages (règle encodée)

| Cas | Voie | Coût |
|---|---|---|
| Mono-locuteur, ou **budget zéro** (défaut) | **Whisper local** | `rapido-video:montage-express` | gratuit |
| **Multi-locuteurs / 90+ langues / qualité** (interview, podcast) | **Scribe** (diarisation) | `transcription-scribe` (E2) | payant |
| **Réunions live** | **Fireflies** | `rapido-marketing:sales-intelligence-fireflies` | selon plan |

## Doublage — à trancher en E0

Comparer **coût/qualité ElevenLabs `dubbing` vs Higgsfield `dubbing`** (grille E0) ;
la recommandation de routage sera inscrite ici et dans `voix-et-doublage` (H7).

## Règles de tranchage
- **Voix off, narration, clonage, agents vocaux, SFX/musique, jingle** → ElevenLabs.
- **Audio d'un rendu produit DANS Higgsfield** → `generate_audio` Higgsfield (pas
  d'aller-retour inutile).
- **Transcription** : Whisper d'abord (gratuit), Scribe si diarisation/multi-locuteurs,
  Fireflies pour les réunions.
- Un critère ambigu → trancher par le **coût** (grille E0) et la **charte** (voix de
  marque d'abord — cf. `identite-vocale.md`).

> Skills livrés en **E2+** ; en E1 seuls le routage et les garde-fous existent
> (pattern H1). Les noms d'outils exacts sont figés en **E0**.
