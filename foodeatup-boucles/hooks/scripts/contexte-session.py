#!/usr/bin/env python3
"""Hook SessionStart du plugin foodeatup-boucles. Stdlib uniquement.

Un hook `command` ne peut pas appeler les outils MCP lui-même : il injecte donc
en contexte (stdout) la consigne de chargement minimal, plus l'état local connu
(dernier journal d'écritures). Le modèle exécute les lectures dès le premier
tour — c'est ce qui évite de proposer une campagne segmentée à une base de
19 clients sans avoir regardé.

Contrat P2.2 : sortie ≤ 15 lignes, échec silencieux (exit 0 quoi qu'il arrive),
aucun appel d'écriture demandé.
"""
import datetime
import glob
import json
import os
import sys

try:
    lignes = [
        "[foodeatup-boucles] Contexte établissement à charger avant tout échange.",
        "En LECTURE SEULE, avant toute proposition d'action, appeler :",
        "1. get_daily_brief (établissement actif, alertes HACCP du jour) ;",
        "2. get_loyalty_program (état et champ `active` du programme de fidélité) ;",
        "3. list_clients (volumétrie clients — pas de campagne segmentée sous 10 contacts) ;",
        "4. list_campaigns (campagnes en cours).",
        "Restituer en 15 lignes maximum. Si un appel échoue, le noter « indisponible »",
        "et continuer — ne jamais bloquer la session ni inventer les valeurs.",
    ]
    # État local : dernières écritures journalisées par le hook PostToolUse.
    logs = sorted(glob.glob(os.path.join(os.getcwd(), ".claude", "logs",
                                         "ecritures-*.jsonl")))
    if logs:
        dernier = logs[-1]
        try:
            with open(dernier, encoding="utf-8") as f:
                n = sum(1 for _ in f)
            date = os.path.basename(dernier)[len("ecritures-"):-len(".jsonl")]
            lignes.append(f"Journal local : {n} écriture(s) MCP journalisée(s) le {date} "
                          f"({os.path.relpath(dernier)}).")
        except Exception:
            pass
    print("\n".join(lignes[:15]))
except Exception:
    pass  # échec silencieux : jamais de blocage de session
sys.exit(0)
