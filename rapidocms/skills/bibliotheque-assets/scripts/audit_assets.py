#!/usr/bin/env python3
"""Audit de complétude des assets d'une marque (stdlib uniquement).

Compare la checklist canonique des types d'assets à ce qui est réellement
rattaché à une marque, et sort les types manquants + les noms non conformes à
la convention. Le modèle NE calcule JAMAIS cet écart de tête : il appelle ce
script et restitue sa sortie.

Convention de nommage imposée à l'import :
    {marque}-{type}-{variante}-v{N}
    ex. braindcode-logo-blanc-v2 , pronoclip-mascotte-face-v1
- tout en minuscules, séparateur « - », suffixe de version « -v<entier> ».
- {type} est l'un des TYPES_CANONIQUES ci-dessous (il peut contenir un « - »,
  ex. logo-blanc) ; {variante} est libre (un ou plusieurs segments).

Entrée (fichier JSON en argument, ou stdin) :
    {"marque": "braindcode",
     "assets": ["braindcode-logo-blanc-v2", "braindcode-mascotte-face-v1"]}
  `assets` = les NOMS des fichiers rattachés à la marque, c.-à-d. les
  `file.nom` du tableau `assets` renvoyé par get_brand.

Sortie (stdout, JSON) : presents, manquants, non_conformes, conformes, plan.
Code de sortie : 0 (audit, jamais un gate).
"""
import json
import re
import sys

TYPES_CANONIQUES = [
    "logo-principal", "logo-blanc", "logo-noir", "icone", "mascotte",
    "produit", "texture", "template", "photo-equipe",
]

# suffixe de version obligatoire en fin de nom : -v1, -v2, ...
RX_VERSION = re.compile(r"-v\d+$")


def lire_entree():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def type_de(nom):
    """Retourne le type canonique détecté dans un nom, sinon None.

    Match un type comme séquence de segments délimitée par « - » ou les
    bornes, pour ne pas confondre « icone » avec « icone-produit » d'un autre
    type. Le type le plus long qui matche gagne (logo-blanc avant logo).
    """
    for t in sorted(TYPES_CANONIQUES, key=len, reverse=True):
        if re.search(r"(?:^|-)" + re.escape(t) + r"(?:-|$)", nom):
            return t
    return None


def conforme(nom):
    """Nom conforme = minuscules, un type canonique présent, suffixe -vN."""
    if nom != nom.lower():
        return False
    if type_de(nom) is None:
        return False
    return bool(RX_VERSION.search(nom))


def auditer(data):
    marque = (data.get("marque") or "").strip()
    assets = data.get("assets") or []

    conformes, non_conformes = [], []
    types_presents = set()
    for nom in assets:
        nom = (nom or "").strip()
        if not nom:
            continue
        if conforme(nom):
            conformes.append(nom)
            types_presents.add(type_de(nom))
        else:
            raison = []
            if nom != nom.lower():
                raison.append("pas en minuscules")
            if type_de(nom) is None:
                raison.append("type non canonique")
            if not RX_VERSION.search(nom):
                raison.append("suffixe -vN manquant")
            non_conformes.append({"nom": nom, "raisons": raison})

    presents = [t for t in TYPES_CANONIQUES if t in types_presents]
    manquants = [t for t in TYPES_CANONIQUES if t not in types_presents]
    plan = [
        {"type": t, "nom_attendu": f"{marque or '{marque}'}-{t}-{{variante}}-v1"}
        for t in manquants
    ]
    return {
        "marque": marque,
        "total_assets": len([a for a in assets if (a or "").strip()]),
        "presents": presents,
        "manquants": manquants,
        "conformes": conformes,
        "non_conformes": non_conformes,
        "plan_import": plan,
    }


def main():
    print(json.dumps(auditer(lire_entree()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
