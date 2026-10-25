---
name: exposer-et-valider-son-mcp
description: Utiliser quand l'extension expose son propre serveur MCP — « expose le MCP de mon extension », « fais valider mon MCP par une tâche complète », « enregistre la trace de validation ». Edge function par étapes, tâche accomplie sans aide, trace jointe, progression enregistrée.
---

# Exposer et faire valider le MCP de l'extension (critère n° 1)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` (étape 08) ;
- `${CLAUDE_PLUGIN_ROOT}/reference/regles-lovable.md` (MCP côté serveur).

## Démarche
1. **Construire par étapes** (cartes du plan, prompts Lovable) : le MCP de
   l'extension vit en edge function Lovable — outils nommés, schémas
   d'entrée, authentification côté serveur, erreurs propres. Le scope
   reste celui du cahier des charges.
2. **Le valider par l'usage** : TOI (le modèle) accomplis une tâche
   complète de bout en bout en découvrant les outils dynamiquement
   (tools/list), SANS aide ni indice — c'est le test du critère.
3. **La trace** : la conversation de validation (appels, réponses,
   résultat) s'enregistre dans ai_validation_trace via
   `save_project_progress` — SANS secret (hook anti-secret) ; les jetons
   de la trace se masquent avant l'enregistrement.
4. **Les métadonnées** : `save_project_progress` reçoit aussi
   mcp_server_url, mcp_tools_count et mcp_auth_type — relevés réels, pas
   d'arrondi.
5. **Clore** : `complete_prompt_step` (needs_review : c'est une étape
   sensible).

## Pièges
- Une « validation » guidée pas à pas ne vaut rien : la tâche se fait
  sans aide, ou elle échoue et on corrige le MCP.
- Un MCP qui n'expose que des lectures ne porte pas de routine (critère
  n° 5) : prévoir les écritures utiles, avec leurs validations.

## Dégradation propre
La tâche échoue : la trace de l'ÉCHEC se garde aussi, le correctif passe
par une nouvelle carte — jamais de trace embellie.
