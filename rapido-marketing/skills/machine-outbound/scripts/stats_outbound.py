#!/usr/bin/env python3
"""Stats outbound par séquence et par segment ICP (stdlib uniquement).

Le modèle NE calcule JAMAIS les taux de tête : ce script agrège les compteurs
réels (envoyés, réponses, RDV, opportunités) issus du CRM et sort les taux, puis
les compare aux benchmarks maison (./rapido-kb/marketing/benchmarks.md, passés
en entrée).

Entrée (fichier JSON en argument, ou stdin) :
    {"sequences": [
        {"sequence": "S1 fondateurs", "segment": "resto/TPE",
         "envoyes": 200, "reponses": 14, "rdv": 4, "opportunites": 2}, ...],
     "benchmarks": {                         // optionnel
        "taux_reponse": 0.05, "taux_rdv": 0.02}}

Sortie (stdout, JSON) : par ligne les taux (réponse, RDV, opportunité) +
verdict vs benchmark si fourni ; agrégats globaux et par segment. Code : 0.
"""
import json
import sys
from collections import defaultdict


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def taux(num, den):
    return round(num / den, 4) if den else 0.0


def ligne_stats(row):
    env = row.get("envoyes", 0) or 0
    rep = row.get("reponses", 0) or 0
    rdv = row.get("rdv", 0) or 0
    opp = row.get("opportunites", 0) or 0
    return {
        "sequence": row.get("sequence", "?"),
        "segment": row.get("segment", "?"),
        "envoyes": env, "reponses": rep, "rdv": rdv, "opportunites": opp,
        "taux_reponse": taux(rep, env),
        "taux_rdv": taux(rdv, env),
        "taux_opportunite": taux(opp, env),
    }


def verdict(l, bench):
    v = {}
    if "taux_reponse" in bench:
        v["reponse"] = "au-dessus" if l["taux_reponse"] >= bench["taux_reponse"] else "en-dessous"
    if "taux_rdv" in bench:
        v["rdv"] = "au-dessus" if l["taux_rdv"] >= bench["taux_rdv"] else "en-dessous"
    return v


def agreger(lignes):
    tot = defaultdict(int)
    par_seg = defaultdict(lambda: defaultdict(int))
    for l in lignes:
        for k in ("envoyes", "reponses", "rdv", "opportunites"):
            tot[k] += l[k]
            par_seg[l["segment"]][k] += l[k]
    glob = {
        "envoyes": tot["envoyes"], "reponses": tot["reponses"],
        "rdv": tot["rdv"], "opportunites": tot["opportunites"],
        "taux_reponse": taux(tot["reponses"], tot["envoyes"]),
        "taux_rdv": taux(tot["rdv"], tot["envoyes"]),
        "taux_opportunite": taux(tot["opportunites"], tot["envoyes"]),
    }
    segments = {
        seg: {
            **d,
            "taux_reponse": taux(d["reponses"], d["envoyes"]),
            "taux_rdv": taux(d["rdv"], d["envoyes"]),
        } for seg, d in par_seg.items()
    }
    return glob, segments


def analyser(data):
    bench = data.get("benchmarks") or {}
    lignes = [ligne_stats(r) for r in (data.get("sequences") or [])]
    for l in lignes:
        if bench:
            l["vs_benchmark"] = verdict(l, bench)
    glob, segments = agreger(lignes)
    return {
        "formule": "taux = compteur / envoyés (par séquence, segment, global)",
        "benchmarks": bench,
        "global": glob,
        "par_segment": segments,
        "par_sequence": lignes,
    }


def main():
    print(json.dumps(analyser(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
