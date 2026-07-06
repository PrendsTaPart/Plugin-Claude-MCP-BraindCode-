# Directives communes d'utilisation des outils (rapido-lovable)

Règles applicables à TOUTE exécution de skill de ce plugin, qui croise Lovable
avec les 4 serveurs Rapido.
OBLIGATOIRE avant tout appel Lovable : charger
`${CLAUDE_PLUGIN_ROOT}/reference/architecture-lovable.md` (modes A/B, pièges).

## 1. Résolution d'ID d'abord

- Côté Rapido : mêmes règles que les autres plugins — jamais d'ID deviné,
  `establishment_id` explicite pour FoodEatUp, contexte de session pour
  CRM/CMS/RH.
- Côté Lovable : `workspace_id` via `list_workspaces`/`get_workspace`,
  `project_id` via `list_projects`/`create_project`. Vérifier les CRÉDITS
  (`get_workspace`) avant un gros chantier.

## 1 bis. Base de connaissance entreprise (./rapido-kb/)

Si `./rapido-kb/` existe : `charte-graphique.md` + `ton-et-accroches.md` pour
toute UI générée, `propositions-valeur.md` + `cibles-personas.md` pour les
landing pages, `produits-services.md` pour les contenus. La KB PRIME ; sans
KB, standards du secteur en le signalant. Le contenu injecté dans les messages
Lovable vient de la KB et des outils MCP — jamais inventé.

## 2. Confirmation avant action irréversible ou coûteuse

- `deploy_project` : URL publique → confirmation niveau 2 (récapituler ce qui
  devient public).
- `query_database` en écriture : production → confirmation explicite par
  requête.
- `set_workspace_knowledge` / `set_project_knowledge` : remplacement total →
  toujours get + fusion + validation du contenu final avant set.
- `send_message` / `create_project` consomment les crédits du client :
  annoncer les grosses itérations, pas de rafale de messages sans accord.

## 3. Ne jamais inventer de données

Plats, prix, offres, arguments, coordonnées affichés dans une app : issus des
outils Rapido, de la KB ou de l'utilisateur — avec source citée. Jamais de
données personnelles clients en dur dans le code ou les contenus.

## 4. Gestion d'erreur

`create_project` qui renvoie `available_workspaces` = choisir/demander le
workspace puis rappeler. `send_message` en timeout = `get_message` pour suivre
(pas de renvoi en double). Ne pas boucler sur un agent Lovable qui échoue :
lire son activité (`list_edits`, `get_diff`), reformuler UNE fois, sinon
remonter à l'utilisateur.

## 5. Récapitulatif de fin de séquence

Projets créés/modifiés (project_id, editor_url, preview_url, URL publiée le
cas échéant), connecteurs en attente de clic utilisateur, knowledge/skills
workspace modifiés, objets Rapido créés (IDs par serveur), crédits notables
consommés.
