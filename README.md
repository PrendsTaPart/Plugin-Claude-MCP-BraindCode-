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
- Les URL `REMPLACER` dans chaque `.mcp.json` (endpoints des serveurs MCP)

## Conventions des skills

- Frontmatter YAML : `name` (kebab-case, identique au nom du dossier) et
  `description` commençant par « Utiliser quand… » avec des déclencheurs concrets.
- Corps concis, workflow en étapes numérotées.
- Règles métier et garde-fous explicites (seuils, ordres d'appel,
  confirmation avant toute action destructrice).
- Les outils MCP sont référencés par leur nom réel.
- Langue : français.
