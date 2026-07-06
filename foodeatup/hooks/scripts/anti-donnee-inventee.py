#!/usr/bin/env python3
"""Garde-fou déterministe : refuse tout relevé de température hors plage
plausible (-30 °C à +90 °C) sur add_temperature. Exit 0 = allow ;
exit 2 + stderr = deny. Aucun appel réseau."""
import json
import sys

PLAGE_MIN = -30.0
PLAGE_MAX = 90.0

try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

tool_input = data.get("tool_input") or {}
raw = tool_input.get("temperature")

try:
    temperature = float(raw)
except (TypeError, ValueError):
    sys.stderr.write(
        "Température absente ou non numérique : demander le relevé réel à "
        "l'utilisateur avant d'appeler add_temperature (jamais de valeur inventée)."
    )
    sys.exit(2)

if temperature < PLAGE_MIN or temperature > PLAGE_MAX:
    sys.stderr.write(
        f"Température {temperature} °C hors plage plausible "
        f"({PLAGE_MIN:g} °C à {PLAGE_MAX:g} °C) : vérifier le relevé avec "
        "l'utilisateur avant enregistrement. Ne jamais enregistrer une valeur "
        "douteuse ou inventée."
    )
    sys.exit(2)

sys.exit(0)
