#!/usr/bin/env python3
"""camera_check.py — measure a chapter against WRITING.md §2 (the camera).

    python3 tools/camera_check.py chapters/Chapter_01_….md [more files]
    python3 tools/camera_check.py --selftest

Hard failures (exit 1):
  N4  a sentence of more than 60 words, anywhere
  N5  the past tense in narration: was / were / had been / did not / could not /
      would have, outside speech (the scenes are told in the present)

**Deleted 2026-11-12 on the author's order (`O035`):** N2 (a feeling named in the
narration) and N6 (the cause of a feeling explained). The rule that forbade
feelings is gone from this tool, from WRITING.md, from RULES.md and from every
project file. This serial is an Indian daily soap: feeling is named on the page,
its cause may be said, and the room reacts. No later hand may put the rule back.

**Deleted 2026-11-12 on the author's order (`O037`):** N1, the ban on a comparison
in narration — like / as if / as though. The author was asked directly and chose
*cut it entirely*: an Indian soap runs on similes, and the show this book is
following says *the room stopped*, *the way a fan stops*, *like a woman who has
seen it before*. A simile is now ordinary narration. No later hand may put the
rule back.

Printed, not failed:
  N3  the share of paragraphs that are speech (looked at again outside 45-70%)
  N8  the rhythm band: share of narration under 9 words (choppy over 45%), share
      over 45 (stretched over 8). The book leans short; the number is printed so
      the style pass goes to the worst chapters first, and so nobody has to
      argue from feel about whether the prose has gone into stabs.
  N7  the voice stepping in to explain a line, label a memory, or address the
      reader — the author asked for his own problems to be known, and this is
      the shape they take here: a scene that shows well and then tells.

"Speech" is anything inside double quotation marks, straight or curly, and
anything inside *italics* (the voiced aside). The head above the first scene
heading and everything from "## Footer" on are left out.
"""
import re
import statistics
import sys

INTERIOR = re.compile(
    r"\b(feels?|felt|reali[sz]e[sd]?|wonder(?:s|ed)?|seem(?:s|ed)?|"
    r"(?:thinks?|thought) about|(?:knows?|knew) that)\b",
    re.I,
)
QUOTED = re.compile(r"“[^”]*”|\"[^\"]*\"")
OPEN_QUOTE = re.compile(r"[“\"][^”\"]*$")
ITALIC = re.compile(r"(?<!\*)\*(?!\*)[^*\n]+\*(?!\*)")
PAST = re.compile(r"\b(was|were|had been|did not|could not|would have)\b", re.I)
FEELING = re.compile(
    r"\b(feel(?:s|ing)?|felt|fear\w*|afraid|terrif\w*|frighten\w*|scared|"
    r"happ(?:y|iness)|glad|sad(?:ness|ly)?\b|grief|sorrow\w*|anger\w*|angry|furious|"
    r"asham\w*|shame\w*|guilt\w*|proud\w*|pride|relief|relieved|"
    r"hurt|lonel\w*|hopeful|hopeless|love[sd]?|hate[sd]?|joy\w*|delight\w*|"
    r"disgust\w*|uneasy|nervous\w*|anxi\w*|worr(?:y|ies|ied)\w*|despair\w*|"
    r"devastat\w*|stunned|shock\w*|mortified|embarrass\w*|grateful|gratitude|"
    r"tired|weary|exhaust\w*|pains?\b|pain\w*|cry|cries|cried|crying|tears?|"
    r"smile[sd]?|smiling|calm\w*|peace\w*|content|bitter\w*|jealous\w*)\b",
    re.I,
)
CAP = 60
BAND = (45, 70)

# N7 — the three ways this workshop's voice gets in front of the picture and
# explains it, found by hand in Chapter 19 and measured across all nineteen.
# Only phrasings with no other use in English go here: "lies" is the verb of a
# body on a floor eighty times in this book, so the word "lie" is not a signal.
MEMORABLE = re.compile(r"\b[Tt]hat is the thing\b|\bwill remember\b|\bwould remember\b", re.I)
COMMENTARY = re.compile(
    r"\b(?:she|he) (?:has|had) decided\b|\bthe account (?:she|he) gives?\b|\bit is the account\b"
    r"|\b(?:both|neither) (?:of )?(?:these )?(?:sentences|lines) are\b|\bis (?:not true|true)\b"
    r"|\bthe part she (?:would not|will not) have\b", re.I)
APHORISM = re.compile(r"^(?:So )?(?:Say|Tell|Remember|Consider|Imagine|Think of)\b", re.I)


def story_part(text):
    """The scenes only: after the head, before the footer."""
    body = text.split("\n## Footer", 1)[0]
    m = re.search(r"^## ", body, re.M)
    if m:
        body = body[m.start():]
    return body


def paragraphs(body):
    out = []
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or block.startswith("#") or re.fullmatch(r"[*\-_ ]{3,}", block):
            continue
        out.append(" ".join(block.split()))
    return out


def narration_of(par):
    t = QUOTED.sub(" ", par)
    t = OPEN_QUOTE.sub(" ", t)
    t = ITALIC.sub(" ", t)
    return t


def speech_of(par):
    return " ".join(m.group(0).strip("“”\"") for m in QUOTED.finditer(par))


def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?…])\s+", t) if re.search(r"\w", s)]


def figures(sents):
    lens = [len(s.split()) for s in sents]
    if not lens:
        return "none"
    under20 = 100 * sum(1 for n in lens if n < 20) // len(lens)
    return (f"{len(lens)} sentences, mean {statistics.mean(lens):.1f}, "
            f"median {statistics.median(lens):g}, under twenty words {under20}%, longest {max(lens)}")


def check(text):
    fails, notes = [], []
    pars = paragraphs(story_part(text))
    if not pars:
        return ["no story paragraphs found"], notes
    spoken = [p for p in pars if QUOTED.search(p) or OPEN_QUOTE.search(p)]
    share = 100 * len(spoken) / len(pars)
    flag = "" if BAND[0] <= share <= BAND[1] else f"  <- outside {BAND[0]}-{BAND[1]}%, look again"
    notes.append(f"N3  speech in {len(spoken)} of {len(pars)} paragraphs: {share:.0f}%{flag}")

    narr_sents, speech_sents = [], []
    for p in pars:
        narr = narration_of(p)
        for s in sentences(narr):
            narr_sents.append(s)
            m = PAST.search(s)
            if m:
                fails.append(f"N5  past tense in narration ({m.group(0)!r}): {s[:110]}")
        speech_sents += sentences(speech_of(p))
    for s in narr_sents + speech_sents:
        n = len(s.split())
        if n > CAP:
            fails.append(f"N4  a sentence of {n} words (cap {CAP}): {s[:110]}")
    # N7 — the commentary the author says he can hear. Three families, all of
    # them the voice stepping in to tell the reader what a line or a moment
    # means: a character's deception named by the narration, a moment labelled
    # as the one a character will remember, and an aphorism spoken to us.
    # Printed with the sentence, never fatal: whether a given line survives is
    # a call about the show's register, and the author makes it, not the tool.
    for s in narr_sents:
        for pat, why in ((COMMENTARY, "explains a character's lie"),
                         (MEMORABLE, "labels what will be remembered"),
                         (APHORISM, "an aphorism addressed to the reader")):
            m = pat.search(s)
            if m:
                notes.append(f"N7  the voice steps in ({why}, {m.group(0)!r}): {s[:110]}")
                break
    notes.append("N4  narration: " + figures(narr_sents))
    notes.append("N4  speech:    " + figures(speech_sents))
    # N8 — the rhythm band, printed and flagged, never fatal on its own. N6 is NOT
    # reused here: N6 was the feelings check, deleted by O035, and a deleted number
    # stays deleted so the mistake that paid for it keeps its receipt.
    # Chop is what the author hears as "too simple": a chapter built of
    # sentences under nine words reads in stabs. Stretch is the same illness
    # turned the other way. Both are measured on the narration only.
    lens = [len(s.split()) for s in narr_sents]
    if lens:
        chop = 100 * sum(1 for n in lens if n < 9) / len(lens)
        drag = 100 * sum(1 for n in lens if n > 45) / len(lens)
        msg = (f"N8  narration rhythm: {chop:.0f}% of narration under 9 words, "
               f"{drag:.0f}% over 45")
        if chop > 45:
            notes.append(msg + "  <- choppy: merge the stabs, the voice is not breathing")
        elif drag > 8:
            notes.append(msg + "  <- stretched: land the sentence, the reader is still walking")
        else:
            notes.append(msg)
    words = sum(len(p.split()) for p in pars)
    notes.append(f"    {words} words in the scenes")
    return fails, notes


CLEAN = """# Chapter 1 — A Fixture

*Episode reference: Naagin, season 7, Episode 1, "A Title" (first part).*

*Draft; not yet accepted.*

## The Ghat

The bell rings twice. A woman stops on the third step.

"Who is there?" she says.

"Nobody you know."

*He has my mother's eyes.* She puts the lamp down.

"Then why did you come?"

"I was sent."

## Footer

This fixture felt like a real chapter, as if it were one, and the room stopped the way a fan stops.
"""

DIRTY = CLEAN.replace(
    "The bell rings twice.",
    "The bell rings twice. The lamp was cold. "
    + "The river " + "goes on and on and " * 20 + "stops.",
).replace('"Nobody you know."', "He walks away.").replace('"I was sent."', "He goes.") \
 .replace('"Then why did you come?"', "She waits.").replace('"Who is there?" she says.', "She looks up.")


def selftest():
    ok = True
    f, n = check(CLEAN)
    if f:
        ok = False
        print("SELFTEST: the clean fixture failed:", f)
    f, n = check(DIRTY)
    for code in ("N4", "N5"):
        if not any(x.startswith(code) for x in f):
            ok = False
            print(f"SELFTEST: the planted {code} fault was not caught")
    if not any("look again" in x for x in n):
        ok = False
        print("SELFTEST: the low speech share was not flagged")
    print("SELFTEST:", "green — clean fixture passes, similes and all; planted N4, N5 and low speech share all caught. N2 and N6 are deleted by O035; N1 is deleted by O037" if ok else "RED")
    return 0 if ok else 1


def main(argv):
    if len(argv) == 2 and argv[1] == "--selftest":
        return selftest()
    if len(argv) < 2:
        print(__doc__)
        return 2
    bad = 0
    for path in argv[1:]:
        text = open(path, encoding="utf-8").read()
        fails, notes = check(text)
        print(path)
        for x in notes:
            print("  " + x)
        for x in fails:
            print("  FAIL " + x)
        print("  " + ("RED: %d" % len(fails) if fails else "green"))
        bad += len(fails)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
