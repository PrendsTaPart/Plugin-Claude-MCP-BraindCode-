---
name: scale-impact-effort
description: "Utiliser quand l'utilisateur veut placer toutes ses idées sur la matrice et identifier les Quick Wins (parcours scale StartupsForge)."
---

# Impact Effort

**Catégorie** : Scale  
**Durée** : 30 min

## Pourquoi

La matrice Impact/Effort révèle les Quick Wins (haut impact, faible effort) à saisir immédiatement. C'est la priorisation la plus simple et la plus visuelle.

## Objectif

Placer toutes tes idées sur la matrice et identifier les Quick Wins.

## Livrable attendu

Matrice 2x2 avec features placées et plan d'action par quadrant

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister les initiatives** — Features, améliorations, bugs, dettes techniques
2. **Définir les critères** — Impact = valeur business/user, Effort = temps/ressources
3. **Placer sur la matrice** — Chaque item dans un des 4 quadrants
   > Prompt: Comment évaluer l'impact de [FEATURE] pour [TYPE D'UTILISATEUR] ?
4. **Nommer les quadrants** — Quick Wins (HI/LE), Big Bets (HI/HE), Fill-ins (LI/LE), Money Pits (LI/HE)
5. **Définir l'action par quadrant** — QW → Faire, BB → Planifier, FI → Quand dispo, MP → Éviter

## Pro tips

- Les Quick Wins devraient être dans ton sprint actuel
- Challenge les items 'Big Bet' - peuvent-ils être découpés en Quick Wins ?
- Supprime les Money Pits du backlog (ils encombrent)

## Erreurs fréquentes

- Tout mettre en haut à gauche (pas réaliste)
- Confondre effort de développement et effort total (test, doc, deploy)
- Ne pas réviser la matrice régulièrement

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-impact-effort.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
