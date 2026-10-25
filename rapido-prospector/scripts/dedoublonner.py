#!/usr/bin/env python3
"""Dédoublonne les prospects d'une prospection contre la base existante.

Critères (dans l'ordre, affichés tels qu'appliqués) — un prospect est un
DOUBLON dès qu'UN critère matche une fiche existante :
1. placeId identique (place_id / placeId) ;
2. site web identique (domaine normalisé : minuscules, sans www ni schéma) ;
3. téléphone identique après normalisation E.164 (normaliser_telephone) ;
4. e-mail identique (minuscules) ;
5. nom + adresse identiques après normalisation (minuscules, sans accents
   ni ponctuation, espaces réduits).

Usage :
    python3 dedoublonner.py nouveaux.json existants.json [rapport.json]

nouveaux.json : la réponse BRUTE de run_prospection (liste, ou objet avec
une clé prospects/results/clients). existants.json : la réponse BRUTE de
list_clients. Le rapport classe : nouveaux / doublons (avec le critère) /
sans_contact (ni e-mail ni téléphone ni site). Écrit aussi le marqueur de
session .claude/state/prospect-session.json (lu par le hook anti-doublon).
Stdlib uniquement ; rien n'est enregistré côté serveur par ce script.
"""
import datetime
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normaliser_telephone import normaliser  # noqa: E402

RX_PONCT = re.compile(r"[^a-z0-9 ]")


def _liste(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for cle in ("prospects", "results", "clients", "items", "data"):
            if isinstance(data.get(cle), list):
                return data[cle]
    return []


def _texte(fiche, *cles):
    for c in cles:
        v = fiche.get(c)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return ""


def _domaine(url):
    u = url.lower().strip()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    return u.split("/")[0] or None if u else None


def _nom_adresse(fiche):
    brut = (_texte(fiche, "name", "nom") + " " +
            _texte(fiche, "address", "adresse")).lower()
    brut = unicodedata.normalize("NFKD", brut).encode("ascii", "ignore").decode()
    brut = RX_PONCT.sub(" ", brut)
    brut = re.sub(r" +", " ", brut).strip()
    return brut or None


def cles(fiche):
    """Les clés de dédoublonnage d'une fiche, par critère."""
    return {
        "placeId": _texte(fiche, "placeId", "place_id") or None,
        "site": _domaine(_texte(fiche, "website", "site", "url")),
        "telephone": normaliser(_texte(fiche, "phone", "telephone")),
        "email": _texte(fiche, "email").lower() or None,
        "nom+adresse": _nom_adresse(fiche),
    }


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    nouveaux = _liste(json.load(open(argv[1], encoding="utf-8")))
    existants = _liste(json.load(open(argv[2], encoding="utf-8")))

    index = {}
    for fiche in existants:
        for critere, valeur in cles(fiche).items():
            if valeur:
                index[(critere, valeur)] = True

    rapport = {"nouveaux": [], "doublons": [], "sans_contact": []}
    vus = set()
    for p in nouveaux:
        k = cles(p)
        critere = next((c for c, v in k.items() if v and (c, v) in index), None)
        interne = next((c for c, v in k.items() if v and (c, v) in vus), None)
        for c, v in k.items():
            if v:
                vus.add((c, v))
        if critere or interne:
            rapport["doublons"].append(
                {"fiche": p, "critere": critere or f"{interne} (doublon interne au lot)"})
        elif not (k["email"] or k["telephone"] or k["site"]):
            rapport["sans_contact"].append(p)
        else:
            rapport["nouveaux"].append(p)

    if len(argv) > 3:
        with open(argv[3], "w", encoding="utf-8") as f:
            json.dump(rapport, f, ensure_ascii=False, indent=2)
    os.makedirs(".claude/state", exist_ok=True)
    marque = ".claude/state/prospect-session.json"
    try:
        etat = json.load(open(marque, encoding="utf-8"))
    except Exception:  # noqa: BLE001
        etat = {}
    etat["dedoublonnage"] = datetime.datetime.now().isoformat(timespec="seconds")
    etat["dedoublonnage_volumes"] = {k: len(v) for k, v in rapport.items()}
    json.dump(etat, open(marque, "w", encoding="utf-8"), ensure_ascii=False)

    print(f"nouveaux     : {len(rapport['nouveaux'])}")
    print(f"doublons     : {len(rapport['doublons'])}")
    print(f"sans contact : {len(rapport['sans_contact'])} "
          "(ni e-mail, ni téléphone, ni site — à compléter avant d'enregistrer)")
    for d in rapport["doublons"][:10]:
        nom = _texte(d["fiche"], "name", "nom") or "(sans nom)"
        print(f"  doublon [{d['critere']}] {nom}")
    print("# Seuls les « nouveaux » passent à add_clients, après accord.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
