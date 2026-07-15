# Changelog — plugin rapido-elevenlabs

## 0.1.1 — 2026-07-15 — Deux modes de connexion + E0 relocalisé

- **README — deux modes de connexion** documentés : (a) **local stdio** (poste, la
  commande `claude mcp add` complète — mode par défaut, celui de l'audit E0-local) ;
  (b) **environnement conteneurisé** — **passerelle HTTP streamable auto-hébergée**
  (`ELEVENLABS_MCP_URL` + token bearer), marquée **optionnelle, à déployer par
  l'équipe infra**, **aucune clé/token dans le dépôt**.
- `docs/PROMPT-E0-LOCAL.md` : le prompt E0 **relocalisé en session locale Windows**
  (stdio `uvx`, plus de connecteur d'environnement), contenu intégral conservé
  (check_subscription, inventaire outils + signatures, grille de coûts, pont
  TTS→`upload_file_tool` CMS) + **livrable ajouté** : le **catalogue des vrais noms
  d'outils** pour `scripts/tester-skills.py` (clé `elevenlabs`) et les matchers exacts
  des hooks.
- `docs/PREREQUIS-E5.md` : les deux prérequis Jarvis — **connecteur Twilio** (URL
  d'environnement à ajouter avant E5) et **numéro provisionné** (décision E0). E2→E6
  en attente d'E0-local.

## 0.1.0 — 2026-07-15 — Squelette (routage audio, garde-fous)

- Nouveau plugin **rapido-elevenlabs** (17e du marketplace) — **la voix de
  l'écosystème** via le MCP officiel `elevenlabs/elevenlabs-mcp` (MIT). Squelette
  E1 : **routage + garde-fous**, aucun appel ElevenLabs (pattern « squelette avant
  audit », comme H1→H0). Skills livrés en **E2+** après l'audit live **E0**.
- **README — Connecteur** : installation `uvx elevenlabs-mcp`, clé **UNIQUEMENT en
  variable d'environnement** (`ELEVENLABS_API_KEY`), `ELEVENLABS_MCP_BASE_PATH`
  **obligatoire** (sinon sorties sur `~/Desktop`) ; stratégie hybride MCP interactif
  + SDK batch ; **mode dégradé** (connecteur/outil absent → message guidé, arrêt
  propre — pattern Fireflies).
- `.mcp.json` : `ElevenLabs` (stdio `uvx`, clé en `${ELEVENLABS_API_KEY}`) + pont `rapidocms`.
- `reference/pieges-elevenlabs.md` : les **7 pièges** (crédits, `BASE_PATH`, lenteur
  voice design/isolation = faux timeouts, numéro provisionné pour les appels,
  consentement clonage, OS, droits musique) + **relevés à figer en E0**.
- `reference/routage-audio.md` : la **branche son** de l'arbre média + **transcription
  3 étages** (Whisper local gratuit / Scribe diarisation / Fireflies réunions) +
  doublage à trancher en E0. Patch parallèle de `routage-media.md` (commit séparé).
- `reference/identite-vocale.md` : **fiche voix** (voice_id, params, usages,
  consentement) — une voix par marque/personnage ; patch `charte-graphique.md`
  (section « Identité vocale », commit séparé).
- **Hooks** : `garde-couts` (génération payante sans `cout_confirme` → confirmation ;
  `check_subscription` d'abord) · `garde-voix` (clonage/voice design → confirmation
  **forcée** + consentement écrit ToS) · `garde-appels` (`make_outbound_call` →
  confirmation **forcée** : numéro, destinataire, script, plage horaire ; jamais de
  prospection à froid) · **`Stop`** (récap fichiers/voice_id/coûts/appels). Tests
  fonctionnels ajoutés au testeur.
- `NOTICE.md` : MIT (elevenlabs-mcp, SDK) ; ToS ElevenLabs ; consentement clonage ;
  anti-IP musique.
