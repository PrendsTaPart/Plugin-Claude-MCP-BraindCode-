#!/usr/bin/env bash
# Hook SessionStart — la méthode Build en dix étapes et les cinq critères.
set -u
cat <<'FIN'
[braindcode-build] Les cinq critères (non négociables) :
  1. l'extension expose son propre serveur MCP (orchestrable par Plan'It) ;
  2. elle publie son plugin sur la marketplace ;
  3. AUCUN credential MCP n'atteint le navigateur ;
  4. le rapport de test est obligatoire ;
  5. elle ne vaut que par la routine qu'elle fait tourner.
Les dix étapes : connecter → contexte (tools/list, rien supposé) → idée
critiquée → prompts Figma → prompts Lovable (charte) → MCP branché côté
serveur → construire et tester (rapport) → exposer et valider son MCP
(trace) → déclarer dans Plan'It → routine mesurée.
Validations humaines (OAuth, clé, paiement, mise en ligne) :
request_human_validation puis get_pending_validations — jamais de secret
dans une demande, un blocage, un message ou une trace ; jamais d'identifiant
deviné. Lovable : pause awaiting_input = décision humaine via
respond_to_approval ; create_project asynchrone (lire response.status) ;
set_project_knowledge REMPLACE tout. Référence : reference/methode-build.md,
regles-lovable.md, carte-des-interconnexions.md.
FIN
exit 0
