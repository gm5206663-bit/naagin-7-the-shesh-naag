#!/usr/bin/env python3
"""oc_check.py — is Vihaan actually in this chapter, and does the chapter say so?

    python3 tools/oc_check.py chapters/Chapter_04_....md [more files]
    python3 tools/oc_check.py --selftest

The law is `foundation/OC_PRESENCE.md`: a scene may leave him out; a chapter may
not. The chapter declares its touches in the footer, on one line that begins
`OC:`, listing the scene headings, separated by ` · `:

    OC:  The Nine O'Clock News · The Cabin · The Job · The Suri House, Later

That declaration is the point. It cannot drift out of date silently, it costs the
writer a decision per chapter, and this tool checks it against the page.

Fails:
  OC1  no `OC:` line in the footer — the chapter does not say where he is
  OC2  fewer than two scenes declared (the floor is two)
  OC3  a declared scene heading does not exist in the chapter
  OC4  a declared scene does not mention him at all (no name, no he/his/him)
  OC5  the chapter's scenes mention him nowhere, whatever the footer claims
  OC6  fewer than two places where somebody on the page looks at him (O025)
  OC7  a line that disclaims his looks — the hedge the author named
  OC8  a line that makes him small — service words in the narration (O026, gate 22)
  OC9  **a chapter that leaves him without a line.** He is present in three or
       more scenes and the page attributes fewer than two of its quotations to him:
       the man who only watches, counts, and straightens things (the author, on
       Chapter 19: *"Vihaan should talk or others things, you make him silent, that
       is completely wrong"* — `WRITING.md` §0.1, `O040`)
  OC10 **a scene that writes his silence as his part in it.** He is in the scene, the
       narration hands him a silence phrase (*says nothing*, *saying nothing*, *does not
       answer*, *not a word*, *says it to nobody*), and the footer has not said why under
       `SILENT:`. A scene may leave him mute for a reason; it may not do it by default.

Prints each declared scene with one line of what he is doing in it.
"""
import re
import sys

NAME = re.compile(r"\bVihaan\b")
PRONOUN = re.compile(r"\b(he|his|him)\b", re.I)
DECL = re.compile(r"^\s*OC:\s*(.+)$", re.M)
# Others looking at him: a sight verb with him in the object place.
SEEN = re.compile(
    r"(look|looked|looks|looking|stared|stares|staring|glanced|glances|glancing|"
    r"watch|watches|watched|watching|saw|see|seen|noticed|noticing|eyes?\s+(on|to|over|found|went|"
    r"and up|fixed)|turned\s+to\s+look|turns\s+to\s+look|"
    r"looked\s+back\s+at|look\s+at)"
    r"[^.?!\n]{0,40}?\b(him|Vihaan|his\s+face|his\s+hands)\b", re.I)
SAID_OF_LOOKS = re.compile(
    r"(handsome|good-looking|sundar|so\s+fair|beautiful\s+(boy|man|face)|"
    r"look(s|ed)?\s+(at|how)\s+(him|he)\b)", re.I)
# Small: the narration treating him as the help (RULES gate 22, L-22).
SMALL = [
    "small work", "errand boy", "errand-boy", "the help", "gofer", "gopher",
    "dogsbody", "odd jobs", "odd-jobs", "the boy who fetched", "fetch and carry",
    "no standing in the house", "nothing more than a servant",
]
# The hedge: admitting he is noticed and then apologising for it (RULES gate 20, L-20).
DISCLAIM = [
    "that is all it does",
    "all it does is",
    "wins him nobody",
    "nobody's trust",
    "ordinary way",
    "does not trade on it and never",
    "if anything, it puts people off",
    "no one would call him",
    "not conventionally handsome",
    "plain enough",
]
HEAD = re.compile(r"^## (.+)$", re.M)
SILENCE = ("says nothing", "saying nothing", "does not answer", "not a word",
           "says it to nobody", "says it to the floor", "keeps his mouth", "and does not speak")
SILENT_RE = re.compile(r"^\s*SILENT:\s*(.+?)\s*$", re.M)


SAY_TAIL = re.compile(r"^\s*,?\s*(?:\"[^\"]{0,40}\"\s*,?\s*)?(Vihaan\b|he\s+(?:says|asks|answers|repeats|calls|murmurs|shouts|tells|reads)|his\s+voice)")
SAY_HEAD = re.compile(r"(Vihaan|he)\s+(?:it\s+)?(?:also\s+)?(says|asked|asks|answers|answered|repeats|called\s+out|calls|murmurs|shouts|tells|reads)[^.]{0,14}[:.\u2014-]\s*$")


def his_silence(block):
    """The silence phrase, but only when the sentence hands it to him.

    The room is allowed to be quiet at him; he is not allowed to be quiet instead of
    being a person. A clause that opens on him, or ends on his name, is his; a clause
    whose own last name is somebody else's (`when Shyam does not answer`) is not.
    """
    low = block.lower()
    for ph in SILENCE:
        for m in re.finditer(re.escape(ph), low):
            window = block[max(0, m.start() - 110):m.start()]
            clause = re.split(r"[.!?]\s", window)[-1].strip()
            names = re.findall(r"\b(?:Vihaan|[A-Z][a-z]{2,})\b", window)
            if names and names[-1] == "Vihaan":
                return ph
            if not names and re.match(r"^(?:and\s+|but\s+|so\s+)?he\b", clause, re.I) and re.search(r"\bVihaan\b", block[:m.start()]):
                return ph
    return None


def his_turns(body):
    """Quotations the page hands to him: a tag in front of the quote, or his name as the
    sentence that follows it. A floor, not a proof — a bare action beat counts ("Shaadi kab
    hai?" Vihaan sits down) and a line given in a paragraph that never names him does not;
    the human read is `foundation/OC_PRESENCE.md` §5a.
    """
    n = 0
    for para in [x.strip() for x in re.split(r"\n\s*\n", body) if x.strip()]:
        for m in re.finditer(r'"([^"]{4,})"', para):
            if SAY_TAIL.match(para[m.end():m.end() + 60]):
                n += 1
                continue
            if SAY_HEAD.search(para[max(0, m.start() - 90):m.start()]):
                n += 1
    return n


def scene_map(text):
    body = text.split("## Footer")[0]
    marks = [(m.start(), m.group(1).strip()) for m in HEAD.finditer(body)]
    out = {}
    for i, (pos, name) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(body)
        out[name] = body[pos:end]
    return body, out


def first_action(block):
    """The first thing he does in the scene. His name if it is there, then the boy, then a pronoun."""
    sents = [s.replace("\n", " ") for s in re.split(r"(?<=[.!?])\s+", block)]
    for pattern in (NAME, re.compile(r"\bthe boy\b", re.I), PRONOUN):
        for s in sents:
            if pattern.search(s):
                return s.strip()[:120]
    return ""


def check(path):
    text = open(path, encoding="utf-8").read()
    body, smap = scene_map(text)
    footer = text[len(body):]
    fails, notes = [], []

    m = DECL.search(footer)
    if not m:
        if NAME.search(body):
            fails.append("OC1  he is in the scenes but the footer carries no `OC:` line — "
                         "declare the scenes he is in (foundation/OC_PRESENCE.md §4)")
        else:
            fails.append("OC1  no `OC:` line and no him in the scenes — a chapter with no him "
                         "is not this serial (foundation/OC_PRESENCE.md §2 law 1)")
        return fails, notes

    declared = [s.strip() for s in m.group(1).split("·") if s.strip()]
    if len(declared) < 2:
        fails.append(f"OC2  {len(declared)} scene declared — the floor is two")

    for name in declared:
        if name not in smap:
            fails.append(f"OC3  declared scene not found: {name!r}")
            continue
        block = smap[name]
        if not (NAME.search(block) or PRONOUN.search(block)):
            fails.append(f"OC4  declared scene does not mention him: {name!r}")
            continue
        notes.append(f"     · {name} — {first_action(block)}")

    present = [nm for nm, blk in smap.items() if NAME.search(blk)]
    turns = his_turns(body)
    if len(present) >= 3 and turns < 2:
        fails.append(f"OC9  he is in {len(present)} scenes and speaks in none of them worth the name "
                     f"({turns} quotation(s) handed to him) — a man written only to watch is written silent "
                     f"(WRITING.md §0.1; O040; the author's order of 2026-11-12)")
    # OC10 — the silence phrase, scene by scene, unless the footer has owned it.
    m2 = SILENT_RE.search(footer)
    # each item is `Scene Name (the reason)` — the reason is required, not decoration
    exempt, why = set(), {}
    if m2:
        # split on the separator only: a scene name may itself contain a comma
        for item in m2.group(1).split("·"):
            item = item.strip()
            if not item:
                continue
            nm, _, reason = item.partition(" (")
            nm = nm.strip()
            exempt.add(nm)
            if reason:
                why[nm] = reason.rstrip(")").strip()
    quiet = []
    for nm, blk in smap.items():
        if not NAME.search(blk):
            continue
        ph_hit = his_silence(blk)
        if ph_hit and nm not in exempt:
            quiet.append((nm, ph_hit))
    for nm in [q[0] for q in quiet if q[0] in why]:
        notes.append(f"     · {nm} — mute on purpose: {why[nm]}")
    for nm, ph in quiet:
        fails.append(f"OC10  {nm!r} writes his silence ({ph!r}) with no reason on the footer's `SILENT:` line "
                     f"(O040; WRITING.md §0.1)")
    notes.append(f"     · in {len(present)} scene(s), with {turns} line(s) the page gives him"
                 + (f", and {len(quiet)} scene(s) written mute" if quiet else ""))

    if not NAME.search(body) and not any(PRONOUN.search(smap[n]) for n in declared if n in smap):
        fails.append("OC5  the scenes mention him nowhere, whatever the footer says")

    # OC6 and OC7 — is he seen, and is he hedged? (O025; WRITING.md §5a)
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    seen = [p for p in paras
            if (NAME.search(p) or re.search(r"\b(the boy|he|his|him)\b", p, re.I))
            and (SEEN.search(p) or SAID_OF_LOOKS.search(p))]
    # A floor, not a proof: `SEEN` asks for a sight verb with him in the object
    # place. It can be fooled by "he looked at him"; the human read is §5a.
    if len(seen) < 2:
        fails.append(f"OC6  {len(seen)} place(s) where somebody looks at him — the floor is two "
                     f"(O025; WRITING.md §5a)")
    else:
        notes.append(f"     · seen in {len(seen)} paragraph(s)")
    low = body.lower()
    for phrase in DISCLAIM:
        if phrase in low:
            fails.append(f"OC7  the page disclaims his looks: {phrase!r} "
                         f"(RULES gate 20; L-20)")
    for phrase in SMALL:
        if phrase in low:
            fails.append(f"OC8  the page makes him small: {phrase!r} "
                         f"(O026; gate 22; L-22)")

    notes.insert(0, f"OC   declared in {len(declared)} scene(s), on the page in "
                    f"{len(NAME.findall(body))} place(s)")
    return fails, notes


CASES = [
    ("clean", """# T

## One

Vihaan lifts the crate and goes out. The caterer's boy watches him over the crate.

## Two

Two women at the list look at him and lose their place. Vihaan stands on the roof.

## Footer

OC:  One · Two
""", []),
    ("undeclared", """# T

## One

Vihaan lifts the crate.

## Two

Vihaan stands on the roof.

## Footer

Nothing said about him.
""", ["OC1"]),
    ("floor", """# T

## One

Vihaan lifts the crate. Two women look at him, and one of them looks again.

## Two

The room empties. The boy at the door watches him go.

## Footer

OC:  One
""", ["OC2"]),
    ("ghost-scene", """# T

## One

Vihaan lifts the crate. The boy at the door looks at him.

## Two

The room empties. A woman looks at him as she goes past.

## Footer

OC:  One · The Roof
""", ["OC3"]),
    ("empty-scene", """# T

## One

Vihaan lifts the crate. The boy at the door looks at him.

## Two

The room empties and the rain starts.

## Three

A woman on the step turns and looks at him.

## Footer

OC:  One · Two
""", ["OC4"]),
    ("unseen", """# T

## One

Vihaan lifts the crate and goes out.

## Two

Vihaan stands on the roof and watches the car come in.

## Footer

OC:  One · Two
""", ["OC6"]),
    ("small", """# T

## One

Vihaan lifts the crate. The boy at the door looks at him.

## Two

A woman looks at him, and looks again. It is only the small work they give him.

## Footer

OC:  One · Two
""", ["OC8"]),
    ("loud", """# T

## One

Vihaan lifts the crate and goes out. "Rakho idhar, dono." The caterer's boy watches him over the crate.

## Two

"Aur tray kaun uthayega?" Vihaan says it without turning round, and a woman at the list looks at him, and looks again.

## Three

Vihaan stands on the roof. "Do ghante," he says, and the man beside him nods.

## Footer

OC:  One · Two · Three
""", []),
    ("muted-but-owned", """# T

## One

Vihaan lifts the crate. "Rakho idhar, dono," Vihaan says, and a boy looks at him.

## Two

"Kitne?" Vihaan says it, and the woman at the list looks at him, and looks again.

## Three

Vihaan stands at the door, and the driver says "Chaliye, sahab" to nobody, and Vihaan says nothing, because the man in the car is not his to wake.

## Footer

OC:  One · Two · Three
SILENT:  Three
""", []),
    ("mute", """# T

## One

Vihaan lifts the crate and goes out, and says nothing. The caterer's boy watches him over the crate. "Rakho idhar," the boy says to another boy.

## Two

Vihaan stands by the list and counts. A woman at the list looks at him, and looks again. "Ye kitne hain?" the woman says to the man beside her.

## Three

Vihaan is at the door with his hands at his sides, saying nothing, and the driver says "Chaliye, sahab" to nobody, and the lamp dips and steadies.

## Footer

OC:  One · Two · Three
""", ["OC10", "OC9"]),
    ("disclaimed", """# T

## One

Vihaan lifts the crate. The boy looks at him. He is striking to look at, and does not trade on it: that is all it does; it wins him nobody's trust.

## Two

A woman at the list looks at him, and looks again.

## Footer

OC:  One · Two
""", ["OC7"]),
]


def selftest():
    ok = True
    for name, text, expect in CASES:
        path = f"/tmp/oc_selftest_{name}.md"
        open(path, "w", encoding="utf-8").write(text)
        fails, _ = check(path)
        got = sorted({f.split()[0] for f in fails})
        want = sorted(expect)
        if got != want:
            ok = False
            print(f"SELFTEST FAIL {name}: expected {want}, got {got}")
    print("SELFTEST:", "green — planted OC1 to OC10 all caught; the clean, the loud and the disclaimed fixtures pass as they should" if ok else "RED")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    paths = [a for a in argv[1:] if not a.startswith("-")]
    if not paths:
        import glob
        paths = sorted(glob.glob("chapters/*.md"))
    bad = 0
    for p in paths:
        fails, notes = check(p)
        print(p)
        for n in notes:
            print("  " + n)
        for f in fails:
            print("  FAIL " + f)
        print("  " + ("green" if not fails else f"RED: {len(fails)}"))
        bad += len(fails)
    print()
    print("GREEN. Every chapter has him in at least two scenes, says where, somebody looks at him, nobody writes him small, and nobody writes him silent." if not bad
          else f"RED. {bad} problem(s).")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
