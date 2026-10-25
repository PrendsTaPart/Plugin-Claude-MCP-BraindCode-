#!/usr/bin/env python3
"""Lit stripe_stats et restitue le MRR SANS l'embellir.

Règles affichées (et appliquées) :
- le MRR renvoyé par le serveur est une ESTIMATION : il s'affiche
  « MRR estimé », jamais « MRR » tout court ;
- l'évolution n'est calculée QUE si un historique est fourni (fichier JSON
  de relevés précédents [{"date": …, "mrr": …}, …]) :
      évolution % = (MRR_actuel − MRR_précédent) / MRR_précédent × 100
- tout champ absent s'affiche « — » ; aucun chiffre n'est inventé ;
- restitution AGRÉGÉE : aucun e-mail client n'est affiché ni journalisé.

Usage : python3 mrr.py stripe.json [historique.json]
stripe.json : la réponse BRUTE de stripe_stats. Stdlib uniquement.
"""
import json
import sys


def _nombre(d, *cles):
    for c in cles:
        v = d.get(c)
        if isinstance(v, (int, float)):
            return v
        if isinstance(v, list):
            return len(v)
    return None


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    d = json.load(open(argv[1], encoding="utf-8"))
    if not isinstance(d, dict):
        print("stripe_stats : réponse inattendue (pas un objet) — rien à lire.")
        return 1
    mrr = _nombre(d, "mrr", "mrr_estime", "estimated_mrr")
    aff = lambda v, u="": (f"{v}{u}" if v is not None else "—")  # noqa: E731
    print(f"MRR estimé        : {aff(mrr, ' €')} (estimation du serveur, "
          "pas un chiffre comptable)")
    print(f"abonnements actifs : {aff(_nombre(d, 'active_subscriptions', 'subscriptions'))}")
    print(f"clients            : {aff(_nombre(d, 'customers', 'clients'))}")
    print(f"paiements          : {aff(_nombre(d, 'payments'))}")
    print(f"chiffre d'affaires : {aff(_nombre(d, 'revenue', 'total_revenue', 'ca'), ' €')}")
    if len(argv) > 2 and mrr is not None:
        try:
            histo = json.load(open(argv[2], encoding="utf-8"))
            prec = [h for h in histo if isinstance(h.get("mrr"), (int, float))][-1]
            pct = (mrr - prec["mrr"]) / prec["mrr"] * 100 if prec["mrr"] else None
            print(f"évolution          : {aff(round(pct, 1) if pct is not None else None, ' %')} "
                  f"vs {prec.get('date', '?')} (formule : (actuel−précédent)/précédent×100)")
        except Exception:  # noqa: BLE001
            print("évolution          : — (historique illisible)")
    else:
        print("évolution          : — (pas d'historique fourni)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
