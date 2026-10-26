#!/usr/bin/env python3
"""Détecte les créneaux qui se chevauchent entre chaînes.

Règle affichée (et appliquée) : deux créneaux se CHEVAUCHENT si même jour
et moins de `--ecart` minutes d'écart (60 par défaut) — deux chaînes de la
maison qui publient en même temps se cannibalisent l'audience.

Usage :
    python3 grille.py grilles.json [--ecart 60]
grilles.json : {"<nom de chaîne>": réponse BRUTE de yt_list_schedule_slots,
…} — une entrée par chaîne. Les créneaux sont lus dans slots[] (day/jour,
time/heure « HH:MM »). Stdlib uniquement ; une grille vide est signalée,
jamais inventée.
"""
import json
import sys

JOURS = {"mon": "lundi", "tue": "mardi", "wed": "mercredi", "thu": "jeudi",
         "fri": "vendredi", "sat": "samedi", "sun": "dimanche"}


def creneaux(reponse):
    brut = reponse.get("slots") if isinstance(reponse, dict) else reponse
    out = []
    for s in brut or []:
        if not isinstance(s, dict):
            continue
        jour = str(s.get("day") or s.get("jour") or "").lower()[:3]
        heure = str(s.get("time") or s.get("heure") or "")
        if jour and ":" in heure:
            h, m = heure.split(":")[:2]
            out.append((JOURS.get(jour, jour), int(h) * 60 + int(m), heure))
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    ecart = int(argv[argv.index("--ecart") + 1]) if "--ecart" in argv else 60
    grilles = json.load(open(argv[1], encoding="utf-8"))
    tous = []
    for chaine, reponse in grilles.items():
        slots = creneaux(reponse)
        print(f"{chaine} : {len(slots)} créneau(x)"
              + (" — grille VIDE" if not slots else ""))
        tous += [(chaine, j, m, h) for j, m, h in slots]
    conflits = []
    for i, (c1, j1, m1, h1) in enumerate(tous):
        for c2, j2, m2, h2 in tous[i + 1:]:
            if c1 != c2 and j1 == j2 and abs(m1 - m2) < ecart:
                conflits.append(f"  {j1} : {c1} {h1} ↔ {c2} {h2} "
                                f"(écart {abs(m1 - m2)} min < {ecart})")
    if conflits:
        print(f"CHEVAUCHEMENTS ({len(conflits)}) — règle : même jour, "
              f"moins de {ecart} min d'écart entre chaînes :")
        print("\n".join(conflits))
        return 1
    print(f"aucun chevauchement entre chaînes (règle : {ecart} min).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
