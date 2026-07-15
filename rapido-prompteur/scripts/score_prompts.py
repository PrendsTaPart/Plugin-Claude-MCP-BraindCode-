#!/usr/bin/env python3
"""score_prompts.py — boucle d'apprentissage de la bibliothèque de prompts.

Classe chaque prompt en **GAGNANT / NEUTRE** à partir de **métriques RÉELLES**
rapportées par les skills exécutants après production/publication
(post_insights, virality_predictor, réutilisations). **Aucun score n'est
inventé** : seules les métriques présentes dans le fichier de résultats sont
utilisées ; un prompt sans aucune métrique reste **INSUFFISANT** (non taggé).

Le script ne touche à aucun MCP (stdlib, sans réseau). Il :
  1. lit un fichier de résultats JSON (produit à partir de données MCP réelles) ;
  2. calcule le tag selon une formule TRANSPARENTE (affichée) ;
  3. met à jour `apprentissages.md` (journal daté) ;
  4. émet (`--emit-edits`) un plan d'appels `edit_prompt` que l'agent exécute
     pour poser le tag dans la bibliothèque RapidoCMS.

Schéma d'entrée (results.json) :
  {
    "prompts": [
      {"prompt_id": 12, "titre": "packshot — sneaker — studio",
       "metrics": {"engagement_rate": 0.061, "virality_score": 74,
                   "reuse_count": 2, "impressions": 5300}}
    ]
  }
Toute clé de `metrics` absente est traitée comme « non disponible » (jamais 0
par défaut). `metrics` vide ou absent → INSUFFISANT.

Formule (seuils par défaut, surchargeables en CLI) :
  GAGNANT  si  au moins un signal RÉEL disponible dépasse son seuil :
                 engagement_rate >= 0.05  OU  virality_score >= 70
                 OU  reuse_count >= 3
  NEUTRE   si  au moins un signal réel est disponible mais aucun seuil atteint
  INSUFFISANT  si  aucun signal réel n'est disponible
"""
import argparse
import json
import os
import sys

SIGNAUX = ("engagement_rate", "virality_score", "reuse_count")


def classer(metrics, seuils):
    """Retourne (tag, raisons[]) — uniquement d'après les métriques présentes."""
    dispo = {k: metrics[k] for k in SIGNAUX
             if isinstance(metrics.get(k), (int, float))}
    if not dispo:
        return "INSUFFISANT", ["aucune métrique réelle disponible"]
    raisons, gagnant = [], False
    for k, v in dispo.items():
        seuil = seuils[k]
        atteint = v >= seuil
        raisons.append(f"{k}={v} (seuil {seuil}) {'✓' if atteint else '·'}")
        gagnant = gagnant or atteint
    return ("GAGNANT" if gagnant else "NEUTRE"), raisons


def journaliser(chemin, date, lignes):
    """Ajoute une section datée au journal d'apprentissages (crée si absent)."""
    os.makedirs(os.path.dirname(chemin) or ".", exist_ok=True)
    entete = "# Apprentissages — bibliothèque de prompts\n\n"
    corps = f"## {date}\n\n" + "\n".join(lignes) + "\n\n"
    existant = ""
    if os.path.isfile(chemin):
        with open(chemin, encoding="utf-8") as f:
            existant = f.read()
    if not existant.startswith("# Apprentissages"):
        existant = entete + existant
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(existant + corps)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Tag GAGNANT/NEUTRE des prompts (métriques réelles).")
    ap.add_argument("--results", required=True, help="fichier JSON de résultats réels")
    ap.add_argument("--apprentissages",
                    default=os.path.join("rapido-kb", "marketing", "apprentissages.md"))
    ap.add_argument("--date", default=None, help="AAAA-MM-JJ (défaut : date du jour)")
    ap.add_argument("--seuil-engagement", type=float, default=0.05)
    ap.add_argument("--seuil-virality", type=float, default=70)
    ap.add_argument("--seuil-reuse", type=float, default=3)
    ap.add_argument("--emit-edits", action="store_true",
                    help="imprime le plan d'appels edit_prompt (JSON) sur stdout")
    args = ap.parse_args(argv)

    seuils = {"engagement_rate": args.seuil_engagement,
              "virality_score": args.seuil_virality,
              "reuse_count": args.seuil_reuse}

    try:
        with open(args.results, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Erreur lecture results : {e}", file=sys.stderr)
        return 1

    date = args.date
    if not date:
        from datetime import date as _d
        date = _d.today().isoformat()

    edits, lignes = [], []
    for p in data.get("prompts", []):
        pid = p.get("prompt_id")
        titre = p.get("titre", "(sans titre)")
        tag, raisons = classer(p.get("metrics") or {}, seuils)
        lignes.append(f"- `{pid}` **{titre}** → **{tag}** ({'; '.join(raisons)})")
        if tag in ("GAGNANT", "NEUTRE") and pid is not None:
            edits.append({"tool": "edit_prompt", "prompt_id": pid, "tag": tag})

    journaliser(args.apprentissages, date, lignes)
    print(f"{len(lignes)} prompt(s) classé(s) → {args.apprentissages}", file=sys.stderr)
    for l in lignes:
        print("  " + l, file=sys.stderr)
    if args.emit_edits:
        print(json.dumps({"edits": edits}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
