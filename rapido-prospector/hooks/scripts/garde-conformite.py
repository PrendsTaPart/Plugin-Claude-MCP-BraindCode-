#!/usr/bin/env python3
"""Hook PreToolUse — conformité des envois Prospect (deny ou silence).

Refus (exit 2) :
- send_email sans identité d'expéditeur (KB renseignée ET présente dans le
  message) ou sans phrase de désinscription ;
- send_sms sans mention STOP ;
- place_call si les appels automatisés ne sont pas activés dans la KB, ou
  si le texte lu n'identifie pas l'expéditeur ou n'offre pas de refus ;
- tout destinataire présent dans la liste d'opposition de la KB
  (e-mail, numéro E.164 ou connectionId), quel que soit le canal.

Silence (exit 0) sinon : l'ask systématique vient de garde-envois-prospect.
Fail-closed : KB absente = identité absente = refus des e-mails et appels.
Clé de test réservée au harnais CI : kb_test.
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(PLUGIN, "scripts"))
from conformite import verifier  # noqa: E402
from quotas import DEFAUTS, charger_kb  # noqa: E402

RX_OUTIL = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Pp]rospect__([A-Za-z0-9_]+)$")
CANAUX = {"send_email": "email", "send_sms": "sms", "place_call": "appel"}


def deny(raisons):
    print("[garde-conformite] REFUS : " + " ; ".join(raisons), file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        deny(["entrée illisible (fail-closed)"])
    m = RX_OUTIL.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil = m.group(1)
    entree = data.get("tool_input") or {}

    kb = data.get("kb_test")
    if not isinstance(kb, dict):
        kb, _ = charger_kb()
    for cle, val in DEFAUTS.items():
        kb.setdefault(cle, val)

    message = " ".join(str(entree.get(c, "")) for c in
                       ("subject", "content", "message"))
    cibles = []
    for champ in ("recipients", "targets"):
        v = entree.get(champ)
        if isinstance(v, list):
            cibles += [x if isinstance(x, str) else
                       (x.get("email") or x.get("phone") or x.get("to") or "")
                       for x in v]
    if entree.get("connectionId"):
        cibles.append(str(entree["connectionId"]))

    if outil in CANAUX:
        controles = verifier(CANAUX[outil], message, cibles, kb)
    else:  # envois LinkedIn : seule la liste d'opposition s'applique ici
        controles = verifier("", message, cibles, kb)
    problemes = [f"{nom} ({detail})" for nom, ok, detail in controles if not ok]
    if problemes:
        deny(problemes)
    sys.exit(0)


if __name__ == "__main__":
    main()
