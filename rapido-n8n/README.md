# rapido-n8n — Automatisations n8n sur l'instance du client

Automatisations n8n sur l'instance du client : usine à workflows (cycle SDK complet), recettes métier Rapido prêtes à déployer, surveillance des exécutions, mémoire opérationnelle — tâche ponctuelle = Claude, tâche récurrente = workflow n8n.

## Skills (4)

| Skill | Quand l'utiliser |
|---|---|
| `memoire-operationnelle` | Workflow a besoin d'une mémoire entre exécutions |
| `recettes-metier` | Besoin d'automatisation correspond à une recette métier Rapido connue |
| `surveillance-automatisations` | Si ses automatisations tournent ou parle d'erreurs de workflows |
| `usine-automatisations` | Automatiser quelque chose, créer un workflow, ou dit |

## Agents (1)

- **`architecte-automatisations`** — Architecte des automatisations (n8n).

## Serveurs MCP requis

`n8n`, `foodeatup`, `rapidocms`, `rapidocrm`, `rapidorh` — connexion et clés : voir « Prérequis & connecteurs » du [README racine](../README.md). Aucune clé n'est stockée dans le dépôt.

## Déclencheurs (exemples réels)

- « tous les jours / à chaque fois, fais… »

## Version & conventions

v1.6.0 — historique dans [CHANGELOG.md](CHANGELOG.md). Skills en français (« Utiliser quand… »), calculs par script stdlib, garde-fous déterministes, rien d'inventé (KB `./rapido-kb/` prioritaire).
