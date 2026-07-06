#!/usr/bin/env python3
"""Plafond de budget publicitaire (Meta Ads) — deny déterministe.

Refuse (exit 2) toute création/modification dont le budget JOURNALIER dépasse
le plafond maison. Plafond lu dans ./rapido-kb/processus-internes.md
(première ligne contenant « plafond » et un montant en € sur la même ligne,
ex. « Plafond budget pub : 80 €/jour ») ; défaut : 50 €/jour.

Hypothèses : les budgets Meta sont exprimés en CENTIMES (plus petite unité) ;
les clés journalières contiennent « daily_budget », les clés totales
« lifetime_budget » (comparées au plafond × durée estimée, défaut 30 jours).
Le plan de boost (confirmed=false) n'est pas bloqué. Aucun appel réseau."""
import json
import os
import re
import sys

PLAFOND_DEFAUT_EUROS = 50.0
KB_FILE = os.path.join(".", "rapido-kb", "processus-internes.md")
DUREE_LIFETIME_DEFAUT_JOURS = 30


def lire_plafond():
    try:
        with open(KB_FILE, encoding="utf-8") as f:
            for ligne in f:
                if "plafond" in ligne.lower():
                    m = re.search(r"(\d+(?:[.,]\d+)?)\s*€", ligne)
                    if m:
                        return float(m.group(1).replace(",", ".")), "maison (rapido-kb)"
    except OSError:
        pass
    return PLAFOND_DEFAUT_EUROS, "défaut (50 €/jour)"


def collecter_budgets(objet, resultats):
    if isinstance(objet, dict):
        for cle, valeur in objet.items():
            cle_l = str(cle).lower()
            if isinstance(valeur, (int, float)) and "budget" in cle_l:
                resultats.append((cle_l, float(valeur)))
            else:
                collecter_budgets(valeur, resultats)
    elif isinstance(objet, list):
        for v in objet:
            collecter_budgets(v, resultats)
    elif isinstance(objet, str):
        try:
            collecter_budgets(json.loads(objet), resultats)
        except (ValueError, TypeError):
            pass


try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

tool = data.get("tool_name", "")
tool_input = data.get("tool_input") or {}

# Le plan de boost (confirmed=false) est une simulation : ne pas bloquer.
if tool.endswith("ads_boost_ig_post") and not tool_input.get("confirmed"):
    sys.exit(0)

plafond_euros, source = lire_plafond()
plafond_cents_jour = plafond_euros * 100

budgets = []
collecter_budgets(tool_input, budgets)

for cle, valeur_cents in budgets:
    if "lifetime" in cle:
        limite = plafond_cents_jour * DUREE_LIFETIME_DEFAUT_JOURS
        if valeur_cents > limite:
            sys.stderr.write(
                f"REFUS plafond budget : {cle}={valeur_cents:.0f} (centimes) "
                f"dépasse le plafond {source} de {plafond_euros:g} €/jour "
                f"(limite lifetime estimée sur {DUREE_LIFETIME_DEFAUT_JOURS} j : "
                f"{limite:.0f} centimes). Au-delà du plafond, une validation "
                "écrite préalable de l'utilisateur est exigée : la consigner, "
                "ajuster le plafond dans rapido-kb/processus-internes.md, puis "
                "réessayer."
            )
            sys.exit(2)
    else:
        if valeur_cents > plafond_cents_jour:
            sys.stderr.write(
                f"REFUS plafond budget : {cle}={valeur_cents:.0f} (centimes) "
                f"dépasse le plafond {source} de {plafond_euros:g} €/jour "
                f"({plafond_cents_jour:.0f} centimes/jour). Au-delà du plafond, "
                "une validation écrite préalable de l'utilisateur est exigée : "
                "la consigner, ajuster le plafond dans "
                "rapido-kb/processus-internes.md, puis réessayer."
            )
            sys.exit(2)

sys.exit(0)
