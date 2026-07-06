#!/bin/bash
# SessionStart (rapido-suite) : injecte un rappel court dans le contexte.
# Sortie stdout = ajoutée au contexte de la session. Aucun appel réseau.
# Détecte la base de connaissance entreprise ./rapido-kb/ dans le répertoire
# de travail (jamais dans le dossier du plugin).

KB_DIR="./rapido-kb"

cat <<EOF
[rapido-suite] Rappels de session (orchestration de 4 serveurs MCP) :
- Politique d'autonomie : lecture libre ; toute ÉCRITURE exige une confirmation
  utilisateur PAR SYSTÈME (jamais deux serveurs modifiés sur une validation
  globale). Détail : ${CLAUDE_PLUGIN_ROOT}/reference/autonomie.md
- Avant d'agir : charger ${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md
  (IDs d'abord, jamais de donnée inventée, récapitulatif final par serveur).
EOF

if [ -d "$KB_DIR" ]; then
  fichiers=$(ls "$KB_DIR"/*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ' ')
  if [ -n "$fichiers" ]; then
    cat <<EOF
- Base de connaissance entreprise détectée dans $KB_DIR/ : $fichiers
  Charger le(s) fichier(s) pertinent(s) au besoin (priorité : données MCP live
  > KB > références génériques du plugin). Mise à jour : skill mise-a-jour-kb.
EOF
  else
    cat <<EOF
- $KB_DIR/ existe mais est vide : lancer le skill onboarding-entreprise pour
  construire la base de connaissance.
EOF
  fi
else
  cat <<EOF
- Je ne connais pas encore votre entreprise. Lancez l'onboarding (skill
  onboarding-entreprise) pour que je travaille avec vos vraies données.
EOF
fi
exit 0
