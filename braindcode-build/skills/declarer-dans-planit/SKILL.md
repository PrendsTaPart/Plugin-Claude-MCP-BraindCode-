---
name: declarer-dans-planit
description: Utiliser quand le MCP de l'extension entre dans l'orchestrateur — « déclare mon MCP dans Plan'It », « teste le connecteur Plan'It », « référence le serveur sur la marketplace ». add_mcp_server + auth dans l'app, test, outils relevés, déclaration marketplace.
---

# Déclarer le MCP dans Plan'It et sur la marketplace (critère n° 1)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/carte-des-interconnexions.md`.

## Démarche
1. **Déclarer** : `add_mcp_server` (Plan'It) avec l'URL réelle du MCP de
   l'extension — la déclaration n'authentifie RIEN : l'authentification
   se fait dans l'écran Connecteurs de l'app Plan'It, donc
   `request_human_validation` (kind oauth) et attente sur
   `get_pending_validations`.
2. **Tester** : `test_mcp_server` une fois l'auth faite, puis
   `get_mcp_server_tools` — le relevé des outils orchestrables, comparé à
   mcp_tools_count enregistré côté Build.
3. **Marketplace** : la déclaration passe par `declarer_mcp`
   (plugin.braindcode.com) — lire sa description AVANT l'appel ; l'écriture
   part en modération humaine côté serveur, le dire.
4. **Consigner** : `save_project_progress` (déclaration faite, date), et
   la carte close.

## Délégation
La gestion fine des connecteurs Plan'It (états, reconnexions, routines qui
s'y appuient) vit dans le plugin planit s'il est installé : ce skill fait
l'ENTRÉE du MCP de l'extension, pas la vie de l'orchestrateur.

## Pièges
- add_mcp_server réussi ≠ connecté : sans l'auth dans l'app, test échoue
  — c'est l'ordre normal, pas un bug.
- Ne jamais déclarer une URL de préproduction comme MCP officiel.

## Dégradation propre
Plan'It non connecté dans la session : préparer la déclaration (URL, auth
attendue) et le dire — rien n'est simulé.
