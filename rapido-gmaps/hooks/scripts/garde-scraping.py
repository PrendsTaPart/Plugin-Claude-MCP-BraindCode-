#!/usr/bin/env python3
"""garde-scraping — garde-fou déterministe du plugin rapido-gmaps.

Deux responsabilités, indépendantes du modèle (stdin JSON → allow/ask) :

1. VOLUME DE SCRAPING (PreToolUse sur Bash) — quand une commande invoque le
   scraper Google Maps (google-maps-scraper / gms-bin / POST /api/v1/scrape)
   avec une profondeur (`-depth` / `--depth` / `max_depth`) ou un rayon
   (`-radius` / `--radius` / `radius`) au-delà des seuils, force une
   confirmation (ask) avec un avertissement volumétrique. Les seuils sont
   surchargeables par variables d'env (GMAPS_DEPTH_MAX, GMAPS_RADIUS_MAX)
   — miroir de rapido-kb/scraping-config.md — avec des défauts prudents.

2. IMPORT CRM EN LOT (PreToolUse sur enregistrer_tous_prospects) — la création
   groupée de fiches passe toujours par une confirmation (déduplication faite ?).

Ne bloque jamais en dur (aucun deny) : le scraping licite de données publiques
n'est pas interdit — il est cadré. Contrat : ask = exit 0 + JSON stdout ;
allow = exit 0 sans stdout. Aucune I/O réseau, aucun secret.
"""
import json
import os
import re
import sys

MARQUEURS_SCRAPER = (
    "google-maps-scraper",
    "google_maps_scraper",
    "gms-bin",
    "/api/v1/scrape",
    "rapido-gmaps",
)


def demander(raison):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": raison,
        }
    }))
    sys.exit(0)


def _premier_nombre(commande, motifs):
    for m in motifs:
        r = re.search(m, commande, re.IGNORECASE)
        if r:
            try:
                return float(r.group(1))
            except (TypeError, ValueError):
                return None
    return None


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (ValueError, TypeError):
        sys.exit(0)  # entrée illisible → ne bloque pas

    outil = (data.get("tool_name") or "")
    ti = data.get("tool_input") or {}
    ol = outil.lower()

    # 2. Import CRM en lot
    if ol.endswith("enregistrer_tous_prospects"):
        demander(
            "Import CRM en lot (enregistrer_tous_prospects) : confirmez la "
            "création groupée de fiches. La déduplication (rechercher_prospects) "
            "a-t-elle bien été passée pour chaque lead ?"
        )

    # 1. Volume de scraping
    if ol.endswith("bash") or outil == "Bash":
        commande = ti.get("command", "") or ""
        if any(mk in commande.lower() for mk in MARQUEURS_SCRAPER):
            depth = _premier_nombre(commande, [
                r"-depth\s+(\d+)", r"--depth\s+(\d+)",
                r'"max_depth"\s*:\s*(\d+)', r"'max_depth'\s*:\s*(\d+)",
            ])
            radius = _premier_nombre(commande, [
                r"-radius\s+([\d.]+)", r"--radius\s+([\d.]+)",
                r'"radius"\s*:\s*([\d.]+)', r"'radius'\s*:\s*([\d.]+)",
            ])
            try:
                depth_max = int(os.environ.get("GMAPS_DEPTH_MAX", "10"))
            except ValueError:
                depth_max = 10
            try:
                radius_max = float(os.environ.get("GMAPS_RADIUS_MAX", "20"))
            except ValueError:
                radius_max = 20.0

            raisons = []
            if depth is not None and depth > depth_max:
                raisons.append(f"profondeur {int(depth)} > seuil {depth_max}")
            if radius is not None and radius > radius_max:
                raisons.append(f"rayon {radius:g} km > seuil {radius_max:g} km")
            if raisons:
                demander(
                    "Volume de scraping élevé (" + " ; ".join(raisons) + "). "
                    "Vérifiez les plafonds CGU/RGPD (reference/garde-fous-scraping.md "
                    "ou rapido-kb/scraping-config.md) avant de lancer."
                )

    sys.exit(0)  # allow


if __name__ == "__main__":
    main()
