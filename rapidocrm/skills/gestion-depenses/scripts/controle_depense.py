#!/usr/bin/env python3
"""Contrôle de cohérence d'une dépense AVANT saisie CRM (stdlib uniquement).

Entrée : fichier JSON {"total_ht": float, "taux_tva": float,
"total_ttc": float optionnel, "total_tva": float optionnel}.
Sortie : JSON {coherent, ttc_attendu, tva_attendue, ecart_ttc, ecart_tva,
formule_appliquee, entrees}. Tolérance : 0,01 (arrondi au centime).

Usage : python3 controle_depense.py <entrees.json>
"""
import json
import sys

TOLERANCE = 0.01


def controler(entrees):
    try:
        total_ht = float(entrees["total_ht"])
    except (KeyError, TypeError, ValueError):
        return {"erreur": "total_ht manquant ou non numérique (requis)"}
    try:
        taux_tva = float(entrees.get("taux_tva", 0))
    except (TypeError, ValueError):
        return {"erreur": "taux_tva non numérique"}
    if total_ht < 0 or taux_tva < 0:
        return {"erreur": "total_ht et taux_tva doivent être positifs"}

    tva_attendue = round(total_ht * taux_tva / 100.0, 2)
    ttc_attendu = round(total_ht + tva_attendue, 2)

    resultat = {
        "entrees": {"total_ht": total_ht, "taux_tva": taux_tva},
        "tva_attendue": tva_attendue,
        "ttc_attendu": ttc_attendu,
        "formule_appliquee": (
            f"TVA = {total_ht:.2f} × {taux_tva:g} % = {tva_attendue:.2f} ; "
            f"TTC = {total_ht:.2f} + {tva_attendue:.2f} = {ttc_attendu:.2f}"
        ),
        "coherent": True,
    }

    if entrees.get("total_ttc") is not None:
        ecart = round(abs(float(entrees["total_ttc"]) - ttc_attendu), 2)
        resultat["entrees"]["total_ttc"] = float(entrees["total_ttc"])
        resultat["ecart_ttc"] = ecart
        if ecart > TOLERANCE:
            resultat["coherent"] = False
    if entrees.get("total_tva") is not None:
        ecart = round(abs(float(entrees["total_tva"]) - tva_attendue), 2)
        resultat["entrees"]["total_tva"] = float(entrees["total_tva"])
        resultat["ecart_tva"] = ecart
        if ecart > TOLERANCE:
            resultat["coherent"] = False
    return resultat


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"erreur": "usage: controle_depense.py <entrees.json>"}))
        return 1
    try:
        with open(sys.argv[1], encoding="utf-8") as f:
            entrees = json.load(f)
    except Exception as exc:
        print(json.dumps({"erreur": f"JSON illisible : {exc}"}))
        return 1
    resultat = controler(entrees)
    print(json.dumps(resultat, ensure_ascii=False, indent=2))
    return 0 if resultat.get("coherent") and "erreur" not in resultat else 1


if __name__ == "__main__":
    sys.exit(main())
