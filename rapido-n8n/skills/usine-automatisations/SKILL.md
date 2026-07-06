---
name: usine-automatisations
description: Utiliser quand l'utilisateur veut automatiser quelque chose, créer un workflow, ou dit « tous les jours / à chaque fois, fais… ». Fabrique un workflow n8n complet (cycle SDK, validation, test, publication confirmée) qui tournera ensuite sans Claude.
---

# Usine à automatisations (n8n)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-n8n.md`. Si les outils n8n sont
absents : expliquer `N8N_MCP_URL` et renvoyer vers
`${CLAUDE_PLUGIN_ROOT}/README-installation.md` — ne pas échouer sèchement.

## Routage d'abord

Ponctuel → exécuter directement via les MCP Rapido (pas de workflow).
Récurrent → ce skill. En cas de doute : « c'est pour cette fois, ou à chaque
fois ? ». Vérifier aussi `search_workflows` : une automatisation équivalente
existe peut-être déjà.

## Workflow

1. **Brief** — 4 questions : DÉCLENCHEUR (horaire ? événement/webhook ?),
   FRÉQUENCE, ACTION(S) (avec quel système : API Rapido en HTTP, email…),
   QUI EST NOTIFIÉ (et par quel canal). Consulter les `recettes-metier` : si
   le besoin matche une recette, partir d'elle.
2. **Cycle de fabrication** (pieges-n8n.md §1→4) :
   `get_sdk_reference` → `search_nodes` (services + utilitaires) →
   `get_suggested_nodes` (catégorie) → `get_node_types` (TOUS les nœuds, avec
   discriminants) → écrire le code SDK → `validate_workflow` jusqu'à validité
   → `create_workflow_from_code` (avec `description` 1-2 phrases).
3. **Credentials** — si le workflow utilise des comptes (Gmail, HTTP vers les
   API Rapido) : guider l'utilisateur pas à pas dans SON interface n8n
   (Credentials → Add credential), jamais via MCP. Attendre que ce soit fait
   avant le test réel.
4. **Test** (pieges-n8n.md §5) — `prepare_test_pin_data` → données d'exemple
   RÉALISTES et fictives, chaque item en `{"json": {...}}` → `test_workflow` →
   corriger (`update_workflow` après re-validation) jusqu'au vert.
5. **Publication — CONFIRMATION OBLIGATOIRE** — récapitulatif (déclencheur,
   fréquence, actions, notifications, envois externes) puis, après accord,
   `publish_workflow` (le hook demandera confirmation — normal). Respecter le
   niveau d'autonomie : envois externes réels en mode brouillon/notification
   tant que `processus-internes.md` n'autorise pas l'envoi direct.
6. **Registre** — consigner dans `rapido-kb/processus-internes.md` (section
   « Registre des automatisations ») : nom, rôle, fréquence, date de mise en
   service. Proposer la création de la section si absente.

## Garde-fous

- Jamais de paramètre de nœud deviné ; jamais de création sans validation ;
  jamais de publication sans récap confirmé.
- Test d'exécution réel : `execute_workflow` avec `executionMode: "manual"`
  EXPLICITE (le défaut est production !) puis `get_execution`
  (`includeData: false`).
- Un workflow = un rôle clair ; refuser le workflow fourre-tout (en faire
  deux).
