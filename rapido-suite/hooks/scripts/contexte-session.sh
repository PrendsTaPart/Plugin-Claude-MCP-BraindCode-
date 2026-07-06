#!/bin/bash
# SessionStart (rapido-suite) : injecte un rappel court dans le contexte.
# Sortie stdout = ajoutée au contexte de la session. Aucun appel réseau.
cat <<EOF
[rapido-suite] Rappels de session (orchestration de 4 serveurs MCP) :
- Politique d'autonomie : lecture libre ; toute ÉCRITURE exige une confirmation
  utilisateur PAR SYSTÈME (jamais deux serveurs modifiés sur une validation
  globale). Détail : ${CLAUDE_PLUGIN_ROOT}/reference/autonomie.md
- Avant d'agir : charger ${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md
  (IDs d'abord, jamais de donnée inventée, récapitulatif final par serveur).
EOF
exit 0
