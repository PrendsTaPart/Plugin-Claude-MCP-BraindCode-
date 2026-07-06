# Pièges n8n — cycle de fabrication OBLIGATOIRE

À charger avant tout usage des outils n8n. Un workflow publié tourne SEUL,
potentiellement la nuit : la rigueur de fabrication n'est pas optionnelle.

## Le cycle — dans cet ordre, sans sauter d'étape

1. **`get_sdk_reference` EN PREMIER** — patterns, expressions, règles du SDK
   (sections `guidelines` et `design` incluses). Ne jamais écrire de code de
   workflow sans avoir lu la référence dans la session.
2. **`search_nodes` puis `get_node_types` AVANT tout code** — ne JAMAIS
   deviner les noms de paramètres. `get_node_types` avec TOUS les IDs de
   nœuds prévus, EN INCLUANT les discriminants (`resource`/`operation`/`mode`)
   relevés dans les résultats de `search_nodes` — les définitions TypeScript
   exactes en dépendent.
3. **`get_suggested_nodes`** par catégorie de technique (notification,
   scheduling, data_extraction…) : recommandations curées avant de choisir.
4. **`validate_workflow` OBLIGATOIRE** avant `create_workflow_from_code` ou
   `update_workflow` — corriger et re-valider jusqu'à validité. À la création,
   fournir une `description` courte (1-2 phrases) du rôle du workflow.
5. **Tester avec des données épinglées** — `prepare_test_pin_data` (schémas
   attendus par nœud) → générer des données d'exemple RÉALISTES (pas de
   « foo/bar » : de vrais noms de plats, de vraies structures de devis) →
   chaque item ENVELOPPÉ dans `{"json": {...}}` (jamais d'objet plat) →
   `test_workflow`. Les nœuds à credentials/HTTP sont simulés par le pin
   data ; les nœuds logiques s'exécutent réellement.
6. **`publish_workflow` = mise en PRODUCTION** — le workflow tournera seul.
   TOUJOURS un récapitulatif (déclencheur, fréquence, actions, qui est
   notifié, ce qui part vers l'extérieur) + confirmation explicite AVANT.
7. **Exécution** — `execute_workflow` rend un ID IMMÉDIATEMENT (sans attendre
   la fin) → suivre avec `get_execution` (`includeData: false` d'abord — les
   données complètes seulement si nécessaire au diagnostic).
   ⚠️ `executionMode` par DÉFAUT = `production` (exécute la version
   publiée !) — pour tester, passer EXPLICITEMENT `executionMode: "manual"`.
8. **CREDENTIALS — dans l'UI de LEUR instance, jamais via MCP** — les comptes
   (Gmail, HTTP vers les API Rapido…) se configurent dans l'interface n8n du
   CLIENT. S'ils manquent : guider l'utilisateur pas à pas dans SA propre
   interface (Credentials → Add credential → type…), sans jamais supposer une
   instance particulière ni une URL précise.

## 9. Côté Rapido — les deux sens d'intégration

- **Workflow → Rapido** : nœud HTTP Request vers les API Rapido
  (`https://crm.rapidosoftware.com`, `https://foodeatup.com`…) avec
  authentification en credential n8n (configurée dans l'UI, cf. §8). Le
  workflow appelle l'API REST, pas le MCP.
- **Rapido → Workflow** : nœud Webhook n8n qui REÇOIT les événements
  (formulaire Lovable, webhook CRM…) — fournir l'URL du webhook au système
  émetteur et documenter le format attendu du payload.
Documenter le sens choisi dans la description du workflow.

## Règle de routage (à appliquer partout)

- Tâche PONCTUELLE (« relance ce devis », « analyse ma carte ») → Claude
  l'exécute directement via les MCP — pas de workflow.
- Tâche RÉCURRENTE (« tous les jours… », « à chaque nouveau… ») → Claude
  FABRIQUE le workflow n8n qui tournera sans lui.
En cas de doute : demander « c'est pour cette fois, ou à chaque fois ? ».

## Si les outils n8n sont absents

Ne pas échouer silencieusement : expliquer que `N8N_MCP_URL` n'est
probablement pas définie et renvoyer vers
`${CLAUDE_PLUGIN_ROOT}/README-installation.md`.
