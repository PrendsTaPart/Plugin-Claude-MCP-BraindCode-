#!/usr/bin/env python3
"""stats_leadmagnet — KPIs d'une campagne lead magnet (stdlib).

Le modèle ne calcule JAMAIS de tête : ce script applique les formules et affiche
chacune. Aucune donnée inventée — un dénominateur nul ⇒ « — » (non calculable).

Formules :
    CPL (coût par lead)          = depense_ads / soumissions
    taux_conversion_landing (%)  = soumissions / visiteurs × 100
    taux_clic_cta (%)            = clics_cta / visiteurs × 100
    taux_conversion_rdv (%)      = rdv / soumissions × 100

Entrée : JSON via --input FICHIER ou stdin, clés (toutes optionnelles, nombres) :
    visiteurs, clics_cta, soumissions, telechargements, depense_ads, rdv, devise.
Sortie : JSON des KPIs (valeur ou null) + formules, sur stdout.
"""
import argparse
import json
import sys


def _num(d, k):
    try:
        v = d.get(k)
        return float(v) if v is not None else None
    except (TypeError, ValueError):
        return None


def _ratio(num, den, pct=False, nd=2):
    if num is None or den in (None, 0):
        return None
    r = num / den * (100 if pct else 1)
    return round(r, nd)


def main():
    ap = argparse.ArgumentParser(description="KPIs campagne lead magnet")
    ap.add_argument("--input", help="fichier JSON (défaut : stdin)")
    args = ap.parse_args()
    raw = open(args.input, encoding="utf-8").read() if args.input else sys.stdin.read()
    try:
        d = json.loads(raw or "{}")
    except ValueError as e:
        print(f"Entrée JSON invalide : {e}", file=sys.stderr)
        return 1
    if not isinstance(d, dict):
        print("Entrée attendue : objet JSON.", file=sys.stderr)
        return 1

    visiteurs = _num(d, "visiteurs")
    clics_cta = _num(d, "clics_cta")
    soumissions = _num(d, "soumissions")
    depense = _num(d, "depense_ads")
    rdv = _num(d, "rdv")
    devise = d.get("devise") or ""

    kpis = {
        "cpl": _ratio(depense, soumissions),
        "taux_conversion_landing_pct": _ratio(soumissions, visiteurs, pct=True),
        "taux_clic_cta_pct": _ratio(clics_cta, visiteurs, pct=True),
        "taux_conversion_rdv_pct": _ratio(rdv, soumissions, pct=True),
    }
    out = {
        "entrees": {"visiteurs": visiteurs, "clics_cta": clics_cta,
                    "soumissions": soumissions, "depense_ads": depense,
                    "rdv": rdv, "devise": devise},
        "kpis": kpis,
        "formules": {
            "cpl": "depense_ads / soumissions",
            "taux_conversion_landing_pct": "soumissions / visiteurs × 100",
            "taux_clic_cta_pct": "clics_cta / visiteurs × 100",
            "taux_conversion_rdv_pct": "rdv / soumissions × 100",
        },
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    manquants = [k for k, v in kpis.items() if v is None]
    if manquants:
        print("# non calculables (dénominateur nul/absent) : "
              + ", ".join(manquants), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
