# Pièges ElevenLabs (à compléter et figer en E0)

> Relevés du document d'architecture + doc officielle. Les points marqués
> **[E0]** seront confirmés/complétés par l'audit live (`docs/AUDIT-MCP-ELEVENLABS.md`,
> `docs/GRILLE-COUTS-ELEVENLABS.md`) — noms d'outils exacts, coûts réels, termes.

1. **Tout consomme des crédits.** `check_subscription` **avant** toute session de
   production (crédits restants, plan). Une boucle de régénération peut manger
   l'allocation mensuelle en une après-midi. → garde-couts (marqueur `cout_confirme`).
2. **Sorties fichiers sur `~/Desktop` par défaut.** Définir
   **`ELEVENLABS_MCP_BASE_PATH`** vers le dossier de travail du projet (et
   `ELEVENLABS_MCP_OUTPUT_MODE`). Sinon les audios se perdent hors du projet.
3. **Voice design et isolation audio sont LENTS.** Les timeouts de l'inspecteur en
   dev sont de **faux échecs** — l'opération aboutit côté ElevenLabs. Prévenir,
   ne pas conclure à l'échec ni relancer (double coût).
4. **`make_outbound_call` exige un numéro provisionné** sur le compte ElevenLabs —
   vérifier avec `list_phone_numbers`. L'outil **apparaît dans la liste même sans
   numéro** : sa présence ne garantit pas qu'un appel partira.
5. **Clonage : consentement écrit obligatoire** (ToS ElevenLabs — la plateforme
   peut bannir). Notre hook `garde-voix` force la confirmation ; le chemin du
   document de consentement se consigne dans la fiche voix (`identite-vocale.md`).
6. **Windows** : Developer Mode requis pour Claude Desktop ; **Claude Code CLI
   passe sans**. (Ce dépôt tourne aussi en conteneur Linux — le connecteur est
   câblé au niveau de l'environnement.)
7. **Termes d'usage commercial de la musique/SFX générés** : dépendent du plan —
   **à vérifier en [E0]** (source officielle) avant d'alimenter
   `musiques-autorisees.md` de `rapido-video`.

## Relevés E0 (à remplir)
- [E0] Noms + signatures exacts des outils exposés (TTS, Scribe, voice design,
  clonage, SFX, agents, appels) → `docs/AUDIT-MCP-ELEVENLABS.md`.
- [E0] Écarts officiel vs communautaire (`wynandw87` : `generate_music`,
  `speech_to_speech`) → recommandation {officiel seul | + communautaire | + SDK}.
- [E0] Grille de coûts réels (TTS Flash vs Multilingual v2, Scribe 60 s, 1 SFX,
  1 voice design, doublage 30 s **vs** doublage Higgsfield H0).
- [E0] Verdict droits commerciaux musique/SFX → `musiques-autorisees.md`.
