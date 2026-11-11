#!/usr/bin/env python3
"""Keyword search across the Hindi caption tracks.
usage: python3 tools/caption_hits.py 'REGEX' [width=120] [max_per_episode=4] [E05,E06]
Run from the project root. Captions are looked for in captions/ (unpack the archive first if it is packed)."""
import re, glob, sys, os
def hits(pat, width=120, maxper=4, eps=None, root='captions'):
    rx = re.compile(pat); n = 0
    for f in sorted(glob.glob(os.path.join(root, 'E*.hi.txt'))):
        ep = os.path.basename(f)[:3]
        if eps and ep not in eps: continue
        c = 0
        for line in open(f, encoding='utf-8'):
            m = re.match(r'\[(\d\d:\d\d:\d\d)\]\s*(.*)', line)
            if not m: continue
            ts, txt = m.groups()
            for mm in rx.finditer(txt):
                a = max(0, mm.start() - width); b = min(len(txt), mm.end() + width)
                print(f"{ep} {ts} …{txt[a:b]}…"); c += 1; n += 1
                if c >= maxper: break
            if c >= maxper: break
    print('TOTAL shown', n)
if __name__ == '__main__':
    a = sys.argv
    hits(a[1], int(a[2]) if len(a) > 2 else 120, int(a[3]) if len(a) > 3 else 4, set(a[4].split(',')) if len(a) > 4 else None)
