#!/usr/bin/env python3
"""Auto-amorçage des outils vidéo — ZÉRO installation utilisateur (stdlib).

Principe : l'agent installe toutes les dépendances DANS le workspace (binaires
statiques locaux, aucun droit admin, aucune action utilisateur), après avoir
ANNONCÉ ce qu'il va télécharger (tailles) et obtenu UNE confirmation globale.
Tourne à la première invocation d'un skill vidéo.

Étages :
  - ffmpeg/ffprobe : détection PATH → sinon `npm i` LOCAL de `ffmpeg-static` +
    `@ffprobe-installer/ffprobe` (binaires win/mac/linux). Licence : binaires
    appelés en SOUS-PROCESSUS (usage-outil, pas de code lié) → OK commercial.
  - Transcription (2 voies, choix mémorisé) :
      * `faster-whisper` (pip) — modèle téléchargé au 1er usage (poids annoncé) ;
      * `scribe` — 100 % distant via MCP ElevenLabs (payant), aucun local.
  - OpenMontage : OPTIONNEL avancé, jamais requis, installé seulement sur demande
    explicite (~161 Mo, AGPL — cloné en dossier FRÈRE, jamais dans le dépôt).
  - Remotion : via `npx`/npm (Chromium headless auto-téléchargé par Remotion).

Sorties : `rapido-kb/outils-locaux.md` (chemins résolus + choix de transcription)
— fichier KB côté client (gitignoré), jamais dans le dépôt.

Usage :
  python3 bootstrap_video.py --check                 # détection seule (aucun DL)
  python3 bootstrap_video.py --plan ffmpeg,whisper   # annonce tailles + plan
  python3 bootstrap_video.py --install ffmpeg,whisper --yes   # installe (confirmé)
  python3 bootstrap_video.py --transcription scribe --yes     # mémorise le mode distant
Options : --whisper-model {tiny,base,small}  --with-openmontage  --with-remotion
"""
import argparse
import json
import os
import platform
import shutil
import subprocess
import sys

WORKSPACE = os.getcwd()
TOOLS_DIR = os.path.join(WORKSPACE, ".video-tools")   # node_modules local des binaires
KB_DIR = os.path.join(WORKSPACE, "rapido-kb")
KB_FILE = os.path.join(KB_DIR, "outils-locaux.md")

# Tailles indicatives annoncées AVANT tout téléchargement (Mo).
POIDS = {
    "ffmpeg": ("ffmpeg-static + @ffprobe-installer/ffprobe", 110),
    "whisper-tiny": ("faster-whisper + modèle tiny", 120),
    "whisper-base": ("faster-whisper + modèle base", 200),
    "whisper-small": ("faster-whisper + modèle small", 550),
    "openmontage": ("OpenMontage (clone AGPL, dossier frère)", 161),
    "remotion": ("Remotion + Chromium headless", 400),
}


def which(name):
    return shutil.which(name)


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def detect():
    """État courant des outils (aucun téléchargement)."""
    etat = {
        "os": platform.system(), "arch": platform.machine(),
        "ffmpeg": which("ffmpeg"), "ffprobe": which("ffprobe"),
        "node": which("node"), "npm": which("npm"), "npx": which("npx"),
        "python": sys.executable, "pip": which("pip") or which("pip3"),
        "faster_whisper": _pip_has("faster_whisper"),
        "ffmpeg_local": _local_ffmpeg(),
    }
    return etat


def _pip_has(mod):
    r = run([sys.executable, "-c", f"import {mod}"])
    return r.returncode == 0


def _local_ffmpeg():
    """Chemins des binaires installés localement via npm, s'ils existent."""
    ff = os.path.join(TOOLS_DIR, "node_modules", "ffmpeg-static", "ffmpeg")
    fp_dir = os.path.join(TOOLS_DIR, "node_modules", "@ffprobe-installer")
    ffprobe = None
    if os.path.isdir(fp_dir):
        for root, _d, files in os.walk(fp_dir):
            for f in files:
                if f in ("ffprobe", "ffprobe.exe"):
                    ffprobe = os.path.join(root, f)
    ff = ff if os.path.exists(ff) else (ff + ".exe" if os.path.exists(ff + ".exe") else None)
    return {"ffmpeg": ff, "ffprobe": ffprobe}


def _imageio_ffmpeg():
    """ffmpeg fourni par le wheel PyPI imageio-ffmpeg (repli anti github-403)."""
    r = run([sys.executable, "-c",
             "import imageio_ffmpeg,sys; sys.stdout.write(imageio_ffmpeg.get_ffmpeg_exe())"])
    return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else None


def resoudre_ffmpeg(etat):
    """Retourne (ffmpeg, ffprobe) : PATH d'abord, sinon npm local, sinon wheel PyPI.

    Note : le repli PyPI (imageio-ffmpeg) fournit ffmpeg mais PAS ffprobe — le
    probing retombe sur `ffmpeg -i` quand ffprobe est absent.
    """
    ffmpeg = (etat["ffmpeg"] or (etat["ffmpeg_local"] or {}).get("ffmpeg")
              or _imageio_ffmpeg())
    ffprobe = etat["ffprobe"] or (etat["ffmpeg_local"] or {}).get("ffprobe")
    return ffmpeg, ffprobe


def plan(cibles, whisper_model):
    lignes, total = [], 0
    for c in cibles:
        key = f"whisper-{whisper_model}" if c == "whisper" else c
        nom, mo = POIDS.get(key, (c, 0))
        lignes.append(f"  - {nom} : ~{mo} Mo")
        total += mo
    return "\n".join(lignes), total


def install_ffmpeg():
    os.makedirs(TOOLS_DIR, exist_ok=True)
    pkg = os.path.join(TOOLS_DIR, "package.json")
    if not os.path.exists(pkg):
        with open(pkg, "w") as f:
            json.dump({"name": "video-tools", "private": True}, f)
    r = run(["npm", "install", "--no-audit", "--no-fund",
             "ffmpeg-static", "@ffprobe-installer/ffprobe"], cwd=TOOLS_DIR)
    loc = _local_ffmpeg()
    for b in ("ffmpeg", "ffprobe"):
        if loc.get(b) and os.path.exists(loc[b]):
            os.chmod(loc[b], 0o755)
    if loc.get("ffmpeg") and loc.get("ffprobe"):
        return True, {"voie": "npm ffmpeg-static", **loc}
    # Repli : les binaires npm sont téléchargés depuis github (releases) — bloqué
    # sur certains réseaux (proxy 403). Le wheel PyPI imageio-ffmpeg embarque
    # ffmpeg (files.pythonhosted.org) → repli robuste (ffmpeg seul, pas ffprobe).
    rp = run([sys.executable, "-m", "pip", "install", "--quiet", "imageio-ffmpeg"])
    ff = _imageio_ffmpeg()
    if ff:
        return True, {"voie": "pip imageio-ffmpeg (repli github-403)", "ffmpeg": ff,
                      "ffprobe": None, "note": "ffprobe absent → probing via `ffmpeg -i`"}
    return False, (r.stderr[-300:] + " | pip: " + rp.stderr[-200:])


def install_whisper():
    r = run([sys.executable, "-m", "pip", "install", "--quiet", "faster-whisper"])
    return r.returncode == 0, (r.stderr[-400:] if r.returncode else "ok")


def ecrire_kb(etat, transcription_mode, whisper_model):
    os.makedirs(KB_DIR, exist_ok=True)
    ffmpeg, ffprobe = resoudre_ffmpeg(etat)
    contenu = f"""# Outils locaux vidéo (auto-amorçés)

> Écrit par `scripts/bootstrap_video.py`. Fichier KB côté client (gitignoré) —
> jamais dans le dépôt. Régénérer via `python3 scripts/bootstrap_video.py --install …`.

## Environnement
- OS / arch : {etat['os']} / {etat['arch']}
- node : {etat['node']} · npm : {etat['npm']} · python : {etat['python']}

## Binaires résolus (appelés en sous-processus — usage-outil, licences OK commercial)
- ffmpeg  : {ffmpeg or 'ABSENT (lancer --install ffmpeg)'}
- ffprobe : {ffprobe or 'ABSENT (lancer --install ffmpeg)'}

## Transcription
- Mode choisi : **{transcription_mode}**
  - `faster-whisper` : local, modèle `{whisper_model}` (téléchargé au 1er usage) ;
  - `scribe` : 100 % distant via MCP ElevenLabs (payant), aucun local.
"""
    with open(KB_FILE, "w", encoding="utf-8") as f:
        f.write(contenu)
    return KB_FILE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--plan", default="")
    ap.add_argument("--install", default="")
    ap.add_argument("--transcription", choices=["faster-whisper", "scribe"])
    ap.add_argument("--whisper-model", default="small", choices=["tiny", "base", "small"])
    ap.add_argument("--with-openmontage", action="store_true")
    ap.add_argument("--with-remotion", action="store_true")
    ap.add_argument("--yes", action="store_true", help="confirmation globale des téléchargements")
    a = ap.parse_args()

    etat = detect()

    if a.check or (not a.plan and not a.install and not a.transcription):
        ffmpeg, ffprobe = resoudre_ffmpeg(etat)
        print(json.dumps({
            "os": etat["os"], "arch": etat["arch"],
            "ffmpeg": ffmpeg, "ffprobe": ffprobe,
            "faster_whisper_installe": etat["faster_whisper"],
            "node": bool(etat["node"]), "npm": bool(etat["npm"]),
        }, ensure_ascii=False, indent=2))
        return 0

    cibles = [c.strip() for c in (a.plan or a.install).split(",") if c.strip()]
    if a.with_openmontage:
        cibles.append("openmontage")
    if a.with_remotion:
        cibles.append("remotion")

    detail, total = plan(cibles, a.whisper_model)
    print(f"📦 Amorçage vidéo — téléchargements prévus :\n{detail}\n  TOTAL ~{total} Mo")

    if a.plan:  # annonce seule
        print("→ Relancer avec --install <cibles> --yes pour confirmer.")
        return 0

    if not a.yes:
        print("⛔ Confirmation requise : ajouter --yes pour lancer les téléchargements.")
        return 2

    if "ffmpeg" in cibles:
        ok, info = install_ffmpeg()
        print(f"ffmpeg-static : {'OK' if ok else 'ÉCHEC'} {info if not ok else ''}")
        etat = detect()
    if "whisper" in cibles:
        ok, info = install_whisper()
        print(f"faster-whisper : {'OK' if ok else 'ÉCHEC'} — modèle {a.whisper_model} au 1er usage")
        etat = detect()

    mode = a.transcription or ("faster-whisper" if "whisper" in cibles else "scribe")
    kb = ecrire_kb(etat, mode, a.whisper_model)
    print(f"✅ Chemins et choix écrits dans {kb}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
