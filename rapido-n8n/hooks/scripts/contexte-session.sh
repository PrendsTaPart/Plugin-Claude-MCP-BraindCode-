#!/bin/bash
# SessionStart (rapido-n8n) : vérifie la configuration de l'instance n8n du
# client et rappelle la règle de routage. Aucun appel réseau.

if [ -n "$N8N_MCP_URL" ]; then
  cat <<EOF
[rapido-n8n] Instance n8n configurée (N8N_MCP_URL définie).
- Vérification recommandée : search_workflows doit répondre. Si les outils
  n8n sont absents malgré la variable, voir
  ${CLAUDE_PLUGIN_ROOT}/README-installation.md (URL, MCP activé, auth).
- Règle de routage : tâche ponctuelle = exécution directe via les MCP ;
  tâche récurrente = fabriquer un workflow n8n (skill usine-automatisations).
- Avant tout code de workflow : ${CLAUDE_PLUGIN_ROOT}/reference/pieges-n8n.md.
EOF
else
  cat <<EOF
[rapido-n8n] ⚠️ N8N_MCP_URL n'est PAS définie : les outils n8n ne seront pas
disponibles dans cette session.
Pour connecter VOTRE instance n8n (cloud ou auto-hébergée) :
  export N8N_MCP_URL=https://<votre-instance>/mcp-server/http
puis relancer Claude Code. Guide complet :
${CLAUDE_PLUGIN_ROOT}/README-installation.md
Les skills du plugin expliqueront cette étape au lieu d'échouer.
EOF
fi
exit 0
