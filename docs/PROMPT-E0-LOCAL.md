# PROMPT E0-local — audit ElevenLabs (session locale Windows)

> **À exécuter dans une session Claude Code sur ton poste Windows**, où le MCP
> officiel ElevenLabs tourne **en stdio** (`uvx elevenlabs-mcp` + clé en env). Pas
> de connecteur d'environnement conteneurisé ici — c'est le mode local (a) du
> plugin. Les MCP Rapido (RapidoCMS, CRM…) sont des **URL distantes**, donc
> joignables depuis le poste local (le pont TTS→CMS fonctionne).
>
> **STOP à la fin** : décisions à valider avant E2+. Copier le bloc ci-dessous.

---

```
Repo Plugin-Claude-MCP-BraindCode- (session LOCALE, poste Windows). Mission : brancher le MCP
officiel ElevenLabs en stdio local et AUDITER. Générations limitées aux tests listés (petits
formats). AUCUNE clé écrite dans un fichier du repo (clé en variable d'environnement).

1. Installe/vérifie en LOCAL : uv/uvx présent, puis
   claude mcp add ElevenLabs -e ELEVENLABS_API_KEY=<clé en env> -e ELEVENLABS_MCP_BASE_PATH=<dossier
   du projet> -- uvx elevenlabs-mcp
   Vérifie la connexion puis check_subscription (crédits restants, plan).

2. Inventorie les outils réellement exposés (noms + signatures EXACTES) → tableau dans
   docs/AUDIT-MCP-ELEVENLABS.md. Note les écarts avec la doc officielle. Compare avec le serveur
   communautaire wynandw87 (generate_music, speech_to_speech) : liste ce que l'officiel ne couvre
   pas et recommande {officiel seul | officiel + communautaire | + SDK scripts}.

3. Grille de coûts réels docs/GRILLE-COUTS-ELEVENLABS.md : TTS 30 s (Flash vs Multilingual v2),
   transcription Scribe 60 s, 1 effet sonore, 1 voice design, et doublage 30 s — COMPARÉ au même
   doublage via Higgsfield (grille H0) → recommandation de routage doublage.

4. Teste le pont : TTS 10 s "Bienvenue chez FoodEatUp" → fichier récupéré (vérifier
   ELEVENLABS_MCP_BASE_PATH) → upload_file_tool RapidoCMS (MCP distant, joignable en local) →
   asset visible. Documente le chemin complet (local → CMS).

5. Vérifie les termes d'usage commercial de la musique/SFX générés selon mon plan (source
   officielle ElevenLabs) → verdict pour musiques-autorisees.md de rapido-video.

6. LIVRABLE SUPPLÉMENTAIRE — le CATALOGUE des noms d'outils réels pour le testeur : à partir de
   l'inventaire (étape 2), fournis le dictionnaire des vrais noms d'outils ElevenLabs
   (mcp__ElevenLabs__<tool>) à ajouter à la clé "elevenlabs" du CATALOGUE de scripts/tester-skills.py,
   afin que les skills E2+ puissent citer ces outils sans WARN. Donne aussi les matchers exacts à
   figer dans rapido-elevenlabs/hooks/hooks.json (garde-couts / garde-voix / garde-appels).

7. Décisions à me soumettre (STOP) : (a) créer des voix de marque dédiées ? (b) provisionner un
   numéro de téléphone ElevenLabs pour Jarvis (coût ?) ou passer par le pont Twilio existant ?
   (c) périmètre du serveur communautaire.
```

---

## Livrables attendus de E0-local

- `docs/AUDIT-MCP-ELEVENLABS.md` — inventaire outils + signatures + écarts.
- `docs/GRILLE-COUTS-ELEVENLABS.md` — coûts réels + comparatif doublage vs Higgsfield.
- **Catalogue des vrais noms d'outils** pour `scripts/tester-skills.py` (clé `elevenlabs`)
  + matchers exacts pour `hooks.json`.
- Verdict droits commerciaux musique/SFX (→ `musiques-autorisees.md`).
- Réponses aux 3 décisions STOP (voix de marque · numéro vs Twilio · serveur communautaire).

> **E2→E6 restent en attente de E0-local.** Une fois le catalogue rapporté, j'ajoute
> la clé `elevenlabs` au testeur puis j'enchaîne les skills (studio-voix, etc.).
