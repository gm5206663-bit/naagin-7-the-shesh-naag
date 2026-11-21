#!/usr/bin/env python3
"""tools/eyes_check.py — who is allowed to have an opinion about Purvi's face.

The law is `canon/STYLE_CANON.md` §1g; the ruling is `O033`.

    python3 tools/eyes_check.py chapters/*.md
    python3 tools/eyes_check.py --selftest

What it reports
  RED   the NARRATION grades her: beautiful / beauty / pretty / gorgeous /
        lovely / stunning / sundar / khoobsurat / haseen, outside speech.
        The camera loves her and does not grade her. There is no whitelist.
  AMBER a line of SPEECH about her looks from somebody who is not allowed one.
        Only one exception is canon law on this page: Ananta in Chapter 2,
        over-correcting her sister out of love, which Purvi refuses.
  AMBER a line of speech in which anybody in the Suri house praises her face.
  NOTE  which of the five `O033` devices a chapter has spent, so the count can
        be seen (device detection is a keyword guess, printed, never failed).

It cannot check the thing that matters most: whether his eyes are actually on
her in the frame, and whether the timing of one step back is doing the work.
Green here is permission, not a draft.
"""
import re
import sys

FOOTER = "## Footer"

GRADE = re.compile(
    r"\b(beautiful|beauty|prett(?:y|iest)|gorgeous|lovely|stunning|"
    r"sundar\w*|khoobsurat|haseen\w*)\b",
    re.I,
)
HER = re.compile(r"\b(purvi|her|she|uska|uski|uske|woh|tu|tum|teri|tera|tumhara|tumhari)\b", re.I)
# A beauty word near one of these is about a garment, a jewel or the dragon, not a face.
NOT_HER = re.compile(r"\b(jacket|sari|saree|kameez|kurta|shirt|muffler|dupatta|gown|jewel|necklace|experiment|dragon|sofa|car|house|room|mandap|halwai|mehndi|rangoli|diya)\b", re.I)

QUOTED = re.compile(r"[“\"][^”\"]*[”\"]", re.S)
SCENE = re.compile(r"^##\s+(.+)$", re.M)

# The one permitted voice in the whole book so far (§2 of canon/TWO_PAIRS_OF_EYES.md).
ALLOWED = [
    (r"Chapter_02", r"tu khud bhi toh kitni pretty hai"),
    (r"Chapter_02", r"itni zyada pretty hai"),
]

DEVICES = {
    "one frame, two seeings": r"\b(aunt|masi|chachi|tau ji|pinky|nimrat|the room)\b",
    "the object": r"\b(lens|spectacle|chashma|glass|plate|tray|file|chair|dupatta|card)\b",
    "held look after she turns away": r"\b(turns? (?:to go|away)|goes (?:out|through)|after (?:she|the door))\b",
    "what he remembers": r"\b(remember\w*|yaad)\b",
    "her looking back": r"\b(looks (?:at him|back)|dekht\w*)\b",
}


def scenes_of(text):
    marks = [(m.start(), m.group(1).strip()) for m in SCENE.finditer(text)]
    out = []
    for i, (pos, name) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        if name.lower().startswith("footer"):
            end = pos
            break
        out.append((name, text[pos:end]))
    return out


def check(path, verbosity=2):
    raw = open(path, encoding="utf-8").read()
    body = raw.split(FOOTER, 1)[0]
    fails, warns, notes = [], [], []

    def allowed(chapter, line):
        for ch, pat in ALLOWED:
            if ch in chapter and re.search(pat, line, re.I):
                return True
        return False

    for name, chunk in scenes_of(body):
        # narration = the chunk with every quoted span removed
        narration = QUOTED.sub(" ", chunk)
        for line in narration.split("\n"):
            for m in GRADE.finditer(line):
                fails.append(f"RED   {name}: the narration grades her — “{m.group(0)}” in: {line.strip()[:90]}")

        for line in chunk.split("\n"):
            if not GRADE.search(line):
                continue
            if not QUOTED.search(line):
                continue  # narration already handled above
            if allowed(path, line):
                warns.append(f"KNOWN {name}: Ananta's permitted line — {line.strip()[:90]}")
            elif not HER.search(line) or NOT_HER.search(line):
                notes.append(f"OTHER {name}: a beauty word about a thing, not a face — {line.strip()[:90]}")
            else:
                warns.append(f"AMBER {name}: speech about her looks — {line.strip()[:110]}")

    spent = [d for d, pat in DEVICES.items() if re.search(pat, body, re.I)]

    if verbosity:
        print(f"\n=== {path}")
        for f in fails:
            print("  " + f)
        for w in warns:
            print("  " + w)
        for n in notes:
            print("  " + n)
        print("  NOTE devices present (keyword guess): " + (", ".join(spent) if spent else "none"))
        if not fails and not warns:
            print("  green: no verdict on her face, from anybody, anywhere in this chapter.")
    return fails


def selftest():
    import tempfile, os
    ok = True
    cases = [
        ('She is beautiful.', True),
        ('"Tu bahut sundar hai," the aunt says.', False),
        ('The camera lingers on the beautiful girl.', True),
        ('He looks at the door after she goes.', False),
    ]
    for text, should_fail in cases:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write("## A Scene\n\n" + text + "\n\n## Footer\n")
            p = f.name
        got = bool(check(p, verbosity=0))
        os.unlink(p)
        if got != should_fail:
            print(f"SELFTEST FAIL: {text!r} expected fail={should_fail} got {got}")
            ok = False
    print("selftest", "ok" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "--selftest":
        sys.exit(selftest())
    bad = 0
    for p in args:
        bad += len(check(p))
    print(f"\n{len(args)} chapter(s); {bad} narration verdict(s).")
    print("GREEN — nobody grades her face." if bad == 0 else "RED — the narration is grading her face.")
    sys.exit(0 if bad == 0 else 1)
