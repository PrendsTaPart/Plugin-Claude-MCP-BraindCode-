#!/usr/bin/env python3
"""Garde-fou déterministe : les livrables des exercices forge s'écrivent
UNIQUEMENT dans ./rapido-kb/ — refuse (deny) toute écriture de fichier
hors de rapido-kb/ (les fichiers temporaires restent permis sous /tmp).
Exit 0 = allow ; exit 2 + stderr = deny. Aucun appel réseau."""
import json
import os
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

chemin = (data.get("tool_input") or {}).get("file_path", "")
if not chemin:
    sys.exit(0)  # fail-open : rien à juger

normal = os.path.normpath(chemin).replace("\\", "/")
autorise = (
    "/rapido-kb/" in f"/{normal}/"
    or normal.startswith(("rapido-kb/", "./rapido-kb/"))
    or normal.startswith(("/tmp/", "tmp/"))
)

if autorise:
    sys.exit(0)

sys.stderr.write(
    f"Écriture refusée hors de ./rapido-kb/ ({chemin}) : les livrables des "
    "exercices forge se consignent dans ./rapido-kb/startup/forge/ (journal : "
    "parcours.md) — jamais dans le dépôt du plugin ni ailleurs. Fichier "
    "temporaire ? Utiliser /tmp."
)
sys.exit(2)
