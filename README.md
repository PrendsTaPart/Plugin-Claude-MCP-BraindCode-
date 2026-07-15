# Marketplace Rapido — Plugins Claude Code

Des **agents IA qui pilotent votre entreprise** en parlant directement à vos
systèmes Rapido (FoodEatUp, RapidoCRM, RapidoCMS, RapidoRh) et à leurs outils
satellites — via des **skills métier**, des **personas experts** et des
**garde-fous déterministes** par-dessus vos serveurs **MCP**.

![validation](https://github.com/PrendsTaPart/Plugin-Claude-MCP-BraindCode-/actions/workflows/validation.yml/badge.svg)
![Plugins](https://img.shields.io/badge/plugins-25-blue)
![Skills](https://img.shields.io/badge/skills-380-brightgreen)
![Agents](https://img.shields.io/badge/agents-37-orange)
![Version](https://img.shields.io/github/v/tag/PrendsTaPart/Plugin-Claude-MCP-BraindCode-?label=derni%C3%A8re%20version)
![Licence](https://img.shields.io/badge/licence-Apache%202.0-blue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-marketplace%20de%20plugins-5A3FFF)

> **Pour un agent IA qui lit ce dépôt** : chaque plugin est autonome
> (`<plugin>/.claude-plugin/plugin.json`, `.mcp.json`, `skills/*/SKILL.md`,
> `agents/*.md`, `hooks/`). Le catalogue des routines et des KPIs canoniques est
> `reference/registre-routines.md`. Les données du client vivent hors dépôt dans
> `./rapido-kb/` (jamais commitées). **Aucun secret n'est stocké dans le dépôt.**

**Sommaire** : [Pourquoi](#pourquoi-ce-marketplace) · [Installation](#installation) ·
[Prérequis & connecteurs](#prérequis--connecteurs) · [Les plugins](#les-plugins) ·
[Démarrage rapide](#démarrage-rapide) · [Conventions maison](#conventions-maison) ·
[Structure du dépôt](#structure-du-dépôt) · [Sécurité](#sécurité) ·
[Roadmap & contribution](#roadmap--contribution)

## Pourquoi ce marketplace

Vous utilisez FoodEatUp, RapidoCRM, RapidoCMS ou RapidoRh ? Cette marketplace
transforme Claude Code en **équipe de pilotage qui parle à vos systèmes**. Les
**agents IA** (chef-restaurateur, directeur commercial, CFO virtuel, directeur
général…) chargent votre charte et votre base de connaissance, invoquent les bons
**skills**, exécutent les appels **MCP** sur VOS comptes, et déclenchent des
**routines récurrentes** — le tout sous des **garde-fous déterministes** :
confirmation avant tout ce qui est destructif, payant ou visible par vos clients,
jamais de donnée inventée, calculs par scripts (jamais « de tête »).

Chaque plugin apporte des **skills** (workflows déclenchés par vos phrases), des
**agents** (personas experts), des **hooks** (garde-fous testés, indépendants du
modèle) et une personnalisation par **votre base de connaissance `./rapido-kb/`**
(vos seuils, votre charte, vos personas — jamais stockés dans ce dépôt).

## Installation

1. **Claude Code à jour** (CLI, application desktop ou web), avec les plugins et
   les serveurs MCP activés — https://code.claude.com/docs.
2. **Ajouter la marketplace** dans une session Claude Code :
   ```
   /plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
   ```
3. **Installer les plugins utiles** (`@rapido` = le nom de cette marketplace) :
   ```
   /plugin install rapido-suite@rapido        ← recommandé en premier (onboarding + pilotage)
   /plugin install foodeatup@rapido           ← si vous gérez un restaurant
   /plugin install rapidocrm@rapido           ← ventes, devis, factures, campagnes
   /plugin install rapidocms@rapido           ← réseaux sociaux, visuels, marques
   ```
   …puis les autres selon vos usages (voir [la table des plugins](#les-plugins)).
4. **Recharger** : `/reload-plugins` (ou relancer Claude Code).

Test en local depuis un clone : `/plugin marketplace add ./<dossier-du-clone>`
depuis le dossier parent, puis les mêmes `install`.

## Prérequis & connecteurs

Chaque plugin déclare ses serveurs MCP dans son `.mcp.json` — **vous vous
connectez à VOS comptes**, rien n'est partagé. **Aucune clé n'est stockée dans le
dépôt** : uniquement des **noms de variables d'environnement**, que vous exportez
avant de lancer Claude Code. Après connexion, vérifiez avec `/mcp`. Règle
générale : un serveur **optionnel** non connecté ne casse rien — le skill saute le
volet **en le disant** (dégradation propre).

**A. Serveurs natifs Rapido** — `foodeatup`, `rapidocrm`, `rapidocms`, `rapidorh`.
URLs produit déjà présentes dans les `.mcp.json` ; **rien à fournir** :
authentification OAuth individuelle au premier appel. Vérifiez `/mcp` → « connected ».

**B. Satellites officiels** — OAuth au premier usage, rien à exporter (sauf les URLs
d'instance signalées) :

| Serveur | Plugin(s) | Connexion | À savoir |
|---|---|---|---|
| Gmail / Google Calendar / Google Drive | rapido-direction, rapido-marketing | OAuth Google | Gmail = **brouillons seulement** |
| Stripe | rapido-startup | OAuth Stripe | Écriture confirmée (hook `garde-stripe-write`), montants en centimes |
| Canva | rapido-canva | OAuth Canva | — |
| Lovable | rapido-lovable, rapido-prompteur | OAuth workspace | Chaque message consomme des **crédits** |
| Meta / Facebook Ads | rapido-meta-ads | OAuth Meta Business | Campagnes créées en **PAUSED** + plafond budget (hooks) |
| HyperFrames (HeyGen) | rapidocms (vidéo) | OAuth HeyGen | Rendu vidéo **payant** |
| n8n | rapido-n8n (+ volets optionnels) | URL d'instance | `export N8N_MCP_URL=…` ; sans elle, dégradation propre |

**C. À héberger ou clé en variable d'environnement** — vous auto-hébergez ou
fournissez une clé/URL **en variable d'env, jamais dans le dépôt** :

| Serveur | Plugin(s) | Variable(s) d'env | Accès |
|---|---|---|---|
| ElevenLabs (voix) | rapido-elevenlabs | `ELEVENLABS_API_KEY` + `ELEVENLABS_MCP_BASE_PATH` (local) **ou** `ELEVENLABS_MCP_URL` + `ELEVENLABS_MCP_TOKEN` (passerelle) | Génération payante |
| DataForSEO | rapido-seo, rapido-google-ads | `DATAFORSEO_AUTH` | Hébergé, pay-as-you-go |
| Google Search Console | rapido-seo | `GSC_MCP_URL` | Auto-hébergé, lecture seule |
| Google Analytics 4 | rapido-seo, rapido-google-ads | `GA4_MCP_URL` | Auto-hébergé, lecture seule |
| Google Ads | rapido-google-ads | `GOOGLE_ADS_MCP_URL` | **Lecture seule** (analyse + recommande) |
| TikTok Ads | rapido-tiktok-ads | `TIKTOK_ADS_MCP_URL` | R/W **verrouillé argent réel** (création refusée par hook) |
| Higgsfield | rapido-higgsfield | `HIGGSFIELD_MCP_URL` | URL d'instance, génération payante |

**Connecteurs optionnels** (marqués comme tels dans les skills) : **Fireflies**
(intelligence commerciale de `rapido-marketing` — absent = volet sauté),
**Higgsfield** (option média de `rapido-video`). `rapido-video` n'exige **aucun**
serveur externe : ffmpeg / Whisper / Remotion s'auto-installent localement.

> **Dépannage** : `/mcp` « needs authentication » → relancez l'outil, la fenêtre se
> rouvre. Volet sauté « serveur non connecté » = comportement nominal. Les serveurs
> évoluent : les skills ré-introspectent les schémas avant toute écriture sensible.

## Les plugins

Chiffres lus depuis les fichiers du dépôt (version du `plugin.json`, skills =
dossiers `SKILL.md`, agents = `agents/*.md`, MCP depuis `mcp_requis`/`.mcp.json`).
Table générée par [`scripts/generate_readme_table.py`](scripts/generate_readme_table.py).

<!-- TABLE-PLUGINS:START -->
| Plugin | Version | Skills | Agents | MCP requis | Description |
|---|---|---|---|---|---|
| `foodeatup` | 1.5.1 | 15 | 3 | foodeatup, rapidocrm | Gestion restaurant FoodEatUp |
| `rapidocrm` | 1.7.0 | 29 | 2 | rapidocrm | RapidoCRM |
| `rapidocms` | 1.11.8 | 22 | 6 | rapidocms, hyperframes | RapidoCMS |
| `rapidorh` | 1.0.3 | 11 | 2 | rapidorh | RapidoRh |
| `rapido-suite` | 1.4.2 | 13 | 1 | rapidocrm, rapidocms, rapidorh, foodeatup, lovable, facebook-ads, n8n | Orchestration transverse des 4 serveurs MCP Rapido |
| `rapido-canva` | 1.0.1 | 7 | 1 | canva, foodeatup, rapidocms, rapidocrm, rapidorh | Design Canva alimenté par les données Rapido |
| `rapido-lovable` | 1.5.1 | 10 | 2 | lovable, foodeatup, rapidocms, rapidocrm, rapidorh | Apps et agents IA Lovable alimentés par les données Rapido |
| `rapido-meta-ads` | 1.0.5 | 13 | 1 | facebook-ads, rapidocms, rapidocrm, canva, lovable, foodeatup | Publicité Meta (Facebook/Instagram) pilotée par les données Rapido |
| `rapido-n8n` | 1.6.0 | 4 | 1 | n8n, foodeatup, rapidocms, rapidocrm, rapidorh | Automatisations n8n sur l'instance du client |
| `rapido-direction` | 1.1.0 | 5 | 1 | gmail, google-calendar, google-drive, rapidocrm, foodeatup, n8n | Chef de cabinet du dirigeant |
| `rapido-startup` | 1.9.3 | 5 | 2 | stripe, rapidocrm, rapidocms, rapidorh, foodeatup, google-calendar | Finance & création de startup |
| `rapido-forge` | 1.1.3 | 181 | 4 | rapidocrm, rapidocms, rapidorh | StartupsForge (PrendsTaPart) |
| `rapido-marketing` | 0.18.3 | 17 | 5 | rapidocrm, rapidocms, rapidorh, facebook-ads, canva, lovable, n8n, gmail, google-calendar | Marketing & acquisition Rapido-first |
| `rapido-higgsfield` | 1.0.4 | 9 | 1 | huggsfield, rapidocms, rapidocrm, rapidorh, foodeatup | Usine média IA (Higgsfield) branchée sur l'écosystème Rapido |
| `rapido-video` | 1.0.0 | 2 | 0 | rapidocms | Montage vidéo 100 % libre (ffmpeg + Whisper) |
| `rapido-prompteur` | 0.3.2 | 2 | 1 | lovable, rapidocms, rapidocrm | Directeur de prompts |
| `rapido-elevenlabs` | 0.1.1 | 0 | 0 | ElevenLabs, rapidocms | La voix de l'écosystème (MCP officiel ElevenLabs) |
| `rapido-seo` | 0.1.0 | 6 | 0 | dataforseo, gsc, analytics, rapidocms, rapidocrm | SEO & acquisition organique pilotés par les données |
| `rapido-google-ads` | 0.1.0 | 4 | 0 | google-ads, dataforseo, analytics, rapidocrm | SEA Google Ads en LECTURE SEULE (MCP officiel read-only) |
| `rapido-tiktok-ads` | 0.1.0 | 3 | 0 | tiktok-ads, rapidocms, rapidocrm | TikTok Ads VERROUILLÉ — argent réel (MCP officiel lecture/écriture). Pilotage de performance, lancement de ca… |
| `rapido-relation-client` | 0.2.0 | 6 | 0 | rapidocrm, foodeatup, rapidocms, rapidorh | Service client, fidélité et santé client en boucle |
| `rapido-gmaps` | 0.5.0 | 4 | 1 | rapidocrm, foodeatup, rapidocms | Sourcing de leads Google Maps → pipeline RapidoCRM |
| `rapido-leadmagnet` | 0.5.0 | 4 | 1 | rapidocrm, rapidocms, rapidorh, lovable, facebook-ads | L'usine à lead magnets de bout en bout |
| `rapido-copywriter` | 0.6.0 | 4 | 1 | rapidocms, rapidocrm, foodeatup | Le copywriter LinkedIn · Facebook · Instagram · TikTok |
| `rapido-design` | 0.5.0 | 4 | 1 | rapidocms, lovable | Le studio UX/UI |

**Total : 25 plugins, 380 skills, 37 agents.** Table générée par `scripts/generate_readme_table.py` — ne pas éditer à la main.
<!-- TABLE-PLUGINS:END -->

Historique détaillé des vagues : [`RELEASE-NOTES.md`](RELEASE-NOTES.md).

### Quel plugin pour quel besoin

| Domaine | Plugins | Ce que vous pilotez |
|---|---|---|
| **Restaurant** | `foodeatup` | Salle, cuisine (KDS), HACCP, achats, réservations |
| **Ventes & CRM** | `rapidocrm`, `rapido-gmaps` | Prospection, pipeline, devis/factures, vente terrain, **sourcing Google Maps → CRM** |
| **Relation client** | `rapido-relation-client` | Service client (SLA), NPS, health score, RFM |
| **Contenu & marque** | `rapidocms`, `rapido-copywriter`, `rapido-design` | Réseaux sociaux, visuels, multi-marques, **copy 4 réseaux**, **studio UX/UI** |
| **RH & projets** | `rapidorh` | Kanban, dailies, charge d'équipe, onboarding |
| **Marketing & acquisition** | `rapido-marketing`, `rapido-leadmagnet`, `rapido-seo`, `rapido-google-ads`, `rapido-tiktok-ads`, `rapido-meta-ads` | Leads, tunnel, attribution, **usine à lead magnets**, SEO, SEA, TikTok, Meta |
| **Média IA** | `rapido-higgsfield`, `rapido-video`, `rapido-prompteur`, `rapido-elevenlabs`, `rapido-canva` | Images/vidéos, montage libre, voix, design, prompts |
| **App & automatisation** | `rapido-lovable`, `rapido-n8n` | Sites/apps connectés au CRM, **agent MCP embarqué**, workflows n8n |
| **Direction & finance** | `rapido-suite`, `rapido-startup`, `rapido-direction` | Pilotage transverse (Loop Engine), finance, chef de cabinet |
| **Incubation** | `rapido-forge` | 181 exercices StartupsForge → livrables KB |

Les **routines récurrentes** (Loop Engine : Sense → Plan → Act → Feed → Report)
sont cataloguées dans [`reference/registre-routines.md`](reference/registre-routines.md) —
finance, growth, marketing, vente, acquisition, relation client, sourcing —
**proposées puis installées sur confirmation**, jamais exécutées d'office.

## Démarrage rapide

**Premier lancement** — construisez votre base de connaissance :

> « Apprends à connaître mon entreprise »

L'onboarding (`rapido-suite`) vous interviewe et construit `./rapido-kb/` dans
VOTRE répertoire de travail (seuils, charte, ton, personas). Tous les plugins la
lisent ensuite en priorité. Kit de démarrage :
[`rapido-kb-template/`](rapido-kb-template/). Cette KB reste chez vous.

**Ensuite, parlez naturellement.** Trois phrases pour commencer :

> « Pilote mon commercial » → `rapidocrm` : hygiène du pipeline, relances rédigées
> (envoi après votre OK), revue des opportunités, prochaines actions.

> « Fabrique le lead magnet » → `rapido-leadmagnet` : de la fabrication à la
> capture, la campagne, l'inbound RH et la mesure — étape par étape.

> « Connecte le MCP FoodEatUp au site » → `rapido-lovable` : le kit connecteur MCP
> (edge function, clés côté serveur, scope verrouillé) pour un agent embarqué.

D'autres déclencheurs réels :

| Vous dites… | Ce qui se passe |
|---|---|
| « Mon briefing du matin » | `foodeatup` : notifications, HACCP, salle, staffing, stocks — un écran, 3 priorités |
| « Relance mes factures en retard » | `rapidocrm` : détection, relances RÉDIGÉES (envoi après OK), traçage |
| « Prépare les posts de la semaine » | `rapidocms` : calendrier éditorial, brouillons par réseau à votre ton |
| « Qui est surchargé dans l'équipe ? » | `rapidorh` : charge déclarée vs contractuelle, calculée par script |
| « Surveille ma trésorerie » | `rapido-startup` : sentinelle cash, runway par script, alerte seulement |
| « Pilote mon entreprise » | `rapido-suite` : Loop Engine complet, récap groupé avant toute écriture |

## Conventions maison

Le dépôt est un **produit distribué à tous les clients** : chaque règle sert la
portabilité et la fiabilité.

- **Slug immuable** — le `name` d'un plugin ne change jamais après publication
  (le renommer casse les installations). Renommer = nouveau plugin + dépréciation.
- **Étape 0 `reference/`** — chaque skill charge d'abord ses directives d'outils,
  ses pièges vérifiés et la charte, puis la KB `./rapido-kb/` si pertinent.
- **Calculs par script** — tout chiffre (KPI, budget, charge) passe par un script
  Python **stdlib** embarqué, formule affichée. Jamais « de tête ».
- **Hooks de confirmation** — les actions destructrices, payantes ou visibles par
  des tiers passent par un garde-fou déterministe (allow / ask / deny, testé).
- **Brouillons, jamais de publication directe** — les contenus (posts, emails,
  relances) sont **rédigés** puis envoyés **après votre validation**.
- **Rien d'inventé** — chaque donnée vient d'un outil MCP, de la KB ou de vous ;
  une valeur manquante se dit, elle ne s'estime pas.
- **Versioning + CHANGELOG** — chaque plugin modifié incrémente sa `version` et
  ajoute une entrée datée en tête de son `CHANGELOG.md`.
- **Attribution des sources** — tout skill importé conserve sa LICENSE dans son
  dossier et sa provenance dans l'`ATTRIBUTIONS.md` (ou `NOTICE.md`) du plugin.
- **Portabilité absolue** — aucune donnée client, aucun identifiant ni URL
  d'instance en dur : URLs produit dans `.mcp.json`, variables d'env pour les
  instances, personnalisation dans `./rapido-kb/` (jamais commitée).

## Structure du dépôt

```
Plugin-Claude-MCP-BraindCode-/
├── .claude-plugin/
│   └── marketplace.json      # Catalogue des 25 plugins
├── <plugin>/                 # 25 plugins (foodeatup, rapidocrm, rapido-*, …)
│   ├── .claude-plugin/plugin.json   # Identité : name (slug), version, mcp_requis
│   ├── .mcp.json                    # Serveurs MCP requis
│   ├── skills/<skill>/SKILL.md      # Workflows métier (+ scripts/ de calcul)
│   ├── agents/<agent>.md            # Personas experts
│   ├── hooks/hooks.json + scripts/  # Garde-fous déterministes testés
│   ├── reference/                   # Directives, pièges, chartes
│   ├── CHANGELOG.md   README.md   tests/evals.md
│   └── ATTRIBUTIONS.md | NOTICE.md  # Provenance des skills externes (si concerné)
├── reference/registre-routines.md   # Loop Engine : routines + KPIs canoniques
├── scripts/                  # valider-plugins.py · tester-skills.py · generate_readme_table.py
├── docs/                     # Audits, imports, recettes (runbooks)
├── tests/                    # Rapports de validation
├── rapido-kb-template/       # Kit de démarrage de la base de connaissance client
├── CONTRIBUTING.md   SECURITY.md   LICENSE   RELEASE-NOTES.md
└── README.md
```

## Sécurité

Installer un plugin, c'est lui confier **l'exécution de code** (hooks, scripts) et
**des appels MCP avec les privilèges de vos comptes** — n'installez que depuis ce
dépôt (ou votre fork audité). Les garde-fous déterministes (`<plugin>/hooks/`) sont
la dernière ligne de défense, **indépendante du modèle** : `garde-destructif`
(suppressions, transitions de facture hors DGFiP), `anti-donnee-inventee` (valeurs
invraisemblables), `garde-argent-reel` + `plafond-budget` (dépenses Meta Ads),
`garde-production` (workflows n8n), `garde-stripe-write`, `garde-irreversible`
(Gmail/Drive/Calendar), `garde-ecriture-kb`… Ils imposent une confirmation et
**ne se contournent jamais** — une PR qui affaiblit un hook est refusée.

- **Jamais de secrets dans le dépôt** — authentifications par connecteurs MCP et
  OAuth individuels ; clés en variables d'environnement uniquement.
- `./rapido-kb/` (données client) vit chez le client, **jamais versionnée ici**.

Politique complète et signalement d'une vulnérabilité : [`SECURITY.md`](SECURITY.md).

## Roadmap & contribution

**Chantiers en cours** : les plugins d'acquisition récents sont en amorçage
(`rapido-seo`, `rapido-google-ads`, `rapido-tiktok-ads` en `0.1.0`,
`rapido-elevenlabs` squelette assumé) ; les **recettes de bout en bout** (runbooks
`docs/RECETTE-*.md`) restent à jouer sur données réelles (créent de la donnée de
prod / des coûts). Le suivi documentaire vit dans `docs/` (audits, imports).

**Contribuer** : voir [`CONTRIBUTING.md`](CONTRIBUTING.md) — conventions des skills
(frontmatter, « Utiliser quand… », outils MCP vérifiés sur les serveurs), tests de
déclenchement exigés, version + CHANGELOG, règles d'intégration des skills externes.
Avant toute PR : `python3 scripts/valider-plugins.py` puis
`python3 scripts/tester-skills.py` doivent passer sans erreur.

### Skills tiers et attributions

41 des 380 skills sont importés de dépôts open source, adaptés aux conventions
Rapido (mentions MCP/KB, renvois d'exécution, renommages anti-collision). La
LICENSE de la source est copiée dans chaque dossier de skill ; la provenance
détaillée est dans l'`ATTRIBUTIONS.md` de chaque plugin concerné.

| Source | Licence | Skills | Plugins |
|---|---|---|---|
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Apache 2.0 | 23 | foodeatup (3), rapidocrm (6), rapidocms (3), rapidorh (5), rapido-suite (4), rapido-meta-ads (2) |
| [anthropics/skills](https://github.com/anthropics/skills) | Apache 2.0 | 6 | rapido-canva (3), rapido-lovable (2), rapido-suite (1) |
| [wondelai/skills](https://github.com/wondelai/skills) | MIT | 9 | rapidocms (3), rapidocrm (3), rapido-meta-ads (3) |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT | 2 | rapido-lovable (2) |
| [AgriciDaniel/claude-blog](https://github.com/AgriciDaniel/claude-blog) | MIT | 1 | rapidocms (1) |

### Licence

[Apache License 2.0](LICENSE) — Copyright 2026 BraindCode. Les skills importés
conservent leur licence d'origine (Apache 2.0 ou MIT), embarquée dans leur dossier.
