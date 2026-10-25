#!/usr/bin/env python3
"""Comptes de crédits Plan'It — stdlib, formules affichées.

Usages :
    python3 credits_autonomie.py video <duree_secondes>
        → coût d'une vidéo : credits = max(5, ceil(duree / 2))
          (1 crédit par tranche de 2 s, 5 au minimum ; durée 10 à 60 s).

    python3 credits_autonomie.py bilan <home.json> <routines.json> [reports.json]
        → depuis les réponses BRUTES de get_kpi_home, list_routines et, en
          option, une liste de get_routine_report :
          consommation mensuelle par routine (mesurée si le report la donne,
          estimée sinon — base dite), classement des plus coûteuses, jours
          d'autonomie restants, et comparaison avec ceux annoncés par le
          serveur (un écart se dit).

    option : --si <nom_routine> <executions_par_mois>
        → effet d'un changement de fréquence : nouveau coût mensuel =
          credits_par_execution × executions_par_mois (à CONFIRMER par
          estimate_routine_cost avant toute proposition).

Aucune donnée ne vient d'ailleurs que des outils ; un champ absent rend
« non mesuré », jamais une estimation inventée.
"""
import json
import math
import sys


def video(duree_s):
    credits = max(5, math.ceil(duree_s / 2))
    print(f"durée {duree_s} s → crédits = max(5, ⌈{duree_s}/2⌉) = {credits}")
    if not 10 <= duree_s <= 60:
        print("ATTENTION : la durée doit être entre 10 et 60 s "
              "(compose_video la refusera).")
    return 0


def _charge(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def bilan(args):
    home = _charge(args[0])
    routines = _charge(args[1])
    reports = _charge(args[2]) if len(args) > 2 and not args[2].startswith("--") \
        else []
    si = None
    if "--si" in args:
        i = args.index("--si")
        si = (args[i + 1], float(args[i + 2]))

    lignes_routines = (routines.get("routines") or routines.get("tasks")
                       or routines if isinstance(routines, list) else
                       routines.get("routines", []))
    mesures = {}
    for r in reports if isinstance(reports, list) else [reports]:
        nom = (r.get("name") or r.get("routine") or r.get("task_name") or "")
        credits = (r.get("credits_total") or r.get("credits")
                   or (r.get("executions") or {}).get("credits_total"))
        if nom and isinstance(credits, (int, float)):
            mesures[nom] = credits

    total_mois = 0.0
    tableau = []
    for r in lignes_routines:
        if not isinstance(r, dict):
            continue
        nom = r.get("name") or r.get("nom") or "?"
        cout = r.get("monthly_cost_estimate") or r.get("cout_mensuel") \
            or r.get("credits_month")
        base = "estimée (list_routines)"
        if nom in mesures:
            cout, base = mesures[nom], "mesurée 30 j (get_routine_report)"
        if isinstance(cout, (int, float)):
            total_mois += cout
            tableau.append((cout, nom, base))
        else:
            tableau.append((None, nom, "non mesuré"))

    tableau.sort(key=lambda x: -(x[0] or -1))
    print("Consommation mensuelle par routine (classement) :")
    for cout, nom, base in tableau:
        affiche = f"{cout:.0f} crédits/mois" if cout is not None else "non mesuré"
        print(f"  - {nom} : {affiche} [{base}]")
    print(f"TOTAL mensuel = Σ des lignes = {total_mois:.0f} crédits/mois")

    solde = (home.get("credits") or home.get("solde")
             or (home.get("wallet") or {}).get("credits"))
    if isinstance(solde, (int, float)) and total_mois > 0:
        par_jour = total_mois / 30
        jours = solde / par_jour
        print(f"Jours d'autonomie = solde / (total_mois / 30) = "
              f"{solde:.0f} / {par_jour:.2f} = {jours:.1f} jours")
    else:
        print("Jours d'autonomie : non calculables (solde ou total absent) — "
              "se fier à get_kpi_home.")
    annonce = home.get("autonomy_days") or home.get("jours_autonomie")
    if annonce is not None:
        print(f"Le serveur annonce : {annonce} jours (get_kpi_home) — en cas "
              "d'écart avec le calcul, le serveur prime, l'écart se signale.")

    if si:
        nom, execs = si
        ligne = next((t for t in tableau if t[1] == nom and t[0]), None)
        if ligne:
            # crédits par exécution déduits du mensuel courant : cout / 30 exécutions
            # n'est PAS connu sans la fréquence — on affiche la formule générique.
            print(f"Scénario --si {nom} : nouveau coût mensuel = "
                  f"crédits_par_exécution × {execs:.0f} exécutions/mois — "
                  "les crédits par exécution viennent de estimate_routine_cost "
                  "(à lancer pour confirmer), pas d'une règle de trois muette.")
        else:
            print(f"Scénario --si : routine « {nom} » sans coût connu — "
                  "estimate_routine_cost d'abord.")
    return 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "video":
        return video(float(argv[2]))
    if len(argv) >= 4 and argv[1] == "bilan":
        return bilan(argv[2:])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
