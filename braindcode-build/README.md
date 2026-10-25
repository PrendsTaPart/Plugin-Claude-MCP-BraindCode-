# braindcode-build

**Le chef de chantier BraindCode Build** : Claude Code mène une extension
de bout en bout, comme développeur IA déclaré du projet — choix de l'idée,
cahier des charges sur outils réels, maquettes Figma, construction pas à
pas dans Lovable, MCP produit branché côté serveur, tests et rapport, MCP
de l'extension exposé et validé, déclaration Plan'It, routine et boucle
KPI, plugin publié sur ce dépôt, vitrine, hackathon et demoday. Serveur :
`https://build.braindcode.com/api/mcp` (44 outils relevés, OAuth au
premier appel — aucun jeton dans le dépôt).

## Les cinq critères (le contrat)

1. l'extension **expose son propre serveur MCP** (orchestrable par
   Plan'It) ; 2. elle **publie son plugin** sur la marketplace ;
3. **aucun credential MCP n'atteint le navigateur** (hooks anti-secret et
audit-credentials-front) ; 4. le **rapport de test est obligatoire** ;
5. elle ne vaut que par la **routine qu'elle fait tourner**.

Les validations humaines (OAuth, clé, paiement, **mise en ligne**) passent
par `request_human_validation` puis `get_pending_validations` — le hook
garde-mise-en-ligne REFUSE tout deploy sans validation lue. Les champs
posés par le modèle ne valent jamais confirmation humaine.

## Le parcours complet d'une extension

| Étape | Commande | Ce qui se passe |
|---|---|---|
| Point du jour | `/build` | projets, readiness, validations en attente, kanban |
| Idée | `/idee foodeatup copilote` | 5 idées argumentées, critique honnête, réservation sur accord |
| Démarrage | `/demarrer` | développeur IA déclaré, contexte, journal ouvert |
| Spécification | `/cdc` | outils du MCP produit RELEVÉS (rien supposé), spec enregistrée |
| Design | `/figma` | charte lue, prompts et maquettes, adresses gardées |
| Chantier | `/lovable-nouveau` puis `/etape` ×n | création sur accord (crédits), cartes une à une, pauses à l'humain, diffs relus |
| Connexion | `/brancher-mcp` | modèle officiel, lien tableau de bord, code audité |
| Recette | `/tests` | parcours constaté + 4 cas d'erreur MCP + rapport |
| Exposition | `/mon-mcp` puis `/planit-declarer` | MCP de l'extension validé par une tâche tracée, déclaré dans Plan'It et sur la marketplace |
| Routine | `/routine-projet` | six blocs audités, coût Plan'It annoncé, proposition |
| Livraison | `/plugin-projet`, `/publier`, `/hackathon` | plugin aux normes de ce dépôt, vitrine sur accord, pitch |

Rattrapage des vitrines publiées : `/vitrines` (au relevé du 2026-10-25 :
20 vitrines sans tutoriel, 2 sans démo, Daily Brief en brouillon).
Blocage : `/blocage` — signalé sans secret, chantier qui continue.

## Phrases d'exemple

« Où en sont mes projets Build ? » · « Propose-moi une idée d'extension
RapidoCRM » · « Exécute la prochaine étape du plan » · « Branche le MCP
FoodEatUp dans l'app — côté serveur » · « Fais la recette et le rapport » ·
« Complète les tutoriels des vitrines publiées » · « Inscris le projet au
hackathon » (les dates font foi, pas le statut).

## Interconnexions (délégation, pas de recopie)

`rapido-lovable` (apps et kit connecteur MCP), `rapido-design` (critique
UX), `rapido-prompteur` (prompts Lovable), `rapido-n8n` (automatisations),
`planit` (vie de l'orchestrateur), `rapidocms` / `rapido-prospector`
(promotion de la vitrine) : ce plugin ORCHESTRE le chantier et délègue —
voir reference/carte-des-interconnexions.md. Figma est un serveur MCP de
session (non déclaré ici — précédent rapido-design) ; Academy et Tutoriel
sont optionnels : absents, le volet est sauté en le disant.

## Installation

```
/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
/plugin install braindcode-build@rapido
```

L'authentification Build est l'OAuth du premier appel ; l'Academy
optionnelle lit `${ACADEMY_MCP_TOKEN}` ; aucun secret dans le dépôt.
