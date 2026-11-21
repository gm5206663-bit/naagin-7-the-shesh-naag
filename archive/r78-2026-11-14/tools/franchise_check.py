#!/usr/bin/env python3
"""franchise_check.py — measure the nine chapters against the ten devices in
canon/FRANCHISE_STYLE.md. Descriptive, not a gate: it prints a matrix and a
percentage, and never fails the build. Run: python3 tools/franchise_check.py
"""
import re, sys, glob, os

DEVICES = [
    ("hiss",       r"\bhiss|fuhkaar|phunkaar"),
    ("been",       r"\bbeen\b|bansuri|sapera"),
    ("scales",     r"\bscale|khaal\b|kechuli|papdi"),
    ("hood",       r"\bhood\b"),
    ("fangs",      r"\bfang"),
    ("venom",      r"\bvenom|poison|zeher|zahar"),
    ("eye-change", r"yellow|peeli|gold.{0,20}eye|eye.{0,20}gold|pupil"),
    ("wind",       r"\bwind\b|hawa\b"),
    ("mirror",     r"\bmirror|aaina|sheesha"),
    ("moon",       r"\bmoon\b|chand|purnima|poornima"),
    ("vow",        r"\bkasam\b|qasam|vachan|shapath"),
    ("titles",     r"naagrani|naaginon ke naagin|shesh naagin|mahasapera|sarva"),
    ("stolenface", r"chehra.{0,40}nahin|face.{0,30}not his|same face|uska chehra|unka chehra"),
    ("deadeye",    r"aankh.{0,60}khuli|eyes? open|dead.{0,30}eye"),
]

def main():
    files = sorted(glob.glob("chapters/Chapter_*.md"))
    if not files:
        sys.exit("run from the workshop root")
    hits = {name: [] for name, _ in DEVICES}
    for f in files:
        text = open(f, encoding="utf-8").read()
        n = int(re.search(r"Chapter_(\d+)", f).group(1))
        for name, pat in DEVICES:
            if re.search(pat, text, re.I):
                hits[name].append(n)
    print("device        chapters                           count")
    print("-" * 58)
    for name, _ in DEVICES:
        got = hits[name]
        print(f"{name:<13} {','.join(map(str, got)) or '—':<34} {len(got)}/{len(files)}")
    body = ["scales", "fangs", "venom", "hiss", "eye-change"]
    omen = ["wind", "mirror", "moon"]
    b = sum(len(hits[k]) for k in body)
    o = sum(len(hits[k]) for k in omen)
    print("-" * 58)
    print(f"body devices  {b}/{len(body)*len(files)}   omen devices  {o}/{len(omen)*len(files)}")
    print("target from Episode 4: at least one body device per chapter (canon/FRANCHISE_STYLE.md §7)")

if __name__ == "__main__":
    main()
