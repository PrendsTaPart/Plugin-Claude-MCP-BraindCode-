#!/usr/bin/env python3
"""Vérité des données (PostToolUse, outils Plan'It) — jamais bloquant.

Quand le résultat d'un outil Plan'It contient un marqueur de prudence, ce
hook injecte un rappel de contexte :

- `not_enough_data` → interdit d'annoncer un effet (boucle/routine : il faut
  au moins 3 exécutions ET 14 jours) ;
- `"throttled": true` → la valeur n'est PAS fraîche : la présenter avec son
  âge (`age_minutes`), jamais comme un relevé du moment ;
- base d'estimation `flat_price` ou `default` → une estimation, jamais une
  mesure.

Sortie : JSON PostToolUse `additionalContext` quand un marqueur est présent ;
rien sinon (exit 0). Aucun appel réseau. Les cas de test CI couvrent le
silence (allow) ; le déclenchement se vérifie dans tests/evals.md.
"""
import json
import re
import sys

RX_MCP = re.compile(r"^mcp__[Pp]lan[_-]?[Ii]t__([A-Za-z0-9_]+)$")


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    if not RX_MCP.match(payload.get("tool_name", "")):
        sys.exit(0)
    reponse = payload.get("tool_response")
    if reponse is None:
        sys.exit(0)
    texte = json.dumps(reponse, ensure_ascii=False)
    rappels = []
    if "not_enough_data" in texte:
        rappels.append("un verdict not_enough_data est présent : N'ANNONCE "
                       "AUCUN effet de la routine ou de la boucle concernée "
                       "(il faut au moins 3 exécutions ET 14 jours) — dis "
                       "« pas assez de données ».")
    if re.search(r'"throttled"\s*:\s*true', texte):
        rappels.append("une valeur est renvoyée avec throttled=true : elle "
                       "n'est PAS fraîche — donne son âge (age_minutes) et "
                       "ne la présente jamais comme un relevé du moment.")
    if re.search(r'"(basis|base|cost_basis)"\s*:\s*"(flat_price|default)"',
                 texte) or '"flat_price"' in texte:
        rappels.append("l'estimation repose sur flat_price ou default : "
                       "c'est un tarif, pas une mesure — dis-le tel quel.")
    if rappels:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": "[verite-des-donnees] " + " ".join(rappels),
        }}, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
