# Contribuer à la marketplace Rapido

Merci de contribuer ! Ce dépôt est un PRODUIT distribué à tous les clients
Rapido : chaque contribution doit rester portable (aucune donnée propre à une
entreprise) et vérifiable (aucun outil ni chiffre inventé). Les skills et
agents s'écrivent en français.

## Proposer un skill

Un skill vit dans le plugin auquel il appartient :

```
<plugin>/skills/<nom-du-skill>/
├── SKILL.md            # obligatoire
├── scripts/            # optionnel — calculs en Python stdlib
└── reference/          # optionnel — annexes chargées à la demande
```

**Frontmatter obligatoire** du `SKILL.md` :

```yaml
---
name: nom-du-skill          # kebab-case, IDENTIQUE au nom du dossier
description: Utiliser quand l'utilisateur veut … # en français, déclencheurs concrets
---
```

- La `description` commence par **« Utiliser quand… »** et liste des
  déclencheurs concrets (les formulations réelles d'un utilisateur), puis
  résume ce que le skill produit. C'est elle qui route la demande : sans
  déclencheurs précis, le skill ne se déclenchera jamais — ou se déclenchera
  à la place d'un autre.
- Le `name` est unique dans le plugin (aucun doublon, y compris avec les
  agents).
- Corps du skill : une « Étape 0 » qui charge
  `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et la KB
  (`./rapido-kb/`) si pertinent, un **workflow numéroté**, des règles métier
  explicites et une section pièges si l'outil en a.
- **Tout outil MCP cité existe réellement** : nom vérifié sur le schéma du
  serveur avant d'écrire (jamais de mémoire). Un outil manquant se signale,
  il ne s'invente pas.
- Tout calcul passe par un script embarqué (`scripts/`, Python stdlib, sans
  réseau) — jamais de calcul de tête.
- Incrémenter la `version` du `plugin.json` et ajouter une entrée datée en
  tête du `CHANGELOG.md` du plugin.

**Skill importé d'un dépôt open source** : copier la LICENSE de la source
dans le dossier du skill, documenter provenance/commit/modifications dans
l'`ATTRIBUTIONS.md` du plugin, renommer en cas de collision de `name`, et
purger les artefacts (`__pycache__/`, `*.pyc`, `node_modules/`, `.DS_Store`).

## Proposer un plugin

```
<plugin>/
├── .claude-plugin/plugin.json   # name (slug), version, description, author
├── .mcp.json                    # serveurs MCP requis
├── skills/  agents/  hooks/  reference/
├── CHANGELOG.md
└── ATTRIBUTIONS.md              # si skills externes
```

- **Le slug (`name`) est IMMUABLE une fois publié** — le renommer casse les
  installations. Pour renommer : nouveau plugin + dépréciation de l'ancien.
- Ajouter l'entrée du plugin dans `.claude-plugin/marketplace.json`.
- **Portabilité obligatoire** : aucune URL d'instance ni identifiant client
  en dur — URLs produit uniquement dans `.mcp.json`, variables
  d'environnement (`${N8N_MCP_URL}`) pour les instances des clients, toute
  personnalisation dans `./rapido-kb/` (répertoire de travail du client,
  jamais dans le plugin).
- Un serveur MCP optionnel absent déclenche une **dégradation propre**
  (explication + marche à suivre), jamais une erreur brute.
- Les actions destructrices, irréversibles ou payantes sont couvertes par un
  hook déterministe (`hooks/hooks.json` + script testé, stdin JSON,
  allow/ask/deny, < 1 s, aucun appel réseau).

## Principe de conception : anti-donnée-inventée

C'est LA règle transverse du dépôt, à respecter dans tout skill et tout
agent :

- Chaque donnée métier (prix, chiffre, date, nom, seuil) vient d'un outil
  MCP, de la KB `./rapido-kb/` ou de l'utilisateur — **jamais de mémoire du
  modèle**.
- Une donnée indisponible se dit (« pas de visibilité sur X ») ou se marque
  `### À COMPLÉTER` — elle ne s'estime pas et ne se comble pas par une
  hypothèse.
- Les valeurs par défaut d'un skill sont des standards du secteur, signalés
  comme tels, et la KB du client PRIME toujours dessus.
- En dernier filet, des hooks déterministes refusent les valeurs
  invraisemblables (ex. température hors −30/+90 °C) : ne jamais les
  affaiblir pour « faire passer » un cas.

## Avant toute pull request

1. **Obligatoire : `python3 scripts/valider-plugins.py` puis
   `python3 scripts/tester-skills.py`** doivent passer sans erreur ni FAIL
   (JSON valides, frontmatters `name`+`description`, unicité des `name`,
   artefacts, licences des skills externes ; puis convention « Utiliser
   quand… », placeholders, chemins `${CLAUDE_PLUGIN_ROOT}`, scripts
   compilables, skills mentionnés existants, cohérence MCP, hooks testés sur
   stdin). Les INFO — outils de serveurs à catalogue distant — sont attendus
   et tracés dans `tests/rapports/outils-a-verifier-en-ligne.md`. La CI
   (`.github/workflows/validation.yml`) rejoue ces contrôles à chaque push et
   pull request.
2. Dérouler les évals de `tests/evals.md` quand la contribution touche la KB
   ou le routage.
3. Messages de commit au format
   [Conventional Commits](https://www.conventionalcommits.org/fr/) —
   ex. `feat(rapidocms): skill funnel-tofu-mofu-bofu`.
4. Version + CHANGELOG à jour pour chaque plugin modifié.

Voir aussi [SECURITY.md](SECURITY.md) — les contributions qui affaiblissent
un hook de garde sont refusées.
