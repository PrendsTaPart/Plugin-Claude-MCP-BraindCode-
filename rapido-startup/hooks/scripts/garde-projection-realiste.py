#!/usr/bin/env python3
"""Garde-fou « projection réaliste » (PreToolUse, rapido-startup).

Surveille les écritures du prévisionnel (fichiers sous
business-plan/previsionnel/ ou exécutions de previsionnel.py) :
- REJETTE (deny, exit 2) un churn à 0 (aucune entreprise n'a zéro churn) ;
- REJETTE une croissance > 30 %/mois au-delà du mois 6 sans
  `justification_croissance` (à recopier d'hypotheses.md).

Mêmes règles que la validation interne de previsionnel.py (défense en
profondeur). Fail-open sur toute erreur de parsing. Aucun appel réseau."""
import json
import re
import sys

RX_CHURN_ZERO = re.compile(r'["\']?churn(_mensuel)?["\']?\s*[:=]\s*0(\.0+)?\b')
RX_CROISSANCE = re.compile(r'["\']?croissance(_mensuelle)?["\']?\s*[:=]\s*(0\.[0-9]+|[1-9][0-9]*\.?[0-9]*)')
RX_JUSTIF = re.compile(r"justification_croissance[\"']?\s*[:=]\s*[\"']?[^\s\"',}]{3,}")


def texte_de_l_appel(data):
    ti = data.get("tool_input") or {}
    morceaux = [str(ti.get(k, "")) for k in ("content", "new_string", "command", "file_path")]
    return "\n".join(morceaux)


try:
    data = json.load(sys.stdin)
    texte = texte_de_l_appel(data)
    concerne = ("previsionnel" in texte) or ("business-plan" in texte)
    if not concerne:
        sys.exit(0)
    if RX_CHURN_ZERO.search(texte):
        sys.stderr.write(
            "REJET garde-projection-realiste : churn = 0 dans le prévisionnel. "
            "Aucune entreprise n'a zéro churn — reprendre l'hypothèse dans "
            "hypotheses.md (source + confiance) avant de régénérer.")
        sys.exit(2)
    m = RX_CROISSANCE.search(texte)
    if m and float(m.group(2)) > 0.30 and not RX_JUSTIF.search(texte):
        sys.stderr.write(
            "REJET garde-projection-realiste : croissance > 30 %/mois au-delà "
            "du mois 6 sans justification_croissance écrite (recopier la "
            "justification et sa source depuis hypotheses.md).")
        sys.exit(2)
    sys.exit(0)
except SystemExit:
    raise
except Exception:  # noqa: BLE001 — fail-open
    sys.exit(0)
