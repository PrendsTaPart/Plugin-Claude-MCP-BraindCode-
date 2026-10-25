---
name: comprendre-l-orchestrateur
description: Utiliser quand on veut savoir comment Plan'It traiterait une demande, que l'utilisateur dit « comment l'orchestrateur traiterait ça », « quels outils il prendrait pour… », « est-ce que mon connecteur serait mobilisé ». Interroge le routeur sans rien exécuter et compare avec la sélection d'outils.
---

# Comprendre l'orchestrateur (expliquer sans exécuter)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`route_orchestrator`** sur la demande en langage naturel — les outils
   que l'orchestrateur retiendrait, SANS les exécuter. Répond à « comment ma
   demande serait traitée » et « mon connecteur serait-il mobilisé ».
2. **Comparer** avec **`select_routine_tools`** sur la même consigne
   (jusqu'à trois minutes — prévenir) : la sélection scorée destinée aux
   routines. Les écarts entre les deux se constatent et s'expliquent
   (le routeur répond à une demande ponctuelle, la sélection outille une
   routine durable).
3. **Conclure** : si l'utilisateur veut en faire une routine → skill
   `creer-une-routine` avec la sélection ; s'il manque un connecteur →
   skill `connecteurs-mcp`.

## Garde-fous

- Rien ne s'exécute ici : c'est un banc d'essai de compréhension.
- Les outils cités sont ceux des réponses — jamais complétés de mémoire.
