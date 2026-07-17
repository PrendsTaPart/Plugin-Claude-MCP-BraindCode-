---
name: surveillance-automatisations
description: Utiliser quand l'utilisateur demande si ses automatisations tournent ou parle d'erreurs de workflows. Contrôle les workflows actifs, chasse les exécutions en échec sur 7 jours, diagnostique et propose le correctif.
---

# Surveillance des automatisations

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-n8n.md`. Outils n8n absents →
expliquer `N8N_MCP_URL` + renvoyer vers `README-installation.md`.

## Workflow

1. **Inventaire** — `search_workflows` : les workflows ACTIFS (publiés) ;
   croiser avec le registre de `rapido-kb/processus-internes.md` — un
   workflow actif absent du registre (ou l'inverse) se signale.
2. **Chasse aux échecs** — `search_executions` (`status: ["error",
   "crashed"]`, `startedAfter` = il y a 7 jours) : les exécutions en échec de
   la semaine. Compter aussi les succès pour un TAUX DE SUCCÈS par workflow.
3. **Diagnostic ciblé** — pour chaque workflow en échec : `get_execution`
   (`includeData: false` D'ABORD ; les données complètes uniquement si le
   message d'erreur ne suffit pas). Causes types : credential expirée (→
   guider l'utilisateur dans SON interface n8n), API Rapido indisponible ou
   schéma changé, données inattendues (item non enveloppé, champ manquant).
4. **Correctif** — proposer le fix ; après validation : cycle de modification
   (`get_node_types` si nœuds touchés → code → `validate_workflow` →
   `update_workflow`) puis re-test (`test_workflow` ou `execute_workflow`
   `executionMode: "manual"`) et RE-PUBLICATION confirmée (la version publiée
   ne change qu'à la re-publication).
5. **Restitution** :
   ```
   🤖 AUTOMATISATIONS — 7 derniers jours
   Actifs : N (registre à jour : oui/non)
   Taux de succès global : X % | exécutions : S succès / E échecs
   Taux d'échec par workflow (7 j) : {workflow} = échecs ÷ exécutions = Y %
   Échecs à traiter : workflow | cause probable | correctif proposé
   ```
   > Le **taux d'échec 7 j par workflow** est le format attendu par la fiche
   > d'amélioration « boucle 15 » (`rapido-startup:amelioration-des-routines` /
   > `data/prompts-collections/boucles.json`) : le fournir workflow par workflow,
   > pas seulement en global.

## Garde-fous

- Un workflow qui échoue en silence depuis des jours = alerte prioritaire
  (son rôle n'est PLUS assuré — le dire en ces termes).
- Ne jamais dépublier/archiver pour « faire disparaître » une erreur sans
  accord (hook ask) — et mettre à jour le registre si on le fait.
- Correctifs uniquement après validation utilisateur ; jamais de credential
  manipulée via MCP.
