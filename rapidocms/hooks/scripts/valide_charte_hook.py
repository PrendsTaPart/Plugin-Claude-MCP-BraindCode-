#!/usr/bin/env python3
"""Garde-fou déterministe de validation de format (couche marque RapidoCMS).

REFUSE (exit 2 + message pédagogique sur stderr) une écriture dont un champ est
malformé AVANT l'appel réseau — évite de polluer le CMS avec des couleurs, des
polices, des URLs ou des références d'images invalides. Aucun appel réseau,
stdlib uniquement, < 1 s.

Couverture (matcher hooks.json) :
- create_brand / edit_brand : couleurs (hex,virgules), font_family (enum
  web-safe), logo & site_web (http/https).
- images_to_image : images (http/https, sans espace, nombre <= LIMITE_IMAGES).
- upload_file_tool : type ∈ {image, video, doc}, file_url (http/https).

Décision : allow (exit 0) par défaut ; deny (exit 2 + stderr) si malformé.
"""
import json
import re
import sys

# Borne haute VÉRIFIÉE EN DIRECT (audit P0) : images_to_image fonctionne de 1 à
# 3 références. Au-delà non garanti → on refuse pour rester dans le contrat sûr.
LIMITE_IMAGES = 3

FONTS_WEB_SAFE = {
    "Arial, sans-serif", "Verdana, sans-serif", "Tahoma, sans-serif",
    "Trebuchet MS, sans-serif", "Georgia, serif", "Times New Roman, serif",
    "Garamond, serif", "Courier New, monospace", "Lucida Console, monospace",
}

RX_COULEURS = re.compile(r"^#[0-9A-Fa-f]{6}(,#[0-9A-Fa-f]{6})*$")


def refuser(message):
    """Convention maison : deny = stderr + exit 2."""
    sys.stderr.write("Refus (valide-charte, plugin rapidocms) : " + message)
    sys.exit(2)


def est_http(url):
    return isinstance(url, str) and (
        url.startswith("http://") or url.startswith("https://"))


def bare_name(tool_name):
    return tool_name.rsplit("__", 1)[-1] if tool_name else ""


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # rien à valider → laisser passer

    outil = bare_name(data.get("tool_name", ""))
    ti = data.get("tool_input", {}) or {}

    if outil in ("create_brand", "edit_brand"):
        couleurs = ti.get("couleurs")
        if couleurs and not RX_COULEURS.match(couleurs):
            refuser(
                f"couleurs='{couleurs}' invalide. Format attendu : des hex à 6 "
                "chiffres séparés par des virgules SANS espace, ex. "
                "'#0055FF,#FFFFFF'. Prends les couleurs dans la charte "
                "(./rapido-kb/charte-graphique.md), jamais un nom ('bleu') ni "
                "un hex court ('#00F').")
        font = ti.get("font_family")
        if font and font not in FONTS_WEB_SAFE:
            refuser(
                f"font_family='{font}' hors de l'enum web-safe. Valeurs "
                "admises : " + ", ".join(sorted(FONTS_WEB_SAFE)) + ". Choisis "
                "la pile la plus proche de la charte et explique-le.")
        for champ in ("logo", "site_web"):
            val = ti.get(champ)
            if val and not est_http(val):
                refuser(
                    f"{champ}='{val}' doit être une URL http(s). Un fichier "
                    "local n'est pas accepté : héberge-le d'abord "
                    "(upload_file_tool renvoie une file_url publique).")

    elif outil == "images_to_image":
        images = ti.get("images")
        if images:
            if " " in images:
                refuser(
                    "images contient un espace. Attendu : des URLs publiques "
                    "http(s) séparées par des virgules SANS espace.")
            parts = [u for u in images.split(",") if u]
            if len(parts) > LIMITE_IMAGES:
                refuser(
                    f"{len(parts)} images fournies : la limite vérifiée est "
                    f"{LIMITE_IMAGES}. Passe une sélection minimale (logo + 1-2 "
                    "assets utiles).")
            for u in parts:
                if not est_http(u):
                    refuser(
                        f"référence '{u}' n'est pas une URL http(s). Les "
                        "chemins locaux ne marchent pas : uploade l'image et "
                        "utilise sa file_url publique.")

    elif outil == "upload_file_tool":
        typ = ti.get("type")
        if typ is not None and typ not in ("image", "video", "doc"):
            refuser(
                f"type='{typ}' invalide. Valeurs admises : image, video, doc.")
        fu = ti.get("file_url")
        if fu and not est_http(fu):
            refuser(
                f"file_url='{fu}' doit être une URL publique http(s) "
                "(le serveur télécharge le fichier depuis cette URL).")

    sys.exit(0)


if __name__ == "__main__":
    main()
