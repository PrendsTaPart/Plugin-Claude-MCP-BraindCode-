#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_prompts_data.py — Moissonne les prompts du marketplace Rapido et produit
un export exploitable par un site (galerie de prompts).

Stdlib uniquement. Aucune donnée client, aucun secret : on ne lit que le dépôt.

SOURCES DE MOISSON
  1. SKILLS   : chaque */skills/*/SKILL.md des 25 plugins
                → phrases déclencheuses entre guillemets « … » du frontmatter
                  + un prompt synthétisé depuis la clause « Utiliser quand … veut … ».
  2. AGENTS   : chaque */agents/*.md
                → 3 prompts (diagnostic · action préparée · rapport) depuis la description.
  3. ROUTINES : reference/registre-routines.md (catalogue canonique)
                → 2 prompts par routine (lancer · consulter le dernier journal),
                  avec l'« Act maximum autorisé » en tag.

FUSION
  data/prompts-orchestrations.json (écrit à la main, même format) est fusionné s'il existe
  (orchestrations + sessions). Sinon on continue et on le signale dans le rapport.

SORTIE
  site-export/prompts.json         — l'export (métadonnées + liste `prompts`)
  site-export/RAPPORT-PROMPTS.md   — rapport (total par type, par MCP, par profil, écart vs 1000)

Ids stables = sha1(type|titre|prompt)[:12]. Dédoublonnage sur cet id. Schéma validé.
"""

import os
import re
import io
import sys
import json
import glob
import hashlib
import unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "site-export")
FUSION_FILE = os.path.join(ROOT, "data", "prompts-orchestrations.json")
REGISTRE = os.path.join(ROOT, "reference", "registre-routines.md")

CIBLE = 1000  # objectif d'entrées

# --- Détection d'autonomie (mots-clés — liste explicite, cf. spec) -----------
KW_DRAFT = ["brouillon", "prépare", "préparé", "préparer", "propose", "ébauche",
            "plan préparé", "à confirmer", "avant envoi", "avant publication"]
KW_WRITE = ["crée", "créer", "enregistre", "enregistrer", "planifie", "planifier",
            "publie", "publier", "envoie", "envoyer", "supprime", "supprimer",
            "met à jour", "mets à jour"]

# --- Acronymes à garder en capitales lors de l'humanisation ------------------
ACRONYMES = {
    "cms": "CMS", "crm": "CRM", "rh": "RH", "kpi": "KPI", "seo": "SEO", "sea": "SEA",
    "nps": "NPS", "ugc": "UGC", "pos": "POS", "haccp": "HACCP", "kds": "KDS",
    "tva": "TVA", "cfo": "CFO", "roi": "ROI", "b2b": "B2B", "ia": "IA", "sms": "SMS",
    "cta": "CTA", "aarrr": "AARRR", "codir": "CODIR", "tiktok": "TikTok",
    "linkedin": "LinkedIn", "n8n": "n8n", "gmaps": "GMaps", "kb": "KB",
    "meta": "Meta", "ads": "Ads", "faq": "FAQ", "url": "URL", "dso": "DSO",
    "ltv": "LTV", "cac": "CAC", "mrr": "MRR", "vs": "vs",
}

# --- Mapping plugin → profil -------------------------------------------------
def profil_of(plugin):
    if plugin == "foodeatup":
        return "restaurateur"
    if plugin in ("rapido-forge", "rapido-startup"):
        return "fondateur"
    return "tous"


def humanize(slug):
    """copy-linkedin → 'Copy LinkedIn' ; gestion-depenses → 'Gestion dépenses'."""
    mots = re.split(r"[-_]", slug)
    out = []
    for i, m in enumerate(mots):
        low = m.lower()
        if low in ACRONYMES:
            out.append(ACRONYMES[low])
        elif i == 0:
            out.append(m[:1].upper() + m[1:])
        else:
            out.append(m)
    return " ".join(out)


def slug_var(txt):
    """[marque/produit] → 'marque_produit' pour en faire {marque_produit}."""
    t = unicodedata.normalize("NFKD", txt)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower().strip()
    t = re.sub(r"[^a-z0-9]+", "_", t).strip("_")
    return t or "valeur"


def placeholders_to_vars(prompt):
    """Remplace les placeholders [xxx] par des variables {xxx}."""
    return re.sub(r"\[([^\[\]]+)\]", lambda m: "{" + slug_var(m.group(1)) + "}", prompt)


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    data = {}
    # name
    mn = re.search(r"^name:\s*(.+)$", fm_raw, re.M)
    if mn:
        data["name"] = mn.group(1).strip()
    # description : peut être multi-ligne (>- ou |) — on prend tout jusqu'à la
    # prochaine clé de 1er niveau (tools:/model:) ou la fin du frontmatter.
    md = re.search(r"description:\s*(.*?)(?=\n[a-zA-Z_]+:\s|\Z)", fm_raw, re.S)
    if md:
        desc = md.group(1)
        desc = re.sub(r"^\s*[>|]-?\s*", "", desc)
        desc = re.sub(r"\s+", " ", desc).strip()
        data["description"] = desc
    return data, body


def extract_quotes(txt):
    """Phrases entre guillemets français « … » (nettoyées)."""
    out = []
    for q in re.findall(r"«\s*(.+?)\s*»", txt, re.S):
        q = re.sub(r"\s+", " ", q).strip(" .")
        if q:
            out.append(q)
    return out


def is_trigger(q):
    """Filtre : garde les phrases utilisateur, écarte le bruit (chemins, labels)."""
    if len(q) < 6 or len(q) > 140:
        return False
    if "`" in q or ".md" in q or "${" in q:
        return False
    if q.isupper():           # labels type GAGNANT, NEUTRE
        return False
    if q.count("/") >= 2:     # chemins
        return False
    return True


_TAIL = {"et", "ou", "de", "des", "du", "la", "le", "les", "à", "au", "aux",
         "d", "l", "un", "une", "en", "sur", "pour", "par", "avec", "dans"}


def tidy_tail(s):
    """Retire les conjonctions/prépositions orphelines en fin de phrase tronquée."""
    s = s.strip(" ,.;:—-")
    words = s.split()
    while words and words[-1].lower().strip("'’") in _TAIL:
        words.pop()
    return " ".join(words).strip()


def autonomie_of(text):
    low = text.lower()
    if any(k in low for k in KW_DRAFT):
        return 1
    if any(k in low for k in KW_WRITE):
        return 2
    return 0


def mk_id(typ, titre, prompt):
    h = hashlib.sha1(f"{typ}|{titre}|{prompt}".encode("utf-8")).hexdigest()
    return h[:12]


def add_entry(entries, seen, typ, titre, prompt, mcps, autonomie, profil,
              source, act_max=None):
    prompt = placeholders_to_vars(prompt.strip())
    prompt = re.sub(r"\s+", " ", prompt).strip()
    if not prompt:
        return
    eid = mk_id(typ, titre, prompt)
    if eid in seen:
        return
    seen.add(eid)
    e = {
        "id": eid,
        "type": typ,
        "titre": titre,
        "prompt": prompt,
        "mcps": mcps,
        "autonomie": autonomie,
        "profil": profil,
        "source": source,
    }
    if act_max is not None:
        e["act_max"] = act_max
    entries.append(e)


# ---------------------------------------------------------------------------
# 1. MOISSON SKILLS
# ---------------------------------------------------------------------------
def harvest_skills(mcp_by_plugin, entries, seen, stats):
    for f in sorted(glob.glob(os.path.join(ROOT, "*", "skills", "*", "SKILL.md"))):
        plugin = f[len(ROOT) + 1:].split(os.sep)[0]
        if plugin not in mcp_by_plugin:
            continue
        text = open(f, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        name = fm.get("name") or os.path.basename(os.path.dirname(f))
        desc = fm.get("description", "")
        titre = humanize(name)
        mcps = mcp_by_plugin[plugin]
        profil = profil_of(plugin)
        auto = autonomie_of(desc + " " + body[:600])

        # (a) phrases déclencheuses entre guillemets du frontmatter
        quotes = [q for q in extract_quotes(desc) if is_trigger(q)]
        for q in quotes:
            add_entry(entries, seen, "skill", titre, q, mcps, auto, profil, plugin)
            stats["skill_quotes"] += 1

        # (b) prompt synthétisé depuis « Utiliser quand … veut … »
        m = re.search(r"[Uu]tiliser\s+quand[^.]*?veut\s+(.+?)(?:[—.\-]| «|«|$)", desc)
        besoin = None
        if m:
            besoin = tidy_tail(m.group(1))
        if besoin and 6 <= len(besoin) <= 120:
            synth = besoin[0].upper() + besoin[1:]
            if not synth.endswith((".", "?", "!")):
                synth += "."
            add_entry(entries, seen, "skill", titre, synth, mcps, auto, profil, plugin)
            stats["skill_besoin"] += 1
        elif not quotes:
            # Aucun guillemet ET pas de clause « veut » exploitable :
            # au moins un prompt générique pour que le skill soit représenté.
            fallback = f"{titre} : {desc.split('.')[0].strip()}." if desc else titre
            add_entry(entries, seen, "skill", titre, fallback, mcps, auto, profil, plugin)
            stats["skill_fallback"] += 1


# ---------------------------------------------------------------------------
# 2. MOISSON AGENTS
# ---------------------------------------------------------------------------
def harvest_agents(mcp_by_plugin, entries, seen, stats):
    for f in sorted(glob.glob(os.path.join(ROOT, "*", "agents", "*.md"))):
        plugin = f[len(ROOT) + 1:].split(os.sep)[0]
        if plugin not in mcp_by_plugin:
            continue
        text = open(f, encoding="utf-8").read()
        fm, _ = parse_frontmatter(text)
        name = fm.get("name") or os.path.splitext(os.path.basename(f))[0]
        desc = fm.get("description", "")
        titre = humanize(name)
        mcps = mcp_by_plugin[plugin]
        profil = profil_of(plugin)

        # rôle = avant le premier point ; sujet = après « Utiliser pour … »
        role = desc.split(".")[0].strip() if desc else titre
        msuj = re.search(r"[Uu]tiliser\s+pour\s+(.+?)(?:[—;.]|\bou\s+quand\b|«|$)", desc)
        sujet = (msuj.group(1) if msuj else role).lower()
        if len(sujet) > 110:
            sujet = sujet[:110].rsplit(" ", 1)[0]
        sujet = tidy_tail(sujet) or role.lower()

        p_diag = f"En tant que {role.lower()}, fais-moi un diagnostic sur {sujet}."
        p_act = f"En tant que {role.lower()}, prépare une action sur {sujet} — je validerai avant tout envoi."
        p_rap = f"En tant que {role.lower()}, rédige-moi un rapport de synthèse sur {sujet}."

        add_entry(entries, seen, "agent", titre, p_diag, mcps, 0, profil, plugin)
        add_entry(entries, seen, "agent", titre, p_act, mcps, 1, profil, plugin)
        add_entry(entries, seen, "agent", titre, p_rap, mcps, 0, profil, plugin)
        stats["agents"] += 1


# ---------------------------------------------------------------------------
# 3. MOISSON ROUTINES
# ---------------------------------------------------------------------------
# Plugin propriétaire (pour en déduire les MCP et le profil) par préfixe.
OWNER_BY_PREFIX = {
    "FIN": "rapido-startup", "STARTUP": "rapido-startup", "GROWTH": "rapido-startup",
    "VIDEO": "rapido-startup", "MKT": "rapido-marketing", "VENTE": "rapidocrm",
    "OPS": "rapido-n8n", "SEO": "rapido-seo", "SEA": "rapido-google-ads",
    "TIKTOK": "rapido-tiktok-ads", "RC": "rapido-relation-client",
    "GMAPS": "rapido-gmaps",
}


def harvest_routines(mcp_by_plugin, entries, seen, stats):
    if not os.path.exists(REGISTRE):
        return
    text = open(REGISTRE, encoding="utf-8").read()
    # Découpe en blocs de routine : chaque `### ID ...` jusqu'au prochain `###` ou `---`.
    blocs = re.split(r"\n### ", text)
    for bloc in blocs[1:]:
        # Ne garder que le catalogue (avant la section « Registre des KPIs »)
        if "Registre des KPIs" in bloc:
            bloc = bloc.split("Registre des KPIs")[0]
        header = bloc.splitlines()[0]
        rid = header.split("*")[0].strip()
        rid = re.sub(r"\s+", " ", rid).strip()
        if not rid or " " in rid.strip() and not re.match(r"^[A-Z]", rid):
            continue
        # id propre (avant parenthèse d'alias / « (si compte actif) »)
        rid_clean = re.split(r"\s*\(", rid)[0].strip()
        if not re.match(r"^[A-Z][A-Z\-]+", rid_clean):
            continue
        prefix = rid_clean.split("-")[0]
        owner = OWNER_BY_PREFIX.get(prefix)
        if not owner:
            continue
        mcps = mcp_by_plugin.get(owner, [])
        profil = profil_of(owner)

        # « Act maximum autorisé » ← ligne « Autonomie : … »
        mact = re.search(r"\*\*Autonomie\*\*\s*:\s*(.+)", bloc)
        act_max = None
        if mact:
            act_max = re.sub(r"\s+", " ", mact.group(1)).strip(" .")
            act_max = re.sub(r"\*\*", "", act_max)
            if len(act_max) > 160:
                act_max = act_max[:160].rsplit(" ", 1)[0] + "…"

        titre = f"Routine {rid_clean}"
        p_lance = f"Lance la routine {rid_clean}."
        p_journal = f"Montre-moi le dernier journal de la routine {rid_clean}."
        # autonomie numérique déduite du texte d'autonomie
        auto = 0
        if act_max:
            la = act_max.lower()
            if "niveau 2" in la:
                auto = 2
            elif "niveau 1" in la:
                auto = 1
            elif "niveau 0" in la or "alerte" in la:
                auto = 0
        add_entry(entries, seen, "routine", titre, p_lance, mcps, auto, profil,
                  owner, act_max=act_max)
        add_entry(entries, seen, "routine", titre, p_journal, mcps, 0, profil,
                  owner, act_max=act_max)
        stats["routines"] += 1


# ---------------------------------------------------------------------------
# 4. FUSION
# ---------------------------------------------------------------------------
REQUIRED = ("id", "type", "titre", "prompt", "mcps", "autonomie", "profil")


COLLECTIONS_DIR = os.path.join(ROOT, "data", "prompts-collections")


def _items_from(path):
    """Charge une source de fusion (liste nue, {prompts:[…]} ou {entries:[…]})."""
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict):
        return data.get("prompts") or data.get("entries") or []
    if isinstance(data, list):
        return data
    return []


def load_fusion():
    """Retourne [(source_label, [items], state), …] pour toutes les sources écrites main :
    data/prompts-orchestrations.json + data/prompts-collections/*.json."""
    sources = []
    # Orchestrations + sessions (§4)
    if os.path.exists(FUSION_FILE):
        try:
            sources.append(("orchestrations-main", _items_from(FUSION_FILE), "chargé"))
        except Exception as e:
            sources.append(("orchestrations-main", [], f"illisible ({e})"))
    else:
        sources.append(("orchestrations-main", [], "absent"))
    # Collections thématiques
    for path in sorted(glob.glob(os.path.join(COLLECTIONS_DIR, "*.json"))):
        label = "collection:" + os.path.splitext(os.path.basename(path))[0]
        try:
            sources.append((label, _items_from(path), "chargé"))
        except Exception as e:
            sources.append((label, [], f"illisible ({e})"))
    return sources


def validate(entry):
    for k in REQUIRED:
        if k not in entry:
            return False, f"clé manquante: {k}"
    if not isinstance(entry["mcps"], list):
        return False, "mcps n'est pas une liste"
    if not isinstance(entry["autonomie"], int) or entry["autonomie"] not in (0, 1, 2, 3):
        return False, "autonomie invalide"
    if not isinstance(entry["prompt"], str) or not entry["prompt"].strip():
        return False, "prompt vide"
    return True, ""


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    # MCP requis par plugin
    mcp_by_plugin = {}
    for pj in sorted(glob.glob(os.path.join(ROOT, "*", ".claude-plugin", "plugin.json"))):
        d = json.load(open(pj, encoding="utf-8"))
        mcp_by_plugin[d["name"]] = d.get("mcp_requis", [])

    entries, seen = [], set()
    stats = Counter()

    harvest_skills(mcp_by_plugin, entries, seen, stats)
    harvest_agents(mcp_by_plugin, entries, seen, stats)
    harvest_routines(mcp_by_plugin, entries, seen, stats)

    moisson_total = len(entries)

    # Fusion — sources écrites main (orchestrations + collections)
    fusion_sources = load_fusion()
    fused = 0
    fusion_detail = []          # (label, state, ajoutées)
    for label, items, state in fusion_sources:
        added = 0
        for it in items:
            ok, _ = validate(it)
            if not ok:
                continue
            eid = it["id"]
            if eid in seen:
                continue
            seen.add(eid)
            it.setdefault("source", label)
            entries.append(it)
            added += 1
            fused += 1
        fusion_detail.append((label, state, added))

    # Validation finale du schéma
    valid, invalid = [], []
    for e in entries:
        ok, why = validate(e)
        (valid if ok else invalid).append((e, why))
    entries = [e for e, _ in valid]

    # --- Rapport : agrégats ---
    by_type = Counter(e["type"] for e in entries)
    by_profil = Counter(e["profil"] for e in entries)
    by_mcp = Counter()
    for e in entries:
        for m in e["mcps"]:
            by_mcp[m] += 1
    by_auto = Counter(e["autonomie"] for e in entries)

    total = len(entries)

    # --- Écrire l'export ---
    os.makedirs(OUT_DIR, exist_ok=True)
    export = {
        "version": 1,
        "total": total,
        "cible": CIBLE,
        "par_type": dict(by_type),
        "par_profil": dict(by_profil),
        "prompts": entries,
    }
    out_json = os.path.join(OUT_DIR, "prompts.json")
    with io.open(out_json, "w", encoding="utf-8") as fh:
        json.dump(export, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    # --- Écrire le rapport Markdown ---
    lignes = []
    lignes.append("# Rapport — export marketplace de prompts")
    lignes.append("")
    lignes.append(f"**Total : {total} entrées** (cible : {CIBLE}).")
    ecart = CIBLE - total
    if ecart > 0:
        lignes.append(f"> ⚠️ **{ecart} sous la cible.** Voir « Ce qui manque » ci-dessous — "
                      "aucune entrée n'a été gonflée artificiellement.")
    else:
        lignes.append("> ✅ Cible atteinte.")
    lignes.append("")
    lignes.append("## Par type")
    lignes.append("")
    lignes.append("| Type | Entrées |")
    lignes.append("|---|---|")
    for t, n in by_type.most_common():
        lignes.append(f"| {t} | {n} |")
    lignes.append("")
    lignes.append("## Par profil")
    lignes.append("")
    lignes.append("| Profil | Entrées |")
    lignes.append("|---|---|")
    for p, n in by_profil.most_common():
        lignes.append(f"| {p} | {n} |")
    lignes.append("")
    lignes.append("## Par niveau d'autonomie")
    lignes.append("")
    lignes.append("| Niveau | Entrées |")
    lignes.append("|---|---|")
    for a in sorted(by_auto):
        lignes.append(f"| {a} | {by_auto[a]} |")
    lignes.append("")
    lignes.append("## Par MCP requis")
    lignes.append("")
    lignes.append("| MCP | Entrées citant ce MCP |")
    lignes.append("|---|---|")
    for m, n in by_mcp.most_common():
        lignes.append(f"| {m} | {n} |")
    lignes.append("")
    lignes.append("## Détail de la moisson")
    lignes.append("")
    lignes.append(f"- Skills — phrases entre guillemets : **{stats['skill_quotes']}**")
    lignes.append(f"- Skills — prompt « besoin » synthétisé : **{stats['skill_besoin']}**")
    lignes.append(f"- Skills — repli générique (ni guillemet ni clause) : **{stats['skill_fallback']}**")
    lignes.append(f"- Agents moissonnés (×3 prompts) : **{stats['agents']}**")
    lignes.append(f"- Routines moissonnées (×2 prompts) : **{stats['routines']}**")
    lignes.append(f"- **Fusion sources écrites main** → {fused} entrée(s) ajoutée(s) :")
    for label, state, added in fusion_detail:
        lignes.append(f"    - `{label}` : **{state}** → {added}")
    if invalid:
        lignes.append(f"- Entrées écartées à la validation du schéma : **{len(invalid)}**")
    lignes.append("")
    if ecart > 0:
        lignes.append("## Ce qui manque pour atteindre 1000 (à produire côté source, pas à gonfler)")
        lignes.append("")
        manque = []
        orch = [s for (lbl, s, _) in fusion_detail if lbl == "orchestrations-main"]
        if orch and orch[0] == "absent":
            manque.append(
                "- **`data/prompts-orchestrations.json` non fourni.** C'est la brique "
                "« orchestrations + sessions » écrite à la main (§4 de la mission). "
                "Elle apportera un complément une fois rédigée : scénarios "
                "multi-skills, playbooks de session, parcours guidés par profil.")
        collections_fournies = [lbl for (lbl, s, _) in fusion_detail
                                if lbl.startswith("collection:") and s == "chargé"]
        manque.append(
            "- **Collections restantes** : "
            f"{len(collections_fournies)} collection(s) fournie(s) "
            f"({', '.join(l.split(':', 1)[1] for l in collections_fournies) or '—'}). "
            "Les 3 autres annoncées (routines, boucles, sessions-loop) restent à "
            "déposer dans `data/prompts-collections/` pour compléter les 139 attendues.")
        manque.append(
            "- **Skills sans phrase déclencheuse explicite** : sur les 385 skills, "
            f"seuls {stats['skill_quotes']} déclencheurs « … » ont été trouvés dans les "
            "frontmatters. Ajouter 2–3 exemples de formulation utilisateur « … » dans "
            "le `description` des skills qui n'en ont pas multiplierait la moisson.")
        manque.append(
            "- **Variantes par profil** : chaque prompt pourrait être décliné "
            "restaurateur / fondateur / marketeur (×2–3) une fois les KB de profil "
            "définies — non fait ici car ce serait une duplication mécanique, pas du contenu réel.")
        manque.append(
            "- **Orchestrations inter-plugins** : les enchaînements documentés "
            "(routines → skills → agents) peuvent devenir des prompts « parcours », "
            "à écrire explicitement dans le fichier de fusion.")
        lignes.extend(manque)
        lignes.append("")
    rapport = os.path.join(OUT_DIR, "RAPPORT-PROMPTS.md")
    with io.open(rapport, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lignes) + "\n")

    # --- Sortie console ---
    print("=" * 60)
    print(f"EXPORT PROMPTS — {total} entrées (cible {CIBLE})")
    print("=" * 60)
    print("Par type   :", dict(by_type))
    print("Par profil :", dict(by_profil))
    print("Par auto   :", dict(sorted(by_auto.items())))
    print("Moisson    : quotes=%d besoin=%d fallback=%d agents=%d routines=%d"
          % (stats['skill_quotes'], stats['skill_besoin'], stats['skill_fallback'],
             stats['agents'], stats['routines']))
    print("Fusion     :", fused, "ajout(s) —",
          ", ".join(f"{lbl}:{added}" for lbl, _, added in fusion_detail))
    if invalid:
        print("Écartées   :", len(invalid))
    print("→", out_json)
    print("→", rapport)
    if ecart > 0:
        print(f"⚠️  {ecart} sous la cible — voir « Ce qui manque » dans le rapport.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
