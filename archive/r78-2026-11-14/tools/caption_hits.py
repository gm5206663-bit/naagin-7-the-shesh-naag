#!/usr/bin/env python3
"""tools/caption_hits.py — keyword search across the Hindi caption tracks.

    python3 tools/caption_hits.py 'REGEX' [width=120] [max_per_episode=4] [E05,E06]
    python3 tools/caption_hits.py --selftest

Run from the workshop root. The tracks are in `captions/` as `E##.hi.txt`, one cue per line, written
`[00:18:17] …the line…`, and **the lines are in Devanagari** — `नागमणि`, `शाप`, not `naagmani`, `shraap`.
Unpack the archive first if the folder holds only the zip.

Why the summary line and the exit code exist. The old version printed `TOTAL shown 0` whether the word
was genuinely absent from fifty episodes or the folder was empty, or the searcher had typed the word in
Latin letters. `L-25`'s rule for an unevidenced fact is *change it*, so the tool now says how many
tracks it read, and refuses to be read as a verdict when it read none. `tools/README.md`'s table
carries the same sentence.
"""
import glob
import io
import os
import contextlib
import re
import sys
import tempfile


def hits(pat, width=120, maxper=4, eps=None, root="captions"):
    """Print every cue of every track matching `pat`. Returns (tracks read, hits shown)."""
    rx = re.compile(pat)
    n = 0
    read = 0
    for f in sorted(glob.glob(os.path.join(root, "E*.hi.txt"))):
        ep = os.path.basename(f)[:3]
        if eps and ep not in eps:
            continue
        read += 1
        c = 0
        for line in open(f, encoding="utf-8"):
            m = re.match(r"\[(\d\d:\d\d:\d\d)\]\s*(.*)", line)
            if not m:
                continue
            ts, txt = m.groups()
            for mm in rx.finditer(txt):
                a = max(0, mm.start() - width)
                b = min(len(txt), mm.end() + width)
                print(f"{ep} {ts} …{txt[a:b]}…")
                c += 1
                n += 1
                if c >= maxper:
                    break
            if c >= maxper:
                break
    print(f"TRACKS read {read}, HITS shown {n}")
    if n == 0 and read:
        # the failure mode that produced a wrong "it is not in the episode": a Latin pattern cannot
        # match a Devanagari track, and the count cannot tell that from an absence.
        if all(ord(ch) < 128 for ch in pat):
            print("NOTE   zero hits with a Latin-script pattern over Devanagari tracks — search the "
                  "word as it is written (नागमणि, शाप, अगली), or this proves nothing")
    return read, n


def selftest():
    ok = True
    d = tempfile.mkdtemp(prefix="caption_hits_")
    with open(os.path.join(d, "E99.hi.txt"), "w", encoding="utf-8") as fh:
        fh.write("[00:12:34] वीरापुर का राजा अपनी बेटी को नागिन बनाता है।\n"
                 "not a cue line — no time mark, so it is not searchable\n"
                 "[00:13:01] वह शीशे में अपनी आँखें देखती है।\n")
    with open(os.path.join(d, "E98.hi.txt"), "w", encoding="utf-8") as fh:
        fh.write("[00:01:00] कोई दूसरी लाइन।\n")

    def run(*a, **k):
        buf = io.StringIO()
        k.setdefault("root", d)
        with contextlib.redirect_stdout(buf):
            got = hits(*a, **k)
        return got, buf.getvalue()

    got, out = run("आँखें")
    print("selftest a word that is there, in the tracks' own script:", "ok" if got == (2, 1) else f"FAILED {got}")
    ok &= got == (2, 1)
    got, out = run("राजा|दूसरी")
    print("selftest a word in each track is counted in both:", "ok" if got == (2, 2) else f"FAILED {got}")
    ok &= got == (2, 2)
    got, out = run("aankhein")
    good = got[1] == 0 and "Latin-script pattern" in out
    print("selftest a Latin pattern that finds nothing says the script is why:", "ok" if good else f"FAILED {got} / {out.strip().splitlines()[-1:]}")
    ok &= good
    got, out = run("छोटी छवि", maxper=1)
    print("selftest an absent Devanagari phrase reads as a plain zero:", "ok" if got[1] == 0 and "Latin" not in out else f"FAILED {out!r}")
    ok &= got[1] == 0 and "Latin" not in out
    got, out = run("कुछ भी", root=d + "_missing")
    print("selftest an unreadable folder is zero tracks, not zero hits:", "ok" if got == (0, 0) else f"FAILED {got}")
    ok &= got == (0, 0)
    print("\nSELFTEST " + ("green" if ok else "RED"))
    return 0 if ok else 1


if __name__ == "__main__":
    a = sys.argv
    if "--selftest" in a:
        sys.exit(selftest())
    if len(a) < 2:
        print(__doc__)
        sys.exit(2)
    read, n = hits(a[1], int(a[2]) if len(a) > 2 else 120, int(a[3]) if len(a) > 3 else 4,
                   set(a[4].split(",")) if len(a) > 4 else None)
    if read == 0:
        print("NO CAPTION TRACKS in captions/ — the archive is not unpacked here; this run proves nothing")
        sys.exit(2)
