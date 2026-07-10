#!/usr/bin/env python3
"""Garde-fou « KPI sans script » (Stop, rapido-startup).

Si la réponse du tour annonce un KPI avec une valeur chiffrée (MRR, CAC,
LTV, churn, runway, burn, NRR, Rule of 40, DSO, point mort, vélocité,
coverage, food cost, ARPU, marge brute, ticket moyen…) alors qu'aucune
exécution de calcul_kpi.py n'a eu lieu dans le tour, la fin de tour est
BLOQUÉE (exit 2) avec le message « KPI sans script ».

Lecture du transcript (dernier tour = depuis le dernier message user) ;
fail-open (exit 0) sur toute erreur de parsing pour ne jamais bloquer à
tort. Aucun appel réseau."""
import json
import re
import sys

KPI = (r"\b(mrr|cac|ltv|churn|runway|burn|nrr|rule\s*of\s*40|dso|"
       r"point\s+mort|v[ée]locit[ée]|coverage|food\s*cost|arpu|"
       r"marge\s+brute|ticket\s+moyen|break[- ]?even)\b")
# KPI et un chiffre sur la même ligne (valeur annoncée)
RX_KPI_CHIFFRE = re.compile(KPI + r"[^\n]{0,80}?\d", re.I)


def texte_du_tour(chemin_transcript):
    """(texte assistant, trace outils) depuis le dernier message user réel."""
    lignes = open(chemin_transcript, encoding="utf-8", errors="ignore").read().splitlines()
    entrees = []
    for l in lignes:
        try:
            entrees.append(json.loads(l))
        except Exception:  # noqa: BLE001
            continue
    dernier_user = max((i for i, e in enumerate(entrees) if e.get("type") == "user"
                        and not e.get("isMeta")), default=-1)
    texte, outils = [], []
    for e in entrees[dernier_user + 1:]:
        message = e.get("message") or {}
        contenu = message.get("content")
        if isinstance(contenu, list):
            for bloc in contenu:
                if bloc.get("type") == "text":
                    texte.append(bloc.get("text", ""))
                elif bloc.get("type") == "tool_use":
                    outils.append(json.dumps(bloc.get("input", {}), ensure_ascii=False))
        elif isinstance(contenu, str):
            texte.append(contenu)
    return "\n".join(texte), "\n".join(outils)


try:
    donnees = json.load(sys.stdin)
    if donnees.get("stop_hook_active"):
        sys.exit(0)  # éviter la boucle de blocage
    chemin = donnees.get("transcript_path")
    if not chemin:
        sys.exit(0)
    texte, outils = texte_du_tour(chemin)
    if RX_KPI_CHIFFRE.search(texte) and "calcul_kpi.py" not in outils:
        sys.stderr.write(
            "KPI sans script : la réponse annonce un KPI chiffré sans exécution "
            "de calcul_kpi.py dans ce tour. Exécuter le script du skill "
            "catalogue-kpi (JSON d'entrées sourcées → calcul_kpi.py) et "
            "afficher la formule appliquée avec les valeurs."
        )
        sys.exit(2)
    sys.exit(0)
except SystemExit:
    raise
except Exception:  # noqa: BLE001 — fail-open : ne jamais bloquer à tort
    sys.exit(0)
