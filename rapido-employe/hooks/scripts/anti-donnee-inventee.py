#!/usr/bin/env python3
"""Anti-donnée-inventée (PreToolUse, écritures MCP) — version employé.

Règle de la maison : aucun client inventé, aucun chiffre sans source, aucune
promesse de revenus. Un hook déterministe ne lit pas les intentions, mais il
attrape les signatures mécaniques de l'invention dans les ÉCRITURES :

- coordonnées d'exemple : domaines example.com/exemple.com/test.com, numéros
  0600000000 / 0123456789 / +33600000000, « Jean Dupont » ;
- texte gabarit : lorem ipsum, « À COMPLÉTER », « REMPLACER », placeholders
  [crochets] non remplis dans un champ envoyé à un serveur ;
- promesse chiffrée dans un texte sortant : « garanti » accolé à un € ou un %.

deny = exit 2 + stderr. Les lectures ne sont pas inspectées. Adapté du hook
anti-donnee-inventee des plugins rapido-suite/foodeatup. Testé en CI.
"""
import json
import re
import sys

RX_MCP = re.compile(r"^mcp__(.+)__([A-Za-z0-9_-]+)$")
RX_LECTURE = re.compile(r"^(list|get|search|check|describe|rechercher|lister|"
                        r"obtenir|preview|read)[_-]")
MOTIFS = [
    ("coordonnée d'exemple",
     re.compile(r"@(?:example|exemple|test)\.(?:com|fr)|"
                r"(?<!\d)(?:06|\+?33ドル?6)0{7,8}(?!\d)|(?<!\d)0123456789(?!\d)|"
                r"\bjean\s+dupont\b", re.I)),
    ("texte gabarit non rempli",
     re.compile(r"lorem\s+ipsum|À\s+COMPLÉTER|REMPLACER[_ ]?MOI|"
                r"\[(?:nom|prix|date|ville|téléphone|telephone|email)\]", re.I)),
    ("promesse chiffrée",
     re.compile(r"garanti[es]?\b[^.\n]{0,40}(?:€|%)|"
                r"(?:€|%)[^.\n]{0,40}\bgaranti[es]?\b", re.I)),
]


def texte_de(obj):
    if isinstance(obj, dict):
        return " ".join(texte_de(v) for v in obj.values())
    if isinstance(obj, list):
        return " ".join(texte_de(v) for v in obj)
    return obj if isinstance(obj, str) else ""


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    m = RX_MCP.match(payload.get("tool_name", ""))
    if not m or RX_LECTURE.match(m.group(2)):
        sys.exit(0)
    entree = payload.get("tool_input", {}) or {}
    # Héritage du hook d'origine (contrat commun du dépôt) : un relevé de
    # température se LIT sur le thermomètre, il ne s'invente pas.
    if m.group(2) == "add_temperature":
        t = entree.get("temperature")
        if not isinstance(t, (int, float)) or not -30 <= t <= 90 \
                or not entree.get("equipment_id"):
            print("anti-donnee-inventee : relevé de température invraisemblable "
                  "ou sans equipment_id — la valeur est lue par le client, "
                  "jamais supposée.", file=sys.stderr)
            sys.exit(2)
    texte = texte_de(entree)
    for nom, rx in MOTIFS:
        if rx.search(texte):
            print(f"anti-donnee-inventee : {nom} détecté dans une écriture "
                  f"vers « {m.group(2)} » — rien d'inventé : la donnée réelle "
                  "vient du client, du CRM ou d'un outil, et une valeur "
                  "manquante SE DIT au lieu de se remplir.", file=sys.stderr)
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
