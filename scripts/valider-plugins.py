#!/usr/bin/env python3
"""Validation structurelle de la marketplace Rapido (rapide, sans réseau).

Python stdlib uniquement. Exit 0 = valide ; exit 1 = au moins une erreur.

Contrôles (complémentaires de scripts/tester-skills.py, qui ajoute les
placeholders, la convention de description, la cohérence MCP et les tests
fonctionnels des hooks) :
- STRUCTURE : tous les .json du dépôt parsent (dossiers cachés compris) ;
  chaque SKILL.md et agents/*.md a un frontmatter avec name + description
  non vides ; name unique par plugin (skills et agents confondus) ; chaque
  plugin a plugin.json + une entrée dans marketplace.json ; pas d'artefacts
  (__pycache__/, *.pyc, .coverage, node_modules/, .DS_Store).
- RÉFÉRENCES : tout chemin ${CLAUDE_PLUGIN_ROOT}/… cité dans un skill/agent
  existe dans le plugin ; chaque skill listé dans un ATTRIBUTIONS.md embarque
  sa LICENSE (ou LICENSE.txt).
- HOOKS JSON : chaque hooks.json parse et chaque script référencé existe.
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RX_FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
RX_PLUGIN_ROOT = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w\-./]+)")
ARTEFACTS = ("__pycache__", "node_modules", ".DS_Store", ".coverage")


def frontmatter_ok(texte):
    m = RX_FRONT.match(texte)
    if not m:
        return False
    bloc = m.group(1)
    for cle in ("name", "description"):
        mm = re.search(rf"^{cle}:\s*(.*)$", bloc, re.M)
        if not mm:
            return False
        val = mm.group(1).strip()
        if not val:
            return False
        if val in (">", ">-", "|", "|-"):  # scalaire plié : au moins une ligne
            pos = bloc.find(mm.group(0)) + len(mm.group(0))
            suite = [l for l in bloc[pos:].splitlines() if l.startswith((" ", "\t")) and l.strip()]
            if not suite:
                return False
    return True


def nom_frontmatter(texte):
    m = RX_FRONT.match(texte)
    if not m:
        return None
    mm = re.search(r"^name:\s*(.+)$", m.group(1), re.M)
    return mm.group(1).strip() if mm else None


def main():
    os.chdir(RACINE)
    erreurs = []

    # 1. Tous les JSON parsent (dossiers cachés compris)
    n_json = 0
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in files:
            if f.endswith(".json"):
                n_json += 1
                p = os.path.join(root, f)
                try:
                    json.load(open(p, encoding="utf-8"))
                except Exception as e:  # noqa: BLE001
                    erreurs.append(f"JSON invalide : {p} — {e}")

    plugins = sorted(d for d in os.listdir(".")
                     if os.path.isfile(os.path.join(d, ".claude-plugin", "plugin.json")))

    # 2. Entrée marketplace pour chaque plugin
    market = os.path.join(".claude-plugin", "marketplace.json")
    if os.path.isfile(market):
        contenu = json.dumps(json.load(open(market, encoding="utf-8")))
        for p in plugins:
            if f'"{p}"' not in contenu:
                erreurs.append(f"marketplace.json : plugin {p} sans entrée")
    else:
        erreurs.append("Fichier .claude-plugin/marketplace.json absent")

    # 3. Frontmatters + unicité + références + hooks + artefacts + licences
    n_md = 0
    for p in plugins:
        noms = {}
        cibles = []
        sk = os.path.join(p, "skills")
        if os.path.isdir(sk):
            cibles += [os.path.join(sk, d, "SKILL.md") for d in sorted(os.listdir(sk))
                       if os.path.isfile(os.path.join(sk, d, "SKILL.md"))]
        ag = os.path.join(p, "agents")
        if os.path.isdir(ag):
            cibles += [os.path.join(ag, f) for f in sorted(os.listdir(ag)) if f.endswith(".md")]
        for chemin in cibles:
            n_md += 1
            texte = open(chemin, encoding="utf-8").read()
            if not frontmatter_ok(texte):
                erreurs.append(f"Frontmatter invalide (name/description) : {chemin}")
                continue
            nom = nom_frontmatter(texte)
            if nom in noms:
                erreurs.append(f"Doublon de name `{nom}` dans {p} : {noms[nom]} et {chemin}")
            noms[nom] = chemin
            for cible in RX_PLUGIN_ROOT.findall(texte):
                if not os.path.exists(os.path.join(p, cible.rstrip(".,;:"))):
                    erreurs.append(
                        f"{chemin} : ${{CLAUDE_PLUGIN_ROOT}}/{cible} introuvable")

        hooks_json = os.path.join(p, "hooks", "hooks.json")
        if os.path.isfile(hooks_json):
            try:
                contenu = json.load(open(hooks_json, encoding="utf-8"))
                for s in sorted(set(RX_PLUGIN_ROOT.findall(json.dumps(contenu)))):
                    if not os.path.isfile(os.path.join(p, s)):
                        erreurs.append(f"{hooks_json} référence {s} qui n'existe pas")
            except Exception as e:  # noqa: BLE001
                erreurs.append(f"{hooks_json} ne parse pas ({e})")

        for root, dirs, files in os.walk(p):
            for d in list(dirs):
                if d in ARTEFACTS:
                    erreurs.append(f"Artefact à purger : {os.path.join(root, d)}/")
            for f in files:
                if f.endswith(".pyc") or f in ARTEFACTS:
                    erreurs.append(f"Artefact à purger : {os.path.join(root, f)}")

        for attrib in (os.path.join(p, "ATTRIBUTIONS.md"),
                       os.path.join(p, "skills", "ATTRIBUTIONS.md")):
            if not os.path.isfile(attrib):
                continue
            for ligne in open(attrib, encoding="utf-8"):
                m = re.match(r"\|\s*`([a-z0-9\-]+)", ligne)
                if not m:
                    continue
                dossier = os.path.join(p, "skills", m.group(1))
                if os.path.isdir(dossier) and not (
                        os.path.isfile(os.path.join(dossier, "LICENSE"))
                        or os.path.isfile(os.path.join(dossier, "LICENSE.txt"))):
                    erreurs.append(f"Skill externe sans LICENSE : {dossier}")

    print(f"valider-plugins.py — {len(plugins)} plugins, {n_json} JSON, "
          f"{n_md} frontmatters vérifiés")
    if erreurs:
        print(f"\n{len(erreurs)} ERREUR(S) :")
        for e in erreurs:
            print(" -", e)
        return 1
    print("TOUT VALIDE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
