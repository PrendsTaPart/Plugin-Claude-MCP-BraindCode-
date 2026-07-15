#!/usr/bin/env python3
"""Audit GEO déterministe d'un contenu (stdlib uniquement).

Applique une checklist GEO (Generative Engine Optimization — être cité par les
moteurs génératifs) sourcée de docs/methodo/etat-de-lart-2026.md §8. Le modèle
NE score JAMAIS de tête : ce script mesure des critères objectifs sur le texte
et sort un score + les corrections à proposer.

Entrée (fichier JSON en argument, ou stdin) :
    {"contenu": "<markdown ou texte de l'article>",
     "meta": {"date_maj": "2026-07-01",          // optionnel
              "date_reference": "2026-07-14",     // optionnel (pour l'âge)
              "auteur": "Nom Prénom",             // optionnel
              "schema": true}}                    // schema markup présent ?

Sortie (stdout, JSON) : chaque critère {ok, detail}, score global (%),
corrections. Code de sortie : 0 (audit, jamais un gate).
"""
import json
import re
import sys
from datetime import date

PHRASES_SUBJECTIVES = [
    r"\bje pense\b", r"\bje crois\b", r"\bà mon avis\b", r"\bselon moi\b",
    r"\bnous pensons\b", r"\bi think\b", r"\bwe believe\b", r"\bin my opinion\b",
]
RX_LIEN = re.compile(r"\]\(https?://", re.I)
RX_STAT = re.compile(r"\b\d+([.,]\d+)?\s?%|\b\d{2,}\b")
RX_ANCRE = re.compile(r"\{#[\w\-]+\}|id\s*=\s*[\"'][\w\-]+[\"']")
RX_FAQ = re.compile(r"(^|\n)#{1,6}\s*(faq|questions|définition|definition)",
                    re.I)
RX_DATE = re.compile(r"\b(20\d{2})-(\d{2})-(\d{2})\b")


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def mots(txt):
    return re.findall(r"\w+", txt, re.UNICODE)


def premier_bloc(txt):
    """Mots avant le premier titre markdown ou la première ligne vide."""
    lignes = []
    for l in txt.splitlines():
        if l.strip().startswith("#"):
            if lignes:
                break
            continue
        if not l.strip() and lignes:
            break
        if l.strip():
            lignes.append(l.strip())
    return " ".join(lignes)


def auditer(data):
    txt = data.get("contenu") or ""
    meta = data.get("meta") or {}
    nb_mots = max(len(mots(txt)), 1)
    crit = {}

    # 1. Réponse directe en 40-60 premiers mots
    intro = premier_bloc(txt)
    n_intro = len(mots(intro))
    crit["reponse_directe_40_60_mots"] = {
        "ok": 15 <= n_intro <= 65 and intro.endswith((".", "!", "?")) or (15 <= n_intro <= 65),
        "detail": f"{n_intro} mots dans le bloc d'intro (cible 40-60)",
    }

    # 2. Densité de faits : une stat toutes les ~150-200 mots
    n_stats = len(RX_STAT.findall(txt))
    ratio = nb_mots / max(n_stats, 1)
    crit["densite_faits"] = {
        "ok": n_stats > 0 and ratio <= 200,
        "detail": f"{n_stats} stats / {nb_mots} mots (1 toutes ~{round(ratio)} mots ; cible <=200)",
    }

    # 3. Sources autoritaires citées (liens http)
    n_liens = len(RX_LIEN.findall(txt))
    crit["sources_autoritaires"] = {
        "ok": n_liens >= 2,
        "detail": f"{n_liens} lien(s) source (cible >=2)",
    }

    # 4. Schema markup
    crit["schema_markup"] = {
        "ok": bool(meta.get("schema")),
        "detail": "meta.schema=" + str(meta.get("schema")),
    }

    # 5. Ancres de citation (id sur les blocs)
    n_ancres = len(RX_ANCRE.findall(txt))
    crit["ancres_citation"] = {
        "ok": n_ancres >= 1,
        "detail": f"{n_ancres} ancre(s) id",
    }

    # 6. Blocs FAQ / définition
    crit["blocs_faq_definition"] = {
        "ok": bool(RX_FAQ.search(txt)),
        "detail": "bloc FAQ/définition détecté" if RX_FAQ.search(txt) else "aucun",
    }

    # 7. Auteur (autorité E-E-A-T)
    crit["auteur_present"] = {
        "ok": bool(meta.get("auteur")),
        "detail": "auteur=" + str(meta.get("auteur")),
    }

    # 8. Style déclaratif (pas de tournures subjectives)
    subj = sum(len(re.findall(p, txt, re.I)) for p in PHRASES_SUBJECTIVES)
    crit["style_declaratif"] = {
        "ok": subj == 0,
        "detail": f"{subj} tournure(s) subjective(s) (cible 0)",
    }

    # 9. Fraîcheur
    dmaj = meta.get("date_maj")
    dref = meta.get("date_reference")
    if dmaj and dref and RX_DATE.match(dmaj) and RX_DATE.match(dref):
        y1, m1, d1 = map(int, dmaj.split("-"))
        y2, m2, d2 = map(int, dref.split("-"))
        age = (date(y2, m2, d2) - date(y1, m1, d1)).days
        crit["fraicheur"] = {"ok": 0 <= age <= 90,
                             "detail": f"maj il y a {age} j (cible <=90)"}
    else:
        crit["fraicheur"] = {"ok": bool(dmaj),
                             "detail": "date_maj présente" if dmaj else "aucune date_maj"}

    n_ok = sum(1 for c in crit.values() if c["ok"])
    total = len(crit)
    corrections = [k for k, c in crit.items() if not c["ok"]]
    return {
        "score_geo_pct": round(100 * n_ok / total, 1),
        "criteres_ok": n_ok,
        "criteres_total": total,
        "criteres": crit,
        "corrections_a_proposer": corrections,
        "formule": "score = critères OK / critères total * 100",
    }


def main():
    print(json.dumps(auditer(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
