---
name: demarrer-le-projet
description: Utiliser quand l'idée est choisie et qu'on lance le chantier Build — « démarre le projet », « déclare-toi développeur IA de cette idée », « initialise le journal d'exécution ». register_ai_developer d'abord, contexte, initialisation, espace Lovable visé.
---

# Démarrer le projet (développeur IA déclaré)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` (le journal
  d'exécution).

## Démarche
1. **Se déclarer** : `register_ai_developer` en mode HYBRIDE par défaut
   (l'humain garde les validations) — il crée le projet, réserve l'idée et
   ouvre le journal d'exécution. C'est le préalable de tout le reste.
2. **Tout le contexte** : `get_project_context` — fiche, logiciel,
   identité visuelle, prompts, feuille de route (`get_project_roadmap`
   pour le détail daté).
3. **Initialiser** : `save_project_progress` avec l'état de départ (rien
   d'inventé : ce qui existe réellement).
4. **L'espace Lovable visé** : une fois le projet Lovable choisi ou créé
   (skill `creer-le-projet-lovable`), `set_workspace_target` l'enregistre
   côté Build.

## Pièges
- `get_prompt_execution_plan` AVANT `register_ai_developer` échoue ou crée
  un plan orphelin : l'ordre est strict (pièges vérifiés).
- Mode `ia` (sans validations humaines intermédiaires) : seulement si
  l'humain le demande explicitement — les validations OAuth / paiement /
  mise en ligne restent humaines quoi qu'il arrive.

## Dégradation propre
Idée déjà réservée par quelqu'un d'autre : le dire et revenir au skill
`choisir-une-idee`.
