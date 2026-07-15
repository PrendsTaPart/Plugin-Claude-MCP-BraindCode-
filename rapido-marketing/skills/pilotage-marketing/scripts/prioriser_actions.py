#!/usr/bin/env python3
"""Priorisation ICE des actions de pilotage marketing + allocation machine (stdlib).

Le modèle ne priorise JAMAIS de tête : ce script calcule le score ICE de chaque
action candidate, la range par machine (inbound / outbound / tunnel / paid), et
signale les doublons — soit contre les tâches déjà au Kanban RapidoRH (passées en
entrée), soit entre actions candidates. La décision reste humaine ; ce script
n'ordonnance que des chiffres.

Entrée (fichier JSON en argument, ou stdin) :
    {"actions": [
        {"nom": "Relancer les leads dormants", "machine": "outbound",
         "impact": 8, "confidence": 7, "ease": 6},
        ...],
     "taches_kanban": ["Relancer les leads dormants", ...]}   // titres existants

ICE : chaque axe 1-10 ; score = moyenne(impact, confidence, ease) ;
produit = impact*confidence*ease (départage). machine ∈ inbound|outbound|tunnel|paid|autre.

Sortie (stdout, JSON) : actions triées (rang, score, machine, flags doublon),
répartition par machine, liste des doublons Kanban. Code : 0.
"""
import json
import re
import sys
from collections import defaultdict

MACHINES = ("inbound", "outbound", "tunnel", "paid")


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def borne(x):
    try:
        return max(1.0, min(10.0, float(x)))
    except (TypeError, ValueError):
        return 1.0


def norm(titre):
    return re.sub(r"\s+", " ", (titre or "").strip().lower())


def prioriser(data):
    kanban = {norm(t) for t in (data.get("taches_kanban") or [])}
    vus = defaultdict(int)
    lignes = []
    for a in (data.get("actions") or []):
        i, c, e = borne(a.get("impact")), borne(a.get("confidence")), borne(a.get("ease"))
        machine = a.get("machine") if a.get("machine") in MACHINES else "autre"
        n = norm(a.get("nom"))
        vus[n] += 1
        lignes.append({
            "nom": a.get("nom", "?"),
            "machine": machine,
            "impact": i, "confidence": c, "ease": e,
            "score_ice": round((i + c + e) / 3, 2),
            "produit": round(i * c * e, 1),
            "doublon_kanban": n in kanban,
            "doublon_interne": False,  # complété ci-dessous
        })
    for l in lignes:
        if vus[norm(l["nom"])] > 1:
            l["doublon_interne"] = True

    lignes.sort(key=lambda x: (x["score_ice"], x["produit"]), reverse=True)
    for rang, l in enumerate(lignes, 1):
        l["rang"] = rang

    par_machine = defaultdict(lambda: {"n": 0, "actions": []})
    for l in lignes:
        par_machine[l["machine"]]["n"] += 1
        par_machine[l["machine"]]["actions"].append(l["nom"])

    doublons = [l["nom"] for l in lignes if l["doublon_kanban"] or l["doublon_interne"]]

    return {
        "formule": "score_ice = moyenne(impact, confidence, ease), axes 1-10 ; "
                   "produit = impact*confidence*ease (départage)",
        "actions_priorisees": lignes,
        "par_machine": {m: dict(v) for m, v in par_machine.items()},
        "doublons_a_ne_pas_recreer": doublons,
        "note": "Doublon Kanban / interne = NE PAS recréer ; vérifier le Kanban RapidoRH avant toute création.",
    }


def main():
    print(json.dumps(prioriser(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
