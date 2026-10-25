#!/usr/bin/env python3
"""Contrôle de conformité d'un message AVANT enregistrement ou envoi.

Contrôles par canal (mêmes règles que le hook garde-conformite) :
- email : identité d'expéditeur renseignée dans la KB ET présente dans le
  message, phrase de désinscription présente (celle de la KB, ou à défaut
  un mot de la famille « désinscri / unsubscribe ») ;
- sms   : mention STOP présente, longueur ≤ 1 600 caractères ;
- appel : appels automatisés activés dans la KB, identité d'expéditeur
  présente dans le texte, formule de refus présente (« refuser », « STOP »,
  « ne plus être contacté ») ;
- tous  : aucun destinataire dans la liste d'opposition de la KB.

Usage :
    python3 conformite.py --canal email message.txt [cibles.json]
    python3 conformite.py --canal sms - < message.txt
Sortie : un verdict par contrôle, exit 0 si tout est conforme, 1 sinon.
Stdlib uniquement ; KB : ./rapido-kb/prospection.md (défauts prudents).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quotas import charger_kb  # noqa: E402

MOTS_DESINSCRIPTION = ("désinscri", "desinscri", "unsubscribe",
                       "ne plus recevoir")
MOTS_REFUS_APPEL = ("refuser", "stop", "ne plus être contacté",
                    "ne plus etre contacte")


def _rempli(valeur):
    return isinstance(valeur, str) and valeur.strip() \
        and "À COMPLÉTER" not in valeur


def verifier(canal, message, cibles, kb):
    """Liste de (controle, ok, detail)."""
    exp = kb.get("expediteur", {})
    bas = message.lower()
    out = []
    if canal == "email":
        out.append(("identité d'expéditeur (KB)", _rempli(exp.get("identite")),
                    "renseigner expediteur.identite dans ./rapido-kb/prospection.md"))
        out.append(("identité dans le message",
                    _rempli(exp.get("identite")) and exp["identite"].lower() in bas,
                    "le message doit dire qui écrit"))
        phrase = exp.get("desinscription", "")
        ok_des = (_rempli(phrase) and phrase.lower() in bas) or \
            any(m in bas for m in MOTS_DESINSCRIPTION)
        out.append(("désinscription", ok_des,
                    "phrase de désinscription obligatoire dans chaque e-mail"))
    elif canal == "sms":
        out.append(("mention STOP", "stop" in bas,
                    "mention STOP obligatoire dans chaque SMS"))
        out.append(("longueur ≤ 1 600", len(message) <= 1600,
                    f"{len(message)} caractères (plafond serveur 1 600)"))
    elif canal == "appel":
        out.append(("appels automatisés activés (KB)",
                    bool(kb.get("appels_automatises", {}).get("actives")),
                    "désactivés par défaut : validation juridique requise"))
        out.append(("identité dans le texte lu",
                    _rempli(exp.get("identite")) and exp["identite"].lower() in bas,
                    "le texte s'identifie dès les premières secondes"))
        out.append(("formule de refus", any(m in bas for m in MOTS_REFUS_APPEL),
                    "le texte offre un moyen de refuser"))
    opposition = {str(x).lower() for x in kb.get("liste_opposition", [])}
    bloquees = [c for c in cibles if str(c).lower() in opposition]
    out.append(("liste d'opposition", not bloquees,
                f"cible(s) opposée(s) : {bloquees[:3]}" if bloquees
                else "aucune cible opposée"))
    return out


def main(argv):
    if "--canal" not in argv:
        print(__doc__)
        return 2
    canal = argv[argv.index("--canal") + 1]
    reste = [a for a in argv[argv.index("--canal") + 2:]]
    message = sys.stdin.read() if (not reste or reste[0] == "-") \
        else open(reste[0], encoding="utf-8").read()
    cibles = []
    if len(reste) > 1 and os.path.isfile(reste[1]):
        brut = json.load(open(reste[1], encoding="utf-8"))
        cibles = brut if isinstance(brut, list) else []
    kb, source = charger_kb()
    print(f"KB : {source}")
    tout_ok = True
    for controle, ok, detail in verifier(canal, message, cibles, kb):
        print(f"  [{'OK' if ok else 'NON CONFORME'}] {controle} — {detail}")
        tout_ok &= bool(ok)
    print("verdict : " + ("conforme" if tout_ok else
                          "NON CONFORME — ne pas enregistrer, ne pas envoyer"))
    return 0 if tout_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
