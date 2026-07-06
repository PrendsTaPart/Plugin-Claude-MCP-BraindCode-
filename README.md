# Marketplace Rapido — Plugins Claude Code

Marketplace Claude Code regroupant 5 plugins, chacun packageant des skills
par-dessus un serveur MCP existant.

## Structure

```
.                                        <- racine du dépôt = la marketplace
├── .claude-plugin/
│   └── marketplace.json                 <- catalogue racine (5 plugins)
├── foodeatup/                           <- Gestion restaurant (HACCP, salle, cuisine, achats)
│   ├── .claude-plugin/plugin.json
│   ├── .mcp.json                        <- connexion au serveur MCP FoodEatUp
│   ├── reference/                       <- règles partagées, chargées par les skills
│   │   ├── directives-outils.md         <- directives communes (IDs, confirmations…)
│   │   └── charte-graphique.md          <- (plugins à contenu visible uniquement)
│   └── skills/                          <- un sous-dossier par skill (SKILL.md)
├── rapidocrm/                           <- CRM : prospection, pipeline, facturation, marketing
├── rapidocms/                           <- Contenu & réseaux sociaux, cartes digitales
├── rapidorh/                            <- RH : projets, Kanban, dailies, onboarding
└── rapido-suite/                        <- Orchestration transverse des 4 MCP
```

Chaque plugin suit la même structure : `.claude-plugin/plugin.json`,
`.mcp.json` et `skills/`.

## Test en local (avant tout push GitHub)

Depuis le dossier parent du clone :

```
/plugin marketplace add ./rapido-plugins
/plugin install foodeatup@rapido
/reload-plugins
```

(`./rapido-plugins` = chemin vers le clone local de ce dépôt ; adaptez si le
dossier porte un autre nom.)

Puis vérifiez le déclenchement des skills avec les scénarios de test fournis
pour chaque plugin.

## À remplacer avant publication

- `owner.name` dans `.claude-plugin/marketplace.json`
- `author.name` dans chaque `plugin.json`
- Les sections `### À COMPLÉTER` des `reference/charte-graphique.md`
  (codes hex, URLs de logo, typographies, ton de voix)

## Fichiers de référence (progressive disclosure)

Chaque plugin embarque un dossier `reference/` (les règles voyagent AVEC le
plugin installé — pas de CLAUDE.md racine) :

- `directives-outils.md` (tous les plugins) : résolution d'ID avant action,
  confirmations obligatoires, interdiction d'inventer des données, locale
  euros/ISO, gestion d'erreur, récapitulatif final.
- `charte-graphique.md` (rapidocms, rapidocrm, rapido-suite) : couleurs hex,
  typographies, logos et variantes, ton de voix do/don't. Pour rapidocms et
  rapido-suite, les valeurs live `get_brand`/`get_company`/`get_profile` restent
  prioritaires ; le fichier sert de repli.

Chaque SKILL.md charge ces fichiers en « Étape 0 » via
`${CLAUDE_PLUGIN_ROOT}/reference/…` (chargés au besoin, pas dans le contexte de
base).

## Conventions des skills

- Frontmatter YAML : `name` (kebab-case, identique au nom du dossier) et
  `description` commençant par « Utiliser quand… » avec des déclencheurs concrets.
- Corps concis, workflow en étapes numérotées.
- Règles métier et garde-fous explicites (seuils, ordres d'appel,
  confirmation avant toute action destructrice).
- Les outils MCP sont référencés par leur nom réel.
- Langue : français.
