#!/usr/bin/env python3
"""tools/recount.py — the word ledger, one method, reproducible.

    python3 tools/recount.py            per chapter, per scene, and the total
    python3 tools/recount.py --total    the total only

What it counts: every whitespace-separated token in a chapter's scenes — from the
first `## ` heading after the head to the `## Footer` line — with heading lines
themselves not counted and the footer not counted. Two scripts were in use
before 2026-11-11 and disagreed by a few words per chapter; this is the one that
is used from now on, and the figures in `STATUS.md` are read off it.
"""
import glob
import re
import sys

SCENE = re.compile(r'^##\s+(.+)$')


def count(path):
    raw = open(path, encoding='utf-8').read()
    body = raw.split('\n## Footer')[0]
    start = body.index('\n## ')
    body = body[start:]
    scenes, cur = [], None
    for line in body.split('\n'):
        m = SCENE.match(line)
        if m:
            if cur:
                scenes.append(cur)
            cur = [m.group(1).strip(), 0]
            continue
        if cur is not None:
            cur[1] += len(line.split())
    if cur:
        scenes.append(cur)
    return scenes


def main(argv):
    rows, total = [], 0
    for p in sorted(glob.glob('chapters/Chapter_*.md')):
        sc = count(p)
        n = sum(s[1] for s in sc)
        total += n
        rows.append((p, n, sc))
    if '--total' in argv:
        print(total)
        return 0
    for p, n, sc in rows:
        print(f'\n{p.split("/")[-1][:34]:35}{n:>7,}')
        for name, w in sc:
            print(f'    {name[:44]:46}{w:>6,}')
    print(f'\nTOTAL {total:,} words in the scenes, {len(rows)} chapters')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
