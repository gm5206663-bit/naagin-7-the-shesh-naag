import sys, glob, re
def body(path):
    s = open(path, encoding='utf-8').read()
    # drop header lines (title/source/published) if present
    lines = s.split('\n')
    title = lines[0].lstrip('# ').strip()
    txt = '\n'.join(l for l in lines[1:] if not re.match(r'^(Source|Published|URL|Fetched)\s*:', l.strip()))
    txt = re.sub(r'\s+', ' ', txt).strip()
    # cut trailing review / precap / nav
    for mark in [' Review This', ' Review: ', ' Review ', ' Ratings:', ' Precap:', ' Also Read', ' ← ', ' Episode Review', ' Our Take', ' Final Thoughts', ' Verdict']:
        i = txt.find(mark)
        if i > len(txt) * 0.55:
            txt = txt[:i]
    return title, txt
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        pub, ep = arg.split(':')
        d = {'tr': 'tellyreviews', 'tb': 'tellyboosters'}[pub]
        fs = glob.glob(f'{d}/E{int(ep):02d}_*')
        if not fs: print(f'## E{ep} {pub}: NO FILE'); continue
        t, b = body(fs[0])
        print(f'\n## E{int(ep):02d} [{pub}] {t}\n{b}\n({len(b.split())} words)')
