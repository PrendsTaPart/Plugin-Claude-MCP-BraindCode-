---
name: projet-rh-lead-magnet
description: Utiliser quand l'utilisateur veut organiser la campagne lead magnet dans RapidoRH — « crée les tâches du lead magnet », « projet RH de la campagne », « organise la campagne dans RapidoRH ». Crée le projet, les colonnes Kanban et les ~20 tâches du parcours, affectées aux agents IA (users RH) ou en fallback humain. À NE PAS utiliser pour fabriquer/diffuser (les autres skills du plugin).
---

# Projet RH du lead magnet

Matérialise la campagne dans RapidoRH : un projet, un Kanban, ~20 tâches (une par
livrable du parcours), **affectées aux agents IA** quand ils existent en RH.

## Étape 0 — contexte

Lire `reference/parcours-lead-magnet.md` (les 9 étapes = la source des tâches) et
`reference/garde-fous-leadmagnet.md`. Récupérer le projet/colonnes via
`rapido-kb/`. Nom du lead magnet requis (slug).

## 1. Projet + Kanban

Déléguer à `rapidorh:setup-projet` (ou `create-project-tool` +
`create-task-list-tool`) : projet « **LM — {nom}** » avec colonnes **À faire / En
cours / Validation / Fait**. Récupérer les `tasklist_id` via `get-task-lists-tool`.

## 2. Les ~20 tâches (une par livrable du parcours)

Créer via `create-task-tool` (une tâche par livrable des 9 étapes), chacune avec un
**critère de done** repris du parcours. Exemples (à adapter) :

- **Conception** : valider la sortie `lead-magnet-machine` (problème/type/format/nom).
- **Fabrication** : rédiger le contenu · passer le gate qualité · mettre en page le PDF
  brandé · publier dans la bibliothèque + vérifier l'URL.
- **Page** : copy de landing · construire la landing Lovable · brancher segment +
  pipeline · email de livraison · **test de bout en bout**.
- **Organique** : campagne CMS · 4 posts · post LinkedIn (semi-auto).
- **Payant** : vidéo (self_ai_disclosure) · visuels ads · campagne Meta **PAUSED**.
- **Nurturing** : séquence J2/J5 (gate délivrabilité).
- **Mesure** : rapport J+7 · rapport J+30.

## 3. Affectation aux agents IA (résolution dynamique)

Résoudre les agents via `get-users-list-tool` : repérer les **users IA** (nom
`🤖`/`🧠`, email `@braindcode.ai`) et récupérer leur **ID**. Assigner par
`assigned_users:[id]` selon le type de tâche : contenu/visuels → **Agent CMS** ;
CRM/pipeline → **Agent CRM** ; coordination → **Agent Orchestrateur** ; RH → **Agent
RH**. **Aucun ID en dur** — toujours résolu à l'exécution (portabilité).

**Fallback** (rôle sans agent-user dédié, ex. « Agent Marketing ») : préfixer le titre
`[AGENT:{rôle}]` + assigner au **responsable humain**. Si l'assignation à un agent
nécessitait un outil dédié absent → entrée `docs/OUTILS-MCP-MANQUANTS.md`.

## 4. Suivi

Déléguer `rapidorh:revue-projet-hebdo` pour l'avancement (déplacer les tâches au fil
de la campagne — l'agent `chef-usine-leadmagnet` s'en charge).

## Passerelles

Exécution des tâches → les 4 skills du plugin. Orchestration → agent
`chef-usine-leadmagnet`.

## Règles

- Une tâche par livrable, **critère de done** explicite.
- Agents résolus **dynamiquement** (jamais d'ID client en dur).
- Fallback documenté si un rôle n'a pas d'agent-user.
