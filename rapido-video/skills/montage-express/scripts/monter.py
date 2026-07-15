#!/usr/bin/env python3
"""Wrapper ffmpeg — recettes de montage (stdlib + subprocess). 100 % libre.

Le modèle n'écrit JAMAIS une commande ffmpeg de tête : il appelle une **recette**
de ce script. Chaque sous-commande imprime la commande ffmpeg exécutée (auditable).
ffmpeg est résolu depuis `rapido-kb/outils-locaux.md` (bootstrap), sinon PATH,
sinon le wheel PyPI `imageio-ffmpeg`.

Recettes : probe · normalize · concat · cut · xfade · overlay-logo · reframe
(crop|blur) · speed · extract-audio · mix · remove-silence · burn-srt · preset.

Usage : python3 monter.py <recette> [options]  (voir --help par recette).
"""
import argparse
import os
import re
import shlex
import subprocess
import sys

PRESETS = {   # plateforme -> (largeur, hauteur, fps)
    "reels": (1080, 1920, 30), "tiktok": (1080, 1920, 30),
    "shorts": (1080, 1920, 30), "linkedin": (1080, 1080, 30),
    "youtube": (1920, 1080, 30),
}
RATIOS = {"9:16": (1080, 1920), "1:1": (1080, 1080), "16:9": (1920, 1080)}
POS = {"tl": "10:10", "tr": "W-w-10:10", "bl": "10:H-h-10", "br": "W-w-10:H-h-10"}


def resolve_ffmpeg():
    """PATH → rapido-kb/outils-locaux.md → imageio-ffmpeg (repli PyPI)."""
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


FF = None  # résolu dans main()


def run_ff(args, out=None):
    cmd = [FF, "-y", "-hide_banner", "-loglevel", "error"] + args
    print("  ffmpeg " + " ".join(shlex.quote(a) for a in args), file=sys.stderr)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERREUR ffmpeg:\n" + r.stderr[-800:], file=sys.stderr)
        sys.exit(1)
    if out:
        print(out)
    return r


def duration(path):
    r = subprocess.run([FF, "-hide_banner", "-i", path], capture_output=True, text=True)
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", r.stderr)
    if not m:
        return None
    h, mn, s = m.groups()
    return int(h) * 3600 + int(mn) * 60 + float(s)


# ------------------------------------------------------------------- recettes
def op_probe(a):
    d = duration(a.input)
    print(f"{a.input} : durée={d}s")


def op_normalize(a):
    """Uniformise en 1080p / 30 fps / h264 + aac (préalable au concat)."""
    w, h = 1920, 1080
    run_ff(["-i", a.input,
            "-vf", f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
                   f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30",
            "-c:v", "libx264", "-crf", "20", "-c:a", "aac", "-ar", "48000",
            a.output], out=a.output)


def op_concat(a):
    """Concat par filtre concat (ré-encodage sûr). Normaliser d'abord si formats différents."""
    inp = []
    for f in a.inputs:
        inp += ["-i", f]
    n = len(a.inputs)
    streams = "".join(f"[{i}:v][{i}:a]" for i in range(n))
    run_ff(inp + ["-filter_complex", f"{streams}concat=n={n}:v=1:a=1[v][a]",
                  "-map", "[v]", "-map", "[a]", a.output], out=a.output)


def op_cut(a):
    run_ff(["-ss", str(a.start), "-to", str(a.end), "-i", a.input,
            "-c:v", "libx264", "-crf", "20", "-c:a", "aac", a.output], out=a.output)


def op_xfade(a):
    off = a.offset if a.offset is not None else max(0.0, (duration(a.first) or 1) - a.duration)
    run_ff(["-i", a.first, "-i", a.second, "-filter_complex",
            f"[0:v][1:v]xfade=transition=fade:duration={a.duration}:offset={off}[v];"
            f"[0:a][1:a]acrossfade=d={a.duration}[a]",
            "-map", "[v]", "-map", "[a]", a.output], out=a.output)


def op_overlay_logo(a):
    xy = POS.get(a.pos, POS["br"])
    run_ff(["-i", a.input, "-i", a.logo, "-filter_complex",
            f"[1:v]scale=iw*{a.scale}:-1[lg];[0:v][lg]overlay={xy}",
            "-c:a", "copy", a.output], out=a.output)


def op_reframe(a):
    w, h = RATIOS[a.target]
    if a.mode == "blur":
        vf = (f"split[a][b];[b]scale={w}:{h}:force_original_aspect_ratio=increase,"
              f"crop={w}:{h},gblur=sigma=20[bg];"
              f"[a]scale={w}:{h}:force_original_aspect_ratio=decrease[fg];"
              f"[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1")
    else:  # crop intelligent (centre)
        vf = (f"scale={w}:{h}:force_original_aspect_ratio=increase,"
              f"crop={w}:{h},setsar=1")
    run_ff(["-i", a.input, "-vf", vf, "-c:a", "copy", a.output], out=a.output)


def op_speed(a):
    # vidéo : setpts=1/f ; audio : atempo (chaîné si hors [0.5,2])
    f = a.factor
    at, rem = [], f
    while rem > 2.0:
        at.append("atempo=2.0"); rem /= 2.0
    while rem < 0.5:
        at.append("atempo=0.5"); rem /= 0.5
    at.append(f"atempo={rem:.4f}")
    run_ff(["-i", a.input, "-filter_complex",
            f"[0:v]setpts={1/f}*PTS[v];[0:a]{','.join(at)}[a]",
            "-map", "[v]", "-map", "[a]", a.output], out=a.output)


def op_extract_audio(a):
    run_ff(["-i", a.input, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", a.output],
           out=a.output)


def op_mix(a):
    """Mix voix (piste vidéo) + musique. --sidechain baisse la musique sous la voix."""
    if a.sidechain:
        fc = ("[0:a]asplit=2[voix][sc];"
              "[1:a][sc]sidechaincompress=threshold=0.03:ratio=8:release=300[duck];"
              "[voix][duck]amix=inputs=2:duration=first[a]")
    else:
        fc = "[0:a][1:a]amix=inputs=2:duration=first:weights=1 0.3[a]"
    run_ff(["-i", a.input, "-i", a.music, "-filter_complex", fc,
            "-map", "0:v", "-map", "[a]", "-c:v", "copy", a.output], out=a.output)


def op_remove_silence(a):
    """Détecte les silences (silencedetect) puis coupe (pattern auto-video-edit, MIT)."""
    r = subprocess.run([FF, "-hide_banner", "-i", a.input, "-af",
                        f"silencedetect=noise={a.threshold}dB:d={a.min_silence}",
                        "-f", "null", "-"], capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r"silence_start:\s*([\d.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end:\s*([\d.]+)", r.stderr)]
    total = duration(a.input) or 0
    # segments à GARDER = complément des silences
    keep, cur = [], 0.0
    for s, e in zip(starts, ends):
        if s > cur:
            keep.append((cur, s))
        cur = e
    if cur < total:
        keep.append((cur, total))
    if not keep:
        print("Aucun silence détecté (ou tout silence) — sortie = entrée.", file=sys.stderr)
        keep = [(0.0, total)]
    sel = "+".join(f"between(t,{s:.3f},{e:.3f})" for s, e in keep)
    run_ff(["-i", a.input, "-vf", f"select='{sel}',setpts=N/FRAME_RATE/TB",
            "-af", f"aselect='{sel}',asetpts=N/SR/TB", a.output],
           out=f"{a.output}  (segments gardés: {len(keep)})")


def op_burn_srt(a):
    style = (f"FontName={a.font},Fontsize={a.size},PrimaryColour=&HFFFFFF&,"
             f"Outline=2,Shadow=1,MarginV={a.margin_v}")
    srt = a.srt.replace("\\", "/").replace(":", r"\:")
    run_ff(["-i", a.input, "-vf", f"subtitles={srt}:force_style='{style}'",
            "-c:a", "copy", a.output], out=a.output)


def op_preset(a):
    w, h, fps = PRESETS[a.platform]
    vf = (f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
          f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={fps}")
    run_ff(["-i", a.input, "-vf", vf, "-c:v", "libx264", "-crf", "21",
            "-c:a", "aac", "-b:a", "128k", a.output],
           out=f"{a.output}  (preset {a.platform} {w}x{h}@{fps})")


def main():
    global FF
    p = argparse.ArgumentParser(description="Recettes ffmpeg de montage.")
    sub = p.add_subparsers(dest="op", required=True)

    def add(name, fn, args):
        sp = sub.add_parser(name)
        for flags, kw in args:
            sp.add_argument(*flags, **kw)
        sp.set_defaults(fn=fn)

    outp = (["-o", "--output"], {"required": True})
    add("probe", op_probe, [(["input"], {})])
    add("normalize", op_normalize, [(["input"], {}), outp])
    add("concat", op_concat, [(["inputs"], {"nargs": "+"}), outp])
    add("cut", op_cut, [(["input"], {}), (["--start"], {"required": True}),
                        (["--end"], {"required": True}), outp])
    add("xfade", op_xfade, [(["first"], {}), (["second"], {}),
                            (["--duration"], {"type": float, "default": 1.0}),
                            (["--offset"], {"type": float, "default": None}), outp])
    add("overlay-logo", op_overlay_logo, [(["input"], {}), (["--logo"], {"required": True}),
                                          (["--pos"], {"default": "br"}),
                                          (["--scale"], {"type": float, "default": 0.12}), outp])
    add("reframe", op_reframe, [(["input"], {}), (["--target"], {"choices": list(RATIOS), "required": True}),
                                (["--mode"], {"choices": ["crop", "blur"], "default": "crop"}), outp])
    add("speed", op_speed, [(["input"], {}), (["--factor"], {"type": float, "required": True}), outp])
    add("extract-audio", op_extract_audio, [(["input"], {}), outp])
    add("mix", op_mix, [(["input"], {}), (["--music"], {"required": True}),
                        (["--sidechain"], {"action": "store_true"}), outp])
    add("remove-silence", op_remove_silence, [(["input"], {}),
                                              (["--threshold"], {"type": float, "default": -30}),
                                              (["--min-silence"], {"type": float, "default": 0.5}), outp])
    add("burn-srt", op_burn_srt, [(["input"], {}), (["--srt"], {"required": True}),
                                  (["--font"], {"default": "DejaVu Sans"}),
                                  (["--size"], {"type": int, "default": 28}),
                                  (["--margin-v"], {"type": int, "default": 170}), outp])
    add("preset", op_preset, [(["input"], {}), (["--platform"], {"choices": list(PRESETS), "required": True}), outp])

    a = p.parse_args()
    FF = resolve_ffmpeg()
    if not FF:
        print("ffmpeg introuvable — lancer d'abord scripts/bootstrap_video.py --install ffmpeg --yes",
              file=sys.stderr)
        return 2
    a.fn(a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
