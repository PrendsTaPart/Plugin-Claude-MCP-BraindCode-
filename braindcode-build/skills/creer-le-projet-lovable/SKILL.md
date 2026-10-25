---
name: creer-le-projet-lovable
description: Utiliser quand l'utilisateur crée l'app Lovable d'une extension Build — « crée le projet Lovable », « pars d'un remix de cette réalisation », « importe la maquette Claude Design ». Création sur accord (crédits), message initial conforme, knowledge, workspace cible.
---

# Créer le projet Lovable

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/regles-lovable.md` EN ENTIER — chaque
  règle finit dans le message initial et le knowledge.

## Démarche
1. **Où créer** : `get_me` (workspaces et rôles) ou `list_workspaces` ;
   `list_design_systems` et `list_template_projects` pour partir du bon
   socle.
2. **Le message initial** : tiré de `get_project_prompts` kind lovable +
   les règles Lovable (IA intégrée, e-mails intégrés, MCP côté serveur,
   charte du produit, CTA devis FoodEatUp) + les maquettes Figma.
3. **Créer SUR ACCORD** (crédits — hook garde-credits-lovable) :
   `create_project` (initial_message, workspace_id). La création est
   ASYNCHRONE : suivre par `render_project_widget`, `get_message`,
   `get_project` — lire response.status, jamais le statut de premier
   niveau.
4. **Pause éventuelle** : awaiting_input → montrer la demande à l'humain,
   répondre par `respond_to_approval` avec SA décision (jamais un nouveau
   send_message : il annule la pause).
5. **Le knowledge** : `get_project_knowledge` d'abord (il peut exister),
   puis `set_project_knowledge` avec charte, règles de sécurité MCP et
   conventions — en sachant qu'il REMPLACE tout (hook).
6. **Relier à Build** : `set_workspace_target`, puis la carte du kanban
   mise à jour (`update_task`) et `save_project_progress`.

## Variantes
- **Remix** : `remix_project` d'une réalisation comparable, sur accord
  (crédits).
- **Maquette Claude Design** : `import-claude-design-from-url` avec l'URL
  du design, puis le même knowledge.

## Pièges
- Un create_project « pour essayer » consomme des crédits : une création
  = un message initial complet, pas trois itérations de cadrage.
- preview_url n'existe qu'après le premier build : le lire dans
  `get_project`, pas le construire à la main.

## Dégradation propre
Création en échec côté Lovable : lire le message réel, `report_blocker`
côté Build (sans secret), ne pas recréer en boucle.
