#!/bin/sh
# Garde-fou déterministe : refuse tout relevé de température hors plage
# plausible (-30 °C à +90 °C) ou sans equipment_id sur add_temperature
# (le schéma serveur l'exige — vérifié le 2026-07-10 — et il ne doit jamais
# être deviné : résolution via search_entities). Exit 0 = allow ;
# exit 2 + stderr = deny. Shell POSIX uniquement (sed, grep, awk) : aucun
# appel réseau, aucun fichier lu hormis l'entrée standard.

PLAGE_MIN=-30
PLAGE_MAX=90

entree=$(cat | tr '\n' ' ')

# Valeur brute d'un champ JSON scalaire (chaîne, nombre, null, booléen).
champ() {
  printf '%s' "$entree" \
    | sed -n -E "s/.*\"$1\"[[:space:]]*:[[:space:]]*(\"[^\"]*\"|[-+0-9.eE]+|null|true|false).*/\1/p" \
    | tr -d '"' | tr -d ' '
}

equipment_id=$(champ equipment_id)
case "$equipment_id" in
  ""|null|0|false)
    echo "equipment_id absent : le schéma serveur l'exige et il ne doit jamais être deviné. Résoudre l'équipement via search_entities (types: [\"equipment\"]) à partir du nom dicté (« frigo 3 »), demander confirmation si ambiguous=true, puis rappeler add_temperature." >&2
    exit 2
    ;;
esac

temperature=$(champ temperature)
if ! printf '%s' "$temperature" | grep -Eq '^[-+]?([0-9]+\.?[0-9]*|\.[0-9]+)([eE][-+]?[0-9]+)?$'; then
  echo "Température absente ou non numérique : demander le relevé réel à l'utilisateur avant d'appeler add_temperature (jamais de valeur inventée)." >&2
  exit 2
fi

if awk -v t="$temperature" -v min="$PLAGE_MIN" -v max="$PLAGE_MAX" \
     'BEGIN { exit !((t + 0) < min || (t + 0) > max) }'; then
  echo "Température $temperature °C hors plage plausible ($PLAGE_MIN °C à $PLAGE_MAX °C) : vérifier le relevé avec l'utilisateur avant enregistrement. Ne jamais enregistrer une valeur douteuse ou inventée." >&2
  exit 2
fi

exit 0
