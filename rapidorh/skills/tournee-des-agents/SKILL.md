---
name: tournee-des-agents
description: Utiliser quand l'utilisateur veut exécuter les tâches du jour confiées aux agents sur le Kanban RapidoRh — « fais la tournée des agents », « réalise les tâches du jour », « exécute les tâches IA d'aujourd'hui ». Lit chaque tâche À faire assignée à un agent, exécute le prompt de son relais dans la limite de son niveau d'autonomie, déplace la carte et rend un récap. Ne jamais exécuter un niveau 3 ni une tâche au relais absent/ambigu.
---

# Tournée des agents — exécuter les tâches du jour, dans les limites d'autonomie

Ce skill parcourt les tâches Kanban **du jour** confiées à des **agents** et les
exécute **au niveau d'autonomie déclaré**, sans jamais dépasser ce plafond ni
inventer un ordre manquant.

## Étape 0 — Références (obligatoire)

Charger et appliquer :
- `${CLAUDE_PLUGIN_ROOT}/reference/relais-par-tache.md` — le contrat de chaque tâche
  (assignation, bloc RELAIS dans la `description`, garde-fous).
- `${CLAUDE_PLUGIN_ROOT}/reference/autonomie.md` — les 4 niveaux et le comportement
  **en tournée** (0-1 = Fait · 2 = Validation · 3 = jamais).
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` — IDs réels, rien d'inventé, récap final.

## 1. Lister les tâches du jour assignées aux agents

1. `get-projects-list-tool` → les projets concernés (par nom si besoin).
2. Pour chaque projet : `get-task-lists-tool` (IDs réels des colonnes) puis
   `get-project-tasks-tool` → tâches en colonne **« À faire »** (Todo).
3. Ne garder que les tâches **du jour** (`due_date` = aujourd'hui, ou non datées à
   traiter selon la demande) **et assignées à un agent** :
   - `assigned_users` = un utilisateur-agent (si RH V2), **ou**
   - titre préfixé `[AGENT:{nom}]`.
4. Aucune tâche agent aujourd'hui → le dire et s'arrêter (récap vide).

## 2. Pour CHAQUE tâche — lire, vérifier, exécuter, déplacer

Dans l'ordre, sans en sauter :

1. **Lire le relais** dans la `description` : `PROMPT`, `LIVRABLE`, `DONE`,
   `AUTONOMIE`, `ROUTINE`.
2. **Blocage si relais absent/ambigu** — pas de bloc RELAIS, `PROMPT` manquant,
   `{placeholder}` non résolu, ou `AUTONOMIE` illisible → **carte laissée en place**,
   consignée **bloquée** au récap (avec la raison), **JAMAIS d'interprétation inventée**.
3. **Vérifier le niveau d'autonomie** (`reference/autonomie.md`) :
   - **niveau 3** → **jamais exécuté en tournée** : préparer ce qui est préparable et
     **signaler** ; carte → **Validation**, mention explicite au récap.
   - **niveau 2** (écriture confirmée) → **préparer** l'écriture, **ne pas écrire** sans
     confirmation ; carte → **Validation**.
   - **niveau 0-1** → exécutable en tournée.
4. **Déléguer** l'exécution du `PROMPT` au skill ou à l'agent compétent — celui nommé
   dans `[AGENT:{nom}]`, sinon celui qu'impose le besoin. La tournée **orchestre**, elle
   ne réimplémente pas le métier.
5. **Consigner le résultat** : au **récap de tournée** (RapidoRh n'expose ni outil de
   commentaire ni mise à jour de tâche — cf. `relais-par-tache.md`). Si RH V2 expose un
   commentaire/mise à jour de tâche, y écrire aussi le résultat et l'ID.
6. **Déplacer la carte** (`move-task-tool`, `from_list` = colonne réelle actuelle) :
   - **Fait** si niveau 0-1 terminé conformément au `DONE` ;
   - **Validation** si écriture confirmée requise (niveau 2) ou niveau 3 préparé.
   - Colonne « Validation » absente du projet → laisser en « À faire »/« En cours » et
     le **signaler au récap** (ne pas inventer de colonne ; cf. `flux-kanban`).

## 3. Récap final (obligatoire)

Terminer par trois listes, avec les **IDs réels** :
- **Faites** — tâche, agent, livrable, colonne (Fait).
- **En validation** — tâche, ce qui est préparé, pourquoi une confirmation est requise
  (niveau 2/3), colonne (Validation).
- **Bloquées** — tâche, raison du blocage (relais absent/ambigu), colonne inchangée.

## Garde-fous

- **Niveau 3 = jamais en tournée.** Aucune exception : préparer et signaler.
- **Pas de brief lisible = blocage**, pas d'interprétation.
- **Colonnes et IDs réels** : lire les colonnes via `get-task-lists-tool`, ne jamais
  deviner un `tasklist_id` ni une colonne « Validation » qui n'existe pas.
- **Rien d'inventé** : un `PROMPT` incomplet ne se complète pas, il se bloque.
