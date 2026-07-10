# Marketplace Rapido — Plugins Claude Code

Marketplace de plugins Claude Code pour les systèmes Rapido (FoodEatUp,
RapidoCRM, RapidoCMS, RapidoRh) et leurs outils satellites (Canva, Lovable,
Meta Ads, n8n, Google Workspace) : des skills métier, des agents et des
garde-fous déterministes par-dessus vos serveurs MCP, pour piloter une
entreprise de A à Z.

![validation](https://github.com/PrendsTaPart/Plugin-Claude-MCP-BraindCode-/actions/workflows/validation.yml/badge.svg)
![Plugins](https://img.shields.io/badge/plugins-11-blue)
![Skills](https://img.shields.io/badge/skills-112-brightgreen)
![Licence](https://img.shields.io/badge/licence-Apache%202.0-blue)

## Les plugins

Chiffres lus depuis les fichiers du dépôt : version dans
`<plugin>/.claude-plugin/plugin.json`, skills = dossiers contenant un
`SKILL.md`, agents = fichiers `agents/*.md`, serveurs depuis
`<plugin>/.mcp.json`.

| Plugin | Version | Skills | Agents | Serveurs MCP requis | Variables d'env |
|---|---|---|---|---|---|
| `foodeatup` | 1.0.0 | 14 | 2 | foodeatup | — |
| `rapidocrm` | 1.0.0 | 19 | 2 | rapidocrm | — |
| `rapidocms` | 1.0.0 | 16 | 4 | rapidocms, hyperframes | — |
| `rapidorh` | 1.0.0 | 11 | 2 | rapidorh | — |
| `rapido-suite` | 1.0.0 | 11 | 1 | rapidocrm, rapidocms, rapidorh, foodeatup | — |
| `rapido-canva` | 1.0.0 | 7 | 1 | canva, foodeatup, rapidocms, rapidocrm, rapidorh | — |
| `rapido-lovable` | 1.0.0 | 8 | 0 | lovable, foodeatup, rapidocms, rapidocrm, rapidorh | — |
| `rapido-meta-ads` | 1.0.0 | 13 | 1 | facebook-ads, rapidocms, rapidocrm, canva, lovable | — |
| `rapido-n8n` | 1.0.0 | 4 | 0 | n8n, foodeatup, rapidocms, rapidocrm, rapidorh | `N8N_MCP_URL` |
| `rapido-direction` | 1.0.1 | 5 | 1 | gmail, google-calendar, google-drive, rapidocrm, foodeatup, n8n | `N8N_MCP_URL` |
| `rapido-startup` | 1.4.0 | 4 | 1 | stripe, rapidocrm, rapidocms, rapidorh, foodeatup, google-calendar | — |

**Total : 11 plugins, 112 skills, 15 agents.** (`rapido-startup` — finance &
création de startup : interview business plan + coach, autres skills à venir.)

## Démarrage rapide

```
/plugin marketplace add <org>/rapido-plugins
/plugin install rapido-suite@rapido
/reload-plugins
```

Remplacer `<org>` par l'organisation GitHub qui héberge ce dépôt, puis
installer les plugins dont vous avez besoin (`/plugin install <nom>@rapido`).
Premier lancement recommandé : « apprends à connaître mon entreprise » —
l'onboarding (rapido-suite) construit `./rapido-kb/`, la base de connaissance
qui personnalise tous les plugins.

**Kit de démarrage — [`rapido-kb-template/`](rapido-kb-template/)** : le
template vierge de la base de connaissance (8 fichiers à copier dans VOTRE
répertoire de travail sous le nom `rapido-kb/`, puis à committer dans VOTRE
git — jamais dans ce dépôt), accompagné du mégaprompt de démarrage
(`PROMPT-CLAUDE-CODE-MASTER.md`), d'une bibliothèque de prompts testés par
domaine (`PROMPTS-CLAUDE-CODE.md`) et d'un prompt de site vitrine Lovable
(`PROMPT-LOVABLE-SITE.md`). Mode d'emploi : `rapido-kb-template/README.md`.

**Prérequis :**

- **Claude Code** (CLI, desktop ou web) — https://code.claude.com/docs
- **Comptes Rapido** : chaque utilisateur se connecte à SON compte FoodEatUp /
  RapidoCRM / RapidoCMS / RapidoRh (URLs produit dans les `.mcp.json`,
  authentification individuelle).
- **`N8N_MCP_URL`** — seule variable d'environnement détectée dans le dépôt,
  requise pour `rapido-n8n` et le volet automatisations de `rapido-direction` :
  URL du serveur MCP de VOTRE instance n8n, à exporter avant de lancer
  Claude Code (`export N8N_MCP_URL=https://<votre-instance>/mcp-server/http`,
  guide : `rapido-n8n/README-installation.md`). Sans elle, ces plugins
  dégradent proprement.
- **Comptes tiers selon les plugins** : Canva, Lovable, Meta Ads et
  HyperFrames via leurs connecteurs ; Google (Gmail, Calendar, Drive) via
  OAuth individuel au premier usage
  (`rapido-direction/README-installation.md`).
- `GITHUB_TOKEN` — uniquement si ce dépôt est hébergé en privé (mises à jour
  automatiques de la marketplace).

Test en local avant tout push : `/plugin marketplace add ./rapido-plugins`
depuis le dossier parent du clone, puis les mêmes `install`.

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

40 des 108 skills sont importés de dépôts open source, adaptés aux
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
