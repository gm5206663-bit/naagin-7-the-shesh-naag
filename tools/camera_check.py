#!/usr/bin/env python3
"""camera_check.py — measure a chapter against WRITING.md §2 (the camera).

    python3 tools/camera_check.py chapters/Chapter_01_….md [more files]
    python3 tools/camera_check.py --selftest

Hard failures (exit 1):
  N1  a comparison in narration: like / as if / as though, outside speech
  N2  a feeling named in the narration. NOT a failure: the author's ruling O019
      asks for the feeling to be named where canon shows it. It is printed so the
      writer can check each one against the scene.
  N6  the cause of a feeling explained in the narration: a feeling word and
      because / why in the same sentence
  N4  a sentence of more than 60 words, anywhere
  N5  the past tense in narration: was / were / had been / did not / could not /
      would have, outside speech (the scenes are told in the present)

Printed, not failed:
  N3  the share of paragraphs that are speech (looked at again outside 45-70%)
  sentence figures for the narration and for the speech

"Speech" is anything inside double quotation marks, straight or curly, and
anything inside *italics* (the voiced aside). The head above the first scene
heading and everything from "## Footer" on are left out.
"""
import re
import statistics
import sys

SIMILE = re.compile(r"\b(like|as if|as though)\b", re.I)
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
    fails, notes, feelings = [], [], []
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
            m = SIMILE.search(s)
            if m:
                fails.append(f"N1  comparison in narration ({m.group(0)!r}): {s[:110]}")
            m = INTERIOR.search(s)
            if m:
                feelings.append(f"N2  feeling or thought named in narration ({m.group(0)!r}): {s[:110]}")
            m = FEELING.search(s)
            if m:
                feelings.append(f"N2  feeling named in narration ({m.group(0)!r}): {s[:110]}")
                if re.search(r"\b(because|why)\b", s, re.I):
                    fails.append(f"N6  the cause of a feeling explained ({m.group(0)!r}): {s[:110]}")
            m = PAST.search(s)
            if m:
                fails.append(f"N5  past tense in narration ({m.group(0)!r}): {s[:110]}")
        speech_sents += sentences(speech_of(p))
    for s in narr_sents + speech_sents:
        n = len(s.split())
        if n > CAP:
            fails.append(f"N4  a sentence of {n} words (cap {CAP}): {s[:110]}")
    notes.append(f"N2  {len(feelings)} feeling(s) named in the narration:")
    notes += ["      " + f for f in feelings]
    notes.append("N4  narration: " + figures(narr_sents))
    notes.append("N4  speech:    " + figures(speech_sents))
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

This fixture felt like a real chapter, as if it were one.
"""

DIRTY = CLEAN.replace(
    "The bell rings twice.",
    "The bell rings twice like a warning. She felt cold. It seemed late. She felt cold because he came. The lamp was cold. "
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
    for code in ("N1", "N4", "N5", "N6"):
        if not any(x.startswith(code) for x in f):
            ok = False
            print(f"SELFTEST: the planted {code} fault was not caught")
    if not any(x.startswith("N2") for x in n):
        ok = False
        print("SELFTEST: the planted feeling was not listed under N2")
    if not any("look again" in x for x in n):
        ok = False
        print("SELFTEST: the low speech share was not flagged")
    print("SELFTEST:", "green — clean fixture passes; planted N1, N4, N5, N6 and low speech share all caught, and N2 lists the feeling" if ok else "RED")
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
