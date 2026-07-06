# Marketplace Rapido — Plugins Claude Code

Marketplace de plugins Claude Code adossés aux serveurs MCP Rapido et
FoodEatUp. Chaque plugin packge des skills métier, des agents (personas), des
références chargées à la demande et des hooks déterministes par-dessus un ou
plusieurs serveurs MCP : les 4 serveurs Rapido (FoodEatUp, RapidoCRM,
RapidoCMS, RapidoRh) et, pour les plugins d'agrégation, Canva, HyperFrames
(HeyGen), Lovable, Meta Ads, n8n et Google (Gmail, Calendar, Drive).

**La promesse : une entreprise pilotée de A à Z — les systèmes Rapido
tiennent les données, Claude pense et crée, n8n exécute en continu, Google
porte la communication.**

## Les 10 plugins

Versions lues depuis `<plugin>/.claude-plugin/plugin.json`, serveurs depuis
`<plugin>/.mcp.json`. **105 skills au total**, dont 40 importés de dépôts
open source (voir « Skills externes & attributions »).

| Plugin | Version | Skills | Description courte | Serveurs MCP requis | Variable d'env |
|---|---|---|---|---|---|
| `foodeatup` | 0.9.0 | 14 | Gestion restaurant : HACCP, salle, recettes & marges, production, réappro, carte en ligne, planning, commandes | foodeatup | — |
| `rapidocrm` | 0.9.0 | 19 | CRM : prospection, pipeline, devis/factures, contrats, RDV, campagnes, communication, performance | rapidocrm | — |
| `rapidocms` | 0.7.0 | 14 | Contenu & réseaux sociaux, campagnes de posts, cartes digitales, vidéos marketing, conformité de marque | rapidocms, hyperframes | — |
| `rapidorh` | 0.7.1 | 11 | RH & projets : Kanban, dailies, onboarding employés, revues projet, charge d'équipe | rapidorh | — |
| `rapido-suite` | 0.13.0 | 10 | Orchestration : onboarding client 360°, revue business, CODIR, base de connaissance `./rapido-kb/` | rapidocrm, rapidocms, rapidorh, foodeatup | — |
| `rapido-canva` | 0.5.1 | 7 | Design Canva piloté par les données : menus imprimables, visuels sociaux, supports commerciaux, slides CODIR | canva, foodeatup, rapidocms, rapidocrm, rapidorh | — |
| `rapido-lovable` | 0.4.0 | 8 | Apps et agents IA Lovable : site restaurant, landing pages, agent IA produit, marque synchronisée | lovable, foodeatup, rapidocms, rapidocrm, rapidorh | — |
| `rapido-meta-ads` | 0.3.0 | 13 | **Argent réel (verrouillé)** : campagnes Meta, boosts IG, audiences CRM, pixel, pilotage, A/B tests | facebook-ads, rapidocms, rapidocrm, canva, lovable | — |
| `rapido-n8n` | 0.1.0 | 4 | Automatisations qui tournent sans Claude : usine à workflows, recettes métier, surveillance, mémoire | n8n (instance du client), foodeatup, rapidocms, rapidocrm, rapidorh | `N8N_MCP_URL` |
| `rapido-direction` | 0.1.0 | 5 | Chef de cabinet : journée du dirigeant, tri de boîte mail en brouillons, secrétariat, coffre Drive | gmail, google-calendar, google-drive (OAuth individuel), rapidocrm, foodeatup, n8n | `N8N_MCP_URL` (volet automatisations) |

## Skills externes & attributions

Une partie des skills est importée de dépôts open source, adaptée aux
conventions Rapido (mentions MCP/KB, renvois vers les skills d'exécution,
renommages anti-collision) :

| Source | Licence | Plugins concernés |
|---|---|---|
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Apache 2.0 | foodeatup, rapidocrm, rapidocms, rapidorh, rapido-suite, rapido-meta-ads |
| [anthropics/skills](https://github.com/anthropics/skills) | Apache 2.0 (LICENSE.txt par skill) | rapido-canva, rapido-lovable, rapido-suite (`skill-creator`) |
| [wondelai/skills](https://github.com/wondelai/skills) | MIT | rapidocms, rapidocrm, rapido-meta-ads |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT | rapido-lovable |

Règles : chaque skill externe embarque sa LICENSE dans son dossier ; chaque
plugin concerné tient un `ATTRIBUTIONS.md` (provenance, commit, licence,
modifications locales). Les skills basés sur des livres (wondelai) ne sont
pas modifiés. Le skill `skill-creator` (rapido-suite) sert à créer et évaluer
les nouveaux skills maison.

## Prérequis

- **Claude Code installé** (CLI, desktop ou web) — voir
  https://code.claude.com/docs
- **Accès authentifié aux serveurs MCP Rapido** : chaque utilisateur se
  connecte à SON compte (FoodEatUp, RapidoCRM, RapidoCMS, RapidoRh — les URLs
  produit sont dans les `.mcp.json`, l'authentification est individuelle).
- **Variables d'environnement** :
  - `N8N_MCP_URL` — requise pour `rapido-n8n` et pour le volet
    automatisations de `rapido-direction` : URL du serveur MCP de VOTRE
    instance n8n. À exporter AVANT de lancer Claude Code :
    `export N8N_MCP_URL=https://<votre-instance>/mcp-server/http`
    (guide : `rapido-n8n/README-installation.md`). Sans elle, ces plugins
    dégradent proprement et expliquent la configuration.
  - `GITHUB_TOKEN` — uniquement si ce dépôt est privé (mises à jour
    automatiques de la marketplace).
- **Comptes tiers selon les plugins** : Canva, Lovable, Meta Ads et
  HyperFrames s'authentifient via leurs connecteurs ; Google (Gmail,
  Calendar, Drive) via OAuth individuel au premier usage
  (`rapido-direction/README-installation.md`).

## Installation

```
/plugin marketplace add <org>/rapido-plugins
/plugin install foodeatup@rapido
/plugin install rapidocrm@rapido
/plugin install rapidocms@rapido
/plugin install rapidorh@rapido
/plugin install rapido-suite@rapido
/plugin install rapido-canva@rapido
/plugin install rapido-lovable@rapido
/plugin install rapido-meta-ads@rapido
/plugin install rapido-n8n@rapido
/plugin install rapido-direction@rapido
/reload-plugins
```

Remplacer `<org>` par l'organisation GitHub qui héberge ce dépôt. Installer
uniquement les plugins dont vous avez besoin. Test en local avant tout push :
`/plugin marketplace add ./rapido-plugins` depuis le dossier parent du clone,
puis les mêmes `install` et `/reload-plugins`.

Premier lancement recommandé : « apprends à connaître mon entreprise »
(onboarding rapido-suite) — il construit `./rapido-kb/` qui personnalise tous
les autres plugins.

## Dépendances entre plugins

Les 4 plugins de base (`foodeatup`, `rapidocrm`, `rapidocms`, `rapidorh`)
sont autonomes : un seul serveur MCP chacun (plus HyperFrames pour la vidéo
côté rapidocms). Les 6 autres AGRÈGENT plusieurs MCP :

- `rapido-suite` embarque les 4 serveurs Rapido — ses revues (hebdo, CODIR)
  s'enrichissent automatiquement de domaines optionnels si les plugins
  correspondants sont installés : Web/Produits (rapido-lovable), Acquisition
  payante (rapido-meta-ads), Automatisations (rapido-n8n).
- `rapido-canva` et `rapido-lovable` embarquent leur outil de création + les
  4 serveurs Rapido (les designs et les apps sont alimentés par les données
  réelles).
- `rapido-meta-ads` embarque facebook-ads + rapidocms/rapidocrm (audiences,
  posts à booster) + canva/lovable (créatifs, pixel des landings).
- `rapido-n8n` embarque l'instance n8n du client + les 4 serveurs Rapido (les
  workflows appellent les API Rapido en HTTP).
- `rapido-direction` embarque Google (Gmail/Calendar/Drive) + rapidocrm/
  foodeatup (agenda triple, secrétariat) + n8n (délégation du récurrent).

Chaque plugin reste installable SEUL : un MCP optionnel absent déclenche une
dégradation propre (explication + marche à suivre), jamais une erreur brute.
La personnalisation inter-plugins passe par `./rapido-kb/` (voir ci-dessous),
jamais par du couplage de code.

## Base de connaissance entreprise (`./rapido-kb/`)

Le skill `onboarding-entreprise` (rapido-suite) interviewe l'utilisateur et
construit `./rapido-kb/` (8 fichiers markdown : entreprise, produits,
propositions de valeur, personas, charte, ton & accroches, processus
internes, concurrents) dans le **répertoire de travail du client** — jamais
dans les plugins — donc versionnable dans son git et conservée lors des mises
à jour. Tous les skills/agents des 10 plugins la chargent au besoin et **elle
PRIME sur les valeurs par défaut** (seuils, cadences, plafonds pub, fuseau,
devise, arguments) ; sans KB, les skills utilisent les standards du secteur
en le signalant. Mise à jour via `mise-a-jour-kb`.

Chaque plugin embarque en plus un dossier `reference/` (directives, pièges
par outil MCP, chartes) chargé par les skills en « Étape 0 », et les skills
d'analyse délèguent leurs calculs à des scripts Python stdlib embarqués — le
modèle ne calcule jamais de tête.

## Versionner / contribuer

- **Le slug d'un plugin est IMMUABLE une fois publié** (le renommer casse les
  installations) ; pour renommer : nouveau plugin + dépréciation de l'ancien.
- **Incrémenter `version`** dans `<plugin>/.claude-plugin/plugin.json` à
  chaque changement et **tenir le `CHANGELOG.md`** du plugin.
- Toute modification de skill référence des outils MCP existants (noms
  vérifiés sur le serveur) et passe les évals (`tests/evals.md`) avant merge.

## Sécurité

- Un plugin **exécute du code et appelle des outils avec les privilèges du
  compte connecté** : n'installer que depuis cette source de confiance.
- **Hooks déterministes** (indépendants du modèle, testés) : confirmation
  forcée sur les actions destructrices/irréversibles et les dépenses (Meta,
  publication n8n) ; refus pur des patterns interdits (transitions de facture
  hors DGFiP, températures aberrantes, budgets pub au-delà du plafond de la
  KB) ; récapitulatif de fin de tour exigé après toute écriture.
- Jamais de secrets dans les skills ou `reference/` : ils sont distribués
  avec le plugin.

## Portabilité — le dépôt est un PRODUIT

Ce dépôt est distribué à tous les clients Rapido : il ne contient AUCUNE
donnée propre à une entreprise. URLs produit uniquement dans les `.mcp.json`,
`${N8N_MCP_URL}` pour l'instance n8n, OAuth individuel pour Google. TOUTE
personnalisation vit dans `./rapido-kb/` — jamais dans les plugins (voir
`tests/evals.md`, éval 4 « installation vierge »).

## À compléter avant publication

- Les sections `### À COMPLÉTER` des `reference/charte-graphique.md`
  (codes hex, URLs de logo, typographies, ton de voix).
- Vérifier les URLs des serveurs MCP Google (`rapido-direction/.mcp.json`)
  contre la documentation officielle des connecteurs.
