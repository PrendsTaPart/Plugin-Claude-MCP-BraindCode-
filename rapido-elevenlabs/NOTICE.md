# NOTICE — rapido-elevenlabs

Ce plugin **orchestre** le serveur MCP officiel **ElevenLabs**
(`elevenlabs/elevenlabs-mcp`, **licence MIT**) — il ne le redistribue pas : le
serveur est installé localement par l'utilisateur (`uvx elevenlabs-mcp`), la clé
API reste **en variable d'environnement**, jamais dans ce dépôt.

## Composants tiers (non redistribués)

| Composant | Licence | Usage |
|---|---|---|
| `elevenlabs/elevenlabs-mcp` (MCP officiel) | MIT | serveur MCP interactif (TTS, Scribe, voice design, clonage, SFX, agents, appels) |
| SDK Python `elevenlabs` | MIT | scripts de **batch** déterministe (narration de série, coûts maîtrisés) |
| `wynandw87/claude-code-elevenlabs-mcp` (communautaire, optionnel) | à vérifier en E0 | complément éventuel (`generate_music`, `speech_to_speech`) — périmètre tranché en E0 |

> Le service **ElevenLabs** lui-même est payant (crédits) et soumis à ses **ToS**
> (consentement écrit obligatoire pour le clonage de voix réelles ; termes d'usage
> commercial de la musique/SFX selon le plan — à figer en E0). Ce plugin encode
> ces contraintes dans ses garde-fous, mais ne s'y substitue pas.

## Voix, musique et IP

- Aucune voix clonée sans **consentement écrit archivé** (chemin consigné dans la
  fiche voix). Avatar Mika (HeyGen) : ne pas cloner sans vérifier la licence HeyGen.
- Sound design : **jamais « à la manière de [artiste/morceau] »** — descriptions
  d'ambiance uniquement (cohérent avec la politique anti-IP de `rapido-prompteur`).
