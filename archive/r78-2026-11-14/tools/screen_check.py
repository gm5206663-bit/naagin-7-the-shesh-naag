#!/usr/bin/env python3
"""screen_check.py — the furniture in the chapters: what is heard and what is behind
the actors (canon/SOUND_AND_SCREEN.md). Descriptive, never fails the build.
Run from the workshop root: python3 tools/screen_check.py
"""
import re, glob

REGISTERS = [
    ("been / sapera",   r"\bbeen\b|bansuri|sapera|pungi"),
    ("a named song",    r"title song|love theme|\bsong\b.{0,40}(plays|starts|comes on)"),
    ("love theme",      r"love theme|their theme"),
    ("his cue (Ek Taar)",r"Ek Taar|one low string|the string he (is given|leaves)"),
    ("their theme (Woh Do Log)", r"Woh Do Log"),
    ("the cut declared",   r"no score|the score (goes out|stops|has no part)"),
    ("power / devotion",r"aarti|conch|shankh|chant|mantra|tandav|dhol|drum"),
    ("the sting",       r"\bsting\b|surge|the score stops|music stops"),
    ("rain",            r"\brain\b|barish|baaris|downpour"),
    ("moon",            r"\bmoon\b|chand|purnima|poornima"),
    ("lamps / diya",    r"\blamp|diya|deepak|chandelier"),
    ("festival",        r"mehendi|mehndi|haldi|sangeet|marigold|genda|\bdhol\b|baraat"),
    ("gold",            r"\bgold"),
    ("green",           r"\bgreen"),
    ("crimson / red",   r"\bred\b|crimson|laal"),
    ("a song sequence", r"song sequence|montage"),
]

def main():
    files = sorted(glob.glob("chapters/Chapter_*.md"))
    if not files:
        raise SystemExit("run from the workshop root")
    print(f"{'register':<18}{'chapters':<24}{'uses':>5}")
    print("-" * 48)
    for name, pat in REGISTERS:
        ch, n = [], 0
        for f in files:
            t = open(f, encoding="utf-8").read()
            k = len(re.findall(pat, t, re.I))
            if k:
                ch.append(re.search(r"Chapter_(\d+)", f).group(1))
                n += k
        print(f"{name:<18}{','.join(ch) or '—':<24}{n:>5}")
    print("-" * 48)
    print("target from Chapter 10 (SOUND_AND_SCREEN.md §8): one named cue per chapter,")
    print("rain before the fourth meeting's aftermath, the festival with the sangeet,")
    print("and a precap at every chapter's foot.")

if __name__ == "__main__":
    main()
