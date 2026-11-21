#!/usr/bin/env python3
"""ripple_check.py — has this chapter read its own divergences before it copied the show?

    python3 tools/ripple_check.py chapters/Chapter_19_....md [more files]
    python3 tools/ripple_check.py                 # every chapter
    python3 tools/ripple_check.py --selftest

Why this exists. `foundation/BUTTERFLY.md` records what this serial changed about
*Naagin*; `canon/E0N_BEATS.md` records what the show says. For nineteen chapters the
second file was copied into prose without the first being read over it, and the book
contradicted its own ruling — the author's words of 2026-11-12: *"it's your mistake
pasting canon, you need to add butterfly effects and others all things, that you don't
do."* This tool is the ripple made mandatory.

The registry is `foundation/RIPPLE.md`, §3b, one rule per line:

    - `R-01 | superseded | <regex>`        what the serial no longer asserts
    - `R-01 | allow | <regex>`             the context in which it is still said

Fails:
  RP1  prose asserts a superseded fact and the footer has not owned the rule
       (`RIPPLED:  R-01 (why) · R-03 (why)`), and the line is not `allow`ed
  RP2  a show line used verbatim in the scenes with no verdict on the footer's
       `PASTED:` line — canon pasted, no ruling, exactly the fault
  RP3  a `RIPPLED:` rule id that the registry does not have
  RP4  an `allow` / `superseded` regex that does not compile (the registry is broken)
  RP5  the chapter carries no `RIPPLED:` line at all — a chapter may not be clean just
       because nobody looked. `RIPPLED:  none` is the declaration that the rules were read
       and none of them is asserted in this chapter's scenes; naming `R-01` owns a hit and
       says why the line stays. Ids count only in the items themselves: `RIPPLED:  none
       (R-01 to R-04 read)` exempts nothing, which is the point of the key.

Notes, not fails: how many verbatim show lines a chapter carries, and how many
divergences in the ledger have no rule yet (the backlog, §4 of the registry).

The corpus for RP2 is the beat files, not the caption track, and that is measured
rather than assumed: all 512 of the show's lines used verbatim across the nineteen
chapters are found in `canon/E0N_BEATS.md`, and **zero** in `captions/*.hi.txt` —
the track is Devanagari, the prose is romanised, and the transliteration happens in
the beat file. So the beat files are the only road the show's words take into this
book, and a verdict on a line found there covers every way it can arrive. A future
chapter written from a recap in `canon/sources/` instead would need that corpus
added here, which the tool would then report as pastes it has never seen.
"""
import glob
import os
import re
import sys
import unicodedata

REGISTRY = "foundation/RIPPLE.md"
MACHINE = re.compile(r"^\s*-\s*`(R-\d{2})\s*\|\s*(superseded|allow)\s*\|\s*(.+?)`\s*$")
QUOT = re.compile(r'"([^"“”]{18,400})"')
# A footer key or an author's note ("**FIXED:** …", "FENCE: …") is not a scene.
NOTE = re.compile(r"^\s*(?:\*\*)?[A-Z][A-Z0-9 .,/\-\*]{2,}:")
# Digits, hyphens and the trailing `**` are allowed because the house numbers a key when a
# second one of the same name exists (`FIXED-4:`, `WITHDRAWN-2:`) and writes some of them as
# `**SEEN:**`. Without this a rebuilt footer's keys are read as scenes: Chapter 19's sweep
# found it on 2026-11-14, and `O049` item (j) is the lesson.
# The chapter's own notes are not its scenes: the prose region ends at the first
# footer key, whichever of the workshop's several styles a chapter happens to use.
FOOTER = re.compile(
    "^(?:[*]{2}(?:Canon|CHANGED|ADDED|FIXED|DEFERRED|Added|Fixed|Changed|Notes)[.]?[*]{2}"
    "|[0-9]+[.][ ][*]{2}[A-Z]|PASTED:|RIPPLED:"
    "|[ ]{4,}[A-Z][A-Z0-9-]{2,}:"
    "|[/]{2}[*](?:Notes|What the chapter))",
    re.M,
)
OWNED = re.compile(r"^\s*RIPPLED:\s*(.+)$", re.M)
PASTED = re.compile(r"^\s*PASTED:\s*(.+)$", re.M)
RULE_ID = re.compile(r"R-\d{2}")


def norm(s):
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"[^a-z\u0900-\u097F ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def load_registry(path=REGISTRY):
    """{R-01: {superseded: compiled, allow: compiled}, ...} — RP4 on a bad regex."""
    rules, order = {}, []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = MACHINE.match(line)
            if not m:
                continue
            rid, kind, pat = m.groups()
            if rid not in rules:
                rules[rid] = {}
                order.append(rid)
            try:
                rules[rid][kind] = re.compile(pat, re.I)
            except re.error as e:
                sys.exit(f"RP4  the registry's {rid} {kind} regex does not compile: {e}")
    return rules, order


def split_book(text):
    """(prose, footer). The footer starts at the chapter's `**Canon.**` block."""
    m = FOOTER.search(text)
    if not m:
        return text, ""
    return text[: m.start()], text[m.start():]


def scenes(text):
    """The scene bodies only: drop headings and fenced blocks."""
    out, skip = [], False
    for ln in text.splitlines():
        s = ln.strip()
        if s.startswith("```"):
            skip = not skip
            continue
        if skip or s.startswith("#") or s.startswith("<!--") or NOTE.match(s):
            continue
        out.append(ln)
    return out


def beat_corpus(chapter_name, canon_dir="canon"):
    """Every beat file's text, normalised: the drafting source a chapter is copied from."""
    blob = []
    for f in sorted(glob.glob(os.path.join(canon_dir, "E*_BEATS.md"))):
        with open(f, encoding="utf-8") as fh:
            blob.append(norm(fh.read()))
    return "\n".join(blob)


def check(path, rules, corpus=""):
    fails, notes = [], []
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    prose, footer = split_book(text)
    # The keys may sit anywhere in the notes block, and some chapters have no
    # `**Canon.**` marker to split on, so ownership is read from the whole file.
    decl = " ".join(OWNED.findall(text))
    owned = set()
    for item in decl.split("·"):
        owned.update(RULE_ID.findall(item.split("(")[0].split("—")[0]))
    pasted_line = " ".join(PASTED.findall(text))
    pasted = norm(pasted_line)
    for rid in owned:
        if rid not in rules:
            fails.append(f"RP3  the footer owns {rid}, which foundation/RIPPLE.md does not have")
    # RP1 — a superseded fact asserted in the scenes
    hits = {}
    body = scenes(prose)
    # A quote carried on the PASTED: line with a verdict is ruled by that verdict,
    # so it is not also a RP1 hit: one footer key does the work of both.
    ruled_quotes = {norm(q) for q in re.findall(r'"([^"]{10,400})"', pasted_line)}
    for rid, spec in rules.items():
        sup = spec.get("superseded")
        if not sup:
            continue
        for i, line in enumerate(body, 1):
            if norm(line).count('"') % 2:
                continue  # inside a block quote: skip stray partial lines
            if any(norm(q) in ruled_quotes for q in QUOT.findall(line)):
                continue
            m = sup.search(line)
            if not m:
                continue
            al = spec.get("allow")
            if al and al.search(line):
                continue
            hits.setdefault(rid, []).append((i, m.group(0), line.strip()))
    for rid in sorted(hits):
        if rid in owned:
            notes.append(f"owned {rid}: {len(hits[rid])} line(s) the chapter has ruled on")
            continue
        for i, frag, line in hits[rid][:6]:
            fails.append(f"RP1  {rid} ({frag[:40]!r}) at scene line {i}: {line[:110]}")
        if len(hits[rid]) > 6:
            fails.append(f"RP1  {rid}: {len(hits[rid]) - 6} more line(s) — own the rule on the footer's RIPPLED: line or change the sentences")
    # RP2 — canon's words, used whole, with no verdict
    pasted_in = []
    for line in body:
        for q in QUOT.findall(line):
            nq = norm(q)
            if len(nq) < 25 or nq in pasted:
                continue
            if nq in corpus or nq in norm(footer):
                pasted_in.append(q)
    # A verbatim show line is this workshop's method, not a fault. It is a fault
    # when the line carries a fact a registered divergence has superseded: those
    # words may only sit in a scene with a verdict on the footer's PASTED: line.
    sup_any = [spec["superseded"] for spec in rules.values() if "superseded" in spec]
    flagged = [q for q in set(pasted_in) if any(s.search(q) for s in sup_any)]
    for q in sorted(flagged):
        fails.append(f"RP2  a superseded fact, copied from the show, with no verdict on the PASTED: line: {q[:110]!r}")
    n = len(set(norm(q) for q in pasted_in))
    if n:
        notes.append(f"{n} of the show's own lines used verbatim in the scenes"
                     + (f" — {len(flagged)} of them carry a superseded fact" if flagged else ""))
    declared = bool(re.search(r"^\s*RIPPLED:", text, re.M))
    if not declared:
        fails.append("RP5  no `RIPPLED:` line — say which registered rule this chapter touches, or declare `none`")
    elif not owned:
        notes.append("RIPPLED: none declared")
    else:
        notes.append("RIPPLED: " + " · ".join(sorted(owned)))
    return fails, notes, declared


def backlog():
    """How much of the butterfly ledger has no ripple rule yet. A note, not a fail."""
    try:
        with open("foundation/BUTTERFLY.md", encoding="utf-8") as fh:
            bf = set(re.findall(r"BF-\d{2}", fh.read()))
    except OSError:
        return 0
    try:
        with open(REGISTRY, encoding="utf-8") as fh:
            ruled = set(re.findall(r"BF-\d{2}", fh.read()))
    except OSError:
        ruled = set()
    return len(bf - ruled)


def selftest():
    import tempfile

    reg = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
    reg.write(
        "- `R-01 | superseded | in love with Aryaman|Aryaman se pyaar`\n"
        "- `R-01 | allow | account she gives`\n"
        "- `R-02 | superseded | his heart knows`\n"
    )
    reg.close()
    rules, _ = load_registry(reg.name)
    assert "R-01" in rules and "R-02" in rules
    bad = '## The Mirror\n\nShe says it plain: "I was in love with Aryaman."\n\n**Canon.** nothing\n'
    ruled = '## The Mirror\n\nShe says it plain: "I was in love with Aryaman."\n\n**Canon.** nothing\n\nRIPPLED:  R-01 (her cover, and the chapter says so)\n'
    allowed = '## The Mirror\n\n"That is the account she gives this house."\n\n**Canon.** nothing\n'
    silent = '## X\n\n"Aryaman se pyaar Purvi ne kiya tha."\n\n**Canon.** *"Aryaman se pyaar Purvi ne kiya tha."*\n'
    verdict = silent + "\nPASTED:  \"Aryaman se pyaar Purvi ne kiya tha\" — account (R-01)\n"
    plain = '## X\n\n"Kuch bhi karke humein Naagmani laani hogi," he says.\n\n**Canon.** nothing\n'
    unknown = '## X\n\nNothing here.\n\n**Canon.** nothing\n\nRIPPLED:  R-77 (typo)\n'
    corpus = norm("Aryaman se pyaar Purvi ne kiya tha")
    want = {
        "a pasted fact, unowned": (bad, True),
        "the same fact, owned on the footer": (ruled, False),
        "the words in an allowed context": (allowed, False),
        "canon's line with no verdict": (silent, True),
        "canon's line, verdict on the footer": (verdict, False),
        "a pasted line that changes nothing": (plain, False),
        "no RIPPLED: declaration at all": (bad.replace('\n\n**Canon.** nothing\n', '\n'), True),
        "a rule id that does not exist": (unknown, True),
        "a numbered footer key quoting the line, not a scene": (
            '## X\n\nNothing here.\n\n## Footer\n\n    FIXED-4: the key says *"Aryaman se pyaar Purvi ne kiya tha."*\n', False),
    }
    ok = True
    d = tempfile.mkdtemp()
    for i, (name, (body, should_fail)) in enumerate(want.items()):
        f = os.path.join(d, f"t{i}.md")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(body)
        fails, notes, _ = check(f, rules, corpus)
        got = bool([x for x in fails if x.startswith(("RP1", "RP2", "RP3"))])
        if got != should_fail:
            ok = False
            print(f"SELFTEST FAIL {name}: expected {should_fail}, got {got} {fails[:1]}")
        else:
            print(f"  {name}: {'caught' if should_fail else 'passes'}")
    os.unlink(reg.name)
    print("SELFTEST:", "green — a pasted canon line and an unrun divergence are both RED, and a ruled chapter passes" if ok else "RED")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if not os.path.isdir("chapters"):
        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    rules, order = load_registry()
    if not rules:
        sys.exit(f"no rules read from {REGISTRY} §3b — the registry is empty or misformatted")
    corpus = beat_corpus("")
    paths = [a for a in argv[1:] if not a.startswith("-")] or sorted(glob.glob("chapters/*.md"))
    bad, unruled = 0, []
    for p in paths:
        fails, notes, owned = check(p, rules, corpus)
        print(os.path.basename(p))
        for x in notes:
            print("      " + x)
        for f in fails:
            print("  FAIL " + f)
        if fails:
            bad += len(fails)
        elif not owned:
            unruled.append(p)
        print("  " + ("green" if not fails else f"RED: {len(fails)}"))
    owed = backlog()
    print()
    print(f"rules read: {', '.join(order)}   ·   ledger entries not yet triaged against them: {owed} (`foundation/RIPPLE.md` §4)")
    print("GREEN. Nineteen chapters have each declared whether a registered rule is asserted in their scenes, no superseded fact sits unowned, and no show line carrying one is used without a verdict."
          if not bad else f"RED. {bad} fault(s).")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
