#!/usr/bin/env python3
"""Convert a YouTube json3 auto-caption file into (a) an .srt and (b) a compact timestamped .txt.
Auto-captions are speech recognition output: wording and names may be wrong; music and silent action are not captured."""
import json, sys, re

def load(path):
    data = json.load(open(path, encoding='utf-8'))
    cues = []
    for ev in data.get('events', []):
        segs = ev.get('segs')
        if not segs:
            continue
        text = ''.join(s.get('utf8', '') for s in segs)
        text = re.sub(r'\s+', ' ', text).strip()
        if not text:
            continue
        start = ev.get('tStartMs', 0)
        dur = ev.get('dDurationMs', 0)
        cues.append([start, start + dur, text])
    # clamp overlapping ends (rolling captions)
    for i in range(len(cues) - 1):
        if cues[i][1] > cues[i + 1][0]:
            cues[i][1] = cues[i + 1][0]
    return cues

def ts(ms, sep=','):
    h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"

def to_srt(cues):
    out = []
    for i, (a, b, t) in enumerate(cues, 1):
        out.append(f"{i}\n{ts(a)} --> {ts(b)}\n{t}\n")
    return '\n'.join(out)

def to_txt(cues, gap_ms=2500, max_chars=420):
    """Merge consecutive cues into paragraphs; start a new paragraph on a pause or when long."""
    paras = []
    cur_start, cur_text, last_end = None, '', None
    for a, b, t in cues:
        if cur_start is None:
            cur_start, cur_text = a, t
        elif (a - last_end) > gap_ms or len(cur_text) > max_chars:
            paras.append((cur_start, cur_text))
            cur_start, cur_text = a, t
        else:
            cur_text += ' ' + t
        last_end = b
    if cur_start is not None:
        paras.append((cur_start, cur_text))
    return '\n'.join(f"[{ts(a, '.')[:8]}] {t}" for a, t in paras)

if __name__ == '__main__':
    src, srt_out, txt_out = sys.argv[1:4]
    cues = load(src)
    open(srt_out, 'w', encoding='utf-8').write(to_srt(cues))
    open(txt_out, 'w', encoding='utf-8').write(to_txt(cues) + '\n')
    print(f"{src}: {len(cues)} cues, last cue ends {ts(cues[-1][1])}, {sum(len(c[2]) for c in cues)} chars")
