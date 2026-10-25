#!/usr/bin/env python3
"""Remplit un widget HTML du plugin rapido-prospector depuis le JSON des outils.

Usage :
    python3 render_widget.py <widget> <donnees.json> [sortie.html]

widget ∈ tableau-de-bord-prospection | resultats-de-zone | apercu-email |
         apercu-sms | file-linkedin-du-jour | chronologie-prospect |
         calendrier-editorial-semaine | mrr-stripe

`donnees.json` rassemble les réponses BRUTES des outils concernés (clés
décrites par renderer ci-dessous). Sortie PAR DÉFAUT dans
.claude/widgets-rendus/ (ignoré par git) : AUCUNE donnée personnelle de
prospect n'est écrite dans le dépôt. Stdlib uniquement ; un champ absent
s'affiche « — », jamais estimé.
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
sys.path.insert(0, ICI)
from segments_sms import segments  # noqa: E402


def e(v):
    return html.escape(str(v)) if v not in (None, "") else "—"


def _liste(d, *cles):
    for c in cles:
        v = d.get(c)
        if isinstance(v, list):
            return v
        if isinstance(v, dict):
            for sous in ("items", "results", "data"):
                if isinstance(v.get(sous), list):
                    return v[sous]
    return []


def barre(valeur, maxi):
    pct = int(valeur / maxi * 100) if maxi else 0
    return f'<div class="barre"><span style="width:{pct}%"></span></div>'


def tableau_de_bord(d):
    # clés : clients(list_clients), quotas(sortie quotas.py --json),
    # linkedin(list_linkedin_scheduled_day), stripe(stripe_stats),
    # contactes(int|None), priorites([str])
    clients = _liste(d, "clients")
    maxi = len(clients) or 1
    etapes = [("prospects", len(clients) if "clients" in d else None),
              ("contactés", d.get("contactes")),
              ("réponses", d.get("reponses")),
              ("rendez-vous", d.get("rendez_vous")),
              ("clients", (d.get("stripe") or {}).get("customers"))]
    entonnoir = "\n".join(
        f"<tr><td>{e(nom)}</td><td>{e(v)}</td>"
        f"<td>{barre(v, maxi) if isinstance(v, int) else ''}</td></tr>"
        for nom, v in etapes)
    quotas = "\n".join(
        f"<tr><td>{e(canal)}</td><td>{e(c.get('envoyes'))}</td>"
        f"<td>{e(c.get('quota_jour'))}</td><td>{e(c.get('restant'))}</td></tr>"
        for canal, c in (d.get("quotas", {}).get("canaux", {})).items())
    linkedin = "\n".join(
        f"<li>{e(m.get('scheduledAt') or m.get('time'))} — "
        f"{e(m.get('connection') or m.get('connectionId'))}</li>"
        for m in _liste(d, "linkedin")) or "<li>—</li>"
    stripe = d.get("stripe") or {}
    return {
        "ENTONNOIR": entonnoir, "QUOTAS": quotas or "<tr><td colspan=4>—</td></tr>",
        "LINKEDIN": linkedin,
        "MRR": e(stripe.get("mrr") or stripe.get("mrr_estime")),
        "ABONNEMENTS": e(stripe.get("active_subscriptions")),
        "CA": e(stripe.get("revenue") or stripe.get("total_revenue")),
        "PRIORITES": "\n".join(f"<li>{e(p)}</li>" for p in d.get("priorites", []))
        or "<li>—</li>",
    }


def resultats_de_zone(d):
    # clés : le rapport de dedoublonner.py (+ zone)
    def ligne_n(p):
        contact = p.get("email") or p.get("phone") or p.get("website") or "—"
        return (f"<tr><td>{e(p.get('name') or p.get('nom'))}</td>"
                f"<td>{e(contact)}</td><td>{e(p.get('rating') or p.get('note'))}</td>"
                f"<td>{e(p.get('reviews') or p.get('avis'))}</td></tr>")
    return {
        "ZONE": e(d.get("zone")),
        "NB_NOUVEAUX": str(len(d.get("nouveaux", []))),
        "NB_DOUBLONS": str(len(d.get("doublons", []))),
        "NB_SANS_CONTACT": str(len(d.get("sans_contact", []))),
        "NOUVEAUX": "\n".join(ligne_n(p) for p in d.get("nouveaux", []))
        or "<tr><td colspan=4>—</td></tr>",
        "DOUBLONS": "\n".join(
            f"<tr><td>{e((x.get('fiche') or {}).get('name'))}</td>"
            f"<td>{e(x.get('critere'))}</td></tr>" for x in d.get("doublons", []))
        or "<tr><td colspan=2>—</td></tr>",
        "SANS_CONTACT": "\n".join(
            f"<li>{e(p.get('name') or p.get('nom'))}</li>"
            for p in d.get("sans_contact", [])) or "<li>—</li>",
    }


def apercu_email(d):
    # clés : subject, content (html), expediteur, recipients, controles
    c = d.get("controles", {})
    return {
        "EXPEDITEUR": e(d.get("expediteur")), "OBJET": e(d.get("subject")),
        "NB_DESTINATAIRES": str(len(d.get("recipients", []))),
        "CORPS": d.get("content") or "—",  # html rendu tel quel, volontaire
        "DESINSCRIPTION": e(c.get("desinscription", "à vérifier (conformite.py)")),
        "IDENTITE": e(c.get("identite", "à vérifier (conformite.py)")),
        "OPPOSITION": e(c.get("opposition", "à vérifier (conformite.py)")),
    }


def apercu_sms(d):
    texte = d.get("content") or ""
    enc, longueur, nb = segments(texte)
    return {
        "TEXTE": e(texte), "ENCODAGE": enc, "LONGUEUR": str(longueur),
        "SEGMENTS": str(nb),
        "NB_DESTINATAIRES": str(len(d.get("targets", []))),
        "STOP": "présent" if "stop" in texte.lower() else "ABSENT (refusé)",
    }


def file_linkedin(d):
    # clés : jour, quota_restant, messages(list_linkedin_scheduled_day),
    # historique({connectionId: nb de messages déjà envoyés})
    histo = d.get("historique", {})
    lignes = "\n".join(
        f"<tr><td>{e(m.get('scheduledAt') or m.get('time'))}</td>"
        f"<td>{e(m.get('connection') or m.get('connectionId'))}</td>"
        f"<td>{e(m.get('type') or ('modèle' if m.get('templateId') else 'message'))}</td>"
        f"<td>{e((m.get('message') or '')[:80])}</td>"
        f"<td>{e(histo.get(str(m.get('connectionId')), '—'))} envoi(s)</td></tr>"
        for m in _liste(d, "messages")) or "<tr><td colspan=5>—</td></tr>"
    return {"JOUR": e(d.get("jour")), "NB_MESSAGES": str(len(_liste(d, "messages"))),
            "QUOTA_RESTANT": e(d.get("quota_restant")), "LIGNES": lignes}


def chronologie(d):
    # clés : fiche(client), evenements([{date, canal, contenu, statut}]), relance
    f = d.get("fiche", {})
    lignes = "\n".join(
        f"<tr><td>{e(x.get('date'))}</td><td>{e(x.get('canal'))}</td>"
        f"<td>{e((x.get('contenu') or '')[:80])}</td><td>{e(x.get('statut'))}</td></tr>"
        for x in sorted(d.get("evenements", []),
                        key=lambda x: str(x.get("date", "")))) \
        or "<tr><td colspan=4>—</td></tr>"
    dates = [x.get("date") for x in d.get("evenements", []) if x.get("date")]
    return {"NOM": e(f.get("name")), "VILLE": e(f.get("city")),
            "SPECIALITE": e(f.get("speciality")), "STATUT": e(f.get("status")),
            "DERNIER_CONTACT": e(max(dates) if dates else None),
            "LIGNES": lignes, "RELANCE": e(d.get("relance"))}


def calendrier_semaine(d):
    # clés : posts, blog, videos, webinaires (réponses brutes des list_*)
    elements = []
    for genre, cle, champ_date in (("post", "posts", "scheduled_at"),
                                   ("article", "blog", "scheduled_at"),
                                   ("vidéo", "videos", "scheduled_at"),
                                   ("webinaire", "webinaires", "event_date")):
        for x in _liste(d, cle):
            elements.append((str(x.get(champ_date, ""))[:10], genre,
                             x.get("subject") or x.get("title"),
                             x.get("status") or
                             ("actif" if x.get("is_active") else "inactif")))
    jours = []
    for jour in sorted({d0 for d0, *_ in elements if d0}):
        items = "\n".join(
            f"<li>[{e(genre)}] {e(titre)} <span class=\"badge\">{e(statut)}</span></li>"
            for d0, genre, titre, statut in elements if d0 == jour)
        jours.append(f'<h2>{e(jour)}</h2><div class="carte"><ul>{items}</ul></div>')
    return {"JOURS": "\n".join(jours) or '<div class="carte">—</div>'}


def mrr_stripe(d):
    s = d.get("stripe", d)
    return {
        "MRR": e(s.get("mrr") or s.get("mrr_estime")),
        "CLIENTS": e(s.get("customers")), "PAIEMENTS": e(s.get("payments")),
        "ABONNEMENTS": e(s.get("active_subscriptions")),
        "CA": e(s.get("revenue") or s.get("total_revenue")),
        "EVOLUTION": e(d.get("evolution")),
    }


RENDUS = {
    "tableau-de-bord-prospection": tableau_de_bord,
    "resultats-de-zone": resultats_de_zone,
    "apercu-email": apercu_email,
    "apercu-sms": apercu_sms,
    "file-linkedin-du-jour": file_linkedin,
    "chronologie-prospect": chronologie,
    "calendrier-editorial-semaine": calendrier_semaine,
    "mrr-stripe": mrr_stripe,
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
    print(f"{nom} → {dst} (dossier ignoré par git : aucune donnée de "
          "prospect dans le dépôt)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
