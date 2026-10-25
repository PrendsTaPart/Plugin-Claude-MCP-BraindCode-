#!/usr/bin/env python3
"""Remplit un widget HTML du plugin rapido-employe depuis le JSON des outils.

Usage :
    python3 render_widget.py <widget> <donnees.json> <sortie.html>

widget ∈ plan-de-travail-du-jour | tableau-de-bord-kpi | pipeline-de-la-zone |
         progression-formation-et-badges | calendrier-editorial-semaine |
         avancement-du-deploiement

`donnees.json` est la réponse BRUTE de l'outil MCP correspondant :
get_work_plan, get_report_brief (type vendredi — son gabaritHtml officiel
reste la référence du rapport ; ce widget en est la vue « tableau de bord »),
get_pipeline/get_stats_pipeline, get_my_progress (+ list_my_badges sous la
clé "badges"), le calendrier éditorial, get_deployment_plan.

Stdlib uniquement. AUCUNE donnée ne vient d'ailleurs que des outils : un
champ absent s'affiche « — », jamais estimé. Palette : les jetons de la
charte FoodEatUp Academy relus dans le gabarit de get_report_brief
(--nuit #0f1a23, --bleu #007bff, --orange #ffa500, --creme #fcf9e6).
Calculs affichés : les totaux sont des sommes simples, reproduites en pied
de page (total = Σ des éléments listés).
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


def plan_de_travail_du_jour(d):
    familles = "\n".join(
        f"<tr><td>{e(f.get('nom') or f.get('famille'))}</td>"
        f"<td class=\"niv-{e(f.get('niveau')).lower()}\">{e(f.get('niveau'))}"
        f"</td><td>{e(', '.join(f.get('connecteurs', [])) or '—')}</td></tr>"
        for f in d.get("autonomie", [])) or "<tr><td colspan=\"3\">—</td></tr>"
    q = d.get("quotas_jour", {})
    b = d.get("budget", {})
    routines = li(d.get("routines", []), lambda r: (
        f"<li><strong>{e(r.get('nom'))}</strong> — {e(r.get('cadence'))} "
        f"<small>({e(r.get('etape'))} · {e(r.get('autonomie'))})</small></li>"))
    mission = d.get("prochaine_mission", {}) or {}
    return {
        "ETAT": "EN SERVICE" if d.get("actif") else "ARRÊTÉ — rapport seulement",
        "CLASSE_ETAT": "ok" if d.get("actif") else "stop",
        "FAMILLES": familles,
        "ENVOIS": e(q.get("envoisJour")), "PUBLIS": e(q.get("publicationsJour")),
        "REPONSES": e(q.get("reponsesJour")),
        "BUDGET_MOIS": e(b.get("mensuel")), "BUDGET_JOUR": e(b.get("plafond_jour")),
        "BUDGET_RESTE": e(b.get("reste_mois")),
        "MISSION": e(mission.get("titre")),
        "MISSION_FORMATION": e(mission.get("formation")),
        "ROUTINES": routines,
    }


def tableau_de_bord_kpi(d):
    cartes = []
    for i in d.get("indicateurs", []):
        etat = e(i.get("etat"))
        cartes.append(
            f"<div class=\"carte etat-{etat}\"><div class=\"nom\">"
            f"{e(i.get('nom'))}</div><div class=\"valeur\">{e(i.get('valeur'))}"
            f"</div><div class=\"obj\">objectif : {e(i.get('objectif'))} · "
            f"tendance : {e(i.get('tendance'))}</div>"
            f"<div class=\"decision\">{e(i.get('decision'))}</div></div>")
    g = d.get("donneesGabarit", {})
    sections = "\n".join(
        f"<section><h3>{e(s.get('titre'))}</h3><ul>"
        + li(s.get("lignes", []), lambda l: f"<li>{e(l)}</li>")
        + "</ul></section>" for s in g.get("sections", []))
    r = d.get("resume", {})
    return {
        "TITRE": e(g.get("titre") or "Tableau de bord KPI"),
        "PERIODE": e(g.get("periode")), "PHRASE": e(g.get("phrase")),
        "CARTES": "\n".join(cartes) or "—", "SECTIONS": sections or "",
        "RESUME": (f"{e(r.get('mesures'))} mesure(s), {e(r.get('enAlerte'))} "
                   f"alerte(s), objectifs atteints : "
                   f"{e(r.get('objectifsAtteints'))}/{e(r.get('objectifsSuivis'))}"),
    }


def pipeline_de_la_zone(d):
    etapes = (d.get("etapes") or d.get("pipeline") or d.get("stages") or [])
    lignes, total = [], 0
    for et in etapes:
        if not isinstance(et, dict):
            continue
        prospects = (et.get("prospects") or et.get("deals") or [])
        n = et.get("nombre", len(prospects) if prospects else et.get("count"))
        n = n if isinstance(n, int) else 0
        total += n
        noms = ", ".join(e(p.get("nom") or p.get("name") or p)
                         for p in prospects[:6]) if prospects else "—"
        lignes.append(f"<tr><td>{e(et.get('nom') or et.get('etape') or et.get('name'))}"
                      f"</td><td>{n}</td><td class=\"noms\">{noms}</td></tr>")
    return {
        "ZONE": e(d.get("zone") or d.get("pipeline_nom") or d.get("nom")),
        "LIGNES": "\n".join(lignes) or "<tr><td colspan=\"3\">—</td></tr>",
        "TOTAL": str(total),
        "FORMULE": f"total = Σ des prospects par étape = {total}",
    }


def progression_formation_et_badges(d):
    prog = d.get("progression", d)
    badges = d.get("badges") or []
    etapes = d.get("chemin") or []
    blocs = []
    for et in etapes:
        fs = li(et.get("formations", []), lambda f: (
            f"<li>{e(f.get('nom'))} <small>{e(f.get('validees'))}/"
            f"{e(f.get('missions'))} missions</small></li>"))
        blocs.append(f"<section class=\"etape\"><h3>{e(et.get('etape'))}</h3>"
                     f"<ul>{fs}</ul></section>")
    lb = li(badges, lambda b: f"<li>🏅 {e(b.get('nom') or b.get('titre') or b)}</li>")
    return {
        "MISSIONS": e(prog.get("missions") or prog.get("missionsValidees")),
        "ETOILES": e(prog.get("etoiles")), "POINTS": e(prog.get("points")),
        "CERTIF": e(prog.get("certification")),
        "ETAPES": "\n".join(blocs) or "—", "BADGES": lb,
    }


def calendrier_editorial_semaine(d):
    posts = (d.get("posts") or d.get("calendrier") or d.get("publications")
             or [])
    lignes = li(posts, lambda p: (
        f"<li><strong>{e(p.get('date') or p.get('jour'))}</strong> · "
        f"{e(p.get('reseau') or p.get('canal'))} — {e(p.get('titre') or p.get('sujet'))} "
        f"<small>[{e(p.get('statut'))}]</small></li>") if isinstance(p, dict)
        else f"<li>{e(p)}</li>")
    trous = li(d.get("trous") or d.get("gaps") or [],
               lambda t: f"<li>{e(t)}</li>")
    return {"POSTS": lignes, "TROUS": trous,
            "SEMAINE": e(d.get("semaine") or d.get("periode"))}


def avancement_du_deploiement(d):
    etapes = d.get("etapes", [])
    faites = sum(1 for et in etapes
                 if str(et.get("statut", "")).lower() not in ("à faire", "a faire", ""))
    lignes = "\n".join(
        f"<tr class=\"{'fait' if str(et.get('statut','')).lower() not in ('à faire','a faire','') else 'afaire'}\">"
        f"<td>{e(et.get('numero'))}</td><td>{e(et.get('titre'))}</td>"
        f"<td>{e(et.get('statut'))}</td><td>{e(et.get('note'))}</td></tr>"
        for et in etapes) or "<tr><td colspan=\"4\">—</td></tr>"
    questions = li(d.get("questions_a_poser", []),
                   lambda q: f"<li>{e(q.get('question'))} "
                             f"<small>ex. {e(q.get('exemple'))}</small></li>"
                   if isinstance(q, dict) else f"<li>{e(q)}</li>")
    return {
        "LIGNES": lignes, "FAITES": str(faites), "TOTAL": str(len(etapes)),
        "QUESTIONS": questions,
        "ETAPE_COURANTE": e((d.get("etape_courante") or {}).get("titre")),
        "FORMULE": (f"avancement = étapes hors « À faire » / total = "
                    f"{faites}/{len(etapes)}"),
    }


RENDUS = {
    "plan-de-travail-du-jour": plan_de_travail_du_jour,
    "tableau-de-bord-kpi": tableau_de_bord_kpi,
    "pipeline-de-la-zone": pipeline_de_la_zone,
    "progression-formation-et-badges": progression_formation_et_badges,
    "calendrier-editorial-semaine": calendrier_editorial_semaine,
    "avancement-du-deploiement": avancement_du_deploiement,
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
