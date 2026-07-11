#!/usr/bin/env python3
"""Génère rapido-forge/reference/catalogue.json — LE fichier que les agents
forge et la recherche (forge_recherche.py) consomment.

Pour chaque skill : {name, parcours, jour?, description, tags, niveau,
prerequis, voir_aussi, livrable_path}. Le script VALIDE le graphe des
prérequis : toute cible référencée existe, aucun cycle (tri topologique —
en cas de cycle, la liste est affichée et le script échoue, exit 1).

Relançable à volonté (sortie déterministe, triée par name). Tourne en CI
(step dédié de .github/workflows/validation.yml). 100 % stdlib.

Usage : python3 scripts/forge_catalogue.py [--check]
  --check : valide sans réécrire le fichier (mode CI).
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(RACINE, "rapido-forge", "skills")
SORTIE = os.path.join(RACINE, "rapido-forge", "reference", "catalogue.json")

RX_FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
RX_LISTE = re.compile(r"\[(.*?)\]")
RX_JOUR = re.compile(r"\*\*Bootcamp 5 jours — Jour (\d)\*\*")
RX_LIVRABLE = re.compile(r"`(\./rapido-kb/[\w\-/\.]+)`")
RX_REF = re.compile(r"`([a-z][\w\-]+:[a-z][\w\-]+)`")


def champ(fm, cle):
    m = re.search(rf"^{cle}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip("\"'") if m else None


def liste(fm, cle):
    v = champ(fm, cle)
    if not v:
        return []
    m = RX_LISTE.search(v)
    return [x.strip() for x in m.group(1).split(",")] if m else [v]


def construire():
    entrees = []
    for d in sorted(os.listdir(SKILLS)):
        f = os.path.join(SKILLS, d, "SKILL.md")
        if not os.path.isfile(f):
            continue
        src = open(f, encoding="utf-8").read()
        m = RX_FRONT.match(src)
        if not m:
            print(f"ERREUR : frontmatter absent — {d}")
            return None
        fm, corps = m.group(1), src[m.end():]
        jour = RX_JOUR.search(corps)
        pos = corps.find("## Voir aussi")
        voir_aussi = RX_REF.findall(corps[pos:]) if pos >= 0 else []
        pos_l = corps.find("## Livrable — toujours dans la KB")
        livrable = RX_LIVRABLE.search(corps[pos_l:] if pos_l >= 0 else corps)
        entree = {
            "name": champ(fm, "name"),
            "parcours": d.split("-")[0],
            "description": champ(fm, "description"),
            "tags": liste(fm, "tags"),
            "niveau": champ(fm, "niveau"),
            "prerequis": liste(fm, "prerequis"),
            "voir_aussi": voir_aussi,
            "livrable_path": livrable.group(1) if livrable else None,
        }
        if jour:
            entree["jour"] = int(jour.group(1))
        entrees.append(entree)
    return entrees


def valider_graphe(entrees):
    noms = {e["name"] for e in entrees}
    erreurs = []
    aretes = {e["name"]: [p for p in e["prerequis"]] for e in entrees}
    for nom, prs in aretes.items():
        for p in prs:
            if p not in noms:
                erreurs.append(f"prérequis inexistant : {nom} <= {p}")
    # tri topologique (Kahn) — reste = cycle
    degre = {n: 0 for n in noms}
    for nom, prs in aretes.items():
        for p in prs:
            if p in noms:
                degre[nom] += 0  # les arêtes vont de p vers nom
    entrants = {n: set(p for p in aretes[n] if p in noms) for n in noms}
    file_ = [n for n in sorted(noms) if not entrants[n]]
    vus = set()
    while file_:
        n = file_.pop()
        vus.add(n)
        for m2 in sorted(noms):
            if n in entrants[m2]:
                entrants[m2].discard(n)
                if not entrants[m2] and m2 not in vus:
                    file_.append(m2)
    cycle = sorted(noms - vus)
    if cycle:
        erreurs.append("CYCLE détecté entre : " + ", ".join(cycle))
    return erreurs


def main():
    check = "--check" in sys.argv
    entrees = construire()
    if entrees is None:
        return 1
    erreurs = valider_graphe(entrees)
    if erreurs:
        for e in erreurs:
            print("ERREUR :", e)
        return 1
    if not check:
        with open(SORTIE, "w", encoding="utf-8") as f:
            json.dump(entrees, f, ensure_ascii=False, indent=2)
            f.write("\n")
    n_pre = sum(1 for e in entrees if e["prerequis"])
    print(f"catalogue : {len(entrees)} skills, {n_pre} avec prérequis, "
          f"graphe validé sans cycle{' (check seul)' if check else ' — écrit : ' + os.path.relpath(SORTIE, RACINE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
