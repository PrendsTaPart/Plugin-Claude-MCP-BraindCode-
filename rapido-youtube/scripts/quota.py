#!/usr/bin/env python3
"""Estime le coût en quota d'une campagne et dit si elle tient.

Formules affichées (et appliquées) :
    coût(campagne) = envois_complets × coût_envoi
                   + 50 × (miniatures poussées + réponses aux commentaires)
                   + extras (recherches avec concurrence, sync, refresh…)
    verdict : coût ≤ disponible_réel (lu dans yt_get_quota_status) ?

La base est TOUJOURS la lecture de yt_get_quota_status : quota du jour,
part réservée aux publications planifiées sous 24 h, disponible réel,
risque (ok / tight / will_fail). Le disponible réel peut être à zéro alors
que le quota brut ne l'est pas. Rien n'est estimé sans cette lecture.

Usage :
    python3 quota.py quota.json --envois 3 --miniatures 2 --reponses 5 \
        [--extras 300] [--cout-envoi 1600]
quota.json : la réponse BRUTE de yt_get_quota_status. --cout-envoi est le
coût d'un envoi complet tel que servi par le serveur (champ upload_cost de
la réponse s'il existe, sinon la valeur passée ; 1 600 unités est la
valeur API YouTube documentée, affichée comme hypothèse). Stdlib.
"""
import argparse
import json
import sys


def disponible(q):
    for cle in ("available", "disponible_reel", "available_real", "remaining"):
        v = q.get(cle)
        if isinstance(v, (int, float)):
            return v
    return None


def main(argv):
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument("quota_json")
    p.add_argument("--envois", type=int, default=0)
    p.add_argument("--miniatures", type=int, default=0)
    p.add_argument("--reponses", type=int, default=0)
    p.add_argument("--extras", type=int, default=0)
    p.add_argument("--cout-envoi", type=int, default=None)
    try:
        a = p.parse_args(argv[1:])
    except SystemExit:
        print(__doc__)
        return 2
    q = json.load(open(a.quota_json, encoding="utf-8"))
    if not isinstance(q, dict):
        print("yt_get_quota_status : réponse inattendue — rien à estimer.")
        return 1
    cout_envoi = a.cout_envoi
    source_envoi = "argument"
    for cle in ("upload_cost", "cout_envoi", "cost_per_upload"):
        if isinstance(q.get(cle), (int, float)):
            cout_envoi, source_envoi = q[cle], "serveur"
            break
    if cout_envoi is None:
        cout_envoi, source_envoi = 1600, "hypothèse (valeur API documentée)"
    cout = (a.envois * cout_envoi + 50 * (a.miniatures + a.reponses)
            + a.extras)
    dispo = disponible(q)
    risque = q.get("risk") or q.get("risque")
    print(f"coût estimé    : {a.envois} envoi(s) × {cout_envoi} ({source_envoi})"
          f" + 50 × ({a.miniatures} miniature(s) + {a.reponses} réponse(s))"
          f" + {a.extras} extra(s) = {cout} unité(s)")
    print(f"disponible réel : {dispo if dispo is not None else '— (champ absent)'}"
          f" — risque serveur : {risque or '—'}")
    if dispo is None:
        print("verdict        : IMPOSSIBLE à rendre sans le disponible réel.")
        return 1
    if risque == "will_fail":
        print("verdict        : NE PASSE PAS — risque will_fail : le hook "
              "garde-quota refusera tout envoi. Vérifier le planning sous "
              "24 h avant quoi que ce soit.")
        return 1
    if cout <= dispo:
        print(f"verdict        : tient dans le disponible ({cout} ≤ {dispo})"
              + (" — risque tight : confirmer quand même." if risque == "tight" else ""))
        return 0
    print(f"verdict        : NE TIENT PAS ({cout} > {dispo}) — découper la "
          "campagne ou attendre la remise à zéro ; jamais de fractionnement "
          "pour contourner.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
