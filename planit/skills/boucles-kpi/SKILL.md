---
name: boucles-kpi
description: Utiliser quand une routine se mesure, que l'utilisateur dit « est-ce que cette routine sert à quelque chose », « rattache un KPI à la routine », « où en sont mes boucles », « repars d'une nouvelle référence ». Monte et lit les boucles routine ↔ KPI — référence figée au rattachement, verdict seulement après 3 exécutions ET 14 jours.
---

# Boucles KPI (le loop engineering Plan'It)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **`list_kpi_catalog`** — le KPI candidat : formule, unité, sens de
   lecture, connecteur (connecté ?), coût de collecte.
2. **`attach_kpi_to_routine`** (routine seulement — une tâche simple
   refuse) : rôle `target` (le KPI que la routine doit faire bouger) ou
   `watch` (effet de bord surveillé). PRÉVENIR : la valeur de référence se
   FIGE maintenant depuis le dernier relevé, et s'il n'y en a aucun, une
   collecte est provoquée — qui peut coûter des crédits pour un KPI métier.
3. **`list_active_loops`** — chaque boucle : référence figée, valeur
   courante, écart ORIENTÉ (une baisse d'un coût est un progrès), tours,
   crédits consommés, verdict.
4. **`evaluate_loops`** — verdict à l'instant : improving / flat / degrading,
   ou **not_enough_data tant que < 3 exécutions ET < 14 jours** — dans ce
   cas on dit « pas assez de données », on n'annonce RIEN d'autre.
5. **Repartir d'une nouvelle référence** : `detach_kpi_from_routine` (la
   boucle, sa référence et son verdict disparaissent — la routine et le KPI
   restent) puis `attach_kpi_to_routine` à nouveau.
6. Mise en page : widget `boucles-kpi` (mention « pas assez de données »
   explicite).

## Garde-fous

- La référence figée ne se « corrige » pas : elle se refige par
  detach/attach, en le disant.
- Les verdicts viennent du serveur — jamais un « ça a l'air de marcher » sur
  une courbe lue de tête.
- Le hook verite-des-donnees rappelle la règle à chaque not_enough_data.
