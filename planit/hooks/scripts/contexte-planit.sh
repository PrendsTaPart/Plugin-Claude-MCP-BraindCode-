#!/bin/bash
# SessionStart (plugin planit) : rappels d'ouverture. Aucun appel réseau.

cat <<EOF
[planit] Pilotage Plan'It — rappels de session :
- Ouvrir par get_kpi_home (crédits, autonomie, widgets, boucles, alertes)
  puis list_pending_routine_actions : ne JAMAIS reproposer ce qui attend
  déjà une décision.
- Tout coût s'annonce avant (estimate_routine_cost, list_kpi_catalog) ; les
  10 outils destructifs du serveur exigent une confirmation humaine ; une
  proposition refusée est définitive à l'identique ; aucun effet annoncé
  sur not_enough_data. Détail : \${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md
EOF
exit 0
