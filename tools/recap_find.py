#!/usr/bin/env python3
"""tools/recap_find.py - find the sentences of a recap that carry given words.

Run from canon/sources:
    python3 ../../tools/recap_find.py tr:3 Rajat Mayuri "glasses|bus" pregnan
Each argument after the first is a regex; the first sentence or two matching it are printed.
"""
import sys, re, glob
sys.path.insert(0, __import__('os').path.dirname(__file__))
from read_recap import body

pub, ep = sys.argv[1].split(':')
d = {'tr': 'tellyreviews', 'tb': 'tellyboosters'}[pub]
fs = glob.glob(f'{d}/E{int(ep):02d}_*')
if not fs:
    print('NO FILE'); sys.exit(0)
t, b = body(fs[0])
sents = re.split(r'(?<=[.!?])\s+', b)
print(f'## E{int(ep):02d} [{pub}] {len(b.split())} words')
for pat in sys.argv[2:]:
    hits = [s for s in sents if re.search(pat, s, re.I)]
    print(f'[{pat}] {len(hits)} hit(s): ' + ' // '.join(h[:230] for h in hits[:2]))
