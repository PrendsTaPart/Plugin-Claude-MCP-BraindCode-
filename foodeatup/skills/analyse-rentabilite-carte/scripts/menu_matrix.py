#!/usr/bin/env python3
"""Ingénierie de menu — matrice popularité × marge (stdlib uniquement).

Entrée (fichier JSON en argument, ou stdin) :
  [{"plat": "...", "prix_vente": 12.5, "cout_ingredients": 4.1,
    "quantite_vendue": 87}, ...]
  (prix en euros HT ; quantités sur la période analysée)

Sortie (stdout, JSON) : food cost %, marge €, quadrant
(Stars / Plow-horses / Puzzles / Dogs), recommandation par plat, seuils utilisés.

Seuils (Kasavana-Smith) :
  - popularité haute : quantite_vendue >= 70 % de la quantité moyenne ;
  - marge haute : marge unitaire >= marge unitaire moyenne.
Alerte food cost si > 30 %.
"""
import json
import sys

SEUIL_POPULARITE = 0.70   # part de la quantité moyenne
SEUIL_FOOD_COST = 30.0    # % d'alerte

RECOMMANDATIONS = {
    "Stars": "Ne pas toucher : mettre en avant (carte, suggestion) et surveiller la constance.",
    "Plow-horses": "Repricer ou re-costifier : hausse modérée du prix ou réduction du coût matière sans dégrader la qualité perçue.",
    "Puzzles": "Repositionner : nom, place sur la carte, photo, vente par l'équipe. Retirer si toujours invendu après repositionnement.",
    "Dogs": "Retirer ou transformer (recette revisitée, plat du jour). Un seul cycle de seconde chance.",
}


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def main():
    try:
        plats = lire_entree()
    except Exception as e:
        sys.stderr.write(f"Entrée JSON invalide : {e}\n")
        sys.exit(1)

    if not isinstance(plats, list) or not plats:
        sys.stderr.write("Entrée attendue : liste non vide de plats.\n")
        sys.exit(1)

    valides, exclus = [], []
    for p in plats:
        try:
            prix = float(p["prix_vente"])
            cout = float(p["cout_ingredients"])
            qte = float(p["quantite_vendue"])
            if prix <= 0 or cout < 0 or qte < 0:
                raise ValueError("valeurs négatives ou prix nul")
            valides.append({"plat": str(p.get("plat", "?")), "prix": prix,
                            "cout": cout, "qte": qte})
        except (KeyError, TypeError, ValueError) as e:
            exclus.append({"plat": str(p.get("plat", "?")), "raison": str(e)})

    if not valides:
        sys.stderr.write("Aucun plat exploitable (données manquantes/invalides).\n")
        sys.exit(1)

    qte_moyenne = sum(p["qte"] for p in valides) / len(valides)
    seuil_qte = SEUIL_POPULARITE * qte_moyenne
    marges = [p["prix"] - p["cout"] for p in valides]
    marge_moyenne = sum(marges) / len(marges)

    resultats = []
    for p in valides:
        marge = p["prix"] - p["cout"]
        food_cost = (p["cout"] / p["prix"]) * 100.0
        populaire = p["qte"] >= seuil_qte
        marge_haute = marge >= marge_moyenne
        quadrant = ("Stars" if populaire and marge_haute else
                    "Plow-horses" if populaire else
                    "Puzzles" if marge_haute else "Dogs")
        resultats.append({
            "plat": p["plat"],
            "prix_vente": round(p["prix"], 2),
            "cout_ingredients": round(p["cout"], 2),
            "food_cost_pct": round(food_cost, 1),
            "alerte_food_cost": food_cost > SEUIL_FOOD_COST,
            "marge_unitaire_eur": round(marge, 2),
            "marge_totale_eur": round(marge * p["qte"], 2),
            "quantite_vendue": p["qte"],
            "quadrant": quadrant,
            "recommandation": RECOMMANDATIONS[quadrant],
        })

    ordre = {"Stars": 0, "Plow-horses": 1, "Puzzles": 2, "Dogs": 3}
    resultats.sort(key=lambda r: (ordre[r["quadrant"]], -r["marge_totale_eur"]))

    print(json.dumps({
        "seuils": {
            "quantite_moyenne": round(qte_moyenne, 1),
            "seuil_popularite": round(seuil_qte, 1),
            "marge_unitaire_moyenne_eur": round(marge_moyenne, 2),
            "seuil_alerte_food_cost_pct": SEUIL_FOOD_COST,
        },
        "plats": resultats,
        "exclus": exclus,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
