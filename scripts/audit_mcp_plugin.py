#!/usr/bin/env python3
"""Harnais d'audit MCP ↔ plugin — croise les outils réellement exposés par un
serveur MCP Rapido avec ceux que les skills/agents/hooks du plugin citent.

Entrées :
  - `serveur`  : foodeatup | rapidocrm | rapidocms | rapidorh
  - `plugin`   : chemin du plugin correspondant (ex. ./foodeatup)

Le script NE DEVINE RIEN sur le serveur : il consomme un inventaire figé
`docs/inventaires/{serveur}-tools.json` (généré par introspection du MCP connecté
— voir docs/audits/METHODE.md). Contrat du JSON :
  { "server": "...", "date": "YYYY-MM-DD", "source": "...",
    "tools": [ {"name": "...", "description": "...",
                "params_required": [...], "params_optional": [...]} ] }

Sorties (idempotentes, datées, comparables d'un run à l'autre) :
  docs/audits/AUDIT-{serveur}-{date}.md
    - OUTILS ORPHELINS   : exposés, cités par aucun skill (valeur dormante), par famille
    - RÉFÉRENCES MORTES  : cités par les skills, absents du serveur (drift, PRIORITÉ 1)
    - COUVERTURE         : skill × outils utilisés + % d'outils serveur exploités
    - DELTA PARAMÈTRES   : params requis apparus/disparus depuis l'inventaire précédent

Usage :
  python3 scripts/audit_mcp_plugin.py <serveur> <plugin> [--date YYYY-MM-DD]
                                      [--prev docs/inventaires/xxx.json]

Stdlib uniquement.
"""
import json
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Préfixe mcp__<Prefixe>__ tel qu'exposé côté client (pour capter les citations préfixées).
SERVER_PREFIX = {
    "foodeatup": "Foodeatup",
    "rapidocrm": "RapidoCRM",
    "rapidocms": "RapidoCMS",
    "rapidorh": "RapidoRh",
}

# Un identifiant d'outil = snake_case (au moins un underscore), minuscule.
RE_BACKTICK = re.compile(r"`([a-z][a-z0-9]*(?:_[a-z0-9]+)+)`")
RE_PREFIXED = re.compile(r"mcp__[A-Za-z0-9]+__([a-z0-9_]+)")

# Verbes d'action réels : un token n'est une « référence morte » suspecte que s'il
# commence par l'un d'eux (sinon c'est probablement un paramètre ou un champ).
ACTION_VERBS = {
    "create", "list", "get", "update", "delete", "add", "adjust", "approve",
    "assign", "cancel", "checkin", "confirm", "record", "reject", "seat",
    "import", "search", "edit", "remove", "send", "schedule", "set", "toggle",
    "apply", "publish", "open", "close", "moderate", "reply", "enregistrer",
    "deplacer", "lancer", "recalculer", "rechercher", "prospecter", "close",
}


def load_inventory(server):
    path = os.path.join(ROOT, "docs", "inventaires", f"{server}-tools.json")
    if not os.path.exists(path):
        sys.stderr.write(
            f"ERREUR : inventaire absent : {path}\n"
            "Générer d'abord le JSON par introspection du MCP (voir METHODE.md).\n"
        )
        sys.exit(2)
    data = json.load(open(path, encoding="utf-8"))
    tools = {t["name"]: t for t in data.get("tools", [])}
    return data, tools


def family_of(name):
    """Famille fonctionnelle déduite du nom (entité après le verbe)."""
    segs = name.split("_")
    verbs = {
        "create", "list", "get", "update", "delete", "add", "adjust", "approve",
        "assign", "cancel", "checkin", "confirm", "record", "reject", "seat",
        "import", "no", "search", "set", "toggle", "apply", "publish", "open",
        "close", "moderate", "reply", "check", "send", "schedule", "remove",
        "edit", "upsert", "validate", "enregistrer", "deplacer", "lancer",
        "recalculer", "rechercher", "prospecter", "log",
    }
    ent = segs[1] if segs[0] in verbs and len(segs) > 1 else segs[0]
    # normalisation légère du pluriel (sans casser les mots courts : pos, tva…)
    if ent.endswith("ies"):
        ent = ent[:-3] + "y"
    elif ent.endswith("s") and not ent.endswith("ss") and len(ent) > 4:
        ent = ent[:-1]
    return ent


def load_all_inventories(current_server):
    """{outil: serveur} pour tous les inventaires connus SAUF le serveur audité."""
    m = {}
    for p in glob.glob(os.path.join(ROOT, "docs", "inventaires", "*-tools.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        srv = d.get("server", os.path.basename(p).replace("-tools.json", ""))
        if srv == current_server:
            continue
        for t in d.get("tools", []):
            m.setdefault(t["name"], srv)
    return m


def plugin_secondary_servers(plugin_dir, current_server):
    """Serveurs déclarés dans le .mcp.json du plugin, hors serveur audité."""
    mj = os.path.join(plugin_dir, ".mcp.json")
    try:
        d = json.load(open(mj, encoding="utf-8"))
        srv = list((d.get("mcpServers") or {}).keys())
    except Exception:
        srv = []
    return [s for s in srv if s.lower() != current_server.lower()]


def scan_plugin(plugin_dir, prefix):
    """Retourne {citation: [fichiers]} pour chaque identifiant d'outil cité."""
    cites = {}
    globs = [
        os.path.join(plugin_dir, "skills", "**", "*.md"),
        os.path.join(plugin_dir, "agents", "*.md"),
        os.path.join(plugin_dir, "hooks", "**", "*"),
        os.path.join(plugin_dir, "scripts", "**", "*"),
    ]
    files = []
    for g in globs:
        files += [f for f in glob.glob(g, recursive=True) if os.path.isfile(f)]
    for f in files:
        try:
            txt = open(f, encoding="utf-8", errors="ignore").read()
        except Exception:
            continue
        toks = set(RE_BACKTICK.findall(txt))
        for m in RE_PREFIXED.findall(txt):
            toks.add(m)
        rel = os.path.relpath(f, ROOT)
        for t in toks:
            cites.setdefault(t, set()).add(rel)
    return cites


def skill_coverage(plugin_dir, server_names):
    """Pour chaque skill : les outils serveur qu'il cite."""
    cov = {}
    for sk in sorted(glob.glob(os.path.join(plugin_dir, "skills", "*", "SKILL.md"))):
        name = os.path.basename(os.path.dirname(sk))
        txt = open(sk, encoding="utf-8", errors="ignore").read()
        toks = set(RE_BACKTICK.findall(txt)) | set(RE_PREFIXED.findall(txt))
        used = sorted(toks & server_names)
        cov[name] = used
    return cov


def param_delta(cur_tools, prev_path):
    if not prev_path or not os.path.exists(prev_path):
        return None
    prev = {t["name"]: t for t in json.load(open(prev_path, encoding="utf-8")).get("tools", [])}
    rows = []
    for name, t in cur_tools.items():
        if name not in prev:
            continue
        cur_req = set(t.get("params_required", []))
        old_req = set(prev[name].get("params_required", []))
        apparus = sorted(cur_req - old_req)
        disparus = sorted(old_req - cur_req)
        if apparus or disparus:
            rows.append((name, apparus, disparus))
    return rows


def build_report(server, date, inv_data, tools, cites, coverage, prev_path,
                 other_inv, secondary_srv):
    names = set(tools)
    used = {c for c in cites if c in names}
    orphans = sorted(names - used)
    # Citations hors serveur audité, classées :
    #  - cross-serveur : appartiennent à un autre inventaire connu (légitime)
    #  - mortes        : verbe d'action réel, dans aucun inventaire (drift probable)
    #  - (le reste = paramètres/champs, ignoré)
    cross = {}
    dead = []
    for c in cites:
        if c in names:
            continue
        if c in other_inv:
            cross.setdefault(other_inv[c], []).append(c)
        elif c.split("_")[0] in ACTION_VERBS:
            dead.append(c)
    dead = sorted(dead)
    delta = param_delta(tools, prev_path)

    L = []
    L.append(f"# Audit MCP ↔ plugin — {server} — {date}")
    L.append("")
    L.append(f"- Inventaire serveur : {len(names)} outils "
             f"(`docs/inventaires/{server}-tools.json`, source : "
             f"{inv_data.get('source', 'introspection MCP')}).")
    pct = round(100 * len(used) / len(names)) if names else 0
    L.append(f"- Couverture : **{len(used)}/{len(names)} outils exploités ({pct} %)** "
             f"par les skills du plugin.")
    L.append(f"- Orphelins : **{len(orphans)}** · Références mortes suspectes : "
             f"**{len(dead)}**.")
    L.append("")

    L.append("## 1. Références mortes (PRIORITÉ 1 — drift, bug silencieux)")
    L.append("")
    sans_inv = [s for s in secondary_srv
                if s not in {v for v in other_inv.values()}]
    if dead:
        note = ("Identifiants à **verbe d'action**, cités par le plugin mais absents de "
                "**tout** inventaire connu → drift probable à corriger.")
        if sans_inv:
            note += (f" ⚠️ Serveurs secondaires déclarés sans inventaire encore construit : "
                     f"**{', '.join(sans_inv)}** — un identifiant ci-dessous peut en venir ; "
                     f"confirmer en auditant ces serveurs.")
        L.append(note)
        L.append("")
        L.append("| Identifiant cité | Fichiers |")
        L.append("|---|---|")
        for d in dead:
            fichiers = ", ".join(sorted(cites[d])[:4])
            L.append(f"| `{d}` | {fichiers} |")
    else:
        L.append("_Aucune._ Tout identifiant à verbe d'action cité existe côté serveur "
                 "ou est attribué à un autre serveur connu (voir ci-dessous).")
    L.append("")
    if cross:
        L.append("**Citations cross-serveur** (légitimes — le plugin appelle aussi d'autres "
                 "serveurs déclarés dans son `.mcp.json`) :")
        L.append("")
        L.append("| Serveur | Outils cités |")
        L.append("|---|---|")
        for srv in sorted(cross):
            outs = ", ".join(f"`{o}`" for o in sorted(set(cross[srv])))
            L.append(f"| `{srv}` | {outs} |")
        L.append("")

    L.append("## 2. Outils orphelins (valeur dormante — exposés, cités par aucun skill)")
    L.append("")
    if orphans:
        fam = {}
        for o in orphans:
            fam.setdefault(family_of(o), []).append(o)
        L.append(f"{len(orphans)} outils, groupés par famille fonctionnelle :")
        L.append("")
        for f in sorted(fam):
            L.append(f"### {f} ({len(fam[f])})")
            L.append("")
            L.append("| Outil | Description |")
            L.append("|---|---|")
            for o in sorted(fam[f]):
                desc = (tools[o].get("description") or "").replace("\n", " ").strip()
                if len(desc) > 90:
                    desc = desc[:89] + "…"
                L.append(f"| `{o}` | {desc} |")
            L.append("")
    else:
        L.append("_Aucun._ Tous les outils du serveur sont exploités.")
        L.append("")

    L.append("## 3. Couverture par skill")
    L.append("")
    L.append("| Skill | Outils serveur cités |")
    L.append("|---|---|")
    for sk in sorted(coverage):
        outes = coverage[sk]
        cell = ", ".join(f"`{o}`" for o in outes) if outes else "—"
        L.append(f"| `{sk}` | {cell} |")
    L.append("")

    L.append("## 4. Delta paramètres (vs inventaire précédent)")
    L.append("")
    if delta is None:
        L.append("_Premier inventaire ou aucun précédent fourni_ — pas de comparaison "
                 "possible. Les prochains runs compareront les `params_required`.")
    elif not delta:
        L.append("_Aucun changement_ de paramètres requis sur les outils communs.")
    else:
        L.append("| Outil | Params requis apparus | Params requis disparus |")
        L.append("|---|---|---|")
        for name, ap, di in delta:
            L.append(f"| `{name}` | {', '.join(ap) or '—'} | {', '.join(di) or '—'} |")
    L.append("")
    return "\n".join(L)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = sys.argv[1:]
    if len(args) < 2:
        sys.stderr.write("Usage : audit_mcp_plugin.py <serveur> <plugin> "
                         "[--date YYYY-MM-DD] [--prev chemin.json]\n")
        return 2
    server, plugin = args[0], args[1]
    plugin_dir = os.path.join(ROOT, plugin.lstrip("./"))
    if server not in SERVER_PREFIX:
        sys.stderr.write(f"Serveur inconnu : {server} (attendu : {list(SERVER_PREFIX)})\n")
        return 2

    date = None
    prev = None
    for i, o in enumerate(opts):
        if o == "--date" and i + 1 < len(opts):
            date = opts[i + 1]
        if o == "--prev" and i + 1 < len(opts):
            prev = opts[i + 1]

    inv_data, tools = load_inventory(server)
    date = date or inv_data.get("date", "sans-date")
    cites = scan_plugin(plugin_dir, SERVER_PREFIX[server])
    coverage = skill_coverage(plugin_dir, set(tools))
    other_inv = load_all_inventories(server)
    secondary = plugin_secondary_servers(plugin_dir, server)
    report = build_report(server, date, inv_data, tools, cites, coverage, prev,
                          other_inv, secondary)

    outdir = os.path.join(ROOT, "docs", "audits")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, f"AUDIT-{server}-{date}.md")
    open(outpath, "w", encoding="utf-8").write(report)
    print(f"Rapport écrit : {os.path.relpath(outpath, ROOT)}")
    names = set(tools)
    used = {c for c in cites if c in names}
    print(f"  {len(names)} outils serveur · {len(used)} exploités · "
          f"{len(names) - len(used)} orphelins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
