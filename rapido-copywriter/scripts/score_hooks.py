#!/usr/bin/env python3
"""score_hooks — tague les hooks GAGNANT/NEUTRE sur les VRAIS insights (stdlib).

Le modèle n'invente aucun score : ce script ne lit que les 4 métriques réellement
exposées par RapidoCMS `post_insights` — **liked, shares, comments, views** — par
réseau, et compare chaque hook à la **médiane de son réseau**.

    interactions(post) = liked + shares + comments
    médiane_réseau     = médiane des interactions des posts du réseau (fenêtre 30 j)
    tag(hook) = GAGNANT si moyenne(interactions de ses posts) > médiane_réseau, sinon NEUTRE

Entrée : JSON via --input FICHIER ou stdin :
    {"posts": [{"hook_id":"L1","network":"linkedin",
                "liked":10,"shares":2,"comments":5,"views":300}, ...]}
Sortie : JSON — par hook : réseau, tag, n_posts, moyenne d'interactions, médiane réseau.
Aucune métrique inventée ; un réseau sans posts ⇒ non calculable.
"""
import argparse
import json
import statistics
import sys


def _interactions(p):
    def n(k):
        try:
            return float(p.get(k) or 0)
        except (TypeError, ValueError):
            return 0.0
    return n("liked") + n("shares") + n("comments")


def main():
    ap = argparse.ArgumentParser(description="Scoring des hooks sur insights réels")
    ap.add_argument("--input", help="fichier JSON (défaut : stdin)")
    args = ap.parse_args()
    raw = open(args.input, encoding="utf-8").read() if args.input else sys.stdin.read()
    try:
        data = json.loads(raw or "{}")
    except ValueError as e:
        print(f"Entrée JSON invalide : {e}", file=sys.stderr)
        return 1
    posts = data.get("posts") if isinstance(data, dict) else data
    if not isinstance(posts, list):
        print("Entrée attendue : {\"posts\": [...]}", file=sys.stderr)
        return 1

    # Médiane des interactions par réseau
    par_reseau = {}
    for p in posts:
        if not isinstance(p, dict):
            continue
        net = str(p.get("network") or "?").lower()
        par_reseau.setdefault(net, []).append(_interactions(p))
    medianes = {net: statistics.median(v) for net, v in par_reseau.items() if v}

    # Agrégat par hook (hook_id × réseau)
    par_hook, par_famille = {}, {}
    for p in posts:
        if not isinstance(p, dict):
            continue
        net = str(p.get("network") or "?").lower()
        inter = _interactions(p)
        if p.get("hook_id"):
            par_hook.setdefault((str(p["hook_id"]), net), []).append(inter)
        if p.get("family"):
            par_famille.setdefault((str(p["family"]), net), []).append(inter)

    def _tag(moy, net):
        med = medianes.get(net)
        return ("GAGNANT" if (med is not None and moy > med) else "NEUTRE"), med

    resultats = {}
    for (hid, net), inters in sorted(par_hook.items()):
        moy = round(sum(inters) / len(inters), 2)
        tag, med = _tag(moy, net)
        resultats[f"{hid}@{net}"] = {
            "hook_id": hid, "network": net, "tag": tag,
            "n_posts": len(inters), "moyenne_interactions": moy, "mediane_reseau": med,
        }

    # Agrégat PAR FAMILLE × réseau
    familles = {}
    gagnantes = {}  # réseau → familles GAGNANT
    for (fam, net), inters in sorted(par_famille.items()):
        moy = round(sum(inters) / len(inters), 2)
        tag, med = _tag(moy, net)
        familles[f"{fam}@{net}"] = {
            "famille": fam, "network": net, "tag": tag,
            "n_posts": len(inters), "moyenne_interactions": moy, "mediane_reseau": med,
        }
        if tag == "GAGNANT":
            gagnantes.setdefault(net, []).append(fam)

    print(json.dumps({
        "medianes_reseau": {k: round(v, 2) for k, v in medianes.items()},
        "hooks": resultats,
        "familles": familles,
        "familles_gagnantes_par_reseau": gagnantes,
        "formule": "interactions = liked + shares + comments ; "
                   "GAGNANT si moyenne > médiane du réseau (par hook ET par famille)",
    }, ensure_ascii=False, indent=2))
    print(f"# {len(resultats)} hooks, {len(familles)} couples famille×réseau "
          f"sur {len(posts)} posts ({len(medianes)} réseaux) — métriques réelles "
          f"uniquement. Écrire la synthèse « familles gagnantes » dans banque-hooks.md "
          f"+ apprentissages.md.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
