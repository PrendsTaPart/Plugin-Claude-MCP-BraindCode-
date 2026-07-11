#!/usr/bin/env python3
"""Recherche sémantique locale dans le catalogue rapido-forge — 100 %
hors-ligne, zéro dépendance (TF-IDF maison + cosinus ; accents repliés).

Entrée : requête libre (argument ou stdin) + filtres optionnels.
Sortie : JSON top 5 {name, score, niveau, prerequis_manquants} — les
prérequis déjà réalisés sont détectés dans le journal du client
`./rapido-kb/startup/forge/parcours.md` (lignes `- [x] <skill> — …`).

Usage :
  python3 forge_recherche.py "structurer mes prix" [--tags finance]
          [--niveau debutant|intermediaire|expert] [--parcours bootcamp]
          [--embeddings]   # sentence-transformers SI installé, sinon
                           # repli TF-IDF silencieux (portabilité)
"""
import json
import math
import os
import re
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
CATALOGUE = os.path.join(ICI, "..", "reference", "catalogue.json")
JOURNAL = os.path.join(os.getcwd(), "rapido-kb", "startup", "forge", "parcours.md")

MOTS_VIDES = set("""le la les un une des du de d l au aux et ou mais pour par
sur dans avec sans que qui quoi comment je tu il nous vous ils mon ma mes
son sa ses ce cette ces est sont a ai as avons avez ont veux veut voulons
faire fait mettre mes notre vos leur leurs plus très bien tout tous toute
en y ne pas se sa si on aide aidez moi produit projet exercice framework
utiliser quand utilisateur skill""".split())


# Pont FR -> EN : les names des skills sont en anglais, les requêtes en
# français — on replie les deux vers un token canonique commun.
SYNONYMES = {
    "prix": "pricing", "tarif": "pricing", "tarifs": "pricing",
    "tarification": "pricing", "pub": "ads", "publicite": "ads",
    "publicites": "ads", "levee": "fundraising", "fonds": "fundraising",
    "investisseur": "investor", "investisseurs": "investor",
    "marque": "brand", "lancement": "launch", "lancer": "launch",
    "atterrissage": "landing", "prospection": "outreach",
    "tresorerie": "cash", "previsionnel": "forecast", "concurrence":
    "competitive", "concurrents": "competitive", "sondage": "survey",
    "essai": "testing", "tests": "testing", "referencement": "seo",
    "video": "video", "communaute": "community", "fidelisation":
    "retention", "churn": "retention", "parrainage": "referral",
}


def normaliser(texte):
    texte = unicodedata.normalize("NFD", texte.lower())
    texte = "".join(c for c in texte if unicodedata.category(c) != "Mn")
    toks = [t for t in re.findall(r"[a-z0-9]{2,}", texte) if t not in MOTS_VIDES]
    return [SYNONYMES.get(t, t) for t in toks]


def tfidf(docs):
    df = {}
    tokens_docs = []
    for d in docs:
        toks = normaliser(d)
        tokens_docs.append(toks)
        for t in set(toks):
            df[t] = df.get(t, 0) + 1
    n = len(docs)
    idf = {t: math.log((n + 1) / (c + 1)) + 1 for t, c in df.items()}
    vecteurs = []
    for toks in tokens_docs:
        v = {}
        for t in toks:
            v[t] = v.get(t, 0) + 1
        norme = math.sqrt(sum((tf * idf[t]) ** 2 for t, tf in v.items())) or 1.0
        vecteurs.append({t: tf * idf[t] / norme for t, tf in v.items()})
    return vecteurs, idf


def cosinus(vq, vd):
    return sum(p * vd.get(t, 0.0) for t, p in vq.items())


def faits_du_journal():
    if not os.path.isfile(JOURNAL):
        return set()
    faits = set()
    for ligne in open(JOURNAL, encoding="utf-8"):
        m = re.match(r"\s*- \[x\]\s+`?([\w\-]+)`?", ligne)
        if m:
            faits.add(m.group(1))
    return faits


def main():
    args = sys.argv[1:]
    filtres = {"tags": None, "niveau": None, "parcours": None}
    embeddings = "--embeddings" in args
    if embeddings:
        args.remove("--embeddings")
    libres = []
    i = 0
    while i < len(args):
        if args[i] in ("--tags", "--niveau", "--parcours") and i + 1 < len(args):
            filtres[args[i][2:]] = args[i + 1]
            i += 2
        else:
            libres.append(args[i])
            i += 1
    requete = " ".join(libres).strip() or sys.stdin.read().strip()
    if not requete:
        print(json.dumps({"erreur": "requête vide"}))
        return 1

    entrees = json.load(open(CATALOGUE, encoding="utf-8"))
    if filtres["tags"]:
        voulus = set(filtres["tags"].split(","))
        entrees = [e for e in entrees if voulus & set(e["tags"])]
    if filtres["niveau"]:
        entrees = [e for e in entrees if e["niveau"] == filtres["niveau"]]
    if filtres["parcours"]:
        entrees = [e for e in entrees if e["parcours"] == filtres["parcours"]]
    if not entrees:
        print(json.dumps({"erreur": "aucun skill ne passe les filtres"}))
        return 1

    if embeddings:
        try:
            from sentence_transformers import SentenceTransformer, util  # noqa
            modele = SentenceTransformer("all-MiniLM-L6-v2")
            docs = [f"{e['name']} {e['description']} {' '.join(e['tags'])}" for e in entrees]
            emb = modele.encode(docs + [requete])
            scores = [float(util.cos_sim(emb[-1], emb[i])) for i in range(len(docs))]
        except Exception:
            embeddings = False  # repli TF-IDF silencieux
    if not embeddings:
        titres = [e["name"].replace("-", " ") for e in entrees]
        docs = [f"{titres[i]} {e['description']} {' '.join(e['tags'])}"
                for i, e in enumerate(entrees)]
        vecteurs, idf = tfidf(docs)
        toks = normaliser(requete)
        vq = {}
        for t in toks:
            vq[t] = vq.get(t, 0) + 1
        norme = math.sqrt(sum((tf * idf.get(t, 1.0)) ** 2 for t, tf in vq.items())) or 1.0
        vq = {t: tf * idf.get(t, 1.0) / norme for t, tf in vq.items()}
        scores = [cosinus(vq, v) for v in vecteurs]

    faits = faits_du_journal()
    classement = sorted(zip(scores, entrees), key=lambda x: -x[0])[:5]
    resultat = [{
        "name": e["name"],
        "score": round(s, 4),
        "niveau": e["niveau"],
        "prerequis_manquants": [p for p in e["prerequis"] if p not in faits],
    } for s, e in classement]
    print(json.dumps(resultat, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
