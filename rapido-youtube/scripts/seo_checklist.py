#!/usr/bin/env python3
"""Checklist SEO mécanique d'un titre + d'une description AVANT publication.

Contrôles appliqués (affichés un par un) — le score serveur
(yt_score_video_seo) reste la référence, cette checklist attrape le
mécanisable en local, gratuitement :
- titre : non vide, ≤ 100 caractères (70 recommandés pour l'affichage),
  pas TOUT EN MAJUSCULES, mot-clé présent s'il est fourni ;
- description : non vide, ≥ 200 caractères recommandés, mot-clé dans les
  150 premiers caractères, pas de lien de miniature signé temporaire
  (supabase…token=), chapitres valides si présents (0:00 en premier,
  croissants) ;
- hashtags : ≤ 15 (au-delà YouTube les ignore tous).

Usage :
    python3 seo_checklist.py titre.txt description.txt [mot-cle]
Exit 0 si tout passe, 1 sinon. Stdlib uniquement.
"""
import re
import sys


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    titre = open(argv[1], encoding="utf-8").read().strip()
    description = open(argv[2], encoding="utf-8").read().strip()
    motcle = argv[3].lower() if len(argv) > 3 else None
    verdicts = []

    def check(nom, ok, detail=""):
        verdicts.append(ok)
        print(f"  [{'OK' if ok else 'À CORRIGER'}] {nom}"
              + (f" — {detail}" if detail else ""))

    check("titre non vide", bool(titre))
    check(f"titre ≤ 100 caractères ({len(titre)})", len(titre) <= 100,
          "70 recommandés pour l'affichage" if len(titre) > 70 else "")
    check("titre pas tout en majuscules",
          not (titre.isupper() and len(titre) > 12))
    if motcle:
        check("mot-clé dans le titre", motcle in titre.lower())
        check("mot-clé dans les 150 premiers caractères de la description",
              motcle in description[:150].lower())
    check(f"description ≥ 200 caractères ({len(description)})",
          len(description) >= 200, "recommandation, pas un blocage"
          if len(description) < 200 else "")
    check("aucun lien signé temporaire dans la description",
          not re.search(r"(token=|X-Amz-|supabase\.co/storage)", description),
          "les aperçus de miniatures expirent : jamais dans un contenu durable")
    ts = re.findall(r"^(\d{1,2}:)?\d{1,2}:\d{2} ", description, re.M)
    if ts:
        premiers = re.findall(r"^((?:\d{1,2}:)?\d{1,2}:\d{2}) ", description, re.M)
        check("chapitres : le premier à 0:00", premiers[0] in ("0:00", "00:00"))
        check(f"chapitres : au moins 3 ({len(premiers)})", len(premiers) >= 3)
    hashtags = re.findall(r"#\w+", description)
    check(f"hashtags ≤ 15 ({len(hashtags)})", len(hashtags) <= 15,
          "au-delà de 15, YouTube les ignore TOUS")
    tout = all(verdicts)
    print("verdict : " + ("prêt pour yt_score_video_seo puis publication"
                          if tout else "corriger avant yt_score_video_seo"))
    return 0 if tout else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
