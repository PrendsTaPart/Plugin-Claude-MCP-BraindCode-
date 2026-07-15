# Marketplace Rapido — Plugins Claude Code

Marketplace de **plugins Claude Code** pour les systèmes Rapido (FoodEatUp,
RapidoCRM, RapidoCMS, RapidoRh) et leurs outils satellites (Google Workspace,
Stripe, Canva, Lovable, Meta/Google/TikTok Ads, SEO/DataForSEO, Higgsfield,
ElevenLabs, n8n…) : des **skills métier**, des **agents IA** et des **garde-fous
déterministes** par-dessus vos serveurs **MCP**, plus un **Loop Engine** de
routines récurrentes — pour piloter une entreprise de A à Z.

> **Pour un agent IA qui lit ce dépôt** : chaque plugin est autonome
> (`<plugin>/.claude-plugin/plugin.json`, `.mcp.json`, `skills/*/SKILL.md`,
> `agents/*.md`, `hooks/`). Le catalogue des routines et des KPIs canoniques est
> `reference/registre-routines.md`. Les données du client vivent hors dépôt dans
> `./rapido-kb/` (jamais commitées). Aucun secret n'est stocké dans le dépôt.

![validation](https://github.com/PrendsTaPart/Plugin-Claude-MCP-BraindCode-/actions/workflows/validation.yml/badge.svg)
![Plugins](https://img.shields.io/badge/plugins-24-blue)
![Skills](https://img.shields.io/badge/skills-376-brightgreen)
![Agents](https://img.shields.io/badge/agents-36-orange)
![Licence](https://img.shields.io/badge/licence-Apache%202.0-blue)

**Sommaire** : [À quoi ça sert](#à-quoi-ça-sert) · [Les plugins](#les-plugins) ·
[Domaines couverts](#domaines-couverts) · [Les agents IA](#les-agents-ia) ·
[Les routines (Loop Engine)](#les-routines--le-loop-engine) · [Installation](#installation-5-minutes)
· [Connecter/héberger les MCP](#connecter-ou-héberger-les-serveurs-mcp) ·
[Comment l'utiliser](#comment-lutiliser) · [Architecture](#architecture-dun-plugin)
· [Garde-fous](#garde-fous-intégrés) · [Licence](#licence)

## À quoi ça sert

Vous utilisez FoodEatUp, RapidoCRM, RapidoCMS ou RapidoRh ? Cette
marketplace transforme Claude Code en **équipe de pilotage qui parle à vos
systèmes** : vous dites « mon briefing du matin », « relance mes factures en
retard », « prépare les posts de la semaine », « qui est surchargé dans
l'équipe ? », « lance ma sentinelle trésorerie » — et les skills exécutent
les bons appels sur VOS comptes, avec des garde-fous déterministes
(confirmation avant tout ce qui est destructif, payant ou visible par vos
clients ; jamais de donnée inventée ; calculs par scripts, jamais de tête).

Concrètement, chaque plugin apporte :
- des **skills** (workflows métier prêts à l'emploi, déclenchés par vos
  phrases naturelles),
- des **agents** (personas experts : chef-restaurateur, directeur
  artistique, CFO virtuel, architecte d'automatisations…),
- des **hooks** (garde-fous testés qui s'exécutent indépendamment du
  modèle),
- une personnalisation par **votre base de connaissance `./rapido-kb/`**
  (vos seuils, votre charte, vos personas — jamais stockés dans ce dépôt).

## Les plugins

Chiffres lus depuis les fichiers du dépôt : version dans
`<plugin>/.claude-plugin/plugin.json`, skills = dossiers contenant un
`SKILL.md`, agents = fichiers `agents/*.md`, serveurs depuis
`<plugin>/.mcp.json`.

| Plugin | Version | Skills | Agents | Serveurs MCP requis | Variables d'env |
|---|---|---|---|---|---|
| `foodeatup` | 1.5.1 | 15 | 3 | foodeatup, rapidocrm | — |
| `rapidocrm` | 1.7.0 | 30 | 2 | rapidocrm | — |
| `rapidocms` | 1.11.7 | 22 | 6 | rapidocms, hyperframes | — |
| `rapidorh` | 1.0.3 | 11 | 2 | rapidorh | — |
| `rapido-suite` | 1.4.2 | 13 | 1 | rapidocrm, rapidocms, rapidorh, foodeatup, lovable, facebook-ads, n8n | `N8N_MCP_URL` (optionnel) |
| `rapido-canva` | 1.0.1 | 7 | 1 | canva, foodeatup, rapidocms, rapidocrm, rapidorh | — |
| `rapido-lovable` | 1.5.0 | 10 | 2 | lovable, foodeatup, rapidocms, rapidocrm, rapidorh | — |
| `rapido-meta-ads` | 1.0.5 | 13 | 1 | facebook-ads, rapidocms, rapidocrm, canva, lovable, foodeatup | — |
| `rapido-n8n` | 1.6.0 | 4 | 1 | n8n, foodeatup, rapidocms, rapidocrm, rapidorh | `N8N_MCP_URL` |
| `rapido-direction` | 1.1.0 | 5 | 1 | gmail, google-calendar, google-drive, rapidocrm, foodeatup, n8n | `N8N_MCP_URL` |
| `rapido-startup` | 1.9.3 | 5 | 2 | stripe, rapidocrm, rapidocms, rapidorh, foodeatup, google-calendar | — |
| `rapido-forge` | 1.1.3 | 181 | 4 | rapidocrm, rapidocms, rapidorh | — |
| `rapido-marketing` | 0.18.3 | 17 | 5 | rapidocrm, rapidocms, rapidorh, facebook-ads, canva, lovable, n8n, gmail, google-calendar | `N8N_MCP_URL` (optionnel) ; Fireflies = connecteur optionnel (voir README plugin) |
| `rapido-higgsfield` | 1.0.4 | 9 | 1 | huggsfield, rapidocms, rapidocrm, rapidorh, foodeatup | `HIGGSFIELD_MCP_URL` |
| `rapido-video` | 1.0.0 | 2 | 0 | rapidocms (huggsfield optionnel) | **Prérequis : aucun** — ffmpeg/Whisper/Remotion auto-installés |
| `rapido-prompteur` | 0.3.1 | 2 | 1 | lovable, rapidocms, rapidocrm (orchestre aussi huggsfield, canva) | **Prérequis : aucun** — agent + skills + patterns + hooks |
| `rapido-elevenlabs` | 0.1.1 | 0 | 0 | ElevenLabs (local `uvx` ou passerelle HTTP), rapidocms | `ELEVENLABS_API_KEY` + `ELEVENLABS_MCP_BASE_PATH` (local) **ou** `ELEVENLABS_MCP_URL` + `ELEVENLABS_MCP_TOKEN` (passerelle) — squelette |
| `rapido-seo` | 0.1.0 | 6 | 0 | dataforseo, gsc, analytics (GA4), rapidocms, rapidocrm | `DATAFORSEO_AUTH`, `GSC_MCP_URL`, `GA4_MCP_URL` |
| `rapido-google-ads` | 0.1.0 | 4 | 0 | google-ads (read-only), dataforseo, analytics (GA4), rapidocrm | `GOOGLE_ADS_MCP_URL`, `DATAFORSEO_AUTH`, `GA4_MCP_URL` |
| `rapido-tiktok-ads` | 0.1.0 | 3 | 0 | tiktok-ads (R/W verrouillé), rapidocms, rapidocrm | `TIKTOK_ADS_MCP_URL` |
| `rapido-relation-client` | 0.2.0 | 6 | 0 | rapidocrm, foodeatup, rapidocms, rapidorh | — |
| `rapido-gmaps` | 0.5.0 | 4 | 1 | rapidocrm, foodeatup, rapidocms | Docker **ou** `GMAPS_API_URL`+`GMAPS_API_KEY` (KB) |
| `rapido-leadmagnet` | 0.5.0 | 4 | 1 | rapidocrm, rapidocms, rapidorh, lovable, facebook-ads | — |
| `rapido-copywriter` | 0.6.0 | 4 | 1 | rapidocms, rapidocrm, foodeatup | — |

**Total : 24 plugins, 376 skills, 36 agents.** Historique détaillé des vagues :
[`RELEASE-NOTES.md`](RELEASE-NOTES.md).

## Domaines couverts

Quel plugin pour quel besoin — installez seulement ce qui vous concerne.

| Domaine | Plugins | Ce que vous pilotez |
|---|---|---|
| **Restaurant** | `foodeatup` | Salle, cuisine (écran KDS), HACCP, achats, réservations |
| **Ventes & CRM** | `rapidocrm`, `rapido-gmaps` | Prospection, pipeline, devis/factures, vente terrain (SONCAS, BANT, objections, AARRR), expansion Studio→Agence→SaaS, ambassadeurs, **sourcing de leads Google Maps → CRM** (scoring ICP, dédup, opportunités FoodEatUp) |
| **Relation client** | `rapido-relation-client` | Service client en boucle (SLA), NPS, health score, RFM, 100 premiers jours |
| **Contenu & marque** | `rapidocms`, `rapido-copywriter` | Réseaux sociaux, visuels, cartes digitales, multi-marques, prompts visuels, **copy 4 réseaux** (grammaires natives, banque de hooks, anti-voix-IA) |
| **RH & projets** | `rapidorh` | Kanban, dailies, charge d'équipe, onboarding |
| **Marketing & acquisition** | `rapido-marketing`, `rapido-leadmagnet`, `rapido-seo`, `rapido-google-ads`, `rapido-tiktok-ads`, `rapido-meta-ads` | Leads, tunnel, attribution, **usine à lead magnets** (fabrication → capture → campagne → RH → mesure), SEO organique, SEA Google, TikTok, publicité Meta, influenceurs |
| **Média IA** | `rapido-higgsfield`, `rapido-video`, `rapido-prompteur`, `rapido-elevenlabs`, `rapido-canva` | Images/vidéos génératives, montage libre (ffmpeg), voix (ElevenLabs), design, direction de prompts |
| **App & automatisation** | `rapido-lovable`, `rapido-n8n` | Sites/apps connectés au CRM, **agent embarqué MCP (kit connecteur)**, workflows n8n |
| **Direction & finance** | `rapido-suite`, `rapido-startup`, `rapido-direction` | Pilotage transverse (Loop Engine), finance/trésorerie/board, chef de cabinet (Gmail/Agenda/Drive) |
| **Incubation** | `rapido-forge` | 181 exercices StartupsForge (bootcamp, idéation, scale) → livrables KB, pontés vers l'opérationnel |

## Les agents IA

Les **agents** sont des personas experts (installés avec leur plugin) qui chargent la
charte et la KB **avant** d'agir, invoquent les skills au bon moment, citent leurs
sources et respectent les garde-fous. On les invoque par leur rôle (« demande au
directeur commercial… ») ou ils sont mobilisés par les orchestrateurs.

| Plugin | Agents |
|---|---|
| `foodeatup` | chef-restaurateur · chef-cuisine · chef-de-pass |
| `rapidocrm` | directeur-commercial · sdr-prospection |
| `rapidocms` | directeur-artistique · community-manager · gardien-de-marque · gestionnaire-marques · responsable-marketing · prompt-designer |
| `rapidorh` | responsable-rh · chef-de-projet |
| `rapido-suite` | directeur-general (orchestrateur transverse) |
| `rapido-startup` | cfo-virtuel · coach-startup |
| `rapido-marketing` | directeur-marketing · growth-analyst · inbound-manager · outbound-manager · funnel-builder |
| `rapido-meta-ads` | media-buyer |
| `rapido-forge` | directeur-programme · mentor-bootcamp · mentor-ideation · mentor-scale |
| `rapido-canva` | studio-creatif |
| `rapido-lovable` | chef-produit-web · architecte-lovable (kit connecteur MCP) |
| `rapido-copywriter` | copywriter-social (directeur de création 4 réseaux) |
| `rapido-n8n` | architecte-automatisations |
| `rapido-higgsfield` | producteur-studio |
| `rapido-prompteur` | directeur-prompts (orchestre la conception de prompts) |
| `rapido-direction` | assistant-direction |
| `rapido-gmaps` | chasseur-leads (sourcing autonome sur brief) |
| `rapido-leadmagnet` | chef-usine-leadmagnet (orchestre les 9 étapes) |

## Les routines — le Loop Engine

Le marketplace exécute des **routines récurrentes** selon le cycle **Sense → Plan →
Act → Feed → Report** (diagnostiquer → prioriser → déléguer → capitaliser → rapport
une page). Calculs **par script** (`rapido-startup:catalogue-kpi`, **source unique des
formules**), écritures **confirmées**, mémoire d'exécution en **tables n8n**. Catalogue
canonique (id, alias, cadence, plugin, skills délégués, table mémoire) :
[`reference/registre-routines.md`](reference/registre-routines.md).

Les identifiants sont **préfixés par domaine** ; les anciens noms `R4…R9` et `R-MKT-*`
restent des **alias reconnus** (« lance R7 » = `FIN-CASH-SENTINELLE`).

| Domaine | Routines | Cadence |
|---|---|---|
| **Finance** `FIN-*` | FIN-CFO-HEBDO (R4) · FIN-CASH-SENTINELLE (R7) · FIN-BOARD-MENSUEL (R8) | hebdo · quotidien · mensuel |
| **Startup / Growth** | STARTUP-BUILDER (R5) · GROWTH-LOOP (R6) · VIDEO-FACTORY (R9) | hebdo · quotidien |
| **Marketing** `MKT-*` | MKT-HEBDO · MKT-QUOTIDIEN · MKT-MENSUEL · MKT-INFLUENCE-MENSUEL | hebdo → mensuel |
| **Vente** `VENTE-*` | VENTE-HYGIENE · VENTE-RELANCES · VENTE-REVUE · VENTE-EXPANSION | hebdo · quotidien |
| **Vente événementielle** `OPS-*` | OPS-LEAD-CHAUD · OPS-CLIENT-GAGNE · OPS-ALERTE-CHURN | webhook / temps réel |
| **Acquisition** `SEO-*` `SEA-*` `TIKTOK-*` | SEO-HEBDO · SEO-MENSUEL · SEA-HEBDO · TIKTOK-HEBDO | hebdo · mensuel |
| **Relation client** `RC-*` | RC-HEBDO · RC-NPS-TRIMESTRE · RC-SANTE-MENSUEL | hebdo → trimestriel |
| **Sourcing** `GMAPS-*` | GMAPS-HEBDO (sourcing Google Maps → CRM) | hebdo |

Chaque routine est **proposée puis installée sur confirmation** (jamais d'exécution
d'office) ; le récurrent et le volume vivent en **n8n** (recettes dans
`rapido-n8n/reference/`), pas en appels conversationnels. Le **registre des KPIs** (même
fichier) fixe la formule canonique de chaque indicateur (CAC, LTV, runway, DSO, AARRR,
NPS, ROI, part organique/payante…), calculée par `catalogue-kpi` — aucun calcul « de tête ».

## Installation (5 minutes)

1. **Installer Claude Code** (CLI, desktop ou web) —
   https://code.claude.com/docs
2. **Ajouter la marketplace** (dans une session Claude Code) :
   ```
   /plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
   ```
3. **Installer les plugins dont vous avez besoin** (`@rapido` = le nom de
   cette marketplace) :
   ```
   /plugin install rapido-suite@rapido        ← recommandé en premier (onboarding + pilotage)
   /plugin install foodeatup@rapido           ← si vous gérez un restaurant
   /plugin install rapidocrm@rapido           ← ventes, devis, factures, campagnes
   /plugin install rapidocms@rapido           ← réseaux sociaux, visuels, marques
   /plugin install rapido-forge@rapido        ← 180 exercices d'incubateur (bootcamp, idéation, scale)
   ```
   …puis rapidorh, rapido-direction, rapido-startup, rapido-canva,
   rapido-lovable, rapido-meta-ads, rapido-n8n selon vos usages (tableau
   ci-dessus).
4. **Recharger** : `/reload-plugins` (ou relancer Claude Code).

Test en local depuis un clone : `/plugin marketplace add ./<dossier-du-clone>`
depuis le dossier parent, puis les mêmes `install`.

## Connecter ou héberger les serveurs MCP

Chaque plugin déclare ses serveurs dans son `.mcp.json` — **vous vous
connectez à VOS comptes**, rien n'est partagé, **aucune clé n'est stockée dans
le dépôt** (uniquement des noms de variables d'environnement). Après chaque
connexion, vérifiez avec `/mcp` (la commande liste l'état de tous les serveurs).
**Règle générale** : un serveur optionnel non connecté ne casse rien — le skill
saute le volet EN LE DISANT (dégradation propre).

Les serveurs se rangent en **trois niveaux d'effort** :

- **A. Natifs Rapido** — rien à faire, l'URL est déjà là, connexion OAuth au
  premier appel.
- **B. Satellites officiels** — connecteurs hébergés par l'éditeur, OAuth au
  premier appel, aucune URL ni clé à fournir (sauf n8n/Higgsfield qui pointent
  vers VOTRE instance).
- **C. À héberger ou clé en variable d'env** — serveurs que vous auto-hébergez
  ou dont l'accès passe par une clé/URL exportée avant de lancer Claude Code.

### A. Serveurs natifs Rapido — FoodEatUp, RapidoCRM, RapidoCMS, RapidoRh

Utilisés par : foodeatup, rapidocrm, rapidocms, rapidorh, rapido-suite,
rapido-forge, rapido-direction, rapido-startup, rapido-relation-client et les
plugins satellites. **Aucune clé, aucune URL à fournir.**

1. Rien à installer : les URLs produit sont déjà dans les `.mcp.json`
   (`foodeatup.com/api/mcp`, `crm.rapidosoftware.com/mcp`,
   `cms.rapidosoftware.com/mcp`, `rh.rapidosoftware.com/mcp/rapidorh`).
2. Au PREMIER appel d'outil, Claude Code ouvre l'authentification du
   serveur : connectez-vous avec VOTRE compte FoodEatUp / RapidoCRM /
   RapidoCMS / RapidoRh (authentification individuelle par utilisateur).
3. Vérifiez : `/mcp` → les 4 serveurs « connected ».
4. FoodEatUp : les skills demandent votre `establishment_id` à la première
   utilisation (notez-le dans `rapido-kb/entreprise.md` pour ne plus le
   ressaisir).

### B. Satellites officiels (OAuth au premier appel)

Connecteurs hébergés par l'éditeur : OAuth individuel au premier usage, rien à
exporter (sauf les deux URLs d'instance signalées).

| Serveur | Plugin(s) | Connexion | À savoir |
|---|---|---|---|
| **Gmail / Google Calendar / Google Drive** | rapido-direction, rapido-marketing | OAuth Google au 1ᵉʳ appel | Gmail = **brouillons seulement**, rien ne part sans vous |
| **Stripe** (`mcp.stripe.com`) | rapido-startup | OAuth Stripe | Écriture interdite en routine, confirmée hors routine (hook `garde-stripe-write`) ; montants en centimes |
| **Canva** | rapido-canva | OAuth Canva | — |
| **Lovable** | rapido-lovable, rapido-prompteur | OAuth workspace | Chaque message consomme des **crédits** (l'agent cadre avant de construire) |
| **Meta / Facebook Ads** | rapido-meta-ads | OAuth Meta Business | Campagnes créées en **PAUSED** + plafond budget (hooks `plafond-budget` + `garde-argent-reel`) |
| **HyperFrames (HeyGen)** | rapidocms (vidéo) | OAuth HeyGen | Rendu vidéo **payant** (confirmation niveau 3) |
| **Higgsfield** | rapido-higgsfield | URL d'instance | `export HIGGSFIELD_MCP_URL=…` avant de lancer (génération payante) |
| **n8n** | rapido-n8n ; volets optionnels de rapido-direction, rapido-suite, rapido-marketing | URL d'instance | `export N8N_MCP_URL=https://<instance>/mcp-server/http` ; sans elle, dégradation propre. Guide : `rapido-n8n/README-installation.md` |

### C. À héberger ou clé en variable d'environnement

Ces serveurs **ne sont pas encore connectés par défaut** : vous les auto-hébergez
ou vous fournissez une clé/URL en variable d'env AVANT de lancer Claude Code. Les
skills correspondants sont écrits d'après les grammaires documentées (pattern
« construire d'abord » — comme le squelette ElevenLabs) et **se dégradent
proprement** tant que le serveur est absent. **Aucune clé n'est écrite dans le
dépôt.** Détails d'accès dans le README de chaque plugin.

| Serveur | Plugin(s) | Variable(s) d'env | Hébergement / accès |
|---|---|---|---|
| **ElevenLabs** (voix) | rapido-elevenlabs | `ELEVENLABS_API_KEY` + `ELEVENLABS_MCP_BASE_PATH` (mode **local `uvx`**) **ou** `ELEVENLABS_MCP_URL` + `ELEVENLABS_MCP_TOKEN` (mode **passerelle HTTP**) | Local : `uvx elevenlabs-mcp` avec votre clé API. Passerelle : votre serveur HTTP. Génération payante — voir `docs/PREREQUIS-E5.md` |
| **DataForSEO** (SEO/SERP) | rapido-seo, rapido-google-ads | `DATAFORSEO_AUTH` (Basic auth) | Serveur hébergé `mcp.dataforseo.com/mcp`, **pay-as-you-go** — coûts gouvernés par le hook SEO |
| **Google Search Console (GSC)** | rapido-seo | `GSC_MCP_URL` | Serveur **auto-hébergé**, lecture seule ; fraîcheur des données GSC annoncée dans le skill |
| **Google Analytics 4 (GA4)** | rapido-seo, rapido-google-ads | `GA4_MCP_URL` | Serveur **auto-hébergé**, scope `analytics.readonly` (lecture seule) |
| **Google Ads** | rapido-google-ads | `GOOGLE_ADS_MCP_URL` | **Lecture seule** ; nécessite developer token + OAuth Google Ads. Analyse et recommande, exécution manuelle guidée |
| **TikTok Ads** | rapido-tiktok-ads | `TIKTOK_ADS_MCP_URL` | R/W **verrouillé argent réel** : création active **refusée** (hook DENY), budgets en confirmation. OAuth TikTok Business |

> **`rapido-video`** n'a besoin d'**aucun serveur MCP externe** : le montage
> libre (ffmpeg / Whisper / Remotion) s'auto-installe localement. Il branche
> seulement `rapidocms` (et `huggsfield` en option) pour publier.

### Dépannage rapide

- `/mcp` → serveur « needs authentication » : relancez l'outil, la fenêtre
  d'authentification se rouvre.
- Un volet est sauté avec un message « serveur non connecté » : c'est le
  comportement nominal (dégradation propre) — connectez le serveur ou
  ignorez le volet.
- Les serveurs évoluent : les skills ré-introspectent les schémas avant
  toute écriture sensible et signalent les écarts (« le serveur fait foi »).

## Comment l'utiliser

**Premier lancement — construisez votre base de connaissance** (recommandé) :

> « Apprends à connaître mon entreprise »

L'onboarding (rapido-suite) vous interviewe et construit `./rapido-kb/`
dans VOTRE répertoire de travail : seuils maison, charte graphique, ton,
personas, processus. Tous les plugins la lisent ensuite en priorité — c'est
elle qui fait passer les skills du générique au sur-mesure. Kit de
démarrage : [`rapido-kb-template/`](rapido-kb-template/) (8 fichiers
vierges + mégaprompt `PROMPT-CLAUDE-CODE-MASTER.md` + bibliothèque de
prompts testés `PROMPTS-CLAUDE-CODE.md` + prompt de pilotage
`PROMPT-PILOTAGE.md` — le prompt maître qui lance le Loop Engine sur toute
l'entreprise, avec ses variantes lundi / sentinelle / board / vidéo). Cette KB reste chez vous — jamais
dans ce dépôt.

**Ensuite, parlez naturellement.** Quelques phrases qui déclenchent les
workflows (une par domaine) :

| Vous dites… | Ce qui se passe |
|---|---|
| « Mon briefing du matin » | foodeatup : notifications, HACCP, salle temps réel, créneaux du midi, staffing, stocks — un écran, 3 priorités |
| « Le tartare de la 12 est prêt » | coordination-cuisine : le plat avance sur le KDS, la commande est proposée au passage quand tout est prêt |
| « Relance mes factures en retard » | rapidocrm : détection, relances RÉDIGÉES (envoi seulement après votre OK), traçage |
| « Prépare les posts de la semaine » | rapidocms : calendrier éditorial, brouillons par réseau à votre ton, planification confirmée |
| « Lance un sondage chez mes clients » | animation-client : modèles existants, confirmation (visible clients), résultats en 3 enseignements |
| « Qui est surchargé dans l'équipe ? » | rapidorh : charge déclarée vs contractuelle, calculée par script, rééquilibrages proposés |
| « Ma journée » | rapido-direction : emails + agenda triple + signaux business en UNE page, 3 priorités |
| « Lance R7 » / « surveille ma trésorerie » | rapido-startup : sentinelle cash — runway calculé par script, alerte seulement, zéro écriture (existe aussi en workflow n8n autonome : `rapido-n8n/reference/recette-r7-cash-sentinel.md`) |
| « Automatise l'envoi du récap hebdo » | rapido-n8n : workflow validé et testé AVANT publication, production sous confirmation |
| « Quel est mon prochain exercice ? » | rapido-forge : le directeur-programme lit votre journal, vérifie les prérequis et propose l'exercice suivant (niveau annoncé) |
| « Je veux lancer un SaaS » | rapido-suite : orchestrateur lancement-projet-360 — la méthode Forge pense, les plugins exécutent, validation entre chaque acte |
| « Pilote mon entreprise » | rapido-suite : le Loop Engine complet sur toute la boîte (Sense → Plan → Act → Feed → Report), KPI par script, récap groupé avant toute écriture, report une page |

**Ce que les garde-fous vous garantissent** : les actions destructrices,
payantes ou visibles par vos clients demandent TOUJOURS votre confirmation
(hooks déterministes, testés — voir la section suivante) ; aucun chiffre
n'est calculé « de tête » (scripts embarqués, formule affichée) ; aucune
donnée n'est inventée (valeur manquante = question posée).

## Architecture d'un plugin

```
<plugin>/
├── .claude-plugin/
│   └── plugin.json        # Identité du plugin
├── .mcp.json              # Serveurs MCP requis
├── skills/
│   └── <skill>/SKILL.md   # Workflows métier (+ scripts/ de calcul)
├── agents/
│   └── <agent>.md         # Personas experts
├── hooks/
│   ├── hooks.json         # Câblage des garde-fous
│   └── scripts/           # Scripts déterministes
├── reference/             # Directives, pièges, chartes
├── CHANGELOG.md           # Historique versionné
└── ATTRIBUTIONS.md        # Provenance des skills externes (si concerné)
```

- **`plugin.json`** — nom (slug immuable une fois publié), version et auteur.
  La version s'incrémente à chaque changement, en miroir du `CHANGELOG.md`.
- **`.mcp.json`** — les serveurs MCP que le plugin branche (URLs produit
  uniquement, `${N8N_MCP_URL}` pour l'instance n8n du client). Un serveur
  optionnel absent déclenche une dégradation propre, jamais une erreur brute.
- **`skills/`** — un dossier par skill, avec un `SKILL.md` (frontmatter
  `name` + `description` en déclencheur « Utiliser quand… », workflow
  numéroté, règles métier). Les skills d'analyse délèguent leurs calculs à
  des scripts Python stdlib embarqués — le modèle ne calcule jamais de tête.
- **`agents/`** — des personas experts (directeur artistique, media buyer,
  directeur général…) qui chargent la charte et la KB avant de produire.
  Chaque agent cite ses sources et invoque les skills du plugin au bon moment.
- **`hooks/`** — des garde-fous déterministes, indépendants du modèle
  (stdin JSON → allow / ask / deny, aucun appel réseau, testés). Ils imposent
  la confirmation avant les actions destructrices et bloquent les patterns
  interdits (voir ci-dessous).
- **`reference/`** — directives par outil MCP, tableaux de pièges vérifiés
  sur les serveurs et chartes graphiques, chargés à la demande par les skills
  en « Étape 0 ». Les valeurs du client priment via `./rapido-kb/` (construite
  par l'onboarding dans SON répertoire de travail, jamais dans le plugin).

## Garde-fous intégrés

Scripts réels du dépôt (`<plugin>/hooks/scripts/`), résumés depuis leurs
docstrings :

- **`garde-destructif`** (foodeatup, rapidocrm, rapidocms, rapidorh,
  rapido-suite) — refuse (deny) toute transition de statut de facture
  interdite par les règles DGFiP et force la confirmation (ask) sur tout
  autre outil destructif ou irréversible (`delete_*`, annulations…).
- **`anti-donnee-inventee`** (foodeatup, rapido-suite) — refuse tout relevé
  de température hors plage plausible (−30 °C à +90 °C) sur `add_temperature`.
- **`garde-argent-reel`** (rapido-meta-ads) — confirmation forcée sur tout ce
  qui engage une dépense : activation d'entité, boost Instagram confirmé,
  mise à jour touchant un budget, suppression d'audience, étude de lift
  payante.
- **`plafond-budget`** (rapido-meta-ads) — refuse toute création/modification
  dont le budget journalier dépasse le plafond maison lu dans
  `./rapido-kb/processus-internes.md` (défaut : 50, dans la devise du compte
  publicitaire).
- **`garde-production`** (rapido-n8n) — confirmation forcée sur
  `publish_workflow`, `unpublish_workflow`, `archive_workflow` et
  `execute_workflow` en mode production — y compris quand `executionMode`
  est absent (le défaut du serveur est « production »).
- **`garde-stripe-write`** (rapido-startup) — confirmation forcée sur toute
  écriture Stripe (remboursement, facture, coupon…) : Stripe est en lecture
  seule dans les routines, en plus du flux d'approbation natif du serveur.
- **`garde-calcul-script`** (rapido-startup, Stop) — bloque toute réponse qui
  annonce un KPI chiffré (MRR, LTV, runway…) sans exécution du script
  calcul_kpi.py dans le tour (« KPI sans script »).
- **`garde-projection-realiste`** (rapido-startup) — rejette un prévisionnel
  à churn nul, ou à croissance > 30 %/mois au-delà du mois 6 sans
  justification écrite dans hypotheses.md.
- **`garde-irreversible`** (rapido-direction) — confirmation forcée sur les
  opérations irréversibles ou visibles par des tiers : corbeille/spam Gmail,
  suppression Drive, suppression d'événement Calendar (les participants
  reçoivent l'annulation).
- **`garde-ecriture-kb`** (rapido-forge) — refuse (deny) toute écriture de
  livrable hors de `./rapido-kb/` : les exercices de la méthode écrivent
  dans VOTRE base de connaissance, jamais dans le dossier du plugin.
- **`rappel-argent-reel`** (rapido-forge) — confirmation forcée quand un
  exercice débouche sur un outil Meta qui dépense de l'argent réel.

S'y ajoutent des hooks `Stop` (récapitulatif des écritures avec IDs exigé en
fin de tour) et `SessionStart` (détection de `./rapido-kb/` et rappel des
directives). Jamais de secrets dans les skills ou `reference/` — ils sont
distribués avec le plugin.

## Skills tiers et attributions

41 des 362 skills sont importés de dépôts open source, adaptés aux
conventions Rapido (mentions MCP/KB, renvois vers les skills d'exécution,
renommages anti-collision). Provenance détaillée — commit, chemin d'origine,
modifications locales — dans l'`ATTRIBUTIONS.md` de chaque plugin concerné ;
la LICENSE de la source est copiée dans chaque dossier de skill.

| Source | Licence | Skills | Plugins |
|---|---|---|---|
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Apache 2.0 | 23 | foodeatup (3), rapidocrm (6), rapidocms (3), rapidorh (5), rapido-suite (4), rapido-meta-ads (2) |
| [anthropics/skills](https://github.com/anthropics/skills) | Apache 2.0 (LICENSE.txt par skill) | 6 | rapido-canva (3), rapido-lovable (2), rapido-suite (1 : `skill-creator`) |
| [wondelai/skills](https://github.com/wondelai/skills) | MIT | 9 | rapidocms (3), rapidocrm (3), rapido-meta-ads (3) |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT | 2 | rapido-lovable (2) |
| [AgriciDaniel/claude-blog](https://github.com/AgriciDaniel/claude-blog) | MIT | 1 | rapidocms (1 : `generation-article-blog`) |

Les skills wondelai (basés sur des livres) ne sont pas modifiés. Cas
particulier documenté dans `rapido-suite/ATTRIBUTIONS.md` : `friday-brief` a
été fusionné dans le skill maison `revue-hebdo-business` au lieu d'être copié.

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md) : conventions des skills (frontmatter,
« Utiliser quand… », outils MCP vérifiés sur les serveurs), slug de plugin
immuable, version + CHANGELOG à chaque changement, évals (`tests/evals.md`)
avant merge, règles d'intégration des skills externes (LICENSE +
ATTRIBUTIONS.md).

## Licence

[Apache License 2.0](LICENSE) — Copyright 2026 BraindCode. Les skills
importés conservent leur licence d'origine (Apache 2.0 ou MIT), embarquée
dans leur dossier — voir « Skills tiers et attributions ».
