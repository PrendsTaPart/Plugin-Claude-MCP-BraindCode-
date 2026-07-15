#!/usr/bin/env python3
"""health_score.py — score de santé client composite (stdlib).

Score 0-100 par client à partir de facteurs RÉELS normalisés (0-1) et de
pondérations lues dans la KB (`./rapido-kb/relation-client/sante-client.md`).
Formule affichée ; aucun facteur inventé (absent = exclu, poids renormalisés).

Facteurs (chacun normalisé 0-1, 1 = meilleur) :
  - recence      : activité récente (jours depuis dernière action ; seuil = "froid")
  - paiement     : régularité de paiement (0-1 fourni, 1 = toujours à l'heure)
  - tickets      : charge de support (nb tickets ouverts ; 0 = meilleur)
  - nps          : satisfaction individuelle (0-10) si connue

Entrée (stdin/--fichier) :
  {"seuil_recence_jours": 45, "seuil_tickets": 5,
   "poids": {"recence": 0.35, "paiement": 0.30, "tickets": 0.15, "nps": 0.20},
   "seuils_couleur": {"vert": 70, "orange": 45},
   "clients": [{"nom": "X", "recence_jours": 12, "paiement": 1.0,
                "tickets_ouverts": 1, "nps": 8}]}
Sortie : clients triés (score, couleur) + formule.
"""
import argparse
import json
import sys

FACTEURS = ("recence", "paiement", "tickets", "nps")


def normaliser(c, seuil_recence, seuil_tickets):
    """Retourne {facteur: valeur 0-1} pour les facteurs DISPONIBLES uniquement."""
    n = {}
    if isinstance(c.get("recence_jours"), (int, float)):
        n["recence"] = max(0.0, 1.0 - float(c["recence_jours"]) / max(1.0, seuil_recence))
    if isinstance(c.get("paiement"), (int, float)):
        n["paiement"] = max(0.0, min(1.0, float(c["paiement"])))
    if isinstance(c.get("tickets_ouverts"), (int, float)):
        n["tickets"] = max(0.0, 1.0 - float(c["tickets_ouverts"]) / max(1.0, seuil_tickets))
    if isinstance(c.get("nps"), (int, float)):
        n["nps"] = max(0.0, min(1.0, float(c["nps"]) / 10.0))
    return n


def score_client(c, poids, seuil_recence, seuil_tickets):
    n = normaliser(c, seuil_recence, seuil_tickets)
    if not n:
        return None, {}
    # renormaliser les poids sur les facteurs disponibles
    total_poids = sum(poids.get(f, 0) for f in n) or 1.0
    score = sum(n[f] * poids.get(f, 0) for f in n) / total_poids * 100
    return round(score, 1), n


def couleur(score, seuils):
    if score >= seuils.get("vert", 70):
        return "vert"
    if score >= seuils.get("orange", 45):
        return "orange"
    return "rouge"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichier")
    args = ap.parse_args(argv)
    try:
        data = json.load(open(args.fichier) if args.fichier else sys.stdin)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Erreur lecture : {e}", file=sys.stderr)
        return 1
    poids = data.get("poids", {"recence": 0.35, "paiement": 0.30, "tickets": 0.15, "nps": 0.20})
    sr = float(data.get("seuil_recence_jours", 45))
    st = float(data.get("seuil_tickets", 5))
    seuils_c = data.get("seuils_couleur", {"vert": 70, "orange": 45})
    out = []
    for c in data.get("clients", []):
        s, n = score_client(c, poids, sr, st)
        if s is None:
            out.append({"nom": c.get("nom"), "score": None, "couleur": "inconnu",
                        "raison": "aucun facteur disponible"})
            continue
        out.append({"nom": c.get("nom"), "score": s, "couleur": couleur(s, seuils_c),
                    "facteurs": n})
    out.sort(key=lambda x: (x["score"] is not None, x["score"] or 0))
    print(json.dumps({
        "formule": "score = Σ(facteur_normalisé × poids) ÷ Σpoids_disponibles × 100 (facteur absent = exclu)",
        "poids": poids, "clients": out,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
