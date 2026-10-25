#!/usr/bin/env python3
"""Quotas d'envoi du jour : ce qui reste par canal, et pourquoi.

Formule affichée (et appliquée) :
    restant(canal) = quota_jour_effectif(canal) − envoyés_du_jour(canal)
    quota_jour_effectif = min(quota KB, cadre Academy s'il existe)
    plafond_lot_effectif = min(plafond_lot KB, plafond serveur)

Sources, dans l'ordre :
- ./rapido-kb/prospection.md — premier bloc ```json (gabarit du dépôt) ;
  absent ou illisible → valeurs PRUDENTES par défaut (appels désactivés) ;
- .claude/state/prospect-envois.json — compteurs du jour (PostToolUse) ;
- .claude/state/cadre-employe.json — cadre Academy (rapido-employe) : son
  plafond d'envois/jour borne chaque canal s'il est plus petit.

Usage : python3 quotas.py          (rapport lisible)
        python3 quotas.py --json   (le même, en JSON)
Stdlib uniquement.
"""
import datetime
import json
import os
import re
import sys

KB = os.path.join("rapido-kb", "prospection.md")
COMPTEURS = os.path.join(".claude", "state", "prospect-envois.json")
CADRE = os.path.join(".claude", "state", "cadre-employe.json")

DEFAUTS = {
    "quotas_jour": {"email": 50, "sms": 20, "appels": 0,
                    "linkedin_invitations": 10, "linkedin_messages": 20},
    "plafonds_lot": {"email": 25, "sms": 10, "appels": 5},
    "fenetre_horaire": {"debut": "09:00", "fin": "18:00",
                        "jours": ["lun", "mar", "mer", "jeu", "ven"],
                        "fuseau": "Europe/Paris"},
    "expediteur": {}, "liste_opposition": [],
    "appels_automatises": {"actives": False},
}
PLAFONDS_SERVEUR = {"sms": 200, "appels": 100}


def charger_kb(racine="."):
    """Le bloc machine de la KB, ou les défauts prudents (jamais d'erreur)."""
    try:
        texte = open(os.path.join(racine, KB), encoding="utf-8").read()
        bloc = re.search(r"```json\s*(\{.*?\})\s*```", texte, re.S).group(1)
        kb = json.loads(bloc)
    except Exception:  # noqa: BLE001
        return dict(DEFAUTS), "défauts prudents (KB absente ou illisible)"
    for cle, val in DEFAUTS.items():
        kb.setdefault(cle, val)
    return kb, KB


def compteurs_du_jour(racine=".", aujourdhui=None):
    aujourdhui = aujourdhui or datetime.date.today().isoformat()
    try:
        c = json.load(open(os.path.join(racine, COMPTEURS), encoding="utf-8"))
        if c.get("date") == aujourdhui:
            return c
    except Exception:  # noqa: BLE001
        pass
    return {"date": aujourdhui, "email": 0, "sms": 0, "appels": 0,
            "linkedin_invitations": 0, "linkedin_messages": 0}


def plafond_academy(racine="."):
    """Le plafond d'envois/jour du cadre Academy, ou None s'il n'existe pas."""
    try:
        cadre = json.load(open(os.path.join(racine, CADRE), encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None
    for chemin in (("quotas", "envoisJour"), ("cadre", "quotas", "envoisJour"),
                   ("envoisJour",)):
        v = cadre
        for cle in chemin:
            v = v.get(cle) if isinstance(v, dict) else None
        if isinstance(v, int):
            return v
    return None


def restants(racine=".", aujourdhui=None):
    kb, source = charger_kb(racine)
    envoyes = compteurs_du_jour(racine, aujourdhui)
    cap = plafond_academy(racine)
    rapport = {"source_kb": source, "date": envoyes["date"],
               "cadre_academy": cap, "canaux": {}}
    for canal, quota in kb["quotas_jour"].items():
        effectif = min(quota, cap) if cap is not None else quota
        fait = envoyes.get(canal, 0)
        if canal.startswith("linkedin_"):
            lot = 1  # LinkedIn : toujours un envoi à la fois, sur accord
        else:
            lot_kb = kb["plafonds_lot"].get(canal, 1)
            lot = min(lot_kb, PLAFONDS_SERVEUR.get(canal, lot_kb))
        rapport["canaux"][canal] = {
            "quota_jour": effectif, "envoyes": fait,
            "restant": max(0, effectif - fait), "plafond_lot": lot,
        }
    return rapport


def main(argv):
    r = restants()
    if "--json" in argv:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return 0
    print(f"Quotas du {r['date']} — source : {r['source_kb']}"
          + (f" — cadre Academy : {r['cadre_academy']}/jour (borne chaque canal)"
             if r["cadre_academy"] is not None else ""))
    for canal, c in r["canaux"].items():
        print(f"  {canal:22s} {c['envoyes']}/{c['quota_jour']} envoyés — "
              f"restant {c['restant']}, lot max {c['plafond_lot']}")
    print("# restant = quota_jour_effectif − envoyés ; "
          "quota effectif = min(KB, cadre Academy).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
