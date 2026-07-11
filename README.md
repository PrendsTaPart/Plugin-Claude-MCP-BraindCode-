# Marketplace Rapido — Plugins Claude Code

Marketplace de plugins Claude Code pour les systèmes Rapido (FoodEatUp,
RapidoCRM, RapidoCMS, RapidoRh) et leurs outils satellites (Canva, Lovable,
Meta Ads, n8n, Google Workspace) : des skills métier, des agents et des
garde-fous déterministes par-dessus vos serveurs MCP, pour piloter une
entreprise de A à Z.

![validation](https://github.com/PrendsTaPart/Plugin-Claude-MCP-BraindCode-/actions/workflows/validation.yml/badge.svg)
![Plugins](https://img.shields.io/badge/plugins-12-blue)
![Skills](https://img.shields.io/badge/skills-299-brightgreen)
![Licence](https://img.shields.io/badge/licence-Apache%202.0-blue)

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
| `foodeatup` | 1.4.0 | 15 | 2 | foodeatup | — |
| `rapidocrm` | 1.3.0 | 21 | 2 | rapidocrm | — |
| `rapidocms` | 1.4.0 | 19 | 5 | rapidocms, hyperframes | — |
| `rapidorh` | 1.0.0 | 11 | 2 | rapidorh | — |
| `rapido-suite` | 1.1.0 | 11 | 1 | rapidocrm, rapidocms, rapidorh, foodeatup, lovable, facebook-ads, n8n | `N8N_MCP_URL` (optionnel) |
| `rapido-canva` | 1.0.0 | 7 | 1 | canva, foodeatup, rapidocms, rapidocrm, rapidorh | — |
| `rapido-lovable` | 1.1.0 | 8 | 1 | lovable, foodeatup, rapidocms, rapidocrm, rapidorh | — |
| `rapido-meta-ads` | 1.0.0 | 13 | 1 | facebook-ads, rapidocms, rapidocrm, canva, lovable | — |
| `rapido-n8n` | 1.1.0 | 4 | 1 | n8n, foodeatup, rapidocms, rapidocrm, rapidorh | `N8N_MCP_URL` |
| `rapido-direction` | 1.1.0 | 5 | 1 | gmail, google-calendar, google-drive, rapidocrm, foodeatup, n8n | `N8N_MCP_URL` |
| `rapido-startup` | 1.7.0 | 5 | 2 | stripe, rapidocrm, rapidocms, rapidorh, foodeatup, google-calendar | — |
| `rapido-forge` | 1.0.0 | 180 | 4 | rapidocrm, rapidocms, rapidorh | — |

**Total : 12 plugins, 299 skills, 23 agents.** (`rapido-startup` — finance &
création de startup : interview BP, KPI, prévisionnel, exécution, routines
Loop Engine R4-R8, avec les 2 agents les plus récents : coach-startup +
cfo-virtuel.)

Nouveau : **`rapido-forge`** (StartupsForge / PrendsTaPart) — 180 exercices
d'incubateur en 3 parcours (bootcamp 5 jours, roadmap idéation, roadmap
scale) pilotés par un directeur de programme et 3 mentors ; livrables dans
`./rapido-kb/startup/forge/`, exécution réelle déléguée aux plugins métier.

Nouveautés de la vague du 2026-07-10 : `gestion-marques` + agent
`gestionnaire-marques` (rapidocms, multi-enseignes), `animation-client` et
`gestion-depenses` (rapidocrm), `coordination-cuisine` (foodeatup, écran
cuisine KDS), routine `R9-VIDEO-FACTORY` (rapido-startup, épisode vidéo du
jour) — et l'audit de vérité clos : 100 % des outils des 3 serveurs Rapido
couverts ou ignorés volontairement avec raison
(`reference/audit-tools-2026-07-10.md`).

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
   ```
   …puis rapidorh, rapido-direction, rapido-startup, rapido-canva,
   rapido-lovable, rapido-meta-ads, rapido-n8n selon vos usages (tableau
   ci-dessus).
4. **Recharger** : `/reload-plugins` (ou relancer Claude Code).

Test en local depuis un clone : `/plugin marketplace add ./<dossier-du-clone>`
depuis le dossier parent, puis les mêmes `install`.

## Connecter les serveurs MCP

Chaque plugin déclare ses serveurs dans son `.mcp.json` — **vous vous
connectez à VOS comptes**, rien n'est partagé :

| Serveur | Comment se connecter |
|---|---|
| **FoodEatUp, RapidoCRM, RapidoCMS, RapidoRh** | Rien à configurer : à la première utilisation, Claude Code ouvre l'authentification du serveur — connectez-vous avec VOTRE compte Rapido. Vérifiez l'état avec `/mcp`. |
| **Google (Gmail, Calendar, Drive)** — rapido-direction | OAuth individuel au premier usage (Gmail est volontairement « brouillons seulement » : rien ne part sans vous). Guide : `rapido-direction/README-installation.md`. |
| **n8n** — rapido-n8n, rapido-direction, rapido-suite (optionnel) | Exportez l'URL MCP de VOTRE instance avant de lancer Claude Code : `export N8N_MCP_URL=https://<votre-instance>/mcp-server/http`. Guide : `rapido-n8n/README-installation.md`. Sans elle, les volets n8n se sautent proprement. |
| **Stripe** — rapido-startup | Connecteur officiel `https://mcp.stripe.com` (OAuth au premier usage). Lecture d'abord ; toute écriture est bloquée en routine et confirmée hors routine. |
| **Canva, Lovable, Meta Ads, HyperFrames** | Connecteurs OAuth respectifs au premier usage (comptes Canva/Lovable/Meta/HeyGen). |

**Règle générale** : un serveur optionnel non connecté ne casse rien — le
skill saute le volet EN LE DISANT (dégradation propre). `/mcp` dans Claude
Code montre l'état de chaque connexion.

## Comment l'utiliser

**Premier lancement — construisez votre base de connaissance** (recommandé) :

> « Apprends à connaître mon entreprise »

L'onboarding (rapido-suite) vous interviewe et construit `./rapido-kb/`
dans VOTRE répertoire de travail : seuils maison, charte graphique, ton,
personas, processus. Tous les plugins la lisent ensuite en priorité — c'est
elle qui fait passer les skills du générique au sur-mesure. Kit de
démarrage : [`rapido-kb-template/`](rapido-kb-template/) (8 fichiers
vierges + mégaprompt `PROMPT-CLAUDE-CODE-MASTER.md` + bibliothèque de
prompts testés `PROMPTS-CLAUDE-CODE.md`). Cette KB reste chez vous — jamais
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
| « Lance R7 » / « surveille ma trésorerie » | rapido-startup : sentinelle cash — runway calculé par script, alerte seulement, zéro écriture |
| « Automatise l'envoi du récap hebdo » | rapido-n8n : workflow validé et testé AVANT publication, production sous confirmation |

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

S'y ajoutent des hooks `Stop` (récapitulatif des écritures avec IDs exigé en
fin de tour) et `SessionStart` (détection de `./rapido-kb/` et rappel des
directives). Jamais de secrets dans les skills ou `reference/` — ils sont
distribués avec le plugin.

## Skills tiers et attributions

41 des 109 skills sont importés de dépôts open source, adaptés aux
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
