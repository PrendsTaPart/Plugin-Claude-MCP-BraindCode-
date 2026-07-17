---
name: amelioration-des-routines
description: Utiliser quand l'utilisateur veut améliorer une routine sur la base de ses résultats, mesurer si ses routines servent encore, ou arbitrer lesquelles garder — « améliore la routine {X} », « la boucle d'amélioration », « est-ce que mes routines servent », « tribunal des routines ». Mesure réelle (MCP), calcule par script (formule affichée), juge sur seuils KB, ajuste UNE variable confirmée, journalise avant/après.
---

# Amélioration des routines — le Loop Engineering qui s'améliore lui-même

Ce skill applique le **protocole boucle d'amélioration** à une routine (ou à toutes,
en mode tribunal) : **mesurer → calculer → juger → ajuster (une variable) → journaliser**.

## Étape 0 — Références (obligatoire)

Charger et appliquer :
- `${CLAUDE_PLUGIN_ROOT}/reference/boucle-amelioration.md` — le protocole en 5 temps
  et la **règle d'or (une variable à la fois)**.
- `${CLAUDE_PLUGIN_ROOT}/reference/autonomie.md` — niveaux (1 proposé · 2 confirmé ·
  **3 jamais** en boucle).
- `./rapido-kb/startup/routines-journal.md` — la mémoire (occurrences, avant/après).
- `./rapido-kb/processus-internes.md` — les seuils de décision (défauts :
  `reference/seuils-defaut.md`, cités comme tels ; **seuil absent = proposé, jamais inventé**).

## 1. Améliorer UNE routine — « améliore la routine {X} »

1. **Charger la fiche d'amélioration** de la routine visée dans
   `data/prompts-collections/boucles.json` (**la fiche fait foi** : KPI, formule,
   requêtes MCP, période). Pas de fiche → le dire, ne pas improviser de KPI.
2. **Exécuter les 5 temps** (`boucle-amelioration.md`) :
   - **MESURER** — seulement les requêtes MCP de la fiche, périodes comparables.
     Donnée indisponible → **« pas de visibilité sur {X} »** + entrée
     `docs/OUTILS-MCP-MANQUANTS.md` ; un proxy est **annoncé comme tel**, jamais silencieux.
   - **CALCULER** — skill `catalogue-kpi` (scripts/calcul_kpi.py), **formule affichée**,
     médiane si asymétrie (jamais moyenner en silence).
   - **JUGER** — seuil KB (ou proposé d'abord si absent).
   - **AJUSTER** — **UNE** variable (seuil · heure · fréquence · ton · ciblage · prompt
     de tâche relais · workflow n8n via `rapido-n8n:surveillance-automatisations`),
     ancienne → nouvelle annoncée.
     Niveau 1 proposé, niveau 2 appliqué après confirmation, **niveau 3 jamais**.
     **Deux modifications demandées = refus motivé** (« une à la fois »), séquencées.
   - **JOURNALISER** — `routines-journal.md` : routine, KPI avant, modification, **date de
     re-mesure**.

## 2. Mode TRIBUNAL — trimestriel (« tribunal des routines », « est-ce que mes routines servent »)

Passer **TOUTES les routines actives** au crible, chacune sur trois questions :
- **Utilisée ?** — occurrences au journal (`routines-journal.md`).
- **Utile ?** — son KPI de fiche vs son seuil.
- **Coûteuse ?** — temps de session / crédits consommés.

Puis un **verdict proposé par routine** : **garder / ajuster** (dire laquelle des variables)
**/ suspendre**. **La décision revient à l'utilisateur**, routine par routine.
Rappeler la règle : *une routine qu'on n'ajuste jamais est une routine qu'on ne regarde plus.*

## Garde-fous

- **Une variable à la fois** — sinon la re-mesure est ininterprétable.
- **Mesure réelle ou « pas de visibilité »** : aucun proxy silencieux, aucun KPI de tête,
  aucun seuil inventé.
- **Niveau 3 jamais** en boucle ; toute écriture (niveau 2) est confirmée et récapitulée (IDs).
- Toute boucle laisse une trace datée (avant → modification → re-mesure) au journal.
