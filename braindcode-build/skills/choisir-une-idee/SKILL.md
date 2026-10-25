---
name: choisir-une-idee
description: Utiliser quand l'utilisateur cherche quoi construire sur Build — « propose-moi une idée d'extension », « quelles idées FoodEatUp en difficulté facile ? », « critique mon idée d'extension ». Cinq idées adaptées au profil, critique honnête, réservation sur accord.
---

# Choisir une idée (catalogue des 100)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` (étape 03 : critique
  honnête).

## Démarche
1. **Profil** : demander niveau, logiciel préféré (foodeatup, rapidocrm,
   rapidocms, rapidorh, planit), temps disponible — sans profil, pas de
   « bonne » idée.
2. **Filtrer** : `list_projects` (product, archetype outil_connecte /
   copilote / orchestrateur / agent_3d, catégorie, difficulté, vedette,
   recherche libre) ; `get_project` sur les retenues.
3. **Comparer au réel** : `get_published_project` sur des réalisations
   proches — ce qui a déjà été fait, pour se situer ; `get_project_agents`
   pour l'équipe officielle de l'idée.
4. **Proposer CINQ idées** argumentées (pourquoi adaptée au profil, outils
   MCP en jeu, difficulté réelle) — widget fiche-idee sur demande.
5. **Critique honnête** de l'idée choisie (ou apportée) : ce qui est
   possible avec les outils réels du produit, ce qui ne l'est pas, les
   actions sensibles — jamais de « super idée » de complaisance.
6. **Réserver** : `reserve_project` SUR ACCORD (réservation trente jours).
   Idée nouvelle hors catalogue : `propose_idea` après aperçu complet
   (hook garde-build : ask).

## Pièges
- Ne jamais deviner un identifiant d'idée : `list_projects` le retrouve.
- L'arène (`get_clash_arena`) montre des réalisations humaines face à
  celles de Claude Code : s'en inspirer, ne pas copier.

## Dégradation propre
Aucune idée ne colle au profil : le dire et proposer `propose_idea` plutôt
que forcer une idée du catalogue.
