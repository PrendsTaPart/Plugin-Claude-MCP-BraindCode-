#!/usr/bin/env python3
"""Garde du cadre employé (PreToolUse, tous les outils MCP) — FAIL-CLOSED.

Le cadre (niveaux d'autonomie par famille, quotas, marche/arrêt) n'est JAMAIS
codé ici : il est relu de get_work_plan par le skill `prise-de-poste`, qui en
écrit un instantané dans .claude/state/cadre-employe.json. Ce hook :

- classe l'outil appelé dans sa famille d'actions grâce à la table versionnée
  reference/familles-outils.json (clé « serveur:outil », puis « outil », puis
  préfixe) ; une LECTURE (outil hors table et sans forme d'écriture) passe ;
- cadre ABSENT, illisible ou PÉRIMÉ (plus de 24 h) → ask : « lancer
  /prise-de-poste » (l'absence de cadre ne vaut jamais autorisation) ;
- agent ARRÊTÉ (actif=false) → deny : on ne fait que le rapport ;
- famille « engager » → TOUJOURS ask, quel que soit le niveau ;
- niveau Aperçu → ask ; Brouillon → allow seulement si la table marque le
  geste `brouillon` (sinon ask) ; Confirmé → allow ;
- un outil d'écriture NON CLASSÉ → ask (fail-closed).

Les champs confirm/confirmed posés par le modèle sont ignorés : ils ne valent
jamais confirmation humaine. Aucun appel réseau. Testé par
scripts/tester-skills.py (la clé racine `cadre_test` du payload, injectable
uniquement par le harnais ou Claude Code — jamais par le modèle, qui ne
contrôle que tool_input —, sert de cadre de test).
"""
import datetime
import json
import os
import re
import sys

RACINE_PLUGIN = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
TABLE = os.path.join(RACINE_PLUGIN, "reference", "familles-outils.json")
ETAT = os.path.join(".claude", "state", "cadre-employe.json")
RX_MCP = re.compile(r"^mcp__(.+)__([A-Za-z0-9_-]+)$")


def decision(permission, raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": permission,
        "permissionDecisionReason": raison,
    }}, ensure_ascii=False))
    sys.exit(0)


def deny(raison):
    print(f"garde-cadre-employe : {raison}", file=sys.stderr)
    sys.exit(2)


def serveur_canonique(brut):
    s = brut.lower().replace("_", "-")
    for motif, canon in (("formation", "academy"), ("academy", "academy"),
                         ("tutoriel", "foodeatup-tutoriel"),
                         ("drive", "google-drive"), ("gmail", "gmail"),
                         ("lovable", "lovable"), ("build", "build"),
                         ("plan-it", "planit"), ("planit", "planit")):
        if motif in s:
            return canon
    return s


def classer(table, serveur, outil):
    """Renvoie (famille, brouillon) ou None si l'outil n'est pas classé."""
    outils = table.get("outils", {})
    entree = outils.get(f"{serveur}:{outil}") or outils.get(outil)
    if entree:
        return entree.get("famille"), bool(entree.get("brouillon"))
    for prefixe, regle in table.get("regles_prefixes", {}).items():
        if outil.startswith(prefixe):
            return regle.get("famille"), bool(regle.get("brouillon"))
    return None


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    m = RX_MCP.match(payload.get("tool_name", ""))
    if not m:
        sys.exit(0)
    serveur = serveur_canonique(m.group(1))
    outil = m.group(2)

    try:
        with open(TABLE, encoding="utf-8") as f:
            table = json.load(f)
    except Exception:  # noqa: BLE001
        decision("ask", "table reference/familles-outils.json illisible — "
                        "fail-closed, confirmation humaine requise.")

    classement = classer(table, serveur, outil)
    if classement is None:
        sys.exit(0)  # lecture : hors périmètre de ce garde
    famille, brouillon = classement

    cadre = payload.get("cadre_test")
    if cadre is None:
        try:
            with open(ETAT, encoding="utf-8") as f:
                cadre = json.load(f)
        except Exception:  # noqa: BLE001
            cadre = None
    if not isinstance(cadre, dict):
        decision("ask", f"écriture « {outil} » (famille {famille}) sans cadre "
                 "du jour : lancer /prise-de-poste (get_claude_brief puis "
                 "get_work_plan) avant d'écrire.")
    try:
        ts = datetime.datetime.fromisoformat(
            str(cadre.get("horodatage", "")).replace("Z", "+00:00"))
        age_h = (datetime.datetime.now(datetime.timezone.utc)
                 - ts).total_seconds() / 3600
    except Exception:  # noqa: BLE001
        age_h = None
    if age_h is None or age_h > 24:
        decision("ask", f"cadre employé périmé ou sans horodatage (> 24 h) : "
                 f"relancer /prise-de-poste avant « {outil} ».")
    if not cadre.get("actif", False):
        deny(f"agent arrêté par le responsable (get_work_plan) : « {outil} » "
             "refusé — seul le rapport de la journée est permis.")

    if famille == "engager":
        decision("ask", f"« {outil} » engage l'entreprise : décision humaine, "
                 "toujours (prix hors grille, contrat, paiement, suppression).")
    niveau = (cadre.get("autonomie") or {}).get(famille)
    if niveau == "Confirmé":
        sys.exit(0)
    if niveau == "Brouillon":
        if brouillon:
            sys.exit(0)
        decision("ask", f"famille « {famille} » en niveau Brouillon : "
                 f"« {outil} » n'est pas un geste de brouillon — accord requis.")
    decision("ask", f"famille « {famille} » en niveau "
             f"{niveau or 'inconnu (fail-closed)'} : Claude montre ce qu'il "
             "ferait et attend l'accord.")


if __name__ == "__main__":
    main()
