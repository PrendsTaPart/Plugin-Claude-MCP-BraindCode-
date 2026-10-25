#!/usr/bin/env python3
"""Remplit un widget HTML du plugin rapido-youtube depuis le JSON des outils.

Usage :
    python3 render_widget.py <widget> <donnees.json> [sortie.html]

widget ∈ tableau-de-bord-chaine | planning-de-publication |
         atelier-miniatures | comparateur-miniatures | momentum |
         outliers | clips-detectes | file-commentaires | rapport-de-chaine

`donnees.json` rassemble les réponses BRUTES des outils (clés par
renderer). Clés communes : "chaine" (nom affiché) et "kit" (la réponse de
yt_list_brand_kits pour la chaîne) — l'en-tête prend les couleurs du kit ;
sans kit, thème neutre et c'est dit. Les aperçus de miniatures sont des
liens signés TEMPORAIRES : affichés comme liens, jamais recopiés dans un
contenu durable. Sortie par défaut : .claude/widgets-rendus/ (gitignoré).
Stdlib ; un champ absent s'affiche « — », jamais estimé.
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
NEUTRE = {"C_ACCENT": "#3b5bdb", "C_FOND_ENTETE": "#15202b",
          "C_TEXTE_ENTETE": "#ffffff"}


def e(v):
    return html.escape(str(v)) if v not in (None, "") else "—"


def _liste(d, *cles):
    for c in cles:
        v = d.get(c)
        if isinstance(v, list):
            return v
        if isinstance(v, dict):
            for sous in ("items", "results", "data", "videos", "comments",
                         "clips", "outliers", "thumbnails", "schedule"):
                if isinstance(v.get(sous), list):
                    return v[sous]
    return []


def couleurs_kit(d):
    kit = d.get("kit")
    kits = kit.get("brand_kits") if isinstance(kit, dict) else None
    k = (kits[0] if isinstance(kits, list) and kits else
         kit if isinstance(kit, dict) else {})
    sortie = dict(NEUTRE)
    for cible, cles in (("C_ACCENT", ("accent", "primary", "primary_color")),
                        ("C_FOND_ENTETE", ("background", "secondary",
                                           "background_color")),
                        ("C_TEXTE_ENTETE", ("text", "text_color",
                                            "foreground"))):
        for c in cles:
            v = k.get(c) if isinstance(k, dict) else None
            if isinstance(v, str) and re.fullmatch(r"#[0-9A-Fa-f]{3,8}", v):
                sortie[cible] = v
                break
    sortie["_neutre"] = sortie == {**NEUTRE, "_neutre": sortie.get("_neutre")} \
        if False else (sortie["C_ACCENT"] == NEUTRE["C_ACCENT"]
                       and sortie["C_FOND_ENTETE"] == NEUTRE["C_FOND_ENTETE"])
    return sortie


def tableau_de_bord(d):
    q = d.get("quota", {})
    total = q.get("daily_quota") or q.get("total") or 0
    consomme = q.get("used") or q.get("consomme") or 0
    risque = str(q.get("risk") or "—")
    planning = "\n".join(
        f"<tr><td>{e(v.get('publish_at') or v.get('date'))}</td>"
        f"<td>{e(v.get('title'))}</td>"
        f"<td>{e(v.get('status'))}"
        + (" <span class=\"badge\">partie en avance</span>"
           if v.get("published_early") else "") + "</td></tr>"
        for v in _liste(d, "planning", "schedule")) \
        or "<tr><td colspan=3>—</td></tr>"
    return {
        "QUOTA_DISPONIBLE": e(q.get("available") or q.get("remaining")),
        "QUOTA_TOTAL": e(total), "QUOTA_CONSOMME": e(consomme),
        "QUOTA_RESERVE": e(q.get("reserved_next_24h") or q.get("reserved")),
        "QUOTA_PCT": str(int(consomme / total * 100)) if total else "0",
        "RISQUE": e(risque),
        "CLASSE_RISQUE": {"ok": "ok", "tight": "attention",
                          "will_fail": "alerte"}.get(risque, "sous"),
        "CREDITS": e((d.get("credits") or {}).get("balance")
                     if isinstance(d.get("credits"), dict) else d.get("credits")),
        "PLANNING": planning,
        "ECHECS": "\n".join(f"<li>{e(v.get('title'))} — {e(v.get('error') or v.get('status'))}</li>"
                            for v in _liste(d, "echecs", "errors")) or "<li>—</li>",
        "SANTE": e(d.get("sante") or (d.get("health") or {}).get("score")),
        "COMMENTAIRES_ATTENTE": e(d.get("commentaires_sans_reponse")),
        "COMPTES": e(d.get("comptes_distribution")),
        "PRIORITES": "\n".join(f"<li>{e(p)}</li>" for p in d.get("priorites", []))
        or "<li>—</li>",
    }


def planning_publication(d):
    jours = {}
    for v in _liste(d, "schedule", "planning"):
        jour = str(v.get("publish_at") or v.get("date") or "")[:10]
        jours.setdefault(jour, []).append(v)
    semaine = "\n".join(
        f'<h2>{e(j)}</h2><div class="carte"><ul>' +
        "".join(f"<li>{e(v.get('title'))} <span class=\"badge\">{e(v.get('status'))}</span>"
                + (" <span class=\"badge\">partie en avance</span>"
                   if v.get("published_early") else "") + "</li>"
                for v in vs) + "</ul></div>"
        for j, vs in sorted(jours.items())[:7]) or '<div class="carte">—</div>'
    mois = "\n".join(
        f"<tr><td>{e(str(v.get('publish_at') or '')[:16])}</td>"
        f"<td>{e(v.get('channel') or v.get('channel_id'))}</td>"
        f"<td>{e(v.get('title'))}</td><td>{e(v.get('status'))}</td></tr>"
        for v in _liste(d, "schedule", "planning")) \
        or "<tr><td colspan=4>—</td></tr>"
    return {"SEMAINE": semaine, "MOIS": mois}


def atelier(d):
    def ligne(t):
        sous = ", ".join(f"{k} {v}" for k, v in
                         (t.get("subscores") or {}).items())
        apercu = "—"
        if t.get("preview_url"):
            apercu = ('<a href="' + html.escape(t["preview_url"])
                      + '">aperçu (lien temporaire)</a>')
        return (f"<tr><td>{e(t.get('id') or t.get('version'))}</td>"
                f"<td>{e(t.get('score'))}</td><td>{e(sous or None)}</td>"
                f"<td>{apercu}</td></tr>")
    versions = "\n".join(ligne(t) for t in _liste(d, "versions", "thumbnails")) \
        or "<tr><td colspan=4>—</td></tr>"
    return {"VERSIONS": versions,
            "SUGGESTIONS": "\n".join(f"<li>{e(s)}</li>"
                                     for s in d.get("suggestions", []))
            or "<li>—</li>",
            "COUT_SEANCE": e(d.get("cout_seance"))}


def comparateur(d):
    lignes = "\n".join(
        f"<tr><th>{e(l.get('critere'))}</th><td>{e(l.get('a'))}</td>"
        f"<td>{e(l.get('b'))}</td></tr>" for l in d.get("lignes", [])) \
        or "<tr><td colspan=3>—</td></tr>"
    return {"LIGNES": lignes, "VERDICT": e(d.get("verdict"))}


def momentum(d):
    m = d.get("momentum", d)
    lignes = "\n".join(
        f"<tr><td>{e(x.get('hour') or x.get('heure'))}</td>"
        f"<td>{e(x.get('views') or x.get('vues'))}</td>"
        f"<td>{e(x.get('vs_usual') or x.get('vs_habituel'))}</td></tr>"
        for x in _liste(m, "hourly", "heures")) or "<tr><td colspan=3>—</td></tr>"
    return {"VIDEO": e(m.get("title") or m.get("video")),
            "AGE": e(m.get("age")),
            "VUES_PAR_HEURE": e(m.get("views_per_hour")),
            "TRAJECTOIRE": e(m.get("usual_trajectory") or m.get("trajectoire")),
            "LIGNES": lignes}


def outliers(d):
    lignes = "\n".join(
        f"<tr><td>{e(o.get('title'))}</td><td>{e(o.get('channel'))}</td>"
        f"<td>×{e(o.get('multiplier') or o.get('score'))}</td>"
        f"<td>{e(o.get('views_per_hour'))}</td>"
        f"<td>{e(o.get('adaptation') or o.get('piste'))}</td></tr>"
        for o in _liste(d, "outliers")) or "<tr><td colspan=5>—</td></tr>"
    return {"LIGNES": lignes}


def clips(d):
    lignes = "\n".join(
        f"<tr><td>{i + 1}</td><td>{e(c.get('start'))} → {e(c.get('end'))}</td>"
        f"<td>{e(c.get('hook') or c.get('accroche'))}</td>"
        f"<td>{e(c.get('viral_score') or c.get('score'))} (estimation)</td>"
        f"<td>{e(c.get('status'))}</td></tr>"
        for i, c in enumerate(_liste(d, "clips"))) \
        or "<tr><td colspan=5>—</td></tr>"
    return {"LIGNES": lignes}


def file_commentaires(d):
    cs = _liste(d, "comments", "commentaires")
    def genre(c):
        t = c.get("type") or ("question" if c.get("is_question")
                              else "négatif" if c.get("is_negative") else "")
        return t or "—"
    lignes = "\n".join(
        f"<tr><td>{e(c.get('published_at') or c.get('date'))}</td>"
        f"<td>{e(c.get('video_title') or c.get('video'))}</td>"
        f"<td>{e((c.get('text') or '')[:90])}</td>"
        f"<td>{e(genre(c))}</td><td>{e((c.get('draft') or '')[:70])}</td></tr>"
        for c in cs) or "<tr><td colspan=5>—</td></tr>"
    return {"NB_SANS_REPONSE": str(len([c for c in cs if not c.get("replied")])),
            "NB_QUESTIONS": str(len([c for c in cs if genre(c) == "question"])),
            "NB_NEGATIFS": str(len([c for c in cs if genre(c) == "négatif"])),
            "LIGNES": lignes}


def rapport(d):
    a = d.get("analytics", d)
    top = "\n".join(
        f"<tr><td>{e(v.get('title'))}</td><td>{e(v.get('views'))}</td>"
        f"<td>{e(v.get('ctr'))}</td><td>{e(v.get('avg_duration'))}</td></tr>"
        for v in _liste(a, "top_videos", "top")) or "<tr><td colspan=4>—</td></tr>"
    return {"PERIODE": e(a.get("period") or d.get("periode")),
            "SANTE": e(d.get("sante")),
            "VUES": e(a.get("views")), "HEURES": e(a.get("watch_hours")),
            "ABONNES": e(a.get("subscribers_gained")), "CTR": e(a.get("ctr")),
            "TOP": top,
            "ENSEIGNEMENTS": "\n".join(f"<li>{e(x)}</li>"
                                       for x in d.get("enseignements", []))
            or "<li>—</li>"}


RENDUS = {
    "tableau-de-bord-chaine": tableau_de_bord,
    "planning-de-publication": planning_publication,
    "atelier-miniatures": atelier,
    "comparateur-miniatures": comparateur,
    "momentum": momentum,
    "outliers": outliers,
    "clips-detectes": clips,
    "file-commentaires": file_commentaires,
    "rapport-de-chaine": rapport,
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
    kit = couleurs_kit(donnees)
    valeurs["CHAINE"] = e(donnees.get("chaine")) + \
        (" (thème neutre : kit de marque non fourni)" if kit.pop("_neutre")
         and not donnees.get("kit") else "")
    valeurs.update({k: v for k, v in kit.items() if k.startswith("C_")})
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
