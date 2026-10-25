#!/usr/bin/env python3
"""Produit des chapitres YouTube valides depuis une transcription horodatée.

Règles YouTube appliquées (et affichées) :
- le premier chapitre commence à 00:00 ;
- au moins 3 chapitres ;
- chaque chapitre dure au moins 10 secondes ;
- horodatages croissants, format M:SS ou H:MM:SS.

Usage :
    python3 chapitres.py transcription.txt [--max 12]
transcription.txt : lignes « [HH:MM:SS] texte » ou « MM:SS texte » (sortie
Whisper/rapido-video) ou JSON [{"start": secondes, "text": …}]. Le script
regroupe en sections et propose un intitulé COURT tiré des mots de la
transcription — jamais inventé. Sortie prête à coller dans la description.
Stdlib uniquement.
"""
import json
import re
import sys

RX_TS = re.compile(r"^\[?(?:(\d{1,2}):)?(\d{1,2}):(\d{2})\]?\s+(.*)$")


def secondes(h, m, s):
    return (int(h or 0)) * 3600 + int(m) * 60 + int(s)


def fmt(t):
    h, r = divmod(int(t), 3600)
    m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def charger(chemin):
    brut = open(chemin, encoding="utf-8").read().strip()
    if brut.startswith("["):
        try:
            data = json.loads(brut)
            return [(float(x.get("start", 0)), str(x.get("text", "")).strip())
                    for x in data if str(x.get("text", "")).strip()]
        except Exception:  # noqa: BLE001
            pass
    lignes = []
    for l in brut.splitlines():
        m = RX_TS.match(l.strip())
        if m:
            lignes.append((secondes(m.group(1), m.group(2), m.group(3)),
                           m.group(4).strip()))
    return lignes


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    maxi = int(argv[argv.index("--max") + 1]) if "--max" in argv else 12
    lignes = charger(argv[1])
    if len(lignes) < 3:
        print("Transcription trop courte ou sans horodatages : pas de "
              "chapitres (YouTube en exige 3, à 10 s d'écart minimum).")
        return 1
    duree = lignes[-1][0]
    pas = max(10.0, duree / maxi)
    chapitres, borne = [], 0.0
    for t, texte in lignes:
        if t >= borne and (not chapitres or t - chapitres[-1][0] >= 10):
            mots = [w for w in re.findall(r"[\w'’-]+", texte) if len(w) > 2]
            titre = " ".join(mots[:6]).capitalize() or texte[:40]
            chapitres.append((t, titre))
            borne = t + pas
        if len(chapitres) >= maxi:
            break
    if chapitres and chapitres[0][0] != 0:
        chapitres.insert(0, (0, "Introduction"))
    chapitres = chapitres[:maxi]
    if len(chapitres) < 3:
        print("Moins de 3 sections exploitables : pas de chapitres plutôt "
              "que des chapitres artificiels.")
        return 1
    print("# Chapitres (premier à 0:00, ≥ 3, ≥ 10 s chacun — règles YouTube)")
    for t, titre in chapitres:
        print(f"{fmt(t)} {titre}")
    print("# Intitulés tirés de la transcription : à relire et raccourcir "
          "par l'humain avant publication.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
