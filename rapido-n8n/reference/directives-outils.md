# Directives communes d'utilisation des outils (rapido-n8n)

Règles applicables à TOUTE exécution de skill de ce plugin.
OBLIGATOIRE avant tout appel n8n : charger
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-n8n.md` (cycle de fabrication,
credentials, routage ponctuel/récurrent).

## 0. Routage ponctuel / récurrent — LA règle du plugin

Tâche ponctuelle → Claude l'exécute directement via les MCP Rapido.
Tâche récurrente → Claude fabrique le workflow n8n qui tourne ensuite SANS
lui. Toujours annoncer le choix (« c'est récurrent → je fabrique un
workflow »).

## 1. Résolution d'ID et de contexte d'abord

- n8n : `search_workflows` / `get_workflow_details` avant toute modification ;
  jamais d'ID de workflow ou de nœud deviné. Instance du CLIENT via
  `N8N_MCP_URL` — aucune URL d'instance en dur, nulle part.
- Rapido : mêmes règles que les autres plugins (`establishment_id` explicite
  pour FoodEatUp, session pour CRM/CMS/RH).

## 1 bis. Base de connaissance entreprise (./rapido-kb/)

- `processus-internes.md` : REGISTRE DES AUTOMATISATIONS (chaque workflow
  créé y est consigné : nom, rôle, fréquence, date) + niveaux d'autorisation
  d'envoi (les envois externes réels démarrent en brouillon/notification tant
  que la KB n'autorise pas l'envoi direct).
- `ton-et-accroches.md` : les textes des emails/notifications générés par les
  workflows.
Sans KB : mode le plus prudent (brouillons), en le signalant.

## 2. Confirmation avant action de production

- `publish_workflow` (le workflow tournera seul), `unpublish_workflow` /
  `archive_workflow` (arrêt d'une automatisation en service),
  `execute_workflow` en mode production (défaut !) : récapitulatif +
  confirmation explicite. Les hooks du plugin forcent ces confirmations.
- Modifier un workflow ACTIF (`update_workflow`) : prévenir que la version
  publiée n'est remplacée qu'à la re-publication.

## 3. Ne jamais inventer de données

Paramètres de nœuds : uniquement depuis `get_node_types`. Données de test :
réalistes mais FICTIVES (jamais de vraies PII clients dans le pin data).
Textes d'emails : KB ou validation utilisateur.

## 4. Gestion d'erreur

Outils n8n absents → expliquer `N8N_MCP_URL` et renvoyer vers
`README-installation.md` (pas d'échec sec). `validate_workflow` en erreur →
corriger et re-valider, pas de création forcée. Exécution en échec →
`get_execution` (`includeData: false` d'abord) pour diagnostiquer.

## 5. Récapitulatif de fin de séquence

Workflows créés/modifiés (ID, nom, statut draft/publié, déclencheur,
fréquence), tables de données créées, credentials à configurer par
l'utilisateur (avec le guidage donné), et la mise à jour du registre dans
`rapido-kb/processus-internes.md`.
