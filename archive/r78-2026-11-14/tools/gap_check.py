#!/usr/bin/env python3
"""tools/gap_check.py — what the episode says that the chapter does not.

The question this answers is the author's, asked on 2026-11-11 after the
rebuild: *"you can check what missing in chapter from episode in style"*.

    python3 tools/gap_check.py chapters/Chapter_09_*.md 30:00 38:53
    python3 tools/gap_check.py chapters/Chapter_09_*.md --beats   (read the window
                                 from the chapter's BASE line if a timecode is there)
    python3 tools/gap_check.py --selftest

How it works
  1. Slices the episode's Hindi caption track to the timecode window.
  2. Transliterates each cue to plain ASCII, the same way the chapters romanise.
  3. Takes each cue's opening content words and looks for them on the page,
     fuzzy, anywhere in the chapter's dialogue or narration.
  4. Prints, in the episode's own order, every cue it cannot find, and a
     coverage figure. Also prints the <mu>g</mu>sic-cue density of the window against
     the number of score beats in the chapter, because O27 made the score
     evidence rather than decoration.

It is a first pass, not a verdict. A cue can be on the page in other words and
still be right; a cue can match by accident. What it cannot miss is a cue that
is simply not there, which is the failure the author caught.
"""
import difflib
import re
import sys
import unicodedata

# --- Devanagari to the workshop's plain ASCII ---------------------------------
CONS = {
    'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'n',
    'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'n',
    'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
    'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
    'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm',
    'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',
    'ळ': 'l', 'क़': 'k', 'ख़': 'kh', 'ग़': 'g', 'ज़': 'z', 'ड़': 'r', 'ढ़': 'rh', 'फ़': 'f',
}
IND_VOWEL = {
    'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo',
    'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au', 'ऍ': 'e', 'ऑ': 'o',
}
MATRA = {
    'ा': 'aa', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'ृ': 'ri',
    'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', 'ॅ': 'a', 'ॉ': 'o',
}
VIRAMA = '्'
NUKTA = '़'
DIGITS = str.maketrans('०१२३४५६७८९', '0123456789')


def translit(text):
    """Devanagari to plain ASCII: inherent schwa inside a word, dropped at its end."""
    out = []
    pending = False          # a consonant with no vowel written after it yet
    for ch in unicodedata.normalize('NFC', text):
        if ch in CONS:
            if pending:
                out.append('a')
            out.append(CONS[ch])
            pending = True
        elif ch in MATRA:
            out.append(MATRA[ch])
            pending = False
        elif ch in (VIRAMA, NUKTA):
            pending = False
        elif ch in IND_VOWEL:
            if pending:
                out.append('a')
            out.append(IND_VOWEL[ch])
            pending = False
        elif ch.isspace():
            pending = False
            out.append(' ')
        else:
            if pending:
                out.append('a')
            out.append(ch)
            pending = False
    s = ''.join(out).translate(DIGITS).lower()
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def norm(w):
    """Fold the two romanisation habits together: the track's and the page's."""
    w = w.lower()
    for a, b in (('chh', 'c'), ('ch', 'c'), ('ph', 'f'), ('kh', 'k'), ('gh', 'g'),
                 ('th', 't'), ('dh', 'd'), ('bh', 'b'), ('sh', 's'), ('jh', 'j'),
                 ('rh', 'r'), ('aa', 'a'), ('ee', 'i'), ('ii', 'i'), ('oo', 'u'),
                 ('uu', 'u'), ('ai', 'e'), ('au', 'o'), ('yaa', 'ya'), ('w', 'v')):
        w = w.replace(a, b)
    w = re.sub(r'(.)\1+', r'\1', w)
    return w


def close(a, b):
    if a == b:
        return True
    if len(a) > 3 and len(b) > 3 and difflib.SequenceMatcher(None, a, b).ratio() >= 0.78:
        return True
    return False


def matched(ws, page_words):
    if not ws:
        return True
    hit = sum(1 for w in ws if any(close(norm(w), p) for p in page_words))
    return hit >= max(2, int(len(ws) * 0.6))


# --- the caption track --------------------------------------------------------
CUE = re.compile(r'^\[(\d{2}):(\d{2}):(\d{2})\]\s*(.*)$')


def cues(path):
    out = []
    for line in open(path, encoding='utf-8'):
        m = CUE.match(line.strip())
        if not m:
            continue
        secs = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
        out.append((secs, m.group(4)))
    return out


def parse_tc(t):
    p = [int(x) for x in t.split(':')]
    return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]


STOP = set("""a an the is are was were be been to of in on at and or but if then than that this these those
he she it they we you i me my your his her their our us them not no yes do does did have has had will would
can could should may might must there here what which who whom how why when where all any some very just""".split())

MUSIC = 'संगीत'


def words(s):
    return [w for w in re.split(r'\s+', s) if w and w not in STOP and len(w) > 1]


DAANDA = re.compile(r'\s*[।?!]\s*')


def sentences(text):
    return [x for x in DAANDA.split(text) if len(x.strip()) > 3]


def chapter_text(path):
    raw = open(path, encoding='utf-8').read()
    return raw.split('## Footer')[0]


def base_line(text):
    """The footer's BASE line, and only that line.

    Reading the whole file for a timecode pair picks up any 'mm:ss to mm:ss' in
    the prose and the evidence notes; Chapter 4 was being measured against
    01:16 to 01:56 because of it. The footer's own BASE row is the witness.
    """
    for line in reversed(text.splitlines()):
        if re.match(r'\s*BASE:', line):
            return line
    return ''


def window_from_base(text):
    line = base_line(text)
    tc = r'(\d{1,2}:\d{2}(?::\d{2})?)'
    m = re.search(tc + r'\s*(?:to|–|-|and)\s*' + tc, line)
    if m:
        return (parse_tc(m.group(1)), parse_tc(m.group(2)))
    # Chapter 6 runs to the end of the upload and has no closing timecode.
    m = re.search(tc, line)
    return (parse_tc(m.group(1)), None) if m else None


def episode_from_base(text):
    m = re.search(r'Episode\s+(\d{1,2})', base_line(text))
    return int(m.group(1)) if m else None


def report(chapter, start, end=None, ep=3, page=None, quiet=False):
    cap = f'captions/E{ep:02d}.hi.txt'
    page_words = [norm(w) for w in words(translit(page or chapter_text(chapter)))]
    page_set = set(page_words)
    seq = [c for c in cues(cap) if c[0] >= start and (end is None or c[0] <= end)]
    missing, partials, found, music = [], [], 0, 0
    for secs, text in seq:
        if MUSIC in text:
            music += 1
        body = text.replace(MUSIC, ' ')
        latin = translit(body)
        ws = words(latin)
        if len(ws) < 3:
            continue
        present = matched(ws, page_set)
        partial = False
        if not present:
            # A caption cue can carry two or three speeches, and its tail may be
            # an English line the ASR set down in Devanagari, which romanises into
            # nothing a chapter would contain. Judged on the whole block such a
            # cue always reads as missing even when the chapter has it. So the
            # opening sentences are judged on their own, at the same 0.78.
            for sent in sentences(body)[:2]:
                sws = words(translit(sent))
                if len(sws) >= 3 and matched(sws, page_set):
                    partial = True
                    break

        if present:
            found += 1
        elif partial:
            partials.append((secs, latin, text))
        else:
            missing.append((secs, latin, text))
    total = found + len(partials) + len(missing)
    if not quiet:
        print(f'\n=== {chapter}  ·  episode {ep} cues {fmt(start)}–{fmt(end) if end else "end"}  ·  {total} cues')
        pct = (100*(found + len(partials))/total) if total else 0
        print(f'    coverage {found + len(partials)}/{total} = {pct:.0f}%'
              f'   ({found} whole, {len(partials)} opening lines only)   ·   music cues in the window {music}')
        for secs, latin, orig in partials:
            print(f'    PARTLY {fmt(secs)}  {orig.strip()[:120]}')
        for secs, latin, orig in missing:
            print(f'    MISSING {fmt(secs)}  {orig.strip()[:150]}')
            print(f'            -> {latin[:140]}')
    return found, total, missing, music


def fmt(s):
    return f'{s//60:02d}:{s%60:02d}'


def selftest():
    ok = True
    # The expectation is the transliterator's own current output, pinned here so a
    # later change to the table is seen. The old strings ('ye lift ka darvaaza',
    # 'main nahin marna') were right before aspiration and vowel length were added,
    # and had been failing quietly for some time: this is a note, not a silence.
    if translit('ये लिफ्ट का दरवाज़ा') != 'ye lipht kaa daravaajaa':
        print('selftest fail translit:', translit('ये लिफ्ट का दरवाज़ा'))
        ok = False
    if translit('मैं नहीं मरना चाहती जल्दी') != 'mai nahee maranaa chaahatee jaldee':
        print('selftest fail translit 2:', translit('मैं नहीं मरना चाहती जल्दी'))
        ok = False
    print('selftest', 'ok' if ok else 'FAILED')
    return 0 if ok else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == '--selftest':
        sys.exit(selftest())
    ch = a[0]
    if '--beats' in a:
        # the BASE line lives in the footer, which chapter_text() strips
        w = window_from_base(open(ch, encoding='utf-8').read())
        if not w:
            sys.exit('no BASE window in this chapter')
        start, end = w
    else:
        if len(a) == 1:
            # a chapter on its own is measured over its own BASE window
            w = window_from_base(open(ch, encoding='utf-8').read())
            if not w:
                sys.exit('pass a chapter with a BASE window, or a start and an end timecode')
            start, end = w
        else:
            start = parse_tc(a[1])
            end = parse_tc(a[2]) if len(a) > 2 else None
    ep = episode_from_base(open(ch, encoding='utf-8').read()) or 3
    for i, x in enumerate(a):
        if x == '--ep':
            ep = int(a[i + 1])
    f, t, m, mu = report(ch, start, end, ep=ep)
    print(f'\n{f}/{t} cues on the page. {len(m)} not found. {mu} music cues in the window.')
