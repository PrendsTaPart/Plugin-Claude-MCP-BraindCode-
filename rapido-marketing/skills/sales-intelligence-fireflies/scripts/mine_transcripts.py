#!/usr/bin/env python3
"""Mining d'objections & de verbatims depuis des transcripts de RDV (stdlib).

Le modèle NE compte JAMAIS de tête : ce script agrège les phrases réelles des
transcripts (fournies par MCP Fireflies) et sort, par catégorie d'objection, la
fréquence CHIFFRÉE, la part, et des verbatims horodatés ANONYMISÉS. Si l'issue
du deal est connue (côté CRM), il ventile les catégories gagné vs perdu.

Anonymisation obligatoire : emails, téléphones et noms/enseignes passés dans
`masquer` sont remplacés par des jetons avant toute sortie — aucun nom de client
ne ressort du script.

Entrée (fichier JSON en argument, ou stdin) :
    {"transcripts": [
        {"id": "abc123", "date": "2026-06-01", "issue": "perdu",
         "masquer": ["Jean Dupont", "jean@acme.fr", "ACME"],
         "phrases": [
            {"role": "externe", "time": 123.4, "texte": "c'est trop cher pour nous"},
            {"role": "interne", "time": 130.0, "texte": "je comprends, regardons le ROI"}
         ]}
     ],
     "categories": {                       // optionnel — sinon défauts ci-dessous
        "prix": ["cher", "budget"], ...}}

Seules les phrases `role == "externe"` (prospect) sont minées pour les
objections et les questions. Issue ∈ {gagne, perdu, null/absent}.

Sortie (stdout, JSON) : formule, par_categorie (count/part/verbatims), questions
récurrentes, patterns_gagne_vs_perdu, totaux. Code retour : 0.
"""
import json
import re
import sys
from collections import Counter, defaultdict

# Catégories d'objection par défaut (déclencheurs FR, minuscule). Surchargables
# via la clé "categories" de l'entrée. Une phrase peut compter dans plusieurs.
CATEGORIES_DEFAUT = {
    "prix": ["cher", "prix", "coût", "cout", "budget", "tarif", "onéreux",
             "onereux", "remise", "gratuit", "rentab"],
    "timing": ["plus tard", "pas le moment", "trimestre", "année prochaine",
               "annee prochaine", "timing", "occupé", "occupe", "priorité",
               "priorite", "reporter", "attendre"],
    "concurrent": ["concurrent", "déjà", "deja", "utilisons", "actuellement",
                   "alternative", "comparer", "en place", "solution existante"],
    "confiance": ["sûr", "sur de", "garantie", "preuve", "risque", "référence",
                  "reference", "avis", "essai", "sécurit", "securit", "confiance",
                  "peur"],
    "technique": ["intégration", "integration", "api", "compatible", "technique",
                  "fonctionnalité", "fonctionnalite", "marche pas", "bug",
                  "migration", "import"],
    "autorite": ["décision", "decision", "patron", "direction", "valider",
                 "équipe", "equipe", "associé", "associe", "décideur", "decideur",
                 "hiérarchie", "hierarchie"],
}

RE_EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
RE_TEL = re.compile(r"\+?\d[\d .()-]{7,}\d")


def anonymiser(texte, masquer):
    """Retire emails, téléphones et noms/enseignes fournis. Jamais de PII en sortie."""
    t = RE_EMAIL.sub("[EMAIL]", texte)
    t = RE_TEL.sub("[TEL]", t)
    for nom in sorted([n for n in (masquer or []) if n], key=len, reverse=True):
        t = re.compile(re.escape(nom), re.IGNORECASE).sub("[NOM]", t)
    return t


def categoriser(texte_min, categories):
    """Retourne l'ensemble des catégories dont un déclencheur apparaît dans la phrase."""
    trouve = set()
    for cat, mots in categories.items():
        if any(m in texte_min for m in mots):
            trouve.add(cat)
    return trouve


def part(num, den):
    return round(num / den, 4) if den else 0.0


def analyser(data):
    categories = data.get("categories") or CATEGORIES_DEFAUT
    transcripts = data.get("transcripts") or []

    compte_cat = Counter()
    verbatims = defaultdict(list)
    questions = Counter()
    par_issue = defaultdict(lambda: Counter())  # issue -> Counter(catégorie)
    n_issue = Counter()
    n_phrases_externes = 0

    for tr in transcripts:
        tid = tr.get("id", "?")
        issue = tr.get("issue") or "inconnu"
        masquer = tr.get("masquer") or []
        n_issue[issue] += 1
        for ph in tr.get("phrases") or []:
            if ph.get("role") != "externe":
                continue
            n_phrases_externes += 1
            texte = ph.get("texte", "") or ""
            texte_min = texte.lower()
            cats = categoriser(texte_min, categories)
            anon = anonymiser(texte, masquer)
            for cat in cats:
                compte_cat[cat] += 1
                par_issue[issue][cat] += 1
                verbatims[cat].append({
                    "transcript": tid,
                    "time": ph.get("time"),
                    "texte_anonymise": anon,
                })
            if "?" in texte:
                questions[anon] += 1

    total_obj = sum(compte_cat.values())
    par_categorie = {
        cat: {
            "count": compte_cat[cat],
            "part": part(compte_cat[cat], total_obj),
            "verbatims": verbatims[cat][:5],  # échantillon anonymisé
        }
        for cat in sorted(compte_cat, key=lambda c: -compte_cat[c])
    }

    patterns = {
        issue: {
            "n_transcripts": n_issue[issue],
            "objections": dict(cnt.most_common()),
        }
        for issue, cnt in par_issue.items()
    }

    return {
        "formule": "part = count(catégorie) / total objections ; fréquences = comptage des phrases externes matchant un déclencheur",
        "n_transcripts": len(transcripts),
        "n_phrases_externes": n_phrases_externes,
        "total_objections": total_obj,
        "par_categorie": par_categorie,
        "questions_recurrentes": [
            {"question": q, "occurrences": n}
            for q, n in questions.most_common(10) if n >= 2
        ],
        "patterns_gagne_vs_perdu": patterns,
        "note": "Aucun nom en sortie (anonymisation) ; une leçon exige >=2 occurrences chiffrées.",
    }


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def main():
    print(json.dumps(analyser(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
