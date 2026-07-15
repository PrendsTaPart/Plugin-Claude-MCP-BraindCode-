# rapido-elevenlabs

**La voix de l'écosystème.** Voix off & narration, transcription **Scribe**
(diarisation), **identité vocale de marque**, clonage sous consentement, **sound
design & musique autorisée**, et **agents vocaux téléphoniques** (Jarvis, pont
FoodEatUp/Twilio) — via le **MCP officiel ElevenLabs** (`elevenlabs/elevenlabs-mcp`, MIT).

> **Squelette 0.1.0** (routage audio + garde-fous). Les skills (`studio-voix`,
> `transcription-scribe`, `identite-vocale-marque`, `clonage-voix`, `sound-design`,
> `agent-vocal-jarvis`) sont livrés en **E2+**, après l'**audit live E0**
> (`docs/AUDIT-MCP-ELEVENLABS.md`) — pattern « squelette avant audit » (comme H1→H0).

## Connecteur — deux modes de connexion

**Clé UNIQUEMENT en variable d'environnement — jamais dans le dépôt** (règle
marketplace), quel que soit le mode.

### (a) Local stdio — mode par défaut (poste Windows/Mac/Linux)

Le serveur officiel tourne **en local** (`uvx elevenlabs-mcp`). C'est le mode de
l'audit **E0-local** (`docs/PROMPT-E0-LOCAL.md`) et de l'usage sur poste :

```
claude mcp add ElevenLabs \
  -e ELEVENLABS_API_KEY=<ta clé> \
  -e ELEVENLABS_MCP_BASE_PATH=<dossier du projet> \
  -- uvx elevenlabs-mcp
```

- **`ELEVENLABS_API_KEY`** : ta clé (env, jamais commitée). Free tier 10 000 crédits/mois.
- **`ELEVENLABS_MCP_BASE_PATH`** : **obligatoire** → sinon les audios sortent sur
  `~/Desktop` (piège 2). Pointer vers le dossier de travail du projet.
- Prérequis : `uv`/`uvx` installé. Les MCP Rapido (RapidoCMS, CRM…) sont des **URL
  distantes**, donc joignables depuis le poste local (pont TTS→`upload_file_tool` OK).
- Le `.mcp.json` du plugin déclare ce mode (`ElevenLabs` via `uvx`, clé en
  `${ELEVENLABS_API_KEY}`) + le pont `rapidocms`.

### (b) Environnement conteneurisé — passerelle HTTP (optionnelle, infra)

Pour une session **conteneurisée** (pas de `uvx`/stdio local), passer par une
**passerelle HTTP streamable auto-hébergée** devant `elevenlabs-mcp` :

```jsonc
// entrée serveur (niveau environnement, PAS dans le repo) :
"ElevenLabs": { "type": "http", "url": "${ELEVENLABS_MCP_URL}",
                "headers": { "Authorization": "Bearer ${ELEVENLABS_MCP_TOKEN}" } }
```

- **`ELEVENLABS_MCP_URL`** + **`ELEVENLABS_MCP_TOKEN`** en variables d'environnement.
- **À déployer par l'équipe infra** — **optionnel**. **Aucune clé ni token dans le
  dépôt** ; la passerelle détient la clé ElevenLabs côté serveur.

**Stratégie hybride** : MCP officiel pour l'**interactif** (orchestré par les skills)
+ **SDK Python `elevenlabs`** dans des scripts pour le **BATCH déterministe** (ex.
narration d'une série d'épisodes : boucle script → audio, coût chiffré avant).

## Mode dégradé (connecteur/outil absent)

Si le connecteur ElevenLabs n'est pas branché, ou si un outil attendu manque :
**message guidé + arrêt propre** (pattern Fireflies) — indiquer la commande
`claude mcp add` ci-dessus et l'outil manquant, ne rien simuler, ne pas facturer.

## Socle (0.1.0)

| Élément | Rôle |
|---|---|
| `reference/pieges-elevenlabs.md` | Les 7 pièges (crédits, BASE_PATH, lenteur voice design, numéro, consentement, OS, droits musique) + relevés à figer en E0 |
| `reference/routage-audio.md` | La branche « son » de l'arbre média + transcription 3 étages (Whisper/Scribe/Fireflies) |
| `reference/identite-vocale.md` | Fiche voix (voice_id, params, usages, consentement) — une voix par marque/personnage |
| `hooks/` | `garde-couts` (crédits) · `garde-voix` (clonage/design → consentement) · `garde-appels` (appel sortant) · `Stop` (récap audio/voice_id/coûts/appels) |

## Garde-fous

- **Crédits** : toute génération payante sans `cout_confirme` → confirmation (`check_subscription` d'abord).
- **Voix** : clonage/voice design sur voix réelle → confirmation **forcée** + consentement écrit archivé (ToS).
- **Appels** : `make_outbound_call` → confirmation **forcée** (numéro, destinataire, script, plage horaire) ; **jamais de prospection à froid vocale**.
- **Anti-IP** (cohérent prompteur) : jamais « à la manière de [artiste/morceau] » — descriptions d'ambiance uniquement.

## Agent Claude Code

Pas de nouvel agent : `rapido-higgsfield:producteur-studio` étend son périmètre au
son, et `rapido-prompteur:directeur-prompts` apprend la grammaire des scripts voix.
Les « agents IA » de ce plugin sont les **agents vocaux ElevenLabs** eux-mêmes,
créés et gouvernés par le skill `agent-vocal-jarvis` (E5).
