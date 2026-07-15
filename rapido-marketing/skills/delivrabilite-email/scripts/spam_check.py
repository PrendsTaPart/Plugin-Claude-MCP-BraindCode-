#!/usr/bin/env python3
"""Contrôle de risque spam d'un email (stdlib). Signale, ne réécrit PAS.

Le modèle ne juge jamais « de tête » : ce script mesure des signaux objectifs de
risque spam sur l'objet + le corps (lexique à risque FR/EN, densité de liens,
excès de majuscules, ponctuation agressive, promesses chiffrées) et rend des
signalements chiffrés + une note de risque. La RÉÉCRITURE est déléguée au skill
`rapidocrm:redaction-commerciale` — ce script ne propose aucune reformulation.

Entrée (fichier JSON en argument, ou stdin) :
    {"objet": "…", "corps": "…"}

Sortie (stdout, JSON) : signalements par catégorie + note (faible/moyen/élevé).
Code retour : 0.
"""
import json
import re
import sys

# Lexique à risque (déclencheurs FR/EN maison, minuscule).
LEXIQUE = [
    "gratuit", "free", "garanti", "guaranteed", "urgent", "offre limitée",
    "limited offer", "cliquez ici", "click here", "gagnez", "cash", "argent",
    "100%", "sans risque", "risk-free", "promo", "réduction", "discount",
    "acheter maintenant", "buy now", "meilleur prix", "best price", "bonus",
    "félicitations", "congratulations", "opportunité", "opportunity",
]
RE_LIEN = re.compile(r"https?://\S+")
RE_MOT = re.compile(r"\b[\wàâäéèêëïîôöùûüç'-]+\b", re.IGNORECASE)
RE_PROMESSE = re.compile(r"(?:x\s?\d+|\d+\s?%|\+\d+\s?%|\d+\s?(?:€|\$|k€|k\$))", re.IGNORECASE)


def analyser(data):
    objet = (data.get("objet") or "").strip()
    corps = (data.get("corps") or "").strip()
    texte = f"{objet}\n{corps}"
    bas = texte.lower()

    lexique_trouve = sorted({m for m in LEXIQUE if m in bas})

    liens = RE_LIEN.findall(texte)
    mots = RE_MOT.findall(texte)
    n_mots = len(mots) or 1
    densite_liens = round(len(liens) / n_mots, 4)

    mots_majuscules = [m for m in mots if len(m) >= 3 and m.isupper()]
    taux_majuscules = round(len(mots_majuscules) / n_mots, 4)

    exclamations = texte.count("!")
    promesses = RE_PROMESSE.findall(texte)

    # Points de risque (formule affichée).
    points = (
        len(lexique_trouve)
        + (2 if densite_liens > 0.03 else 0)
        + (2 if taux_majuscules > 0.1 else 0)
        + (1 if exclamations >= 3 else 0)
        + len(promesses)
    )
    note = "élevé" if points >= 6 else "moyen" if points >= 3 else "faible"

    signalements = []
    if lexique_trouve:
        signalements.append(f"Mots à risque : {', '.join(lexique_trouve)}.")
    if densite_liens > 0.03:
        signalements.append(f"Densité de liens élevée ({len(liens)} lien(s)).")
    if taux_majuscules > 0.1:
        signalements.append(f"Excès de majuscules ({len(mots_majuscules)} mot(s) en capitales).")
    if exclamations >= 3:
        signalements.append(f"Ponctuation agressive ({exclamations} points d'exclamation).")
    if promesses:
        signalements.append(f"Promesses chiffrées agressives : {', '.join(sorted(set(promesses)))}.")

    return {
        "formule": "points = |lexique| + 2*(densite_liens>0.03) + 2*(taux_maj>0.1) + (excl>=3) + |promesses| ; élevé>=6, moyen>=3, sinon faible",
        "n_mots": len(mots),
        "controles": {
            "lexique_risque": lexique_trouve,
            "n_liens": len(liens), "densite_liens": densite_liens,
            "mots_majuscules": len(mots_majuscules), "taux_majuscules": taux_majuscules,
            "exclamations": exclamations,
            "promesses_chiffrees": sorted(set(promesses)),
        },
        "points": points,
        "note_risque": note,
        "signalements": signalements,
        "note": "Réécriture déléguée à rapidocrm:redaction-commerciale — ce script ne reformule pas.",
    }


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def main():
    print(json.dumps(analyser(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
