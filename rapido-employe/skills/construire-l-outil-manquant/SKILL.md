---
name: construire-l-outil-manquant
description: Utiliser quand aucun outil ne couvre un besoin réel, que l'utilisateur dit « il nous manque un outil pour ça », « fais construire le connecteur », « où en est la demande d'outil MCP ». Cherche d'abord un connecteur existant, rédige la demande d'outil, fait construire en préproduction Lovable après accord, relit le diff — l'humain publie.
---

# Construire l'outil manquant (chercher, demander, préproduire)

Famille engagée : **developper** (Brouillon — préproduction seulement,
l'humain publie).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **Chercher d'abord** : `find_connectors` (Academy) et l'annuaire des
   connecteurs — le besoin est-il couvert par un serveur existant pas encore
   branché ? Si oui : le demander à l'humain avec son adresse, fin.
2. **Rédiger la demande** : **`propose_mcp_tool`** — le besoin, les
   entrées/sorties attendues, le serveur qui devrait le porter, et le prompt
   Lovable prêt à l'emploi (aperçu → confirm).
3. **Faire construire, APRÈS accord** : `list_projects` (Lovable) pour
   trouver le projet qui porte le serveur MCP, puis `send_message` avec la
   demande — EN PRÉPRODUCTION (jamais deploy). Pour un projet du hackathon,
   le pendant Build BraindCode (`get_project_context`,
   `start_prompt_step`…) s'applique.
4. **Relire** : `get_diff` — le diff se lit en entier ; tout écart au besoin
   se redemande. `update_mcp_tool_request` pour noter l'avancement.
5. **L'humain publie** : `deploy_project` et la mise en production ne sont
   jamais à l'initiative de l'employé (famille publier, ask). Une fois
   publié : brancher, ajouter à une routine avec un KPI (skill
   `mon-equipe-d-agents`) — chaque semaine, une tâche de plus sait se faire
   seule.

KPI : `routines-en-service`.
Formations : `lovable` (7 missions), `plugin` (9), `mcp-foodeatup`.

## Garde-fous

- On ne code pas « à côté » : la demande d'outil passe par propose_mcp_tool
  et vit dans l'Academy — traçable, relue, journalisée.
- Préproduction uniquement ; aucun secret dans un prompt Lovable (les clés
  vivent côté serveur, kit connecteur maison).
- Le diff se relit AVANT de noter l'avancement — un outil non relu n'existe
  pas.
