#!/usr/bin/env python3
"""Compte les segments d'un SMS avant tout envoi.

Formules affichées (et appliquées) :
- texte entièrement en GSM-7 : 160 caractères pour 1 segment, puis
  153 caractères par segment (en-têtes de concaténation) ;
- un seul caractère hors GSM-7 (emoji, œ, certains guillemets…) fait
  basculer TOUT le message en UCS-2 : 70 caractères, puis 67 par segment ;
- les caractères GSM-7 « étendus » ([ ] { } ~ ^ | € \\) comptent DOUBLE ;
- plafond serveur : 1 600 caractères par message, 200 cibles par envoi.

Usage : python3 segments_sms.py "texte"   (ou texte sur stdin)
Stdlib uniquement.
"""
import sys

GSM7 = set(
    "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
    "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà"
)
GSM7_ETENDU = set("^{}\\[~]|€")


def segments(texte):
    """(encodage, longueur comptée, nb_segments)."""
    if all(c in GSM7 or c in GSM7_ETENDU for c in texte):
        longueur = sum(2 if c in GSM7_ETENDU else 1 for c in texte)
        if longueur <= 160:
            return "GSM-7", longueur, (1 if longueur else 0)
        return "GSM-7", longueur, -(-longueur // 153)
    longueur = len(texte)
    if longueur <= 70:
        return "UCS-2", longueur, (1 if longueur else 0)
    return "UCS-2", longueur, -(-longueur // 67)


def main(argv):
    texte = argv[1] if len(argv) > 1 else sys.stdin.read()
    enc, longueur, nb = segments(texte)
    print(f"encodage   : {enc}")
    print(f"longueur   : {longueur} caractère(s) comptés "
          f"({len(texte)} bruts, plafond serveur 1 600)")
    print(f"segments   : {nb} (formule : "
          f"{'160 puis 153/segment' if enc == 'GSM-7' else '70 puis 67/segment'})")
    if "STOP" not in texte.upper():
        print("ALERTE     : mention STOP absente — l'envoi sera refusé.")
    hors = sorted({c for c in texte if c not in GSM7 and c not in GSM7_ETENDU})
    if hors:
        print(f"hors GSM-7 : {' '.join(hors[:10])} — chacun fait payer l'UCS-2.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
