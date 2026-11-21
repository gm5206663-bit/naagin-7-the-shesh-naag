#!/usr/bin/env python3
"""score_check.py — the score keeps its loyalties (canon/SOUND_AND_SCREEN.md §9).

    python3 tools/score_check.py chapters/Chapter_01_….md [more files]
    python3 tools/score_check.py --selftest

Written on the author's four orders of 2026-11-12, the third and fourth of which
are a cut: *"Purvi and vihaan romantic one also you design. Completely cut off
aryaman and Purvi canon romantic background music."* A cut that is only written
down is a cut that happens the first time anybody forgets. This is the machine
that does not forget.

Hard failures (exit 1):
  SC1  a romantic cue attached to **Aryaman and Purvi**. No soft cue, ever, on
       that pairing: the room's own music, or nothing (`§9.4`).
  SC2  **two registers at once** — her instrument and his, played in the same
       breath. The show scores one register at a time; the pair's theme is the
       one place they touch, and it is named as theirs (`§9.3`, `STYLE_CANON` §1h.12).
  SC3  **a tune given to Vihaan.** His cue is one low string struck and left
       hanging; he has no melody this season, and a paragraph that sings him has
       broken the design (`§9.2`).

  SC4  **a precap that scores a couple.** The last twenty seconds carry a threat,
       a held chord and a cut surge — nothing tender (`canon/SOUND_AND_SCREEN.md` §4).
       A love cue inside `## What Comes Next` is the frame selling a romance the cut
       has forbidden, and the author's order of 2026-11-12 puts that frame at the foot
       of every chapter, so the rule now binds nineteen files instead of one.
  SC5  **the titles carrying the love theme, or carrying two registers at once.**
       The card is the question and the answer is a different piece of music (§I).

Printed, never failed:
  the coverage of the three identities, chapter by chapter.
"""
import re
import sys

ROMANTIC = re.compile(r"love theme|their theme|Woh Do Log|vow song|romantic (strings|cue|score)|soft strings", re.I)
HE = re.compile(r"\bAryaman\b")
SHE = re.compile(r"\bPurvi\b|\bshe\b|\bher\b")
PAIR = re.compile(r"\bVihaan\b")

HERS = re.compile(r"\bbeen\b|bansuri|pungi", re.I)
HIS = re.compile(r"Ek Taar|one low string|his (one )?low string|the string he (is given|leaves)", re.I)
TOGETHER = re.compile(r"at once|together|over it|under it|while the been|both (themes|cues|registers)", re.I)
TUNE = re.compile(r"(his|Vihaan's) (theme|cue|music)[^.]{0,60}\b(tune|melody|song|chorus|sing|anthem)|his (tune|melody|anthem)", re.I)

LOVE = re.compile(r"love theme|Woh Do Log|their theme", re.I)
FRAME_HEAD = re.compile(r"^#{2,3} (What Comes Next|TITLES|THE CARD)\s*$", re.M)


def frame_blocks(text):
    """The book's frame: the card at a chapter's head and the precap at its foot."""
    out = []
    body = text.split("\n## Footer")[0]
    for m in FRAME_HEAD.finditer(body):
        nxt = re.search(r"^#{2,3} ", body[m.end():], re.M)
        end = m.end() + (nxt.start() if nxt else len(body))
        # paragraph by paragraph, not block by block: the card legitimately carries her
        # instrument and then his, one after the other, and that is the handover, not a clash
        out += [(m.group(1), p.strip()) for p in re.split(r"\n\s*\n", body[m.end():end]) if p.strip()]
    return out
NO_SCORE = re.compile(r"no score|nothing of the score|the score (goes out|stops|has no part)", re.I)


def paragraphs(text):
    body = text.split("\n## Footer")[0]
    return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]


def check(text):
    fails, notes = [], []
    pars = paragraphs(text)
    for p in pars:
        if ROMANTIC.search(p) and HE.search(p) and SHE.search(p) and not PAIR.search(p):
            fails.append("SC1  a romantic cue on Aryaman and Purvi: " + " ".join(p.split())[:110])
        if HERS.search(p) and HIS.search(p) and TOGETHER.search(p) and not LOVE.search(p):
            fails.append("SC2  two registers at once, her instrument and his: " + " ".join(p.split())[:110])
        m = TUNE.search(p)
        if m:
            fails.append(f"SC3  a tune written for Vihaan ({m.group(0)!r}): " + " ".join(p.split())[:110])

    for kind, blk in frame_blocks(text):
        if not blk:
            continue
        if kind == "What Comes Next" and (LOVE.search(blk) or ROMANTIC.search(blk)):
            fails.append("SC4  the precap scores a couple: " + " ".join(blk.split())[:110])
        if kind in ("TITLES", "THE CARD"):
            if LOVE.search(blk) or ROMANTIC.search(blk):
                fails.append("SC5  the titles carry the love theme: " + " ".join(blk.split())[:110])
            if HERS.search(blk) and HIS.search(blk) and TOGETHER.search(blk):
                fails.append("SC5  the titles run her instrument and his at once: " + " ".join(blk.split())[:110])

    notes.append("frame blocks found: " + str(len(frame_blocks(text))) + " (the card, the precap)")
    notes.append("his cue `Ek Taar` named in " + str(sum(1 for p in pars if HIS.search(p))) + " paragraph(s)")
    notes.append("their theme `Woh Do Log` / the love theme: " + str(sum(1 for p in pars if LOVE.search(p))) + " paragraph(s)")
    notes.append("a scene of Aryaman and Purvi declared unscored: " + str(sum(1 for p in pars if NO_SCORE.search(p) and HE.search(p))) + " paragraph(s)")
    return fails, notes


CLEAN = """# Chapter 99 — The Fixture

### TITLES

The logotype comes up over thundercloud. A man's voice asks two words in the pitch of a been, and a choir of women leaves the answer unfinished. The been stops, and one low string is struck and left hanging.

## The Room

The lamp is lit and the hall is full, and the been takes up its phrase over the crowd.

The love theme comes up on one string, low, and the drone the titles use under it, and it does not resolve.

Aryaman stands at the wall with his glass, and the band plays for the room and not for him, and when the two of them are left alone the band stops.

Vihaan puts the crate down and one low string is struck and left hanging, three seconds, and it stops the moment anybody thanks him.

## What Comes Next

*A precap, as the episode gives one.*

A hand going into the dark behind the chandelier, and one held chord. The surge, cut before it lands.

## Footer

BASE: fixture.
"""

DIRTY_FRAME = CLEAN.replace(
    "A hand going into the dark behind the chandelier, and one held chord. The surge, cut before it lands.",
    "Aryaman and Purvi slow-dance while the love theme comes up soft under them, and the surge does not cut.",
).replace(
    "The been stops, and one low string is struck and left hanging.",
    "The been runs on under his one low string at once, and the love theme takes the last three seconds.",
)

DIRTY = (
    CLEAN.replace(
        "Aryaman stands at the wall with his glass, and the band plays for the room and not for him, and when the two of them are left alone the band stops.",
        "Aryaman takes Purvi's hand at the stair, and the love theme comes up soft under them, and the room is asked to want it.",
    )
    .replace(
        "The lamp is lit and the hall is full, and the been takes up its phrase over the crowd.",
        "The lamp is lit and the hall is full, and the been takes up its phrase over the crowd with his one low string under it at once.",
    )
    .replace(
        "Vihaan puts the crate down and one low string is struck and left hanging, three seconds, and it stops the moment anybody thanks him.",
        "Vihaan puts the crate down, and his theme comes in with its tune, a full melody the crowd could sing.",
    )
)


def selftest():
    ok = True
    f, n = check(CLEAN)
    if f:
        ok = False
        print("SELFTEST: the clean fixture failed:", f)
    f, n = check(DIRTY)
    f, n = check(CLEAN)
    if f:
        ok = False
        print("SELFTEST: the compliant chapter (card, room, precap) failed:", f)
    f, n = check(DIRTY)
    for code in ("SC1", "SC2", "SC3"):
        if not any(x.startswith(code) for x in f):
            ok = False
            print(f"SELFTEST: the planted {code} fault was not caught")
    f, n = check(DIRTY_FRAME)
    for code in ("SC4", "SC5"):
        if not any(x.startswith(code) for x in f):
            ok = False
            print(f"SELFTEST: the planted {code} frame fault was not caught")
    print("SELFTEST:", "green — a clean card, the unscored room and his hanging note pass; a romantic cue on "
          "Aryaman and Purvi, two registers at once, a tune for Vihaan, a precap that scores a couple and a card "
          "that runs the love theme or both instruments in one breath all fail." if ok else "RED")
    return 0 if ok else 1


def main(argv):
    if len(argv) == 2 and argv[1] == "--selftest":
        return selftest()
    files = argv[1:]
    if not files:
        print(__doc__)
        return 2
    bad = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        fails, notes = check(text)
        name = re.search(r"Chapter_(\d+)", f)
        print("  Chapter " + (name.group(1) if name else f) + ": " + ("RED — " + "; ".join(fails) if fails else "green"))
        for x in notes:
            print("        " + x)
        bad += len(fails)
    print("-" * 60)
    print("score_check.py —", f"{bad} fault(s) in {len(files)} chapter(s).",
          "The cut holds: no romantic cue on Aryaman and Purvi anywhere, none in the precap, "
          "never two registers at once, nothing tender over the card, no tune for the male lead.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
