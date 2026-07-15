#!/usr/bin/env python3
"""Sous-titres — Whisper local → SRT → burn-in (stdlib + faster-whisper + ffmpeg).

100 % libre. Transcription locale (aucune clé, aucun crédit) ; le SRT est
**corrigible par l'utilisateur** avant le burn-in. Deux sous-commandes :
  transcribe <media> --language auto|fr|en… --model tiny|base|small -o sous.srt
  burn <video> --srt sous.srt -o sortie.mp4 [--font --size --safe 9:16]

ffmpeg est résolu comme dans `monter.py` (KB → PATH → imageio-ffmpeg). Le modèle
NE devine PAS les timecodes : ils viennent de Whisper.
"""
import argparse
import os
import re
import subprocess
import sys


def resolve_ffmpeg():
    import shutil
    if shutil.which("ffmpeg"):
        return shutil.which("ffmpeg")
    kb = os.path.join("rapido-kb", "outils-locaux.md")
    if os.path.isfile(kb):
        for line in open(kb, encoding="utf-8"):
            m = re.match(r"- ffmpeg\s*:\s*(\S+)", line)
            if m and os.path.exists(m.group(1)):
                return m.group(1)
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def ts(sec):
    h = int(sec // 3600); m = int((sec % 3600) // 60)
    s = int(sec % 60); ms = int((sec - int(sec)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def op_transcribe(a):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("faster-whisper absent — lancer scripts/bootstrap_video.py --install whisper --yes\n"
              "OU utiliser le mode distant (Scribe MCP ElevenLabs).", file=sys.stderr)
        return 2
    lang = None if a.language in ("auto", "", None) else a.language
    model = WhisperModel(a.model, device="cpu", compute_type="int8")
    segs, info = model.transcribe(a.media, language=lang)
    n = 0
    with open(a.output, "w", encoding="utf-8") as f:
        for seg in segs:
            n += 1
            f.write(f"{n}\n{ts(seg.start)} --> {ts(seg.end)}\n{seg.text.strip()}\n\n")
    print(f"{a.output} : {n} segments · langue détectée={info.language}")
    if n == 0:
        print("(aucune parole détectée — vérifier l'audio source)", file=sys.stderr)
    return 0


def op_burn(a):
    ff = resolve_ffmpeg()
    if not ff:
        print("ffmpeg introuvable — bootstrap_video.py --install ffmpeg --yes", file=sys.stderr)
        return 2
    # safe zones 9:16 : marge basse 170 px (défaut) — respecter le champ visible
    margin_v = a.margin_v
    style = (f"FontName={a.font},Fontsize={a.size},PrimaryColour=&HFFFFFF&,"
             f"Outline=2,Shadow=1,MarginV={margin_v}")
    srt = a.srt.replace("\\", "/").replace(":", r"\:")
    cmd = [ff, "-y", "-hide_banner", "-loglevel", "error", "-i", a.input,
           "-vf", f"subtitles={srt}:force_style='{style}'", "-c:a", "copy", a.output]
    print("  ffmpeg subtitles burn-in →", a.output, file=sys.stderr)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERREUR ffmpeg:\n" + r.stderr[-600:], file=sys.stderr)
        return 1
    print(a.output)
    return 0


def main():
    p = argparse.ArgumentParser(description="Whisper → SRT → burn-in.")
    sub = p.add_subparsers(dest="op", required=True)
    t = sub.add_parser("transcribe")
    t.add_argument("media")
    t.add_argument("--language", default="auto")
    t.add_argument("--model", default="small", choices=["tiny", "base", "small"])
    t.add_argument("-o", "--output", required=True)
    t.set_defaults(fn=op_transcribe)
    b = sub.add_parser("burn")
    b.add_argument("input")
    b.add_argument("--srt", required=True)
    b.add_argument("--font", default="DejaVu Sans")
    b.add_argument("--size", type=int, default=28)          # ≈ 28 px éq. (min charte)
    b.add_argument("--margin-v", dest="margin_v", type=int, default=170)  # safe zone bas 9:16
    b.add_argument("-o", "--output", required=True)
    b.set_defaults(fn=op_burn)
    a = p.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
