#!/usr/bin/env python3
"""Vérification budget média Higgsfield (stdlib) — verdict OK / CONFIRMATION / BLOQUÉ.

Le modèle ne tranche JAMAIS le budget de tête : ce script compare un coût estimé
(issu du préflight get_cost, jamais inventé) au solde de crédits et au plafond
mensuel de la KB (`rapido-kb/budget-media.md`), et rend un verdict déterministe.

Entrée (fichier JSON en argument, ou stdin) :
    {"solde": 8,                       // crédits dispo (balance)
     "cout_estime": 75,                // crédits (get_cost, jamais de tête)
     "plafond_mensuel": 50,            // KB ; null = non défini
     "seuil_confirmation": 5,          // KB ; au-delà → confirmation
     "deja_consomme": 10,              // compteur mensuel KB   OU
     "transactions": [{"type":"spend","credits":2}, ...]}  // pour le recalculer

Sortie (stdout, JSON) : verdict, raisons, formule, solde_apres, reste_plafond.
Code retour : 0 (le verdict est porté par le champ `verdict`).
"""
import json
import sys

SPEND = ("spend", "deduct")


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def consomme(data):
    txs = data.get("transactions")
    if txs is not None:
        return round(sum(abs(t.get("credits", 0) or 0)
                         for t in txs if t.get("type") in SPEND), 4)
    return data.get("deja_consomme", 0) or 0


def evaluer(data):
    solde = data.get("solde")
    cout = data.get("cout_estime", 0) or 0
    plafond = data.get("plafond_mensuel")
    seuil = data.get("seuil_confirmation")
    deja = consomme(data)
    reste_plafond = (plafond - deja) if plafond is not None else None

    raisons = []
    verdict = "OK"
    if solde is not None and cout > solde:
        verdict = "BLOQUÉ"
        raisons.append(f"crédits insuffisants : coût {cout} > solde {solde}")
    elif reste_plafond is not None and cout > reste_plafond:
        verdict = "BLOQUÉ"
        raisons.append(f"dépasse le plafond mensuel KB : coût {cout} > reste {reste_plafond} "
                       f"(plafond {plafond} − déjà consommé {deja})")
    elif seuil is not None and cout > seuil:
        verdict = "CONFIRMATION REQUISE"
        raisons.append(f"coût {cout} > seuil de confirmation {seuil}")
    else:
        raisons.append("coût sous le seuil, budget et plafond OK")

    if plafond is None:
        raisons.append("plafond mensuel NON défini dans budget-media.md (à renseigner)")

    return {
        "formule": "BLOQUÉ si coût>solde OU coût>(plafond−déjà) ; "
                   "CONFIRMATION si coût>seuil ; sinon OK",
        "cout_estime": cout,
        "solde": solde,
        "deja_consomme": deja,
        "plafond_mensuel": plafond,
        "reste_plafond_avant": reste_plafond,
        "verdict": verdict,
        "raisons": raisons,
        "solde_apres_si_execute": (round(solde - cout, 4) if solde is not None else None),
        "reste_plafond_apres_si_execute": (round(reste_plafond - cout, 4)
                                           if reste_plafond is not None else None),
    }


def main():
    print(json.dumps(evaluer(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
