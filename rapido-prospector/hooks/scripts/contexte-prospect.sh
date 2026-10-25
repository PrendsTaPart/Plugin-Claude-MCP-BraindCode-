#!/usr/bin/env bash
# Hook SessionStart — rappel des règles d'envoi du plugin rapido-prospector.
set -u
cat <<'FIN'
[rapido-prospector] Règles d'envoi de la session :
- AUCUN envoi réel (e-mail, SMS, appel, LinkedIn) sans accord humain sur CET
  envoi : liste des cibles + contenu montrés d'abord ; les champs confirm
  posés par le modèle ne valent jamais confirmation.
- Quotas et fenêtre horaire : ./rapido-kb/prospection.md (bloc machine) —
  sans KB, défauts prudents et appels automatisés DÉSACTIVÉS ; si le cadre
  Academy (.claude/state/cadre-employe.json) existe, le plus petit gagne.
- E-mail : identité d'expéditeur + phrase de désinscription. SMS : E.164
  mobiles, mention STOP. Liste d'opposition : bloque l'envoi entier.
- run_prospection n'enregistre rien : dédoublonner (scripts/dedoublonner.py)
  avant add_clients. LinkedIn : enrichir (provider_id) avant d'envoyer,
  relire list_linkedin_message_history avant d'écrire.
- 12 delete_* définitifs (cascades) ; publications (webinaire actif, statut
  « publie ») sur accord. Journal : add_log après chaque série.
FIN
if [ -f "rapido-kb/prospection.md" ]; then
  echo "[rapido-prospector] KB trouvée : rapido-kb/prospection.md (quotas ci-dessous)."
  python3 "$(dirname "$0")/../../scripts/quotas.py" 2>/dev/null || true
else
  echo "[rapido-prospector] KB absente : quotas prudents par défaut (appels à 0)."
fi
exit 0
