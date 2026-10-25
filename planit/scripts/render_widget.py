#!/usr/bin/env python3
"""Remplit un widget HTML du plugin planit depuis le JSON des outils.

Usage :
    python3 render_widget.py <widget> <donnees.json> <sortie.html>

widget ∈ accueil-pilotage | calendrier-des-routines | rapport-de-routine |
         boucles-kpi | diff-amelioration | credits-par-routine

`donnees.json` est la réponse BRUTE de l'outil correspondant (get_kpi_home —
avec, en option, la réponse de list_pending_routine_actions sous la clé
"pending" —, get_calendar, get_routine_report, list_active_loops ou
evaluate_loops, propose_routine_improvement, ou la sortie JSON de
credits_autonomie.py). Stdlib uniquement ; un champ absent s'affiche « — »,
jamais estimé. Thème : AUCUNE charte Plan'It n'est versionnée dans ce dépôt
(vérifié le 2026-10-25) → thème neutre signalé, jetons CSS surchargables.
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
WIDGETS = os.path.join(os.path.dirname(ICI), "widgets")


def e(v):
    return html.escape(str(v)) if v not in (None, "") else "—"


def gabarit(nom):
    with open(os.path.join(WIDGETS, f"{nom}.html"), encoding="utf-8") as f:
        return f.read()


def li(items, rendu):
    return "\n".join(rendu(x) for x in items) or "<li>—</li>"


def accueil_pilotage(d):
    # Forme réelle de get_kpi_home (vérifiée le 2026-10-25) : credits est un
    # objet {balance, days_of_autonomy} ; chaque widget porte definition
    # (label) et snapshot (value_numeric, captured_at).
    credits = d.get("credits")
    solde = credits.get("balance") if isinstance(credits, dict) else credits
    autonomie = (credits.get("days_of_autonomy")
                 if isinstance(credits, dict)
                 else d.get("autonomy_days") or d.get("jours_autonomie"))

    def rendu_widget(w):
        definition = w.get("definition") or {}
        snap = w.get("snapshot") or {}
        nom = (definition.get("label") or w.get("kpi") or w.get("name"))
        valeur = snap.get("value_numeric") if snap else \
            (w.get("value") or w.get("last_value"))
        return (f"<li><strong>{e(nom)}</strong> : {e(valeur)} "
                f"<small>({e(w.get('period'))}, relevé "
                f"{e(snap.get('captured_at'))})</small></li>")

    widgets = li(d.get("widgets", []), rendu_widget)
    boucles = li(d.get("loops") or d.get("boucles") or [], lambda b: (
        f"<li>{e(b.get('routine') or b.get('routine_name'))} ↔ "
        f"{e(b.get('kpi') or b.get('kpi_name'))} — "
        f"{e(b.get('verdict'))}</li>"))
    alertes = li(d.get("alerts") or d.get("alertes") or [], lambda a: (
        f"<li>⚠️ {e(a.get('kpi') or a.get('name'))} : "
        f"{e(a.get('message') or a.get('threshold'))}</li>"))
    pending = d.get("pending") or {}
    decisions = []
    for cle in ("proposals", "improvements", "paused", "alerts"):
        for p in (pending.get(cle) or []):
            if isinstance(p, dict):
                decisions.append(f"<li>{e(p.get('name') or p.get('summary') or p)}"
                                 f" <small>[{cle}]</small></li>")
    return {
        "CREDITS": e(solde),
        "AUTONOMIE": e(autonomie),
        "WIDGETS": widgets, "BOUCLES": boucles, "ALERTES": alertes,
        "DECISIONS": "\n".join(decisions) or "<li>—</li>",
    }


def calendrier_des_routines(d):
    jours = d.get("days") or d.get("jours") or []
    blocs = []
    for j in jours:
        if not isinstance(j, dict):
            continue
        occs = li(j.get("occurrences") or j.get("items") or [], lambda o: (
            f"<li class=\"etat-{e(o.get('status') or o.get('etat'))}\">"
            f"{e(o.get('time') or o.get('heure'))} · "
            f"{e(o.get('name') or o.get('nom'))} "
            f"<small>[{e(o.get('status') or o.get('etat'))}]</small></li>"))
        blocs.append(f"<section class=\"jour\"><h3>{e(j.get('date'))}</h3>"
                     f"<ul>{occs}</ul></section>")
    evenements = li(d.get("event_routines") or [], lambda r: (
        f"<li>{e(r.get('name') or r)}</li>"))
    return {"JOURS": "\n".join(blocs) or "—", "EVENEMENTIELLES": evenements,
            "PLAGE": e(d.get("range") or d.get("plage"))}


def rapport_de_routine(d):
    ex = d.get("executions") or {}
    outils = li(d.get("tools") or d.get("outils") or [], lambda t: (
        f"<li>{e(t.get('tool') or t.get('name'))} — "
        f"{e(t.get('calls') or t.get('appels'))} appel(s), "
        f"{e(t.get('failures') or t.get('echecs'))} échec(s)</li>")
        if isinstance(t, dict) else f"<li>{e(t)}</li>")
    signaux = li(d.get("signals") or d.get("signaux") or [],
                 lambda s: f"<li>{e(s)}</li>")
    return {
        "NOM": e(d.get("name") or d.get("routine") or d.get("task_name")),
        "OBJECTIF": e(d.get("objective") or d.get("objectif")),
        "TOTAL": e(ex.get("total")), "OK": e(ex.get("succeeded") or ex.get("reussies")),
        "KO": e(ex.get("failed") or ex.get("echouees")),
        "TAUX": e(ex.get("success_rate") or ex.get("taux_reussite")),
        "CREDITS": e(d.get("credits_total") or d.get("credits")),
        "MOYENNE": e(d.get("credits_avg") or d.get("credits_par_tour")),
        "OUTILS": outils, "SIGNAUX": signaux,
        "VERDICT": e(d.get("verdict") or d.get("last_verdict")),
    }


def boucles_kpi(d):
    boucles = d.get("loops") or d.get("boucles") or []
    lignes = []
    for b in boucles:
        if not isinstance(b, dict):
            continue
        verdict = str(b.get("verdict") or "")
        affiche = ("pas assez de données" if verdict == "not_enough_data"
                   else e(verdict))
        lignes.append(
            f"<tr class=\"v-{e(verdict)}\">"
            f"<td>{e(b.get('routine') or b.get('routine_name'))}</td>"
            f"<td>{e(b.get('kpi') or b.get('kpi_name'))}</td>"
            f"<td>{e(b.get('baseline') or b.get('reference'))}</td>"
            f"<td>{e(b.get('current') or b.get('valeur_courante'))}</td>"
            f"<td>{e(b.get('delta_pct') or b.get('ecart'))}</td>"
            f"<td>{affiche}</td></tr>")
    return {"LIGNES": "\n".join(lignes) or "<tr><td colspan=\"6\">—</td></tr>"}


def diff_amelioration(d):
    diff = d.get("diff") or {}
    avant, apres = diff.get("before") or {}, diff.get("after") or {}
    cles = sorted(set(avant) | set(apres)) if isinstance(avant, dict) else []
    lignes = "\n".join(
        f"<tr><td>{e(k)}</td><td>{e(avant.get(k))}</td>"
        f"<td>{e(apres.get(k))}</td></tr>" for k in cles) \
        or f"<tr><td colspan=\"3\">{e(diff if diff else None)}</td></tr>"
    return {
        "ROUTINE": e(d.get("routine") or d.get("task_name") or d.get("name")),
        "RESUME": e(d.get("summary") or d.get("resume")),
        "EFFET": e(d.get("expected_effect") or d.get("effet_attendu")),
        "RISQUE": e(d.get("risk") or d.get("risque")),
        "COUT": e(d.get("cost") or d.get("cout")),
        "LIGNES": lignes,
    }


def credits_par_routine(d):
    lignes = li(d.get("routines") or d.get("lignes") or [], lambda r: (
        f"<li><strong>{e(r.get('nom') or r.get('name'))}</strong> : "
        f"{e(r.get('cout') or r.get('credits'))} crédits/mois "
        f"<small>[{e(r.get('base'))}]</small></li>")
        if isinstance(r, dict) else f"<li>{e(r)}</li>")
    return {
        "LIGNES": lignes, "TOTAL": e(d.get("total")),
        "SOLDE": e(d.get("solde") or d.get("credits")),
        "JOURS": e(d.get("jours_autonomie") or d.get("autonomy_days")),
        "FORMULE": e(d.get("formule") or
                     "jours = solde / (total_mensuel / 30)"),
    }


RENDUS = {
    "accueil-pilotage": accueil_pilotage,
    "calendrier-des-routines": calendrier_des_routines,
    "rapport-de-routine": rapport_de_routine,
    "boucles-kpi": boucles_kpi,
    "diff-amelioration": diff_amelioration,
    "credits-par-routine": credits_par_routine,
}


def main(argv):
    if len(argv) != 4 or argv[1] not in RENDUS:
        print(__doc__)
        return 2
    nom, src, dst = argv[1], argv[2], argv[3]
    with open(src, encoding="utf-8") as f:
        donnees = json.load(f)
    page = gabarit(nom)
    for cle, val in RENDUS[nom](donnees).items():
        page = page.replace("{{" + cle + "}}", val)
    for cle in re.findall(r"\{\{([A-Z_]+)\}\}", page):
        page = page.replace("{{" + cle + "}}", "—")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"{nom} → {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
