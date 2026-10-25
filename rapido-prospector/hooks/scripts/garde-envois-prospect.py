#!/usr/bin/env python3
"""Hook PreToolUse — garde des 5 envois réels du serveur Prospect.

Décisions :
- deny  : lot au-dessus du plafond (min entre KB et serveur), quota du jour
  atteint (compteurs .claude/state/prospect-envois.json), ou hors fenêtre
  horaire (Europe/Paris, jours ouvrés de la KB) ;
- ask   : sinon, TOUJOURS — un envoi réel n'est jamais silencieux, et un
  champ `confirm`/`confirmed` posé par le modèle ne vaut rien ici ;
- fail-closed : table des outils sensibles ou horloge illisibles → deny.

Quotas : min(KB ./rapido-kb/prospection.md, cadre Academy
.claude/state/cadre-employe.json s'il existe). Clés de test réservées au
harnais CI (jamais dans tool_input, le modèle ne les contrôle pas) :
kb_test, compteurs_test, maintenant_test.
"""
import datetime
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(PLUGIN, "scripts"))
from quotas import (DEFAUTS, PLAFONDS_SERVEUR, charger_kb,  # noqa: E402
                    compteurs_du_jour, plafond_academy)

RX_OUTIL = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Pp]rospect__([A-Za-z0-9_]+)$")
CANAL = {
    "send_email": ("email", "recipients"),
    "send_sms": ("sms", "targets"),
    "place_call": ("appels", "targets"),
    "send_linkedin_invite": ("linkedin_invitations", "connectionId"),
    "send_linkedin_message": ("linkedin_messages", "connectionId"),
}
JOURS = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]


def deny(raison):
    print(f"[garde-envois-prospect] REFUS : {raison}", file=sys.stderr)
    sys.exit(2)


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": f"[garde-envois-prospect] {raison}"}}))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        deny("entrée illisible (fail-closed)")
    outil = RX_OUTIL.match(data.get("tool_name", ""))
    if not outil or outil.group(1) not in CANAL:
        sys.exit(0)
    canal, champ = CANAL[outil.group(1)]
    entree = data.get("tool_input") or {}

    try:
        sensibles = json.load(open(os.path.join(
            PLUGIN, "reference", "outils-sensibles.json"), encoding="utf-8"))
        regles = sensibles["envois_reels"][outil.group(1)]
    except Exception:  # noqa: BLE001
        deny("reference/outils-sensibles.json illisible (fail-closed)")

    kb = data.get("kb_test")
    if not isinstance(kb, dict):
        kb, _ = charger_kb()
    for cle, val in DEFAUTS.items():
        kb.setdefault(cle, val)

    # 1. taille du lot
    cibles = entree.get(champ)
    lot = len(cibles) if isinstance(cibles, list) else 1
    plafond_lot = regles.get("plafond_lot_defaut", 1)
    if not canal.startswith("linkedin_"):
        plafond_lot = min(kb["plafonds_lot"].get(canal, plafond_lot),
                          regles.get("max_serveur", plafond_lot),
                          PLAFONDS_SERVEUR.get(canal, 10**9))
    if lot > plafond_lot:
        deny(f"lot de {lot} cibles > plafond {plafond_lot} pour {canal} "
             "— réduire le lot, jamais le fractionner pour contourner")

    # 2. quota du jour (min KB / cadre Academy)
    maintenant = data.get("maintenant_test")
    try:
        if maintenant:
            maintenant = datetime.datetime.fromisoformat(maintenant)
        else:
            from zoneinfo import ZoneInfo
            maintenant = datetime.datetime.now(
                ZoneInfo(kb["fenetre_horaire"].get("fuseau", "Europe/Paris")))
    except Exception:  # noqa: BLE001
        deny("horloge illisible (fail-closed)")
    compteurs = data.get("compteurs_test")
    if not isinstance(compteurs, dict):
        compteurs = compteurs_du_jour(aujourdhui=maintenant.date().isoformat())
    quota = kb["quotas_jour"].get(canal, 0)
    cap = plafond_academy()
    if cap is not None:
        quota = min(quota, cap)
    fait = compteurs.get(canal, 0)
    if fait + lot > quota:
        deny(f"quota du jour : {fait} envoyé(s) + lot de {lot} > {quota} "
             f"pour {canal}" + (" (cadre Academy inclus)" if cap is not None
                                else "") +
             (" — appels automatisés désactivés par défaut"
              if canal == "appels" and quota == 0 else ""))

    # 3. fenêtre horaire
    f = kb["fenetre_horaire"]
    jour = JOURS[maintenant.weekday()]
    heure = maintenant.strftime("%H:%M")
    if jour not in f.get("jours", []) or \
            not f.get("debut", "09:00") <= heure < f.get("fin", "18:00"):
        deny(f"hors fenêtre d'envoi ({jour} {heure}, fenêtre "
             f"{'/'.join(f.get('jours', []))} {f.get('debut')}–{f.get('fin')} "
             f"{f.get('fuseau', 'Europe/Paris')})")

    ask(f"envoi réel {outil.group(1)} — lot de {lot}, {fait}/{quota} déjà "
        f"envoyé(s) aujourd'hui sur {canal}. Confirmer CET envoi "
        "(liste des cibles et contenu montrés) ; les champs posés par le "
        "modèle ne valent jamais confirmation humaine.")


if __name__ == "__main__":
    main()
