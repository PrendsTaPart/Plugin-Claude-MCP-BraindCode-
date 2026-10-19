#!/bin/sh
# Garde-fou déterministe sur add_temperature : refuse (permissionDecision
# deny) un relevé sans equipment_id, non numérique ou hors de la plage
# plausible -30 °C à +90 °C. Le schéma serveur exige equipment_id (vérifié le
# 2026-07-10) et il ne doit jamais être deviné. Aucune réponse = autorisé.
# Tout le contrôle est fait par awk sur l'entrée standard : aucune variable
# shell, aucun fichier lu, aucun appel réseau.
awk '
function champ(cle,    p, r, c, i, v) {
  p = index(texte, "\"" cle "\"")
  if (p == 0) return ""
  r = substr(texte, p + length(cle) + 2)
  p = index(r, ":")
  if (p == 0) return ""
  r = substr(r, p + 1)
  v = ""
  for (i = 1; i <= length(r); i++) {
    c = substr(r, i, 1)
    if (c == " " || c == "\t" || c == "\"") { if (v != "") break; continue }
    if (c == "," || c == "}") break
    v = v c
  }
  return v
}
function numerique(v,    i, c, chiffre) {
  if (v == "") return 0
  chiffre = 0
  for (i = 1; i <= length(v); i++) {
    c = substr(v, i, 1)
    if (index("0123456789", c) > 0) chiffre = 1
    else if (index(".-+eE", c) == 0) return 0
  }
  return chiffre
}
function refuser(motif) {
  print "{\"hookSpecificOutput\": {\"hookEventName\": \"PreToolUse\", \"permissionDecision\": \"deny\", \"permissionDecisionReason\": \"" motif "\"}}"
  fini = 1
}
BEGIN {
  while ((getline ligne) > 0) texte = texte " " ligne
  eq = champ("equipment_id")
  if (eq == "" || eq == "null" || eq == "0" || eq == "false") {
    refuser("equipment_id absent : le schéma serveur l exige et il ne doit jamais être deviné. Résoudre l équipement via search_entities (types equipment) à partir du nom dicté, demander confirmation si ambiguous=true, puis rappeler add_temperature.")
  }
  t = champ("temperature")
  if (!fini && !numerique(t)) {
    refuser("Température absente ou non numérique : demander le relevé réel à l utilisateur avant d appeler add_temperature (jamais de valeur inventée).")
  }
  if (!fini && (t + 0 < -30 || t + 0 > 90)) {
    refuser("Température " t " °C hors plage plausible (-30 °C à 90 °C) : vérifier le relevé avec l utilisateur avant enregistrement. Ne jamais enregistrer une valeur douteuse ou inventée.")
  }
}
'
