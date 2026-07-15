#!/usr/bin/env python3
"""Lead scoring transparent à 3 facteurs — stdlib uniquement.

fit ICP × engagement × **fraîcheur du signal** (intention). Le modèle NE calcule
JAMAIS un score de tête : ce script applique des pondérations ÉDITABLES (définies
dans ./rapido-kb/marketing/scoring.md + signaux.md, passées en entrée) aux données
CRM réelles, et sort un score décomposé + une tranche.

Trois axes :
  - fit         = critères booléens (poids ajouté si vrai).
  - engagement  = compteurs (poids * min(compte, cap)) — porte le VOLUME.
  - intention   = signaux datés (poids * fraîcheur) — porte la FRAÎCHEUR ;
                  fraîcheur = max(0, 1 - âge/validité) ; par type, seule
                  l'occurrence la plus récente compte (pas de double compte).

Entrée (fichier JSON en argument, ou stdin) :
    {"model": {
        "fit":        {"secteur_cible": 30, "taille_cible": 20, "region_cible": 10},
        "engagement": {"form_submit": 20, "cta_click": 10, "rdv": 30, "email_open": 5},
        "cap_engagement": 3,
        "intention": {                       // poids + validité (jours) par signal
            "form_submit":        {"poids": 25, "validite_jours": 30},
            "reponse_sequence":   {"poids": 30, "validite_jours": 30},
            "levee_fonds":        {"poids": 25, "validite_jours": 90}
        },
        "seuils": {"chaud": 70, "tiede": 40}
     },
     "date_reference": "2026-07-15",          // défaut : aujourd'hui
     "leads": [
        {"nom": "Prospect A",
         "fit":        {"secteur_cible": true, "taille_cible": true},
         "engagement": {"form_submit": 1, "cta_click": 2},
         "signaux":    [{"type": "levee_fonds", "date": "2026-07-01"},
                        {"type": "form_submit",  "date": "2026-06-20"}]},
        ...]}

Sortie (stdout, JSON) : chaque lead avec fit_score, engagement_score,
intention_score, total, tranche + décomposition ; liste triée par total. Code : 0.
Aucune écriture CRM (le skill écrit APRÈS confirmation).
"""
import datetime
import json
import sys


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def date_ref(data):
    d = data.get("date_reference")
    if d:
        return datetime.date.fromisoformat(d)
    return datetime.date.today()


def fraicheur(age_jours, validite):
    if not validite:
        return 0.0
    if age_jours < 0:  # signal daté dans le futur → traité comme frais
        age_jours = 0
    return max(0.0, round(1 - age_jours / validite, 3))


def score_fit(lead, poids_fit):
    detail, total = {}, 0
    for critere, poids in poids_fit.items():
        if (lead.get("fit") or {}).get(critere):
            detail[critere] = poids
            total += poids
    return total, detail


def score_engagement(lead, poids_eng, cap):
    detail, total = {}, 0
    for signal, poids in poids_eng.items():
        compte = (lead.get("engagement") or {}).get(signal) or 0
        pts = poids * min(compte, cap)
        if pts:
            detail[signal] = pts
            total += pts
    return total, detail


def score_intention(lead, poids_int, ref):
    """poids * fraîcheur ; par type, occurrence la plus récente uniquement."""
    plus_recent = {}  # type -> âge minimal (jours)
    for sig in (lead.get("signaux") or []):
        t = sig.get("type")
        if t not in poids_int or not sig.get("date"):
            continue
        age = (ref - datetime.date.fromisoformat(sig["date"])).days
        if t not in plus_recent or age < plus_recent[t]:
            plus_recent[t] = age
    detail, total = {}, 0.0
    for t, age in plus_recent.items():
        conf = poids_int[t]
        fr = fraicheur(age, conf.get("validite_jours"))
        pts = round(conf.get("poids", 0) * fr, 2)
        if pts:
            detail[t] = {"poids": conf.get("poids", 0), "age_jours": age,
                         "fraicheur": fr, "points": pts}
            total += pts
    return round(total, 2), detail


def tranche_de(total, seuils):
    if total >= seuils.get("chaud", 70):
        return "chaud"
    if total >= seuils.get("tiede", 40):
        return "tiede"
    return "froid"


def scorer(data):
    model = data.get("model") or {}
    poids_fit = model.get("fit", {})
    poids_eng = model.get("engagement", {})
    poids_int = model.get("intention", {})
    cap = model.get("cap_engagement", 3)
    seuils = model.get("seuils", {"chaud": 70, "tiede": 40})
    ref = date_ref(data)

    lignes = []
    for lead in (data.get("leads") or []):
        fit, df = score_fit(lead, poids_fit)
        eng, de = score_engagement(lead, poids_eng, cap)
        intent, di = score_intention(lead, poids_int, ref)
        total = round(fit + eng + intent, 2)
        lignes.append({
            "nom": lead.get("nom", "?"),
            "fit_score": fit,
            "engagement_score": eng,
            "intention_score": intent,
            "total": total,
            "tranche": tranche_de(total, seuils),
            "detail_fit": df,
            "detail_engagement": de,
            "detail_intention": di,
        })
    lignes.sort(key=lambda x: x["total"], reverse=True)
    par_tranche = {t: sum(1 for l in lignes if l["tranche"] == t)
                   for t in ("chaud", "tiede", "froid")}
    return {
        "formule": ("total = somme(poids fit si critère vrai) + "
                    "somme(poids engagement * min(compte, cap)) + "
                    "somme(poids intention * fraîcheur) ; "
                    "fraîcheur = max(0, 1 - âge/validité), occurrence la plus récente/type"),
        "date_reference": ref.isoformat(),
        "seuils": seuils,
        "par_tranche": par_tranche,
        "leads": lignes,
    }


def main():
    print(json.dumps(scorer(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
