#!/usr/bin/env python3
"""Remplit un widget HTML du plugin braindcode-build depuis le JSON des outils.

Usage :
    python3 render_widget.py <widget> <donnees.json> [sortie.html]

widget ∈ tableau-de-bord-build | plan-d-execution | kanban-projet |
         fiche-idee | checklist-de-publication | rapport-de-test |
         apercu-vitrine | arene

`donnees.json` rassemble les réponses BRUTES des outils concernés (clés
décrites par renderer). Pour suivre une CONSTRUCTION Lovable en direct,
c'est render_project_widget (outil Lovable) qui s'utilise — pas ces
gabarits. Sortie par défaut : .claude/widgets-rendus/ (ignoré par git).
Stdlib uniquement ; un champ absent s'affiche « — », jamais estimé.
"""
import datetime
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
WIDGETS = os.path.join(os.path.dirname(ICI), "widgets")
SORTIE_DEFAUT = os.path.join(".claude", "widgets-rendus")


def e(v):
    return html.escape(str(v)) if v not in (None, "") else "—"


def _liste(d, *cles):
    for c in cles:
        v = d.get(c)
        if isinstance(v, list):
            return v
        if isinstance(v, dict):
            for sous in ("items", "results", "data", "projects", "steps",
                         "tasks", "validations"):
                if isinstance(v.get(sous), list):
                    return v[sous]
    return []


def li(items, rendu):
    return "\n".join(rendu(x) for x in items) or "<li>—</li>"


def tableau_de_bord(d):
    # clés : projets([{projet(list_my_projects), readiness}]),
    # validations(get_pending_validations), idees(list_my_ideas)
    lignes = []
    for p in d.get("projets", []):
        fiche = p.get("projet") or p
        manques = p.get("readiness", {}).get("missing") or \
            p.get("readiness", {}).get("manquants") or []
        lignes.append(
            f"<tr><td>{e(fiche.get('title') or fiche.get('name'))}</td>"
            f"<td>{e(fiche.get('status'))}</td>"
            f"<td>{e(', '.join(map(str, manques)) if manques else 'rien')}</td>"
            f"<td>{e(p.get('prochaine_action'))}</td></tr>")
    valids = li(_liste(d, "validations"), lambda v: (
        f"<li>{e(v.get('kind'))} — {e(v.get('project') or v.get('project_id'))}"
        f" <span class=\"badge\">{e(v.get('status'))}</span></li>"))
    idees = li(_liste(d, "idees"), lambda i: (
        f"<li>{e(i.get('title') or i.get('titre'))} "
        f"<span class=\"badge\">{e(i.get('status'))}</span></li>"))
    return {"PROJETS": "\n".join(lignes) or "<tr><td colspan=4>—</td></tr>",
            "VALIDATIONS": valids, "IDEES": idees}


def plan_execution(d):
    # clés : projet, etapes(get_prompt_execution_plan)
    etapes = _liste(d, "etapes", "plan")
    faites = sum(1 for s in etapes
                 if str(s.get("status", "")).lower() in
                 ("done", "termine", "terminé", "completed"))
    total = len(etapes) or 1
    lignes = "\n".join(
        f"<tr><td>{e(s.get('step') or s.get('ordre') or i + 1)}</td>"
        f"<td>{e(s.get('title') or s.get('name'))}</td>"
        f"<td>{e(s.get('status'))}</td>"
        f"<td>{e(s.get('human_validation') or s.get('validation') or 'non')}</td>"
        f"<td>{e(s.get('preview_url'))}</td></tr>"
        for i, s in enumerate(etapes)) or "<tr><td colspan=5>—</td></tr>"
    return {"PROJET": e(d.get("projet")), "AVANCEMENT": str(faites),
            "TOTAL": str(len(etapes)), "PCT": str(int(faites / total * 100)),
            "ETAPES": lignes}


def kanban(d):
    # clés : board(get_board) — colonnes [{name, tasks:[{title,status,…}]}]
    colonnes = []
    for col in _liste(d, "board", "colonnes"):
        if not isinstance(col, dict):
            continue
        cartes = li(col.get("tasks") or col.get("cartes") or [], lambda t: (
            f"<li>{e(t.get('title') or t.get('titre'))}"
            + (f" <span class=\"badge alerte\">bloquée</span>"
               if str(t.get('status', '')).lower() in ('blocked', 'bloquee', 'bloquée')
               else "") + "</li>"))
        colonnes.append(f"<h2>{e(col.get('name') or col.get('nom'))}</h2>"
                        f'<div class="carte"><ul>{cartes}</ul></div>')
    return {"COLONNES": "\n".join(colonnes) or '<div class="carte">—</div>'}


def fiche_idee(d):
    # clés : la fiche get_project (+ get_project_context)
    f = d.get("project") or d
    return {
        "TITRE": e(f.get("title") or f.get("name")),
        "PRODUIT": e(f.get("product")), "ARCHETYPE": e(f.get("archetype")),
        "DIFFICULTE": e(f.get("difficulty") or f.get("difficulte")),
        "ACCROCHE": e(f.get("tagline") or f.get("accroche")),
        "PUNCHLINE": e(f.get("punchline")),
        "IMAGE": e(f.get("cover_image_url") or f.get("image")),
        "MVP": li(f.get("mvp") or [], lambda x: f"<li>{e(x)}</li>"),
        "ACTIONS_SENSIBLES": li(f.get("sensitive_actions")
                                or f.get("actions_sensibles") or [],
                                lambda x: f"<li>{e(x)}</li>"),
    }


def checklist(d):
    # clés : projet, readiness(check_project_readiness),
    # sources({element: source réelle attendue})
    r = d.get("readiness", {})
    manques = set(map(str, r.get("missing") or r.get("manquants") or []))
    elements = r.get("elements") or sorted(manques) or []
    sources = d.get("sources", {})
    lignes = "\n".join(
        f"<tr><td>{e(el)}</td>"
        f"<td class=\"{'alerte' if str(el) in manques else 'ok'}\">"
        f"{'manquant' if str(el) in manques else 'présent'}</td>"
        f"<td>{e(sources.get(str(el)))}</td></tr>"
        for el in elements) or "<tr><td colspan=3>—</td></tr>"
    return {"PROJET": e(d.get("projet")),
            "PRET": "oui" if r.get("ready") else ("non" if manques else "—"),
            "ELEMENTS": lignes}


def rapport_test(d):
    def tbl(cle, colonnes):
        return "\n".join(
            "<tr>" + "".join(f"<td>{e(x.get(c))}</td>" for c in colonnes)
            + "</tr>" for x in d.get(cle, [])) \
            or f"<tr><td colspan={len(colonnes)}>—</td></tr>"
    return {
        "PROJET": e(d.get("projet")), "DATE_TEST": e(d.get("date")),
        "PREVIEW": e(d.get("preview_url")), "VERDICT": e(d.get("verdict")),
        "PARCOURS": tbl("parcours", ("etape", "attendu", "constate", "verdict")),
        "CAS_ERREUR": tbl("cas_erreur", ("cas", "constate", "verdict")),
        "ECARTS": li(d.get("ecarts") or [], lambda x: f"<li>{e(x)}</li>"),
    }


def apercu_vitrine(d):
    f = d.get("project") or d
    return {
        "TITRE": e(f.get("title")), "ACCROCHE": e(f.get("tagline")),
        "DEMO": e(f.get("demo_url")), "REPO": e(f.get("repo_url")),
        "MCP": e(f.get("mcp_server_url")),
        "PLUGIN": e(f.get("marketplace_url") or f.get("plugin_name")),
        "TUTORIEL": e((f.get("tutorial") or f.get("tutoriel") or "")[:600]),
        "FONCTIONNEMENT": e((f.get("how_it_works") or "")[:600]),
        "BUSINESS": e(f.get("business_model")),
    }


def arene(d):
    a = d.get("arena") or d
    duels = "\n".join(
        f"<tr><td>{e(x.get('idea') or x.get('idee'))}</td>"
        f"<td>{e(x.get('human') or x.get('humain'))}</td>"
        f"<td>{e(x.get('ai') or x.get('ia'))}</td>"
        f"<td>{e(x.get('votes'))}</td></tr>"
        for x in _liste(a, "duels", "matches")) or "<tr><td colspan=4>—</td></tr>"
    return {"SCORE_HUMAINS": e(a.get("human_score") or a.get("humains")),
            "SCORE_IA": e(a.get("ai_score") or a.get("ia")),
            "DUELS": duels}


RENDUS = {
    "tableau-de-bord-build": tableau_de_bord,
    "plan-d-execution": plan_execution,
    "kanban-projet": kanban,
    "fiche-idee": fiche_idee,
    "checklist-de-publication": checklist,
    "rapport-de-test": rapport_test,
    "apercu-vitrine": apercu_vitrine,
    "arene": arene,
}


def main(argv):
    if len(argv) < 3 or argv[1] not in RENDUS:
        print(__doc__)
        return 2
    nom, src = argv[1], argv[2]
    if len(argv) > 3:
        dst = argv[3]
    else:
        os.makedirs(SORTIE_DEFAUT, exist_ok=True)
        dst = os.path.join(SORTIE_DEFAUT, f"{nom}.html")
    donnees = json.load(open(src, encoding="utf-8"))
    page = open(os.path.join(WIDGETS, f"{nom}.html"), encoding="utf-8").read()
    valeurs = RENDUS[nom](donnees)
    valeurs["DATE"] = datetime.date.today().isoformat()
    for cle, val in valeurs.items():
        page = page.replace("{{" + cle + "}}", val)
    for cle in re.findall(r"\{\{([A-Z_]+)\}\}", page):
        page = page.replace("{{" + cle + "}}", "—")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"{nom} → {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
