---
name: scale-rice-prioritization
description: "Utiliser quand l'utilisateur veut scorer et prioriser ses features avec la méthode RICE (parcours scale StartupsForge)."
---

# Rice Prioritization

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

RICE (Reach, Impact, Confidence, Effort) te donne un score objectif pour prioriser. Plus de débats sans fin sur 'quelle feature d'abord'. Les équipes RICE shippent 30% plus de valeur.

## Objectif

Scorer et prioriser tes features avec la méthode RICE.

## Livrable attendu

Tableau RICE avec toutes les features scorées et roadmap priorisée

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister les features candidates** — Backlog complet des idées et demandes
2. **Scorer le Reach** — Combien d'utilisateurs impactés par période ?
   > Prompt: Comment estimer le Reach d'une feature [DESCRIPTION] pour [PRODUIT] ?
3. **Scorer l'Impact** — Échelle 0.25 (minimal) à 3 (massif)
4. **Scorer la Confidence** — Certitude de tes estimations : 100%, 80%, 50%
5. **Estimer l'Effort** — En person-weeks ou story points

## Pro tips

- Le score RICE = (Reach × Impact × Confidence) ÷ Effort
- Sois honnête sur la Confidence - trop de 100% est suspect
- Révise les scores après chaque sprint

## Erreurs fréquentes

- Surestimer le Reach (tous les users vs users actifs)
- Confidence toujours à 100% (pas réaliste)
- Sous-estimer l'Effort (ajoute un buffer 30-50%)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-rice-prioritization.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
