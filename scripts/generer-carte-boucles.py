#!/usr/bin/env python3
"""Régénère foodeatup-boucles/reference/carte-marketplace.md depuis le dépôt réel.

Commande : python3 scripts/generer-carte-boucles.py
Stdlib uniquement. Utilisé par le skill `decouvrir-le-plugin` (P4.3) : la carte
est un fichier généré, jamais écrit de mémoire. À relancer après tout ajout ou
retrait de plugin (la CI signale un plugin absent de la carte).
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RACINE)
RX_FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)

# Domaine par plugin + 3 phrases déclencheuses types. Un plugin hors dico part
# en « autres » avec un avertissement : compléter le dico, pas la carte à la main.
DOMAINES = {
    "Restaurant (FoodEatUp)": {
        "plugins": ["foodeatup", "foodeatup-boucles", "foodeatup-iris"],
        "phrases": ["« fais le briefing du jour de mon restaurant »",
                    "« où en sont mes 8 boucles ? »",
                    "« détecte les incohérences entre ma com et mon stock »"],
    },
    "Ventes & CRM": {
        "plugins": ["rapidocrm", "rapido-relation-client", "rapido-gmaps"],
        "phrases": ["« fais ma revue de pipeline »",
                    "« relance les devis en attente »",
                    "« trouve-moi des prospects restaurateurs à Lyon »"],
    },
    "Contenu & réseaux sociaux": {
        "plugins": ["rapidocms", "rapido-copywriter", "rapido-canva",
                    "rapido-design", "rapido-prompteur"],
        "phrases": ["« programme mes posts de la semaine »",
                    "« écris la copy de ce lancement »",
                    "« décline ce visuel aux couleurs de ma marque »"],
    },
    "Publicité & acquisition": {
        "plugins": ["rapido-marketing", "rapido-meta-ads", "rapido-google-ads",
                    "rapido-tiktok-ads", "rapido-leadmagnet", "rapido-seo"],
        "phrases": ["« monte une campagne Meta sur mon audience CRM »",
                    "« construis-moi un lead magnet »",
                    "« audite le SEO de mon site »"],
    },
    "Vidéo & médias IA": {
        "plugins": ["rapido-video", "rapido-higgsfield", "rapido-elevenlabs"],
        "phrases": ["« fais une vidéo de 30 s pour ce plat »",
                    "« génère un packshot 4K de ce produit »",
                    "« double cette vidéo en anglais »"],
    },
    "Équipe & projets": {
        "plugins": ["rapidorh"],
        "phrases": ["« fais la tournée des dailies »",
                    "« crée le projet d'onboarding du nouveau »",
                    "« où en est le Kanban ? »"],
    },
    "Direction & finance": {
        "plugins": ["rapido-direction", "rapido-startup", "rapido-suite"],
        "phrases": ["« prépare mon comité de direction »",
                    "« où en est ma trésorerie ? »",
                    "« pilote la boîte : sense, plan, act »"],
    },
    "Sites & apps": {
        "plugins": ["rapido-lovable", "rapido-n8n"],
        "phrases": ["« construis un MVP multi-pages »",
                    "« automatise ce process dans n8n »",
                    "« branche mon app sur les données Rapido »"],
    },
    "Formation & incubation": {
        "plugins": ["rapido-forge"],
        "phrases": ["« démarre le bootcamp 5 jours »",
                    "« aide-moi à valider mon idée »",
                    "« passe-moi en mode mentor scale »"],
    },
}

plugins = sorted(d for d in os.listdir(".")
                 if os.path.isfile(os.path.join(d, ".claude-plugin", "plugin.json")))
attribues = {p for dom in DOMAINES.values() for p in dom["plugins"]}
orphelins = [p for p in plugins if p not in attribues]
fantomes = sorted(attribues - set(plugins))

infos = {}
for p in plugins:
    pj = json.load(open(os.path.join(p, ".claude-plugin", "plugin.json")))
    n_skills = 0
    sdir = os.path.join(p, "skills")
    if os.path.isdir(sdir):
        n_skills = sum(1 for d in os.listdir(sdir)
                       if os.path.isfile(os.path.join(sdir, d, "SKILL.md")))
    infos[p] = (pj.get("version", "?"), pj.get("description", ""), n_skills)

L = []
L.append("# Carte de la marketplace `rapido` — générée, ne pas éditer à la main\n")
L.append("> Régénérer avec : `python3 scripts/generer-carte-boucles.py` (depuis la")
L.append("> racine du dépôt de la marketplace). Source : les plugin.json réels.\n")
for dom, cfg in DOMAINES.items():
    presents = [p for p in cfg["plugins"] if p in infos]
    if not presents:
        continue
    L.append(f"## {dom}\n")
    L.append("| Plugin | Version | Skills | Description |")
    L.append("|---|---|---|---|")
    for p in presents:
        v, desc, ns = infos[p]
        d = desc.replace("|", "\\|")
        if len(d) > 140:
            d = d[:137] + "…"
        L.append(f"| `{p}` | {v} | {ns} | {d} |")
    L.append("\nPhrases qui déclenchent le bon skill :")
    for ph in cfg["phrases"]:
        L.append(f"- {ph}")
    L.append("")
if orphelins:
    L.append("## Autres (à classer dans scripts/generer-carte-boucles.py)\n")
    for p in orphelins:
        v, desc, ns = infos[p]
        L.append(f"- `{p}` {v} — {desc[:120]}")
    L.append("")

L.append("## Ce que la marketplace ne peut PAS faire (limites connues)\n")
L.append("- Créer/activer une **roue cadeaux** ou un **sondage** FoodEatUp : lecture")
L.append("  seule côté MCP, la création se fait en back-office")
L.append("  (docs/couverture-fidelite-jeux.md).")
L.append("- Encaisser, lancer une campagne, publier un site **sans confirmation")
L.append("  humaine** : les garde-fous PreToolUse l'empêchent volontairement.")
L.append("- Les paiements de la marketplace elle-même : il n'y a pas de rail de")
L.append("  paiement dans le système de plugins Claude Code.")
L.append("- Toute donnée non exposée par les serveurs MCP connectés : rien n'est")
L.append("  estimé à la place d'un outil manquant.\n")

os.makedirs("foodeatup-boucles/reference", exist_ok=True)
open("foodeatup-boucles/reference/carte-marketplace.md", "w",
     encoding="utf-8").write("\n".join(L) + "\n")
msg = f"carte-marketplace.md régénérée — {len(plugins)} plugins"
if orphelins:
    msg += f" ; NON CLASSÉS : {', '.join(orphelins)}"
if fantomes:
    msg += f" ; disparus du dépôt : {', '.join(fantomes)}"
print(msg)
sys.exit(1 if orphelins or fantomes else 0)
