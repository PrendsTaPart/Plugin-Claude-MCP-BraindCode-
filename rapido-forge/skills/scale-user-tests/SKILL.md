---
name: scale-user-tests
description: "Utiliser quand l'utilisateur veut recruter et observer 5 personnes utilisant son produit/prototype (parcours scale StartupsForge)."
---

# User Tests

**Catégorie** : Scale  
**Durée** : 180 min

## Pourquoi

5 tests utilisateurs révèlent 85% des problèmes d'usabilité. C'est le ROI le plus élevé de tout investissement UX. Ne pas tester = construire à l'aveugle.

## Objectif

Recruter et observer 5 personnes utilisant ton produit/prototype.

## Livrable attendu

Rapport de tests avec insights, pain points et recommandations

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Recruter les participants** — 5 personnes correspondant au persona, pas d'amis/famille
2. **Préparer le script** — Scénarios de tâches, questions à poser, métriques
   > Prompt: Crée un script de test utilisateur pour tester [FONCTIONNALITÉ] avec [PERSONA]
3. **Conduire les sessions** — 30-45 min, penser à voix haute, observer sans guider
4. **Analyser les résultats** — Patterns récurrents, pain points, succès
5. **Prioriser les améliorations** — Quick fixes vs refonte, impact vs effort

## Pro tips

- 5 utilisateurs suffisent pour la plupart des problèmes
- Pose des tâches, pas des questions ('Achète ce produit' vs 'Où iriez-vous pour acheter ?')
- Le silence est ton ami - résiste à l'envie d'aider

## Erreurs fréquentes

- Tester avec des amis ou collègues (biais)
- Guider les participants au lieu d'observer
- Ne pas enregistrer les sessions

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-user-tests.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:mom-test` — plan de recherche et tests d'utilisabilité
