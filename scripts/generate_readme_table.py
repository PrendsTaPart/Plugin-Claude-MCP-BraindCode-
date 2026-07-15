#!/usr/bin/env python3
"""Génère la table des plugins du README racine depuis les plugin.json réels.

- Source de vérité : `.claude-plugin/marketplace.json` (ordre) + chaque
  `<plugin>/.claude-plugin/plugin.json` (nom, version, description, mcp_requis)
  + comptage réel des dossiers (`skills/*/SKILL.md`, `agents/*.md`).
- La clé `mcp_requis` est lue dans le plugin.json ; si absente, elle est
  **déduite** des serveurs déclarés dans `<plugin>/.mcp.json` (mcpServers) et
  **écrite** dans le plugin.json (migration idempotente).
- Réécrit UNIQUEMENT la zone entre les marqueurs
  `<!-- TABLE-PLUGINS:START -->` et `<!-- TABLE-PLUGINS:END -->` du README.
- Stdlib uniquement. Idempotent : relancé sans changement de données, aucun diff.

Usage : python3 scripts/generate_readme_table.py [--check]
  --check : ne réécrit rien, sort en erreur si le README n'est pas à jour (CI).
"""
import json
import os
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
MARKETPLACE = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
START = "<!-- TABLE-PLUGINS:START -->"
END = "<!-- TABLE-PLUGINS:END -->"


def plugin_dirs_in_order():
    """Ordre du marketplace ; repli sur l'ordre alphabétique du disque."""
    order = []
    try:
        data = json.load(open(MARKETPLACE, encoding="utf-8"))
        plugins = data["plugins"] if isinstance(data, dict) else data
        for p in plugins:
            src = (p.get("source") or "").lstrip("./")
            if src:
                order.append(src)
    except Exception:
        pass
    if not order:
        order = sorted(
            os.path.dirname(os.path.dirname(p))
            for p in glob.glob(os.path.join(ROOT, "*", ".claude-plugin", "plugin.json"))
        )
    return order


def derive_mcp_requis(plugin_dir):
    """Serveurs déclarés dans .mcp.json (déduction depuis les besoins des skills)."""
    mj = os.path.join(ROOT, plugin_dir, ".mcp.json")
    try:
        d = json.load(open(mj, encoding="utf-8"))
        return list((d.get("mcpServers") or {}).keys())
    except Exception:
        return []


def ensure_mcp_requis(plugin_dir, write=True):
    """Lit mcp_requis du plugin.json ; l'ajoute (déduit de .mcp.json) si absent."""
    pj = os.path.join(ROOT, plugin_dir, ".claude-plugin", "plugin.json")
    d = json.load(open(pj, encoding="utf-8"))
    changed = False
    if "mcp_requis" not in d:
        d["mcp_requis"] = derive_mcp_requis(plugin_dir)
        changed = True
        if write:
            with open(pj, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
                f.write("\n")
    return d, changed


def short_desc(desc):
    """Première phrase de la description, coupée à ~110 caractères."""
    if not desc:
        return ""
    seg = desc.replace("\n", " ").strip()
    for sep in (" : ", ". ", " — "):
        if sep in seg:
            seg = seg.split(sep)[0] + ("" if sep == " : " else "")
            break
    seg = seg.strip()
    if len(seg) > 110:
        seg = seg[:109].rstrip() + "…"
    return seg


def count(plugin_dir, sub, pattern):
    return len(glob.glob(os.path.join(ROOT, plugin_dir, sub, pattern)))


def build_table(write_json=True):
    lines = [
        "| Plugin | Version | Skills | Agents | MCP requis | Description |",
        "|---|---|---|---|---|---|",
    ]
    tot_sk = tot_ag = 0
    changed_any = []
    for pd in plugin_dirs_in_order():
        d, changed = ensure_mcp_requis(pd, write=write_json)
        if changed:
            changed_any.append(pd)
        name = d.get("name", pd)
        ver = d.get("version", "?")
        sk = count(pd, "skills/*", "SKILL.md")
        ag = count(pd, "agents", "*.md")
        tot_sk += sk
        tot_ag += ag
        mcp = ", ".join(d.get("mcp_requis") or []) or "—"
        desc = short_desc(d.get("description", ""))
        lines.append(f"| `{name}` | {ver} | {sk} | {ag} | {mcp} | {desc} |")
    n = len(plugin_dirs_in_order())
    lines.append("")
    lines.append(
        f"**Total : {n} plugins, {tot_sk} skills, {tot_ag} agents.** "
        "Table générée par `scripts/generate_readme_table.py` — ne pas éditer à la main."
    )
    return "\n".join(lines), changed_any


def main():
    check = "--check" in sys.argv
    table, changed = build_table(write_json=not check)
    src = open(README, encoding="utf-8").read()
    if START not in src or END not in src:
        sys.stderr.write(
            f"ERREUR : marqueurs {START} / {END} absents du README.\n"
        )
        return 2
    pre, rest = src.split(START, 1)
    _, post = rest.split(END, 1)
    new = f"{pre}{START}\n{table}\n{END}{post}"
    if check:
        if new != src:
            sys.stderr.write("README non à jour : relancer generate_readme_table.py\n")
            return 1
        print("README à jour.")
        return 0
    if new != src:
        open(README, "w", encoding="utf-8").write(new)
    if changed:
        print("mcp_requis ajouté à :", ", ".join(changed))
    print(f"Table régénérée ({new != src and 'modifiée' or 'inchangée'}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
