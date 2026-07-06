#!/usr/bin/env python3
"""Taux de charge d'équipe (stdlib uniquement).

Entrée (fichier JSON en argument, ou stdin) :
  {
    "periode_jours_ouvres": 10,          // durée analysée en jours ouvrés
    "personnes": [
      {"nom": "Alice", "hours_worked": 35,      // contractuel HEBDOMADAIRE
       "heures_declarees": 82.5,                // total dailies sur la période
       "dailies_remplis": 9, "dailies_attendus": 10,
       "taches_ouvertes": 7, "taches_urgentes": 2}, ...
    ]
  }

Sortie (stdout, JSON) : taux de charge % (déclaré / attendu), signal par
personne (rouge/jaune/vert/blanc), déséquilibres de tâches vs moyenne.
Seuils : > 110 % = surcharge ; 90-110 % = ok ; 60-90 % = à surveiller ;
< 60 % = sous-affectation SAUF si dailies incomplets (données incomplètes).
"""
import json
import sys

SEUIL_SURCHARGE = 110.0
SEUIL_OK_BAS = 90.0
SEUIL_SOUS_AFFECTATION = 60.0
COMPLETUDE_DAILIES_MIN = 0.8   # sous 80 % de dailies remplis → données incomplètes
FACTEUR_DESEQUILIBRE_TACHES = 1.5


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def main():
    try:
        data = lire_entree()
        personnes = data["personnes"]
        jours = float(data.get("periode_jours_ouvres", 10))
        assert isinstance(personnes, list) and personnes and jours > 0
    except Exception as e:
        sys.stderr.write(f"Entrée JSON invalide (clés 'personnes', 'periode_jours_ouvres') : {e}\n")
        sys.exit(1)

    resultats, exclus = [], []
    for p in personnes:
        try:
            hebdo = float(p["hours_worked"])
            declarees = float(p.get("heures_declarees") or 0)
            if hebdo <= 0:
                raise ValueError("hours_worked nul ou négatif")
        except (KeyError, TypeError, ValueError) as e:
            exclus.append({"nom": str(p.get("nom", "?")), "raison": str(e)})
            continue

        attendues = hebdo * (jours / 5.0)
        taux = declarees / attendues * 100.0 if attendues else 0.0
        remplis = p.get("dailies_remplis")
        attendus = p.get("dailies_attendus")
        completude = (float(remplis) / float(attendus)
                      if remplis is not None and attendus else None)

        if taux > SEUIL_SURCHARGE:
            signal, lecture = "rouge", "surcharge"
        elif taux >= SEUIL_OK_BAS:
            signal, lecture = "vert", "ok"
        elif taux >= SEUIL_SOUS_AFFECTATION:
            signal, lecture = "jaune", "à surveiller"
        elif completude is not None and completude < COMPLETUDE_DAILIES_MIN:
            signal, lecture = "blanc", "données incomplètes (dailies manquants — pas une conclusion de sous-charge)"
        else:
            signal, lecture = "jaune", "sous-affectation probable"

        resultats.append({
            "nom": str(p.get("nom", "?")),
            "heures_declarees": round(declarees, 1),
            "heures_attendues": round(attendues, 1),
            "taux_charge_pct": round(taux, 1),
            "completude_dailies_pct": round(completude * 100, 0) if completude is not None else None,
            "taches_ouvertes": p.get("taches_ouvertes"),
            "taches_urgentes": p.get("taches_urgentes"),
            "signal": signal,
            "lecture": lecture,
        })

    if not resultats:
        sys.stderr.write("Aucune personne exploitable.\n")
        sys.exit(1)

    # Déséquilibres de tâches vs moyenne de l'équipe.
    avec_taches = [r for r in resultats if isinstance(r["taches_ouvertes"], (int, float))]
    desequilibres = []
    if avec_taches:
        moyenne = sum(r["taches_ouvertes"] for r in avec_taches) / len(avec_taches)
        for r in avec_taches:
            if moyenne > 0 and r["taches_ouvertes"] > FACTEUR_DESEQUILIBRE_TACHES * moyenne:
                desequilibres.append({
                    "nom": r["nom"], "taches_ouvertes": r["taches_ouvertes"],
                    "moyenne_equipe": round(moyenne, 1),
                    "constat": "nettement au-dessus de la moyenne de l'équipe",
                })

    resultats.sort(key=lambda r: -r["taux_charge_pct"])

    print(json.dumps({
        "periode_jours_ouvres": jours,
        "seuils_pct": {"surcharge": SEUIL_SURCHARGE, "ok_min": SEUIL_OK_BAS,
                       "sous_affectation": SEUIL_SOUS_AFFECTATION},
        "personnes": resultats,
        "desequilibres_taches": desequilibres,
        "exclus": exclus,
        "note_methodo": "Attendu = hours_worked hebdo × (jours ouvrés / 5). Un signal blanc = données incomplètes, à clarifier avant toute conclusion.",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
