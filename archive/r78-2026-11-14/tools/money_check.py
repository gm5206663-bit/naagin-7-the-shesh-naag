#!/usr/bin/env python3
"""tools/money_check.py — every figure in the prose must be in the serial's own money column.

    python3 tools/money_check.py            # check the chapters against foundation/MONEY.md
    python3 tools/money_check.py --scan     # print every money figure the gate can find, with its line
    python3 tools/money_check.py --selftest

Why this exists. On 2026-11-13 the author threw out a number: *"₹350-crore is not enough money that he
needed to leave"*. The figure was not small — it was **pasted**, from his other serial's business, and it
sat in this book's prose and in `foundation/OC_VIHAAN.md` as though it had been decided here. Nothing in
the toolchain could see it, because nothing knew what a rupee is worth in this show. `foundation/MONEY.md`
now says so, and this gate makes every money figure in a chapter's scenes either at the column's scale and
named in it. A number that is not in the column is a number nobody decided — and `L-25`'s rule for a fact
nobody decided is one line: *change it*.

Rules
  MONEY-0  the column is missing or states no ceiling
  MONEY-1  a figure above the ceiling: the year's largest single paper in this serial is the Kumbh feed
           (`OC_VIHAAN.md`: ₹6.2 crore for fifteen days). Anything bigger is another serial's money.
  MONEY-2  a figure not named in the column, at any size — either write it into the column with what it
           buys, or change the number
  MONEY-3  the column lists a figure no chapter says any more: the ledger and the prose have parted,
           which is how a struck number survives in a foundation file (the `₹350 crore` history)
  MONEY-4  a money figure this gate could not parse — printed as a note, never red, so the word list
           gets extended instead of the rule argued with

What is money: a number sitting in front of `lakh` or `crore` (digits, Hindi words or English words), or
after a `₹`. A bare `hazaar` is left alone, because in this book it is a weight (`sola hazaar gram`), a
count or a year (`attara sau aatthaan`); so is any figure followed by `aadmi`/`log`/`gram`/`saal`/`cards`,
which is the difference between *teen crore aadmi* at the mela and *teen crore* of anything. Only the
scenes are read — from the first `##` heading to `## Footer` — and every line number printed is the number
in the file, so it can be grepped straight back.

Exit 0 green, 1 red, 2 used wrongly.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

NUM_WORDS = {
    # Hindi, as the chapters actually say it
    "ek": 1, "do": 2, "teen": 3, "char": 4, "chaar": 4, "panch": 5, "paanch": 5, "chhe": 6, "che": 6,
    "saat": 7, "aath": 8, "nau": 9, "das": 10, "gyarah": 11, "girah": 11, "barah": 12, "terah": 13,
    "chaudah": 14, "pandrah": 15, "solah": 16, "satrah": 17, "atharah": 18, "unnis": 19, "bees": 20,
    "chaubees": 24, "tees": 30, "chalees": 40, "chalis": 40, "pacas": 50, "sath": 60, "assi": 80,
    "navbe": 90, "sau": 100,
    # English, in the prose's own narration
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
    # the same words as the chapters spell them, doubled vowels and all (the fold makes them one)
    "chaalis": 40, "chaalees": 40,
}
FOLD = {"aa": "a", "ee": "e", "oo": "o", "uu": "u"}


def _fold(s):
    """Hindi numbers are spelled every which way in this book — *chalis*, *chalees*, *chaalis*.
    Collapsing the doubled vowels at lookup time keeps the word list short and the prose free to
    spell a figure the way the character says it."""
    return re.sub(r"aa|ee|oo|uu", lambda x: FOLD[x.group(0)], s)


# the lookup map. The spellings this file lists win outright; the folded spelling is added only if
# nothing of that shape exists yet, so `chaalis` reaches `chalis` and `teen` never becomes the
# English `ten`. Two spellings of one number therefore read as one figure, and a Hindi number is
# never reinterpreted as an English one.
NUM = dict(NUM_WORDS)
for _k, _v in NUM_WORDS.items():
    NUM.setdefault(_fold(_k), _v)

UNITS = {"lakh": 100000, "crore": 10000000, "hazaar": 1000, "hazar": 1000, "hezar": 1000}
# words that can stand where a figure stands and are not one; `ek`/`do` are numbers but also 'a' and 'to',
# so they only count immediately in front of a unit (handled in to_number by position, not here)
NONNUM = {"hai", "the", "of", "and", "or", "per", "mahine", "mahina", "ka", "ke", "ki", "ko", "se", "mein",
          "tak", "about", "nearly", "almost", "only", "more", "less", "than", "at", "for", "kai", "bahut",
          "zyada", "kam", "there", "some", "every", "each", "same", "own", "his", "her", "its", "yeh", "aur"}
# a figure with these after it is a count of things or people, not a price
NOT_MONEY = re.compile(r"\b(aadmi|aadmiyon|log|logo|people|persons?|gram|grams|kilo|saal|saalon|sal|ghante|"
                       r"minute|second|baars?|cards?|plates?|glasses|cup|cups|din|mahine|hazaar?\s*gram)\b", re.I)

# a figure: digits, a Hindi number word, or an English one, in front of a unit
N = r"(?:\d[\d.,]*|[a-z]{2,12})"
UNIT_ORDER = {"crore": 3, "lakh": 2, "hazaar": 1}          # descending, so a run reads correctly
RUN = re.compile(rf"(?P<n1>{N})\s*(?P<u1>lakh|crore)?", re.I)
NEXT = re.compile(rf"\s+(?P<n>{N})\s*(?P<u>lakh|hazaar)?", re.I)  # a run never re-ascends to crore


FOLD = {"aa": "a", "ee": "e", "oo": "o", "uu": "u"}


def to_number(tok):
    """A figure as digits, Hindi words or English words. The regex may have taken the word in front of
    the number too ('at six', 'ko chaar'), so the LAST word is the figure unless the pair is a sum
    ('do sau')."""
    if tok is None:
        return None
    s = tok.strip().lower().replace(",", "")
    if re.fullmatch(r"\d+(\.\d+)?", s):
        return float(s.replace(",", ""))
    w = [_fold(x) for x in s.split()]
    if len(w) == 2:
        if w[0] in NUM and w[1] == "sau":
            return float(NUM[w[0]] * 100)
        if w[1] in NONNUM:
            return None
        return float(NUM[w[1]]) if w[1] in NUM else None
    if len(w) == 1 and w[0] in NUM:
        return float(NUM[w[0]])
    return None


def money_in_text(text, base=0):
    """[(rupees, matched text, file line number)] — money phrases only.

    A run is read the way the book says it: `do crore chalees lakh`, `nau lakh chalees hazaar`,
    `chaar lakh pandrah hazaar`, `gyarah lakh chalees` (that last one is eleven lakh and forty
    rupees, and it is in Chapter 6 as a duplicated line in a sheet). Units must DESCEND, so
    `lakh crore` is not a figure and nothing is invented.

    A value of None means MONEY-4: a number in front of `lakh`/`crore` that this word list does not
    know. That is a note, never red — the list gets extended, the prose does not.
    """
    out = []
    for ln, line in enumerate(text.split("\n"), 1 + base):
        if re.search(r"\d\d:\d\d:\d\d", line):        # a timecode or a caption cue is not money
            continue
        low = line.lower()
        # A rupee sign in front of digits IS the figure, with no unit after it: the column writes
        # ₹2,40,00,000 and the prose writes do crore chaalis lakh. Both must mean the same rupees.
        for g in re.finditer(r"\u20b9\s*(\d[\d.,]*)", low):
            after = low[g.end():g.end() + 12].strip()
            if re.match(r"^(lakh|crore|hazaar|\*?\s*(lakh|crore))\b", after):
                continue                                  # `₹6.2 crore` is read by the run below
            digits = g.group(1).replace(",", "").rstrip(".")
            if re.fullmatch(r"\d+(\.\d+)?", digits):
                out.append((float(digits), g.group(0).strip(), ln))
        low = low.replace("\u20b9", " ")                    # from here the sign is only a marker
        pos = 0
        while True:
            m = RUN.search(low, pos)
            if not m:
                break
            pos = m.end()
            unit = (m.group("u1") or "").lower()
            if not unit:
                continue
            # only what FOLLOWS the figure can say it is a count rather than a price:
            # `teen crore aadmi`, `do lakh cards`. A wider window starts reading the next
            # sentence and swallowing real money (found on Chapter 18).
            if NOT_MONEY.search(low[m.end():m.end() + 18]):
                continue
            tok = m.group("n1")
            if tok.strip() in NONNUM:
                continue
            v = to_number(tok)
            if v is None:
                if not any(abs(ln - p) < 1 and True for _, _, p in out if _ is None):
                    out.append((None, m.group(0).strip(), ln))
                continue
            val = v * UNITS[unit]
            raw = m.group(0).strip()
            rank = UNIT_ORDER[unit]
            while True:
                nx = NEXT.match(low, pos)
                if not nx:
                    break
                nu = (nx.group("u") or "").lower()
                nrank = UNIT_ORDER[nu] if nu else 0        # a bare number after a unit is rupees
                if nrank >= rank:                          # units must descend
                    break
                nv = to_number(nx.group("n"))
                if nv is None:
                    break
                val += nv * (UNITS[nu] if nu else 1)
                rank = nrank
                pos = nx.end()
                raw = low[m.start():nx.end()].strip()
                if nu == "hazaar" and not nv:
                    break
            out.append((val, raw, ln))
    return out


def scene_slice(text):
    """The scenes only, with their real line numbers: from the first `##` heading to `## Footer`."""
    lines = text.split("\n")
    start = 0
    for i, l in enumerate(lines):
        if l.startswith("## "):
            start = i
            break
    stop = len(lines)
    for i in range(start, len(lines)):
        if lines[i].strip().lower().startswith("## footer"):
            stop = i
            break
    return "\n".join(lines[start:stop]), start


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def column(md=None):
    """(ceiling, {allowed rupee values}) from foundation/MONEY.md (or from the text given).

    Only the section headed `The column` (or the words `ALLOWED:`) decides what the book may say.
    A figure anywhere else in the file — the ceiling itself, the list of struck numbers — is
    deliberately NOT allowed by that fact, or a struck figure could re-legitimise itself by being
    recorded as struck."""
    if md is None:
        md = read("foundation/MONEY.md")
    ceiling = None
    m = re.search(r"(?i)ceiling[^\d\n]{0,40}(\d[\d.,]*)\s*(lakh|crore)", md)
    if m:
        ceiling = float(m.group(1).replace(",", "")) * UNITS[m.group(2).lower()]
    lines = md.split("\n")
    inside, allowed = False, set()
    for line in lines:
        if line.startswith("## "):
            inside = bool(re.search(r"(?i)^## .*\bcolumn\b", line))
            continue
        if not inside and not line.strip().upper().startswith("ALLOWED:"):
            continue
        for val, _, _ in money_in_text(line):
            if val:
                allowed.add(round(val))
    return ceiling, allowed


def check():
    fails, notes = [], []
    if not os.path.exists("foundation/MONEY.md"):
        return ["MONEY-0 foundation/MONEY.md is missing — the column has to be written before it can be enforced"], []
    ceiling, allowed = column()
    if not allowed:
        fails = ["MONEY-0 the column has no figures in its `## 2 · The column` section — the gate reads that section and nothing else"]
        return fails, []
    if ceiling is None:
        fails.append("MONEY-0 the column states no ceiling. Write one: *Ceiling: ₹6.2 crore*.")
    said = {}
    for p in sorted(os.listdir("chapters")):
        if not p.endswith(".md"):
            continue
        name = "Chapter " + re.sub(r"\D", "", p)
        body, base = scene_slice(read(os.path.join("chapters", p)))
        for val, raw, ln in money_in_text(body, base):
            if val is None:
                notes.append(f"{p}:{ln} MONEY-4 could not parse {raw!r} — extend the word list, do not edit the prose")
                continue
            said.setdefault(round(val), []).append(f"{p}:{ln}")
            if ceiling and val > ceiling + 1:
                fails.append(f"MONEY-1 {p}:{ln} ₹{val:,.0f} ({raw!r}) is above the ceiling ₹{ceiling:,.0f}. "
                             f"A figure that big is not money in this serial, it is another serial's.")
            if round(val) not in allowed:
                fails.append(f"MONEY-2 {p}:{ln} ₹{val:,.0f} ({raw!r}) is not in the column. Either write it into "
                             f"foundation/MONEY.md with what it buys, or change the number (`L-25`).")
    for a in sorted(allowed, reverse=True):
        if a not in said:
            fails.append(f"MONEY-3 the column lists ₹{a:,.0f} and no chapter says it any more — strike the row, "
                         f"or pay it in the prose.")
    return fails, notes


def summary():
    """One line, for `tools/check.py --all` to print when this gate is green. `check()` prints nothing
    itself, because a gate that prints inside a library call buries the line it is reporting."""
    if not os.path.exists("foundation/MONEY.md"):
        return "no column"
    ceiling, allowed = column()
    return f"{len(allowed)} figures in the column" + (f", ceiling ₹{ceiling:,.0f}" if ceiling else "")


def scan():
    for p in sorted(os.listdir("chapters")):
        if not p.endswith(".md"):
            continue
        body, base = scene_slice(read(os.path.join("chapters", p)))
        hits = money_in_text(body, base)
        if not hits:
            continue
        print(f"--- {p}")
        for val, raw, ln in hits:
            print(f"   line {ln:>4}  {('₹' + format(val, ',.0f')) if val else 'unparsed':>14}   {raw}")


_CEIL = "Ceiling: 6.2 crore"
SELF_COL = ("# M\n**Owns: the test column.**\n\n## 1 · The ceiling\n"
            "**Ceiling: 6.2 crore** (the Kumbh feed)\n\n## 2 · The column\n\n"
            "| Figure | Buys | Where |\n|---|---|---|\n| 24 lakh | a month | ch11 |\n"
            "| 6.2 crore | the feed | foundation |\n\n## 3 · Struck\n\n"
            "- ₹350 crore was struck on 2026-11-13. Recording it must not allow it.\n")


def selftest():
    ok = True

    def want(name, text, expect):
        nonlocal ok
        got = [round(v) if v else v for v, _, _ in money_in_text(text)]
        if expect == "UNPARSED":
            good = got == [None]
        elif expect is None:
            good = got == []
        else:
            good = expect in got
        print(f"selftest {name}: " + ("ok" if good else f"FAILED {got}"))
        ok &= good

    want("digits + lakh", "the fee was 24 lakh for the month", 2400000)
    want("hindi words + tail", "\"nau lakh chalees hazaar hai\"", 940000)
    want("a number and a thousand", "chaar lakh pandrah hazaar", 415000)
    want("rupee sign", "₹40 lakh a month", 4000000)
    want("a word in front of the figure", "the yard at six lakh a month", 600000)
    want("a bare thousand is a weight", "sola hazaar gram", None)
    want("crore of people is not money", "teen crore aadmi aate hain", None)
    want("an unlisted word is MONEY-4", "chhappan lakh", "UNPARSED")   # 56 is not in the list; `gyaarah` is
    # the book's own sentences, added the day the parser was written
    want("ch6's duplicated line", "\"Gyarah lakh chalees. Apni sheet dekho.\"", 1100040)
    want("a run of two units", "do crore chalees lakh", 24000000)
    want("a run into rupees", "ab chaar lakh pandrah hazaar dena hai", 415000)
    want("the gold line keeps its price", "sola hazaar gram sona chaar lakh mil jaayenge", 400000)
    want("the crowd is not a price", "teen crore aadmi aate hain", None)
    want("a timecode is not money", "21:58:09 → 22:04:51 · the tent · nine lakh", None)
    c, a = column(SELF_COL)
    good = c == 62000000 and 2400000 in a and 3500000000 not in a
    print("selftest column: ceiling read, the listed figure allowed, the STRUCK figure not allowed: "
          + ("ok" if good else f"FAILED ceiling={c} allowed={sorted(a)}"))
    ok &= good
    print("selftest a crore is a crore: " + ("ok" if to_number("2") * UNITS["crore"] == 20000000 else "FAILED"))
    ok &= to_number("2") * UNITS["crore"] == 20000000
    print("\nSELFTEST " + ("green" if ok else "RED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--scan" in sys.argv:
        scan()
        sys.exit(0)
    print("COLUMN " + summary())
    f, n = check()
    for x in n:
        print("  note:", x)
    if f:
        print(f"\nRED: {len(f)} problem(s)")
        for x in f:
            print("  -", x)
        sys.exit(1)
    print("\nGREEN. Every money figure in the scenes is at this serial's scale and named in the column.")
    sys.exit(0)
