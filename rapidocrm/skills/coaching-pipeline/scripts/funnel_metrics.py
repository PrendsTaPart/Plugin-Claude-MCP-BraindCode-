#!/usr/bin/env python3
"""Métriques de funnel commercial (stdlib uniquement).

Entrée (fichier JSON en argument, ou stdin) :
  {
    "date_reference": "2026-07-06",          // optionnel, défaut = aujourd'hui
    "seuil_dormant_jours": 14,               // optionnel, défaut 14
    "etapes": [                              // dans l'ordre du funnel
      {"nom": "Prospects", "probabilite": 0.10,   // proba de signature 0-1 (optionnel)
       "deals": [{"nom": "ACME", "montant": 5000,
                  "derniere_activite": "2026-06-10"}]},
      ...
    ]
  }

Sortie (stdout, JSON) : compteurs et taux de conversion étape par étape,
deals dormants (> seuil jours sans activité), valeur brute et pondérée du
pipeline.
"""
import json
import sys
from datetime import date


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def parse_date(s):
    y, m, d = str(s).split("-")
    return date(int(y), int(m), int(d))


def main():
    try:
        data = lire_entree()
        etapes = data["etapes"]
        assert isinstance(etapes, list) and etapes
    except Exception as e:
        sys.stderr.write(f"Entrée JSON invalide (clé 'etapes' requise) : {e}\n")
        sys.exit(1)

    seuil = int(data.get("seuil_dormant_jours", 14))
    try:
        ref = parse_date(data["date_reference"]) if "date_reference" in data else date.today()
    except Exception:
        sys.stderr.write("date_reference invalide (format YYYY-MM-DD).\n")
        sys.exit(1)

    funnel, dormants = [], []
    valeur_brute = valeur_ponderee = 0.0

    for i, etape in enumerate(etapes):
        nom = str(etape.get("nom", f"étape {i + 1}"))
        deals = etape.get("deals") or []
        proba = etape.get("probabilite")
        montant_etape = 0.0
        for d in deals:
            montant = float(d.get("montant") or 0)
            montant_etape += montant
            da = d.get("derniere_activite")
            if da:
                try:
                    jours = (ref - parse_date(da)).days
                except Exception:
                    jours = None
                if jours is not None and jours > seuil:
                    dormants.append({
                        "deal": str(d.get("nom", "?")), "etape": nom,
                        "montant": montant,
                        "jours_sans_activite": jours,
                    })
        valeur_brute += montant_etape
        if proba is not None:
            valeur_ponderee += montant_etape * float(proba)
        funnel.append({"etape": nom, "nb_deals": len(deals),
                       "montant_total": round(montant_etape, 2),
                       "probabilite": proba})

    # Taux de conversion étape N -> N+1 (sur les compteurs actuels : approximation
    # instantanée du funnel, pas une cohorte — l'indiquer dans la restitution).
    for i in range(len(funnel) - 1):
        n, n1 = funnel[i]["nb_deals"], funnel[i + 1]["nb_deals"]
        funnel[i]["conversion_vers_etape_suivante_pct"] = (
            round(100.0 * n1 / n, 1) if n else None)

    maillon_faible = None
    candidats = [f for f in funnel if f.get("conversion_vers_etape_suivante_pct") is not None]
    if candidats:
        maillon_faible = min(candidats, key=lambda f: f["conversion_vers_etape_suivante_pct"])["etape"]

    dormants.sort(key=lambda d: -d["jours_sans_activite"])

    print(json.dumps({
        "date_reference": ref.isoformat(),
        "seuil_dormant_jours": seuil,
        "funnel": funnel,
        "maillon_faible": maillon_faible,
        "note_methodo": "Conversions calculées sur l'instantané du pipeline (pas une cohorte).",
        "deals_dormants": dormants,
        "valeur_pipeline": {
            "brute": round(valeur_brute, 2),
            "ponderee": round(valeur_ponderee, 2),
            "ponderation_complete": all(f.get("probabilite") is not None for f in funnel),
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
