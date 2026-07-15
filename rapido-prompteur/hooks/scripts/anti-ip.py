#!/usr/bin/env python3
"""PreToolUse — garde léger anti-IP pour les prompts sortants.

Scanne le prompt envoyé à un outil de GÉNÉRATION (Higgsfield, RapidoCMS,
Lovable, Canva). Si le prompt contient une marque / franchise / œuvre sous
licence connue (liste maison `reference/ip-a-risque.md`) OU une formule de
« style de [artiste] » (in the style of / dans le style de / à la manière de),
il force une CONFIRMATION avec avertissement — l'agent doit décrire l'effet
visuel générique plutôt que nommer une IP ou un artiste vivant.

Ce garde est volontairement LÉGER : il ne bloque pas, il demande confirmation
(permissionDecision = ask). La liste maison est éditable sans toucher au code.

Contrat hook :
  - ask   = exit 0 + stdout JSON {hookSpecificOutput.permissionDecision:"ask"}
  - allow = exit 0 sans stdout
Stdlib uniquement, < 1 s, sans réseau.
"""
import json
import os
import re
import sys

# Suffixes des outils de génération concernés (défense en profondeur : le
# matcher hooks.json filtre déjà, mais on revérifie pour ne rien scanner d'autre).
GEN_SUFFIXES = {
    "generate_image", "generate_video", "generate_audio", "generate_3d",
    "images_to_image", "generate-design", "generate-design-structured",
    "create_project", "send_message",
}

# Formules de « style d'artiste » à signaler quel que soit le nom qui suit.
RX_STYLE = re.compile(
    r"(?:in the style of|dans le style de|à la manière de|style de|"
    r"inspir[ée]?\s+(?:de|par)|--sref)\b",
    re.I,
)


def suffixe(tool):
    return tool.split("__")[-1] if tool else ""


def collecter_chaines(obj, acc):
    """Aplati récursivement toutes les valeurs texte d'un tool_input."""
    if isinstance(obj, str):
        acc.append(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            collecter_chaines(v, acc)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            collecter_chaines(v, acc)


def charger_liste():
    """Termes à risque depuis reference/ip-a-risque.md (relatif au script)."""
    ici = os.path.dirname(os.path.abspath(__file__))
    chemin = os.path.join(ici, "..", "..", "reference", "ip-a-risque.md")
    termes = []
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                m = re.match(r"\s*[-*]\s+(.+?)\s*$", ligne)
                if m:
                    terme = m.group(1).split("—")[0].split("(")[0].strip()
                    if terme and not terme.startswith("#"):
                        termes.append(terme)
    except OSError:
        pass
    return termes


def detecter(blob, termes):
    trouves = []
    for t in termes:
        # frontière de mot des deux côtés, insensible à la casse
        motif = r"(?<![\w'])" + re.escape(t) + r"(?![\w'])"
        if re.search(motif, blob, re.I):
            trouves.append(t)
    style = bool(RX_STYLE.search(blob))
    return trouves, style


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # payload illisible → ne pas gêner

    tool = data.get("tool_name", "") or ""
    if suffixe(tool) not in GEN_SUFFIXES:
        return 0  # allow — pas un outil de génération scanné

    chaines = []
    collecter_chaines(data.get("tool_input") or {}, chaines)
    blob = " \n ".join(chaines)
    if not blob.strip():
        return 0  # allow — rien à scanner

    trouves, style = detecter(blob, charger_liste())
    if not trouves and not style:
        return 0  # allow — prompt propre

    raisons = []
    if trouves:
        raisons.append("IP/marque(s) détectée(s) : " + ", ".join(sorted(set(trouves))))
    if style:
        raisons.append("formule « style de [artiste] » détectée "
                       "(risque : style d'un artiste vivant / œuvre sous licence)")

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                "⚠️ Anti-IP (rapido-prompteur) : " + " ; ".join(raisons) + ".\n"
                "Politique maison : ne jamais nommer une IP tierce ni un artiste "
                "vivant dans un prompt — décrire l'EFFET visuel générique à la "
                "place (ex. « symétrie, pastel, plans larges » plutôt qu'un nom de "
                "réalisateur). Confirmer seulement si l'usage est légitime "
                "(marque du client, IP dont les droits sont détenus)."
            ),
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
