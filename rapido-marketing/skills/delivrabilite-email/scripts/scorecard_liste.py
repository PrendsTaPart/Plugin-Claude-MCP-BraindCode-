#!/usr/bin/env python3
"""Scorecard de liste avant envoi (stdlib). Note A-E + refus si sous le seuil KB.

Le modèle NE juge JAMAIS une liste de tête : ce script mesure la qualité d'un
segment/export (doublons, emails de rôle, formats invalides, diversité des
titres, concentration de domaines, taille vs plafond quotidien) et rend une note
CHIFFRÉE A-E avec formule, plus un booléen `refus` si la note est sous le seuil
défini dans la KB (`rapido-kb/marketing/delivrabilite.md`).

Entrée (fichier JSON en argument, ou stdin) :
    {"contacts": [{"email": "a@x.com", "titre": "CEO"}, ...],   // ou :
     "emails": ["a@x.com", ...],
     "plafond_quotidien": 200,        // du delivrabilite.md
     "seuil_note": "C"}               // refuse si pire que ce seuil (défaut C)

Sortie (stdout, JSON) : métriques par contrôle, note A-E, refus (bool), actions
correctives. Code retour : 0 (le refus est porté par le champ `refus`, pas par
le code de sortie — l'appelant décide).
"""
import json
import re
import sys
from collections import Counter

RE_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
ROLES = {"info", "contact", "sales", "vente", "ventes", "admin", "support",
         "hello", "bonjour", "team", "equipe", "no-reply", "noreply", "ne-pas-repondre",
         "postmaster", "webmaster", "marketing", "rh", "compta", "comptabilite",
         "direction", "accueil", "office"}
BANDES = ["A", "B", "C", "D", "E"]  # index 0 = meilleur


def taux(num, den):
    return round(num / den, 4) if den else 0.0


def normaliser(data):
    if data.get("contacts"):
        return [{"email": (c.get("email") or "").strip(),
                 "titre": (c.get("titre") or "").strip()} for c in data["contacts"]]
    return [{"email": (e or "").strip(), "titre": ""} for e in data.get("emails", [])]


def bande_pour_score(score):
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= 45:
        return "D"
    return "E"


def analyser(data):
    contacts = normaliser(data)
    n = len(contacts)
    plafond = data.get("plafond_quotidien")
    seuil = (data.get("seuil_note") or "C").upper()

    emails = [c["email"].lower() for c in contacts]
    valides = [e for e in emails if RE_EMAIL.match(e)]
    invalides = [e for e in emails if not RE_EMAIL.match(e)]
    doublons = sum(c - 1 for c in Counter(emails).values() if c > 1)
    roles = [e for e in valides if e.split("@")[0] in ROLES]

    domaines = Counter(e.split("@")[1] for e in valides if "@" in e)
    dom_top = domaines.most_common(1)[0] if domaines else (None, 0)
    concentration = taux(dom_top[1], len(valides))

    titres = [c["titre"].lower() for c in contacts if c["titre"]]
    diversite_titres = taux(len(set(titres)), len(titres)) if titres else None

    t_invalide = taux(len(invalides), n)
    t_doublon = taux(doublons, n)
    t_role = taux(len(roles), n)

    # Score 100 - pénalités (formule affichée en sortie).
    score = 100.0
    score -= 100 * t_invalide            # format invalide : lourd
    score -= 60 * t_doublon              # doublons
    score -= 50 * t_role                 # emails de rôle
    if concentration > 0.5:
        score -= 100 * (concentration - 0.5)   # >50 % d'un domaine
    if diversite_titres is not None and diversite_titres < 0.3:
        score -= 20 * (0.3 - diversite_titres) / 0.3
    score = max(0.0, round(score, 1))
    note = bande_pour_score(score)

    depasse_plafond = bool(plafond) and len(valides) > plafond
    refus = BANDES.index(note) > BANDES.index(seuil) if seuil in BANDES else False

    actions = []
    if invalides:
        actions.append(f"Retirer {len(invalides)} email(s) au format invalide.")
    if doublons:
        actions.append(f"Dédoublonner : {doublons} doublon(s).")
    if roles:
        actions.append(f"Écarter {len(roles)} email(s) de rôle (info@, contact@…).")
    if concentration > 0.5:
        actions.append(f"Diversifier les domaines (>{int(concentration*100)}% sur {dom_top[0]}).")
    if diversite_titres is not None and diversite_titres < 0.3:
        actions.append("Faible diversité des titres : vérifier que le ciblage n'est pas trop homogène.")
    if depasse_plafond:
        actions.append(f"Lot ({len(valides)}) > plafond quotidien ({plafond}) : fractionner sur plusieurs jours.")
    if refus:
        actions.insert(0, f"REFUS : note {note} sous le seuil KB {seuil} — corriger la liste (aucune dérogation sans modifier delivrabilite.md).")

    return {
        "formule": "score = 100 - 100*t_invalide - 60*t_doublon - 50*t_role - pénalité_concentration - pénalité_diversité ; bandes A>=90 B>=75 C>=60 D>=45 E<45",
        "n_contacts": n,
        "n_valides": len(valides),
        "controles": {
            "invalides": len(invalides), "taux_invalide": t_invalide,
            "doublons": doublons, "taux_doublon": t_doublon,
            "emails_role": len(roles), "taux_role": t_role,
            "domaine_dominant": dom_top[0], "concentration_domaine": concentration,
            "diversite_titres": diversite_titres,
            "plafond_quotidien": plafond, "depasse_plafond": depasse_plafond,
        },
        "score": score,
        "note": note,
        "seuil_note": seuil,
        "refus": refus,
        "actions_correctives": actions,
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
