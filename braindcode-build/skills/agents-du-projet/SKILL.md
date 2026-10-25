---
name: agents-du-projet
description: Utiliser quand l'équipe IA du projet Build se déclare — « ajoute les agents du projet », « reprends l'équipe officielle de l'idée », « vérifie les agents déclarés ». Photos officielles uniquement, un add par agent, vérification finale.
---

# Agents du projet (l'équipe officielle)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md` (images
  officielles).

## Démarche
1. **L'équipe officielle** : `get_project_agents` — rôles, missions,
   compétences ET les photos officielles de l'idée. C'est la SOURCE
   unique : on n'invente jamais une adresse d'image.
2. **Déclarer** : `add_project_agent` PAR agent — rôle, mission,
   compétences, skills, hooks, photo officielle reprise telle quelle.
   Compléter avec les agents de CE plugin quand ils s'appliquent (chef de
   chantier, bâtisseur, testeur…), décrits avec leurs garde-fous réels.
3. **Vérifier** : `list_project_agents` — l'équipe déclarée correspond à
   ce qui a été montré et accepté.
4. **Consigner** : `save_project_progress`.

## Pièges
- Une photo d'agent générée ou une URL externe : refusé — seules les
  images renvoyées par get_project_agents sont valables.
- Un agent déclaré avec des compétences qu'il n'a pas (outils non
  branchés) : l'équipe doit refléter le RÉEL du projet.

## Dégradation propre
get_project_agents vide pour l'idée : déclarer les seuls agents de ce
plugin, et le dire.
