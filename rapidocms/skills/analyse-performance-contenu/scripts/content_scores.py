#!/usr/bin/env python3
"""Scores de performance de contenu social (stdlib uniquement).

Entrée (fichier JSON en argument, ou stdin) :
  [{"id": "123", "nom": "Post menu été", "reseau": "instagram",
    "format": "image",                    // image | video | texte
    "date": "2026-06-15", "heure": "18:30",   // heure optionnelle
    "likes": 120, "commentaires": 8, "partages": 5,
    "portee": 3400}, ...]

Sortie (stdout, JSON) : taux d'engagement par post, agrégats par format /
réseau / créneau, top 3 / flop 3, tendance (1re vs 2e moitié de période).
Engagement % = (likes + commentaires + partages) / portee * 100.
"""
import json
import sys
from datetime import date

CRENEAUX = [(6, 11, "matin (6-11h)"), (11, 14, "midi (11-14h)"),
            (14, 18, "après-midi (14-18h)"), (18, 23, "soir (18-23h)")]
MIN_POSTS_PATTERN = 3


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def creneau(heure):
    if not heure:
        return "inconnu"
    try:
        h = int(str(heure).split(":")[0].split("-")[0])
    except ValueError:
        return "inconnu"
    for debut, fin, nom in CRENEAUX:
        if debut <= h < fin:
            return nom
    return "nuit (23-6h)"


def parse_date(s):
    y, m, d = str(s).split("-")
    return date(int(y), int(m), int(d))


def agreger(posts, cle):
    groupes = {}
    for p in posts:
        groupes.setdefault(p[cle], []).append(p["engagement_pct"])
    return [
        {cle: k, "nb_posts": len(v),
         "engagement_moyen_pct": round(sum(v) / len(v), 2),
         "signal_faible": len(v) < MIN_POSTS_PATTERN}
        for k, v in sorted(groupes.items(),
                           key=lambda kv: -(sum(kv[1]) / len(kv[1])))
    ]


def main():
    try:
        bruts = lire_entree()
        assert isinstance(bruts, list) and bruts
    except Exception as e:
        sys.stderr.write(f"Entrée JSON invalide (liste de posts requise) : {e}\n")
        sys.exit(1)

    posts, exclus = [], []
    for p in bruts:
        try:
            interactions = (float(p.get("likes") or 0)
                            + float(p.get("commentaires") or 0)
                            + float(p.get("partages") or 0))
            portee = float(p.get("portee") or 0)
            if portee <= 0:
                raise ValueError("portee absente ou nulle")
            posts.append({
                "id": str(p.get("id", "?")),
                "nom": str(p.get("nom", p.get("id", "?"))),
                "reseau": str(p.get("reseau", "inconnu")).lower(),
                "format": str(p.get("format", "inconnu")).lower(),
                "date": str(p.get("date", "")),
                "creneau": creneau(p.get("heure")),
                "engagement_pct": round(interactions / portee * 100.0, 2),
                "portee": portee,
            })
        except (TypeError, ValueError) as e:
            exclus.append({"id": str(p.get("id", "?")), "raison": str(e)})

    if not posts:
        sys.stderr.write("Aucun post exploitable (portée manquante partout ?).\n")
        sys.exit(1)

    classes = sorted(posts, key=lambda p: -p["engagement_pct"])
    top = classes[:3]
    flop = list(reversed(classes[-3:])) if len(classes) > 3 else []

    # Tendance : 1re vs 2e moitié de la période (par date).
    tendance = {"verdict": "indéterminée (dates manquantes ou période trop courte)"}
    dates_ok = [p for p in posts if p["date"]]
    if len(dates_ok) >= 4:
        try:
            dates_ok.sort(key=lambda p: parse_date(p["date"]))
            moitie = len(dates_ok) // 2
            m1 = [p["engagement_pct"] for p in dates_ok[:moitie]]
            m2 = [p["engagement_pct"] for p in dates_ok[moitie:]]
            avg1, avg2 = sum(m1) / len(m1), sum(m2) / len(m2)
            delta = (avg2 - avg1) / avg1 * 100.0 if avg1 else 0.0
            verdict = "↗ hausse" if delta > 10 else "↘ baisse" if delta < -10 else "→ stable"
            tendance = {"engagement_moyen_1re_moitie_pct": round(avg1, 2),
                        "engagement_moyen_2e_moitie_pct": round(avg2, 2),
                        "variation_pct": round(delta, 1), "verdict": verdict}
        except Exception:
            pass

    print(json.dumps({
        "nb_posts_analyses": len(posts),
        "engagement_moyen_pct": round(sum(p["engagement_pct"] for p in posts) / len(posts), 2),
        "par_format": agreger(posts, "format"),
        "par_reseau": agreger(posts, "reseau"),
        "par_creneau": agreger(posts, "creneau"),
        "top": top,
        "flop": flop,
        "tendance": tendance,
        "exclus": exclus,
        "note_methodo": f"Un pattern sous {MIN_POSTS_PATTERN} posts est marqué signal_faible (non concluant).",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
