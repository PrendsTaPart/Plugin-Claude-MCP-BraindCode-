#!/usr/bin/env python3
"""Remplit un widget HTML du plugin foodeatup-tutoriel depuis un JSON serveur.

Usage :
    python3 render_widget.py <widget> <donnees.json> <sortie.html>

widget ∈ carte-tutoriel | lecteur-chapitres | quiz-interactif |
         progression-parcours | plan-formation-equipe

`donnees.json` est la réponse BRUTE de l'outil MCP correspondant (ou, pour
progression-parcours, un objet {"parcours": <réponse>, "dejaVus": [...]}).
Stdlib uniquement ; aucune donnée inventée : un champ absent s'affiche « — ».
Le serveur Académie n'expose aucune ressource MCP Apps (ui://) — vérifié le
2026-10-25 — ces gabarits locaux sont le repli officiel du plugin.

Calcul affiché : la durée totale est la somme des durées « m:ss » des
leçons (total_secondes = Σ (m × 60 + s)), reproduite dans le pied de page.
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


def secondes(duree):
    m = re.fullmatch(r"(\d+):(\d{2})", str(duree or "").strip())
    return int(m.group(1)) * 60 + int(m.group(2)) if m else 0


def fmt(total):
    return f"{total // 60} min {total % 60:02d} s"


def gabarit(nom):
    with open(os.path.join(WIDGETS, f"{nom}.html"), encoding="utf-8") as f:
        return f.read()


def li(items, rendu):
    return "\n".join(rendu(x) for x in items) or "<li>—</li>"


def carte_tutoriel(d):
    etapes = li(d.get("etapes", []), lambda s: f"<li>{e(s)}</li>")
    return {
        "TITRE": e(d.get("titre")), "MODULE": e(d.get("module")),
        "DUREE": e(d.get("duree")), "VIGNETTE": e(d.get("vignetteUrl")),
        "URL": e(d.get("url") or d.get("pageUrl")),
        "A_QUOI": e(d.get("aQuoiCaSert")), "ETAPES": etapes,
        "ASTUCE": e(d.get("astuceDuChef")),
    }


def lecteur_chapitres(d):
    # Piège vérifié : pas de chapitres sur les vidéos courtes → repli `etapes`.
    chapitres = d.get("chapitres") or d.get("etapes") or []
    points = li(chapitres, lambda c: "<li>" + (
        f"<strong>{e(c.get('temps'))}</strong> — {e(c.get('titre'))}"
        if isinstance(c, dict) else e(c)) + "</li>")
    return {
        "TITRE": e(d.get("titre")), "DUREE": e(d.get("duree")),
        "VIDEO": e(d.get("videoUrl")), "VIGNETTE": e(d.get("vignetteUrl")),
        "PAGE": e(d.get("pageUrl")), "YOUTUBE": e(d.get("youtubeUrl")),
        "AVANT": e(d.get("aDireAvantDeLancer")), "CHAPITRES": points,
    }


def quiz_interactif(d):
    blocs = []
    for i, q in enumerate(d.get("questions", []), 1):
        revoir = q.get("revoir") or {}
        blocs.append(
            f"<section class=\"q\"><h3>Question {i} "
            f"<small>({e(q.get('type'))})</small></h3>"
            f"<p>{e(q.get('question'))}</p>"
            f"<details><summary>Voir la réponse</summary>"
            f"<p>{e(q.get('bonneReponse'))}</p>"
            f"<p class=\"revoir\">À revoir : "
            f"<a href=\"{e(revoir.get('url'))}\">{e(revoir.get('titre'))}"
            f"</a></p></details></section>")
    return {
        "SUJET": e(d.get("sujet")), "NOMBRE": e(d.get("nombreDeQuestions")),
        "CONSIGNE": e(d.get("consigne")), "QUESTIONS": "\n".join(blocs) or "—",
    }


def progression_parcours(d):
    parcours = d.get("parcours", d)
    vus = set(d.get("dejaVus", []))
    # Forme réelle de parcours_apprentissage (vérifiée le 2026-10-25) :
    # les leçons sont imbriquées dans seances[].lecons[].
    lecons = [l for s in parcours.get("seances", [])
              for l in s.get("lecons", [])]
    if not lecons:
        lecons = (parcours.get("lecons") or parcours.get("programme")
                  or parcours.get("tutoriels") or [])
    lignes, total, faits = [], 0, 0
    for n, l in enumerate(lecons, 1):
        if not isinstance(l, dict):
            l = {"titre": l}
        slug, duree = l.get("slug", ""), l.get("duree", "")
        fait = slug in vus
        faits += fait
        total += secondes(duree)
        lignes.append(
            f"<tr class=\"{'fait' if fait else 'afaire'}\"><td>{n}</td>"
            f"<td>{'✅' if fait else '⬜'}</td><td>{e(l.get('titre'))}</td>"
            f"<td>{e(l.get('module'))}</td><td>{e(duree)}</td></tr>")
    return {
        "OBJECTIF": e(parcours.get("objectif") or parcours.get("titre")),
        "LIGNES": "\n".join(lignes) or "<tr><td colspan=\"5\">—</td></tr>",
        "FAITS": str(faits), "TOTAL_LECONS": str(len(lecons)),
        "DUREE_TOTALE": fmt(total),
        "FORMULE": ("durée totale = Σ (minutes × 60 + secondes) des leçons "
                    f"= {total} s"),
    }


def plan_formation_equipe(d):
    blocs = []
    for poste in d.get("postes", d.get("plan", [])):
        if not isinstance(poste, dict):
            continue
        # Forme réelle de former_son_equipe (vérifiée le 2026-10-25) :
        # metier est un objet {slug,label,url}, les leçons sont dans
        # premiereSeance[] (titre + url, sans durée).
        metier = poste.get("metier") or poste.get("poste")
        if isinstance(metier, dict):
            metier = metier.get("label") or metier.get("slug")
        lecons = (poste.get("premiereSeance") or poste.get("seances")
                  or poste.get("lecons") or [])
        seances = li(lecons, lambda s: "<li>" + (
            (f"{e(s.get('titre'))}"
             + (f" <small>({e(s.get('duree'))})</small>"
                if s.get("duree") else ""))
            if isinstance(s, dict) else e(s)) + "</li>")
        blocs.append(
            f"<section class=\"poste\"><h3>{e(metier)}"
            f"</h3><ol>{seances}</ol></section>")
    return {
        "TITRE": e(d.get("titre") or "Plan de formation de l'équipe"),
        "POSTES": "\n".join(blocs) or "—",
        "RYTHME": e(d.get("minutesParSeance")),
        "NOTE": ("Plan à remettre en main propre — le plugin n'envoie "
                 "aucun message."),
    }


RENDUS = {
    "carte-tutoriel": carte_tutoriel,
    "lecteur-chapitres": lecteur_chapitres,
    "quiz-interactif": quiz_interactif,
    "progression-parcours": progression_parcours,
    "plan-formation-equipe": plan_formation_equipe,
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
    reste = re.findall(r"\{\{([A-Z_]+)\}\}", page)
    for cle in reste:  # jamais de placeholder résiduel dans la page servie
        page = page.replace("{{" + cle + "}}", "—")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"{nom} → {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
