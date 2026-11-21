#!/usr/bin/env python3
"""thread_check.py — is Vihaan in the chapter, or only visiting it?

    python3 tools/thread_check.py                 (every chapter)
    python3 tools/thread_check.py chapters/Chapter_04_*.md
    python3 tools/thread_check.py --floor 60      (fail below this percentage)

Why this exists. `oc_check.py` asks whether he is present and whether anybody looks
at him. It passed for a year of chapters in which he was in the room for two scenes
and canon ran untouched for the other twenty. The count this tool prints is the one
that was never printed: of a chapter's scenes, how many carry a trace of him at all.

A scene declared under `FENCE:` in the chapter footer is out of the count, in the numerator
and in the denominator both. The fence is canon's, not the writer's comfort: SUPERNATURAL.md
section 2 and a ledger's own section 3 say which rooms he may not be in, and a chapter may
not buy a percentage by putting him in a room where the naag world is spoken. The line lists
the scene headings separated by ` · `, and every declared heading must exist in the chapter:
a fence that names nothing is a hole.

A trace is any one of:
    PRESENT   his name, or the house's name for him, in the scene
    MOUTH     another character says his name, or speaks to him, inside quotes
    OBJECT    something of his — the gate book, the charter, the ledgers, the desk,
              his signature, the money, the register
    COST      someone is doing something, or cannot do something, because of him

A scene with none of the four is a scene of the adaptation, not of this book. Two or
three of those per chapter is a seam. Twenty is a transcription.

He is a child in the 2001 chapters and a man in the present ones; the tool does not
care. It counts traces of him in either, because a father who is building a mission
is still a man with a son asleep upstairs, and the book is allowed to say so once.
"""
import glob
import re
import sys

OBJECTS = [
    'gate book', 'the book', 'register', 'ledger', 'ledgers', 'hisaab', 'charter',
    'signature', 'sign-off', 'appointment letter', 'the desk', 'his desk', 'khata',
    'the file', 'carton', 'gaadi', 'the car keys', 'keys',
]
NAMES = r'\bVihaan\b|\bchhote sahab\b|\bChhote sahab\b|\bchhote sahab\b'


def scenes(text):
    body = text.split('## Footer')[0]
    parts = re.split(r'\n## ', body)
    out = []
    for p in parts[1:]:
        title, _, rest = p.partition('\n')
        out.append((title.strip(), rest))
    return out


def traced(title, body):
    both = title + '\n' + body
    hits = []
    if re.search(NAMES, both):
        hits.append('PRESENT')
    quotes = re.findall(r'"([^"\n]{0,400})"', both)
    if any(re.search(NAMES, q) for q in quotes):
        hits.append('MOUTH')
    low = both.lower()
    if any(o in low for o in OBJECTS):
        hits.append('OBJECT')
    if re.search(r'kyunki woh|uske wajah|uski wajah|because of him|waiting for him|'
                 r'unka intezaar|uske bina|without him|uska hukm|usne kaha', low):
        hits.append('COST')
    return hits


FENCE = re.compile(r"^\s*FENCE:\s*(.+)$", re.M)


def fence(text, titles):
    m = FENCE.search(text)
    if not m:
        return set(), []
    named = [x.strip() for x in m.group(1).split("\u00b7") if x.strip()]
    bad = [x for x in named if x not in titles]
    return set(named), bad


def main(argv):
    floor = 60
    files = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--floor':
            floor = int(argv[i + 1]); i += 2; continue
        if a.endswith('.md'):
            files.append(a)
        i += 1
    if not files:
        files = sorted(glob.glob('chapters/Chapter_*.md'))

    total_s = total_t = total_named = 0
    red = []
    print(f'{"chapter":<44}{"scenes":>7}{"he is named":>13}{"carried":>9}{"share":>8}')
    for f in files:
        raw = open(f, encoding='utf-8').read()
        allsc = scenes(raw)
        fen, stray = fence(raw, [ti for ti, bb in allsc])
        if stray:
            print('!! ' + f.split('/')[-1] + ': FENCE names a scene not in the chapter: ' + ', '.join(stray))
            return 1
        sc = [(ti, bb) for ti, bb in allsc if ti not in fen]
        fenced = len(fen)
        t = sum(1 for ti, b in sc if traced(ti, b))
        named = sum(1 for ti, b in sc if set(traced(ti, b)) & {'PRESENT', 'MOUTH'})
        total_named += named
        n = len(sc)
        pct = (100 * t / n) if n else 0
        total_s += n; total_t += t
        mark = '  ' if pct >= floor else '!!'
        tail = ('   (' + str(fenced) + ' fenced)') if fenced else ''
        print(f'{mark}{f.split("/")[-1][:42]:<42}{n:>7}{named:>13}{t:>9}{pct:>7.0f}%' + tail)
        if pct < floor:
            red.append((f.split('/')[-1], n, t, pct))
        if files and len(files) < 17:
            for ti, b in sc:
                if not traced(ti, b):
                    print(f'      bare: {ti}')
    pct = 100 * total_t / total_s if total_s else 0
    print(f'\nTOTAL {total_t}/{total_s} scenes carry him = {pct:.0f}%; {total_named} of those say his name')
    if red:
        print(f'RED — {len(red)} chapter(s) below {floor}%: ' +
              ', '.join(f'{c} {p:.0f}%' for c, n, t, p in red))
        return 1
    print(f'GREEN — every chapter at or above {floor}% of its scenes carrying him.')
    return 0




FIX_ALL = """# Chapter 90

## First

Vihaan signed the sheet at the gate and the guard read the name twice.

## Second

Vihaan was told the car would wait at the second gate.

## Footer

---
"""

FIX_HALF = """# Chapter 90

## First

Vihaan signed the sheet at the gate and the guard read the name twice.

## Second

Vihaan was told the car would wait at the second gate.

## Third

The milkman came at seven and nobody in the house was awake for him.

## Fourth

The fan turned over the empty dining table and the report lay face down.

## Footer

---
"""

FIX_FENCE = FIX_ALL + """
## Footer

FENCE: A scene that is not in this chapter
"""


def selftest():
    """Three things the counting has to get right: a chapter where every scene carries him is green;
    one where half of them do not is red at the default floor of 60; and a `FENCE:` naming a scene the
    chapter does not have is refused, because a fence that names nothing buys the chapter a percentage
    it has not earned."""
    import os
    import tempfile
    d = tempfile.mkdtemp(prefix="thread_fix_")
    paths = {}
    for name, text in (("all", FIX_ALL), ("half", FIX_HALF), ("fence", FIX_FENCE)):
        p = os.path.join(d, f"Chapter_90_{name}.md")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(text)
        paths[name] = p
    import io, contextlib
    out = {}
    code = {}
    for k in ("all", "half", "fence"):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code[k] = main([paths[k]])
        out[k] = buf.getvalue()
    ok = True
    for k, want in (("all", 0), ("half", 1), ("fence", 1)):
        good = code[k] == want
        ok &= good
        print(f"selftest {k}: " + ("ok" if good else f"FAILED (exit {code[k]}, wanted {want})"))
    good = "not in the chapter" in out["fence"]
    ok &= good
    print("selftest the stray fence is named in the report: " + ("ok" if good else "FAILED"))
    print("\nSELFTEST " + ("green" if ok else "RED"))
    return 0 if ok else 1



if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    sys.exit(main(sys.argv[1:]))
