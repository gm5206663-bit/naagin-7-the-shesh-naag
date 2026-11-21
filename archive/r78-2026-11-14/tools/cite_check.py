#!/usr/bin/env python3
"""tools/cite_check.py - put every caption citation beside the caption it cites.

Run from the project folder:
    python3 tools/cite_check.py            list every (episode, time) cited in the working files
    python3 tools/cite_check.py 1 8        print the cited caption text for Episodes 1..8
    python3 tools/cite_check.py 21 21 700  the same, 700 characters per citation

It finds citations written as "Ep 21 10:18", "Episode 6 captions 00:30", "E50 03:57",
and bare times inside an "### E##" entry of canon/SEASON.md or a "### B##" beat of an
episode ledger. It proves nothing by itself: a person has to read the two side by side.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SKIP = ("canon/sources/", "captions/", "Sara/", "chapters/", "HISTORY.md")
T = r"(\d{1,2}:\d{2}(?::\d{2})?)"

def secs(t):
    p = [int(x) for x in t.split(":")]
    return p[0]*60+p[1] if len(p) == 2 else p[0]*3600+p[1]*60+p[2]

def blocks(ep):
    p = f"captions/E{ep:02d}.hi.txt"
    if not os.path.exists(p):
        return None
    out = []
    txt = open(p, encoding="utf-8").read()
    txt = re.sub(r"\[(?!\d\d:\d\d:\d\d\])[^\]]*\]\s*", "", txt)   # drop [music] and the like; keep time marks
    for m in re.finditer(r"\[(\d\d):(\d\d):(\d\d)\]([^\[]*)", txt):
        out.append((int(m.group(1))*3600+int(m.group(2))*60+int(m.group(3)), m.group(4).strip()))
    return out

cites = {}   # (ep, secs) -> [(file, context)]
for d, dirs, fs in os.walk(ROOT):
    for f in sorted(fs):
        if not f.endswith(".md"): continue
        rel = os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, "/")
        if rel.startswith(SKIP): continue
        cur = None
        m0 = re.match(r"canon/E(\d\d)_BEATS\.md", rel)
        if m0: cur = int(m0.group(1))
        for line in open(rel, encoding="utf-8"):
            h = re.match(r"###? E(\d\d)\b", line)
            if rel == "canon/SEASON.md" and h: cur = int(h.group(1))
            found = set()
            for m in re.finditer(r"(?:Ep(?:isode)?\.?|E)\s?(\d{1,2})(?:\s+captions?)?,?\s+((?:"+T+r"(?:[–-]"+T+r")?(?:,\s*|\s+and\s+)?)+)", line):
                ep = int(m.group(1))
                for t in re.findall(T, m.group(2)):
                    found.add((ep, secs(t)))
            if cur is not None:
                for t in re.findall(r"(?<![\d:])"+T+r"(?!\d|:\d)", line):
                    if not any(s == secs(t) for (_, s) in found):
                        found.add((cur, secs(t)))
            for k in found:
                cites.setdefault(k, []).append((rel, line.strip()[:160]))

keys = sorted(cites)
if len(sys.argv) < 3:
    by = {}
    for ep, s in keys: by.setdefault(ep, []).append(s)
    print(len(keys), "citations over", len(by), "episodes")
    for ep in sorted(by):
        print(f"E{ep:02d}:", " ".join(f"{s//60:02d}:{s%60:02d}" for s in by[ep]))
    sys.exit(0)

lo, hi = int(sys.argv[1]), int(sys.argv[2])
width = int(sys.argv[3]) if len(sys.argv) > 3 else 420
for ep, s in keys:
    if not lo <= ep <= hi: continue
    b = blocks(ep)
    print(f"\n== E{ep:02d} {s//60:02d}:{s%60:02d}  <- " + " | ".join(sorted({c[0] for c in cites[(ep, s)]})))
    print("   CLAIM:", cites[(ep, s)][0][1])
    if b is None:
        print("   NO CAPTION TRACK"); continue
    idx = max((i for i, (t, _) in enumerate(b) if t <= s), default=0)
    text = " ".join(f"[{t//60:02d}:{t%60:02d}] {x}" for t, x in b[idx:idx+3])
    print("   TRACK:", re.sub(r"\[संगीत\]\s*", "", text)[:width])
