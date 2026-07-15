#!/usr/bin/env python3
"""score_leads_gmaps — scoring de priorité des leads Google Maps (stdlib).

Le modèle ne calcule JAMAIS de tête : ce script applique la formule et trie.

    score = review_rating × ln(review_count + 1) × signal_opportunite

    signal_opportunite = 1.5 si (order_online vide ET reservations vide)   ← « sans système numérique »
                         1.0 sinon

Entrée : JSON (tableau d'objets Entry du scraper) via --input FICHIER ou stdin.
Sortie : même tableau enrichi de `score`, `signal_opportunite`,
`sans_systeme_numerique`, trié par `score` décroissant, sur stdout.

Filtres ICP optionnels (n'excluent que si fournis) :
  --min-rating F      note minimale (review_rating)
  --min-reviews N     nombre minimal d'avis (review_count)
  --categories "a,b"  au moins une catégorie contenant l'un de ces termes
                      (insensible à la casse, sur `categories` + `category`)

Aucune I/O réseau. Détermine sur les seules données passées.
"""
import argparse
import json
import math
import sys


def _vide(v):
    return not v  # [] / None / "" / 0 → considéré vide


def signal_opportunite(entry):
    """1.5 si ni commande en ligne ni réservation en ligne, sinon 1.0."""
    sans = _vide(entry.get("order_online")) and _vide(entry.get("reservations"))
    return (1.5 if sans else 1.0), sans


def score_entry(entry):
    try:
        rating = float(entry.get("review_rating") or 0)
    except (TypeError, ValueError):
        rating = 0.0
    try:
        count = int(entry.get("review_count") or 0)
    except (TypeError, ValueError):
        count = 0
    signal, sans = signal_opportunite(entry)
    score = rating * math.log(count + 1) * signal
    return round(score, 3), signal, sans


def _match_categorie(entry, termes):
    if not termes:
        return True
    hay = " ".join(
        [str(entry.get("category") or "")] +
        [str(x) for x in (entry.get("categories") or [])]
    ).lower()
    return any(t in hay for t in termes)


def main():
    ap = argparse.ArgumentParser(description="Scoring leads Google Maps")
    ap.add_argument("--input", help="fichier JSON (défaut : stdin)")
    ap.add_argument("--min-rating", type=float, default=None)
    ap.add_argument("--min-reviews", type=int, default=None)
    ap.add_argument("--categories", default=None,
                    help="termes séparés par des virgules")
    args = ap.parse_args()

    raw = open(args.input, encoding="utf-8").read() if args.input else sys.stdin.read()
    try:
        data = json.loads(raw or "[]")
    except ValueError as e:
        print(f"Entrée JSON invalide : {e}", file=sys.stderr)
        return 1
    if isinstance(data, dict):
        data = data.get("results") or data.get("data") or [data]
    if not isinstance(data, list):
        print("Entrée attendue : tableau JSON d'objets Entry.", file=sys.stderr)
        return 1

    termes = ([t.strip().lower() for t in args.categories.split(",") if t.strip()]
              if args.categories else [])

    enrichis = []
    exclus = 0
    for entry in data:
        if not isinstance(entry, dict):
            continue
        score, signal, sans = score_entry(entry)
        try:
            rating = float(entry.get("review_rating") or 0)
        except (TypeError, ValueError):
            rating = 0.0
        try:
            count = int(entry.get("review_count") or 0)
        except (TypeError, ValueError):
            count = 0
        if args.min_rating is not None and rating < args.min_rating:
            exclus += 1
            continue
        if args.min_reviews is not None and count < args.min_reviews:
            exclus += 1
            continue
        if not _match_categorie(entry, termes):
            exclus += 1
            continue
        out = dict(entry)
        out["score"] = score
        out["signal_opportunite"] = signal
        out["sans_systeme_numerique"] = sans
        enrichis.append(out)

    enrichis.sort(key=lambda e: e["score"], reverse=True)
    print(json.dumps(enrichis, ensure_ascii=False, indent=2))
    print(
        f"# {len(enrichis)} leads scorés"
        + (f", {exclus} exclus par filtre ICP" if exclus else "")
        + f" ; formule score = review_rating × ln(review_count+1) × signal "
        f"(signal=1.5 si sans système numérique).",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
