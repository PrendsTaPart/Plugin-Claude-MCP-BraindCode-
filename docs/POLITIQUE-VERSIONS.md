# Politique de versions et de distribution de la marketplace `rapido` (P5.2)

## Versionnement des plugins — semver

Chaque plugin porte sa version dans `<plugin>/.claude-plugin/plugin.json`
(`MAJEUR.MINEUR.CORRECTIF`), recopiée dans l'entrée correspondante de
`.claude-plugin/marketplace.json`. La CI échoue si les deux divergent
(`scripts/controles-supplementaires.py`, contrôle MARKETPLACE).

Quand incrémenter :

- **CORRECTIF** (x.y.Z) : faute, reformulation, précision d'un SKILL.md ou d'un
  README sans changement de comportement ; correction d'un hook sans changement
  de décision.
- **MINEUR** (x.Y.0) : nouveau skill, command, agent ou hook ; extension d'un
  garde-fou (nouvelles interceptions) ; nouveau volet MCP optionnel.
- **MAJEUR** (X.0.0) : suppression ou renommage d'un skill/command/agent
  (les phrases des utilisateurs cessent de déclencher) ; changement de
  comportement d'un garde-fou vers MOINS de protection ; nouveau serveur MCP
  **obligatoire**.

Un `0.x.y` signale un plugin en préversion/bêta (voir la mention « (bêta) » dans
sa description) : l'interface peut bouger sans passage MAJEUR.

Les champs d'une entrée marketplace : `name`, `source`, `description`,
`version`, `category`. Catégories harmonisées : `restaurant`, `ventes-crm`,
`contenu-marque`, `rh-projets`, `marketing-acquisition`, `media-ia`,
`app-automatisation`, `direction-finance`, `incubation`.

## Mode de distribution — git uniquement

Les `source` de `marketplace.json` sont des **chemins relatifs** (`./<plugin>`).
Ils ne résolvent que si la marketplace est ajoutée **via git** :

```
/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-   # GitHub
/plugin marketplace add <url git>                                     # GitLab/URL git
/plugin marketplace add ./<clone local>                               # test local
```

**La distribution par URL directe du JSON n'est PAS supportée** : servie seule,
`marketplace.json` pointe vers des `./…` qui n'existent pas chez le client, et
l'échec est silencieux. C'est un choix assumé — ne publiez pas l'URL brute du
fichier ; publiez l'URL du dépôt. Si un jour une distribution hors git devient
nécessaire, il faudra convertir les `source` en URLs git absolues par plugin.

## Rythme

- La version du dépôt (tags git, badge « dernière version ») suit les vagues de
  release documentées dans `RELEASE-NOTES.md`.
- Une PR qui modifie un plugin sans toucher sa version est acceptable pour un
  CORRECTIF cumulé ; la version est alors incrémentée au plus tard à la vague
  suivante.
