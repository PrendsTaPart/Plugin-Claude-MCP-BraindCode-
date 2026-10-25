#!/usr/bin/env python3
"""Entonnoir de prospection, calculé depuis les seules réponses du serveur.

Formules affichées (et appliquées) :
    prospects   = fiches de list_clients
    contactés   = fiches distinctes touchées par ≥ 1 envoi
                  (list_emails ∪ list_sms ∪ list_calls ∪
                   list_linkedin_message_history, croisés par clientId,
                   e-mail ou téléphone normalisé)
    réponses / rendez-vous : NON mesurés par le serveur Prospect — affichés
                  « — (hors serveur) » sauf si un export CRM est fourni ;
    clients     = `customers` de stripe_stats si fourni, sinon « — ».

Aucune extrapolation : un chiffre absent s'affiche « — », jamais estimé.

Usage :
    python3 entonnoir.py clients.json [emails.json sms.json appels.json \
            linkedin.json stripe.json]
Chaque fichier est la réponse BRUTE de l'outil correspondant. Stdlib.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dedoublonner import _liste, _texte  # noqa: E402
from normaliser_telephone import normaliser  # noqa: E402


def _cles_contact(fiche):
    out = set()
    if _texte(fiche, "email"):
        out.add(("email", _texte(fiche, "email").lower()))
    tel = normaliser(_texte(fiche, "phone", "telephone", "to"))
    if tel:
        out.add(("tel", tel))
    ident = _texte(fiche, "clientId", "client_id", "id")
    if ident:
        out.add(("id", ident))
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    clients = _liste(json.load(open(argv[1], encoding="utf-8")))
    envois = []
    for chemin in argv[2:6]:
        if chemin and os.path.isfile(chemin):
            envois += _liste(json.load(open(chemin, encoding="utf-8")))
    stripe = None
    if len(argv) > 6 and os.path.isfile(argv[6]):
        stripe = json.load(open(argv[6], encoding="utf-8"))

    touches = set()
    for e in envois:
        touches |= _cles_contact(e)
    contactes = sum(1 for c in clients if _cles_contact(c) & touches) \
        if envois else None

    nb_clients = None
    if isinstance(stripe, dict):
        v = stripe.get("customers") or stripe.get("clients")
        nb_clients = v if isinstance(v, int) else (
            len(v) if isinstance(v, list) else None)

    def aff(v, note=""):
        return str(v) if v is not None else f"— {note}".strip()

    print(f"prospects    : {len(clients)}")
    print(f"contactés    : {aff(contactes, '(aucun historique fourni)')}")
    print("réponses     : — (hors serveur Prospect : à lire côté CRM)")
    print("rendez-vous  : — (hors serveur Prospect : à lire côté CRM)")
    print(f"clients      : {aff(nb_clients, '(stripe_stats non fourni)')}")
    print("# contactés = fiches croisées avec ≥ 1 envoi "
          "(clientId, e-mail ou téléphone E.164).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
