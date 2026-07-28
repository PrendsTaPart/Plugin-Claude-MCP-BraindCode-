#!/usr/bin/env python3
"""Contrôles CI supplémentaires (P5.1). Python stdlib uniquement, exit 1 = échec.

Contrat : chaque détecteur commence par prouver qu'il SAIT échouer (auto-test
sur fixture embarquée). Une CI qui passe sans avoir démontré sa capacité à
échouer ne teste rien — c'était le bug d'origine.

Contrôles (bloquants) :
1. SIMILARITÉ  — deux descriptions de skills trop proches (Jaccard mots
   significatifs > 0,50, hors paires internes à rapido-forge) ;
2. SECRETS     — motifs de tokens/clés dans les fichiers suivis ;
3. OUTILS      — un fichier des plugins foodeatup/foodeatup-boucles cite un
   outil foodeatup absent de la liste versionnée live ; la liste des outils
   destructifs du hook contient un outil inexistant ;
4. CARTO       — docs/boucles-vs-outils.md ne couvre pas exactement la liste
   live (dérive après régénération oubliée) ;
5. CARTE       — un plugin du dépôt manque dans la carte marketplace générée.
"""
import json
import os
import re
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RACINE)
RX_FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
erreurs = []


def fichiers_suivis():
    r = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
    return r.stdout.splitlines()


def lire(p):
    try:
        return open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        return ""


def description(texte):
    m = RX_FRONT.match(texte)
    if not m:
        return None
    mm = re.search(r"^description:\s*(.+)$", m.group(1), re.M)
    if not mm:
        return None
    v = mm.group(1).strip()
    if v in (">", ">-", "|", "|-"):
        out = []
        pos = m.group(1).find(mm.group(0)) + len(mm.group(0))
        for l in m.group(1)[pos:].splitlines():
            if l.startswith((" ", "\t")):
                out.append(l.strip())
            elif l.strip():
                break
        v = " ".join(out)
    return v


# ---------------------------------------------------------------- 1. SIMILARITÉ
STOP = set("""utiliser quand l'utilisateur utilisateur parle demande veut cherche pour
avec dans les des une aucun sans est sont vers tout tous toute toutes leur leurs
n'utilise n'est jamais aussi comme afin cette faire fait plus depuis chaque être
alors avant après entre""".split())


def mots(s):
    return {w for w in re.findall(r"[a-zàâçéèêëîïôùûüœ0-9\-]{4,}", s.lower())
            if w not in STOP}


def jaccard(a, b):
    ma, mb = mots(a), mots(b)
    if not ma or not mb:
        return 0.0
    return len(ma & mb) / len(ma | mb)


# auto-test : le détecteur doit voir deux descriptions quasi identiques
assert jaccard("Utiliser quand l'utilisateur veut créer une campagne emailing ciblée",
               "Utiliser quand l'utilisateur veut créer une campagne emailing précise") > 0.5, \
    "auto-test SIMILARITÉ : le détecteur ne détecte pas un doublon évident"
assert jaccard("Utiliser quand l'utilisateur relève une température HACCP",
               "Utiliser quand l'utilisateur veut poster sur Instagram") < 0.5, \
    "auto-test SIMILARITÉ : le détecteur voit des doublons partout"

descs = []
for f in fichiers_suivis():
    if f.endswith("/SKILL.md") and "/skills/" in f:
        plugin = f.split("/")[0]
        d = description(lire(f))
        if d:
            descs.append((plugin, f, d))
for i in range(len(descs)):
    for j in range(i + 1, len(descs)):
        a, b = descs[i], descs[j]
        if a[0] == b[0] == "rapido-forge":
            continue  # gabarit d'exercices assumé
        s = jaccard(a[2], b[2])
        if s > 0.50:
            erreurs.append(f"SIMILARITÉ {s:.2f} : {a[1]} ≈ {b[1]}")

# ------------------------------------------------------------------- 2. SECRETS
MOTIFS_DETECTION_FUITES = [
    ("clé OpenAI/Stripe-like", re.compile(r"\b(?:sk|rk|pk)-[A-Za-z0-9]{20,}")),
    ("token GitHub", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}")),
    ("token Slack", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}")),
    ("clé AWS", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("clé privée PEM", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("affectation en dur", re.compile(
        r"(?i)\b(?:api[_-]?key|secret|password|token)\b\s*[:=]\s*['\"][A-Za-z0-9+/_\-]{16,}['\"]")),
]
# auto-test : chaque motif doit attraper sa fixture
_FIXTURES = [
    "sk-" + "a" * 24, "ghp_" + "b" * 36, "xoxb-1234567890-abc",
    "AKIA" + "C" * 16, "-----BEGIN RSA PRIVATE KEY-----",
    'api_key = "' + "d" * 20 + '"',
]
for (_, rx), fx in zip(MOTIFS_DETECTION_FUITES, _FIXTURES):
    assert rx.search(fx), f"auto-test SECRETS : motif inerte sur {fx[:20]}…"

BINAIRES = (".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".woff", ".ico")
for f in fichiers_suivis():
    if f.endswith(BINAIRES) or f == "scripts/controles-supplementaires.py":
        continue  # ce script porte les motifs et fixtures : exclu de son propre scan
    contenu = lire(f)
    for nom, rx in MOTIFS_DETECTION_FUITES:
        m = rx.search(contenu)
        if m:
            # Ne JAMAIS reproduire le contenu détecté : le journal CI est
            # public, l'écho d'un secret serait une fuite en soi (CodeQL
            # py/clear-text-logging-sensitive-data). Fichier + ligne suffisent.
            ligne = contenu.count("\n", 0, m.start()) + 1
            erreurs.append(f"SECRET ({nom}) : {f} ligne {ligne} — contenu "
                           "masqué, ouvrir le fichier pour vérifier")

# -------------------------------------------------------------------- 3. OUTILS
live_path = "docs/inventaires/foodeatup-tools-live.txt"
live = {l.strip() for l in lire(live_path).splitlines()
        if l.strip() and not l.startswith("#")}
if len(live) < 100:
    erreurs.append(f"OUTILS : liste live illisible ou suspecte ({live_path})")
    live = set()

RX_TOKEN = re.compile(r"`([a-z][a-z0-9_]{2,})`")
# Un token « en forme d'outil foodeatup » : préfixe d'action + underscore.
RX_FORME_OUTIL = re.compile(
    r"^(?:list|get|create|update|delete|add|upsert|check|record|validate|complete|"
    r"confirm|cancel|seat|open|close|launch|submit|toggle|apply|publish|import|"
    r"adjust|approve|reject|assign|moderate|reply|propose|remove|no|"
    r"lancer|enregistrer|deplacer|prospecter|recalculer|rechercher|ajouter|"
    r"appeler|schedule|send|set|log|search)_[a-z0-9_]+$")
# auto-test : un outil inventé doit être signalé, un vrai non
assert RX_FORME_OUTIL.match("delete_wheel_game"), "auto-test OUTILS : forme non reconnue"
# Les plugins foodeatup* déclarent aussi rapidocrm : leurs outils sont légitimes.
# Source unique : le CATALOGUE de tester-skills.py (chargé sans exécuter main()).
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location(
    "tester_skills", os.path.join(RACINE, "scripts", "tester-skills.py"))
_ts = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ts)
AUTRES_SERVEURS = set().union(*(v for k, v in _ts.CATALOGUE.items()
                                if k != "foodeatup"))
# Périmètres STRICTS par répertoire : les plugins foodeatup* sont découplés de
# RapidoCRM (FoodEatUp a ses propres outils CRM) — ils ne peuvent citer QUE des
# outils foodeatup. rapidocrm/ est contrôlé contre sa liste live + autres
# catalogues (il référence légitimement des skills d'autres serveurs).
PERIMETRES = [
    (("foodeatup/", "foodeatup-boucles/"), live,
     "outils foodeatup uniquement (plugin découplé de RapidoCRM)"),
    (("rapidocrm/",), _ts.CATALOGUE.get("rapidocrm", set()) | AUTRES_SERVEURS | live,
     f"liste live rapidocrm + catalogues"),
]
if live:
    for f in fichiers_suivis():
        if not f.endswith(".md") or f.endswith("CHANGELOG.md"):
            continue  # CHANGELOG : historique, peut citer des outils disparus
        perimetre = next(((autorise, motif) for prefixes, autorise, motif in PERIMETRES
                          if f.startswith(prefixes)), None)
        if not perimetre:
            continue
        autorise, motif = perimetre
        for tok in sorted(set(RX_TOKEN.findall(lire(f)))):
            if RX_FORME_OUTIL.match(tok) and tok not in autorise:
                erreurs.append(f"OUTILS : {f} cite `{tok}` — hors périmètre "
                               f"({motif})")
    # la liste du hook destructif ne doit contenir que des outils existants
    for l in lire("foodeatup-boucles/hooks/scripts/outils-destructifs.txt").splitlines():
        l = l.strip()
        if not l or l.startswith("#"):
            continue
        srv, _, outil = l.partition(":")
        if srv == "foodeatup" and outil not in live:
            erreurs.append(f"OUTILS : outils-destructifs.txt liste foodeatup:{outil}, "
                           "inexistant sur le serveur live")

# --------------------------------------------------------------------- 4. CARTO
carto = lire("docs/boucles-vs-outils.md")
if live and carto:
    cites = {t for t in RX_TOKEN.findall(carto) if t in live or RX_FORME_OUTIL.match(t)}
    manquants = sorted(live - cites)
    if manquants:
        erreurs.append(f"CARTO : docs/boucles-vs-outils.md ne couvre pas "
                       f"{len(manquants)} outil(s) live : {', '.join(manquants[:8])}…"
                       if len(manquants) > 8 else
                       f"CARTO : docs/boucles-vs-outils.md ne couvre pas : "
                       f"{', '.join(manquants)}")
elif not carto:
    erreurs.append("CARTO : docs/boucles-vs-outils.md absent")

# --------------------------------------------------------------------- 5. CARTE
carte = lire("foodeatup-boucles/reference/carte-marketplace.md")
plugins = sorted(d for d in os.listdir(".")
                 if os.path.isfile(os.path.join(d, ".claude-plugin", "plugin.json")))
if not carte:
    erreurs.append("CARTE : carte-marketplace.md absente — lancer "
                   "python3 scripts/generer-carte-boucles.py")
else:
    for p in plugins:
        if f"`{p}`" not in carte:
            erreurs.append(f"CARTE : plugin {p} absent de carte-marketplace.md — "
                           "relancer scripts/generer-carte-boucles.py")

# --------------------------------------------------------------- 6. MARKETPLACE
# Chaque entrée : name/source/description/version/category présents, source
# résout vers un dossier plugin, version synchrone avec plugin.json,
# catégorie dans la liste harmonisée (docs/POLITIQUE-VERSIONS.md).
CATEGORIES = {"restaurant", "ventes-crm", "contenu-marque", "rh-projets",
              "marketing-acquisition", "media-ia", "app-automatisation",
              "direction-finance", "incubation"}
try:
    market = json.load(open(".claude-plugin/marketplace.json", encoding="utf-8"))
except Exception as e:
    market = {}
    erreurs.append(f"MARKETPLACE : marketplace.json illisible ({e})")
for e in market.get("plugins", []):
    n = e.get("name", "?")
    for champ in ("name", "source", "description", "version", "category"):
        if not e.get(champ):
            erreurs.append(f"MARKETPLACE : entrée {n} sans champ `{champ}`")
    src = e.get("source", "")
    pj_path = os.path.join(src, ".claude-plugin", "plugin.json")
    if not (src.startswith("./") and os.path.isfile(pj_path)):
        erreurs.append(f"MARKETPLACE : source `{src}` de {n} ne résout pas "
                       "(chemin relatif attendu, distribution git — "
                       "docs/POLITIQUE-VERSIONS.md)")
        continue
    pj = json.load(open(pj_path, encoding="utf-8"))
    if e.get("version") != pj.get("version"):
        erreurs.append(f"MARKETPLACE : version de {n} divergente "
                       f"(marketplace {e.get('version')} ≠ plugin.json {pj.get('version')})")
    if e.get("category") and e["category"] not in CATEGORIES:
        erreurs.append(f"MARKETPLACE : catégorie `{e['category']}` de {n} hors "
                       "liste harmonisée")

# ---------------------------------------------------------------------- verdict
if erreurs:
    print(f"controles-supplementaires.py — {len(erreurs)} erreur(s) :")
    for e in erreurs:
        print(f"  [FAIL] {e}")
    sys.exit(1)
print(f"controles-supplementaires.py — OK ({len(descs)} descriptions, "
      f"{len(plugins)} plugins, {len(live)} outils live, auto-tests détecteurs passés)")
