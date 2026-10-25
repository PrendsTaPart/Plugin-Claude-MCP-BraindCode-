#!/usr/bin/env python3
"""Garde de la mémoire (PreToolUse sur remember) — rien de sensible ne s'y range.

La mémoire de Claude employé (`remember` : méthode, préférence, correction)
ne contient JAMAIS un secret, une coordonnée bancaire ni une donnée client
nominative. Ce garde refuse (deny) tout remember dont les arguments portent :

- une adresse e-mail, un numéro de téléphone ;
- un IBAN ou un numéro de carte (13 à 19 chiffres, espaces compris) ;
- un jeton ou une clé (motifs sk-/bearer/api_key/token/secret, hex ≥ 32).

deny = exit 2 + stderr. Aucun appel réseau. Testé en CI.
"""
import json
import re
import sys

RX_EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
RX_TEL = re.compile(r"(?<!\d)(?:\+?\d[\d .-]{8,}\d)(?!\d)")
RX_IBAN = re.compile(r"\b[A-Z]{2}\d{2}[ ]?(?:[A-Z0-9][ ]?){11,30}\b")
RX_CARTE = re.compile(r"(?<!\d)(?:\d[ -]?){13,19}(?!\d)")
RX_JETON = re.compile(r"sk-[A-Za-z0-9]{8,}|bearer\s+\S{8,}|"
                      r"(?:api[_-]?key|token|secret)\s*[:=]\s*\S{8,}|"
                      r"\b[0-9a-f]{32,}\b", re.I)


def texte_de(obj):
    if isinstance(obj, dict):
        return " ".join(texte_de(v) for v in obj.values())
    if isinstance(obj, list):
        return " ".join(texte_de(v) for v in obj)
    return str(obj) if isinstance(obj, (str, int, float)) else ""


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    if not re.search(r"__(remember)$", payload.get("tool_name", "")):
        sys.exit(0)
    texte = texte_de(payload.get("tool_input", {}))
    for nom, rx in (("adresse e-mail", RX_EMAIL), ("numéro de téléphone", RX_TEL),
                    ("IBAN", RX_IBAN), ("numéro de carte", RX_CARTE),
                    ("jeton ou clé", RX_JETON)):
        if rx.search(texte):
            print(f"garde-memoire : la mémoire ne range ni secret ni donnée "
                  f"personnelle — motif détecté : {nom}. Retenir la MÉTHODE, "
                  "jamais la coordonnée (la fiche client vit dans le CRM, le "
                  "jeton dans le coffre).", file=sys.stderr)
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
