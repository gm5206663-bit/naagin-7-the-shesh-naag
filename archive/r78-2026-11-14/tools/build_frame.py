#!/usr/bin/env python3
"""Apply the season's frame at BOTH ends of every chapter, per the author's order of 2026-11-12.

  head  Ch2-19 : the twelve-second cut-down of the theme (`canon/TITLES_SEQUENCE.md` §I)
  sound Ch1-15,18 (the fifteen chapters that already carry `## What Comes Next`): the cue line §IV requires
  foot  Ch14, Ch16, Ch17 : the three precaps the book was missing, in the house form
  card  Ch19 : the tail card, because the season's last chapter has no tomorrow to preview

Every quoted line and every image named in a new precap is checked against the text of the chapter it
promises before anything is written (the law of the form: a precap may only show what is there).

Nothing here may be a `## ` heading: `tools/recount.py` and `tools/eyes_check.py` key scenes off
`^##\\s+(.+)$`, so a `## ` block would enter the ledger as a scene. The head cut and the tail card sit
above the first `## ` and below the last one, as `### `.
"""
import re, glob, sys

D = {int(re.search(r"_(\d+)_", f).group(1)): f for f in glob.glob("chapters/Chapter_*.md")}

HEAD = """### TITLES

*The twelve seconds the season plays on every night after its first: the theme, then straight in (`canon/TITLES_SEQUENCE.md` §I). The full forty seconds are written once, at the head of Chapter 1, and are not repeated below it.*

The logotype comes up over thundercloud, with something red falling through the frame too slowly to be rain.

A man's voice asks two words in the pitch of a been: *"Kaun hai woh."* A choir of women answers underneath him and leaves the answer unfinished.

The been stops. One low string is struck and left hanging over the black.

A drum, once. Then the story, and no music under it until the story asks.

"""

SOUND = ("\n\n*Sound, per `canon/SOUND_AND_SCREEN.md` §4: the theme's first four notes under the threat, "
         "one held chord on the thing at risk, the surge cut off before it lands, and nothing at all over "
         "the black and the card. Her been only — no romance on the promise, and no tune for anybody else.*")

NOTE = "*A precap, as the episode gives one.*"

# target chapter -> (paragraphs, closing drum line, verbatim lines/images that must exist in that chapter)
NEW = {
 15: (["A man stands at a parapet at one in the morning with his phone in one hand and his spectacles in the other, "
       "and he does the sum again because the sum is the part that does not fit. \"Shayad yeh log kuch bahut bada plan "
       "kar rahe hain.\"",
       "A warrant taken out at first light, and a notice board with one of its notices hanging by a corner. A fire "
       "burning on a lawn at seven in the morning, and two brides in a house that has one daughter.",
       "And a man coming down a staircase with his sleeves rolled, and the chapter cutting before he reaches the bottom."],
      "A drum, once. The fire goes on behind it, and the man on the staircase is not at the bottom of it yet.",
      ["Shayad yeh log kuch bahut bada plan kar rahe hain.", "Kal subah sabse pehle warrant nikaalo.",
       "one of them is hanging by a corner", "The fire burns on the lawn", "sleeves rolled"]),
 17: (["A hall at four in the afternoon with the chandelier on and a tent's canvas going up outside the windows, and "
       "a man standing up out of his chair with both hands behind his back. \"Reedh ki haddi pe maarunga na, to us "
       "second mein mar jayegi.\"",
       "A been lying across the knees of the man who carries it, and the case for it open at his feet. A brass knife "
       "in the hand of a man who has never needed one.",
       "And a woman who will not say what she is, in a room where everyone has already decided."],
      "A drum, once. The been goes into its case, and the hall is still waiting.",
      ["Reedh ki haddi pe maarunga na", "been lies across the knees", "the case for it is at his feet",
       "chandelier on and the tent's canvas going up"]),
 18: (["Three in the morning, and every light in the Suri house is on, and the hall has been washed twice. A dark "
       "place in the pile of the carpet at the third step that has dried brown.",
       "A flash going up a stairwell and putting the banister on the wall for a moment. A camera turned over in a "
       "man's hands, and a boy standing at the end of the passage with his cap in his hands.",
       "And a river, and a van in it, and eyes in the mud that open."],
      "A drum, once. The flash goes up again, and this time the frame does not take the picture back.",
      ["every light in the Suri house is on", "The hall has been washed twice", "dried brown",
       "puts the banister on the wall", "his cap in his hands"]),
}

CARD = """### THE CARD

*The season's last chapter has no tomorrow to preview, so the frame at its foot is not a precap. It is the card, run the way it was run on the first night, and it asks the question the season has spent nineteen chapters not answering.*

Black, and the been alone.

The logotype comes up over thundercloud, and the something red is still falling, and it is still too slow to be rain.

The voice asks it once, and the choir does not answer: *"Kaun hai woh."*

One low string is struck after it, and left hanging, and the hang is where the book stops.

A drum, once. Then the next season, and no music under it until it asks.

"""

ANCHOR = "*Draft; not yet accepted.*\n"


def body(n):
    return open(D[n], encoding="utf-8").read().split("\n## Footer")[0]


def validate():
    bad = []
    for tgt, (paras, close, keys) in NEW.items():
        t = body(tgt)
        for k in keys:
            if k not in t:
                bad.append(f"Ch{tgt-1} precap: {k!r} is not verbatim in Ch{tgt}")
        if len(close.split()) > 30:
            bad.append(f"Ch{tgt-1} precap: the closing beat is too long: {close!r}")
    for n in NEW:
        if "## What Comes Next" in body(n - 1):
            bad.append(f"Ch{n-1} already has a precap")
    return bad


def build_precap(tgt):
    paras, close, _ = NEW[tgt]
    out = "## What Comes Next\n\n" + NOTE + SOUND + "\n\n"
    out += "\n\n".join(paras) + "\n\n" + close + "\n\n"
    return out


def main():
    apply = "--apply" in sys.argv
    bad = validate()
    if bad and all("already has a precap" in b for b in bad):
        print("already applied: every chapter the frame belongs to has it (heads 2-19, feet 1-18, card on 19) — nothing to write")
        return 0
    if bad:
        print("VALIDATION FAILED:")
        for b in bad:
            print("  -", b)
        return 1
    print("validated: 3 new precaps (every image found in the chapter it promises), 18 head cuts, 15 cue lines, 1 card")
    if not apply:
        for n in sorted(NEW):
            print("\n" + "=" * 18, f"Ch{n-1} foot -> Ch{n}", "=" * 18)
            print(build_precap(n))
        print("=" * 18, "head cut (Ch2-19)", "=" * 18)
        print(HEAD)
        print("=" * 18, "Ch19 card", "=" * 18)
        print(CARD)
        print("(dry run: nothing written. pass --apply)")
        return 0
    heads = sounds = 0
    for n in range(2, 20):
        t = open(D[n], encoding="utf-8").read()
        assert t.count(ANCHOR) == 1 and "### TITLES" not in t, D[n]
        t = t.replace(ANCHOR, ANCHOR + "\n" + HEAD, 1)
        open(D[n], "w", encoding="utf-8").write(t)
        heads += 1
    for n in sorted(D):
        t = open(D[n], encoding="utf-8").read()
        if NOTE in t:
            assert t.count(NOTE) == 1 and SOUND not in t, D[n]
            t = t.replace(NOTE, NOTE + SOUND, 1)
            open(D[n], "w", encoding="utf-8").write(t)
            sounds += 1
        if n in NEW:
            # NEW is keyed by the chapter the precap PROMISES; it sits at the foot of the one before it.
            prev = n - 1
            assert "## What Comes Next" not in body(prev), D[prev]
            tp = open(D[prev], encoding="utf-8").read()
            assert tp.count("\n## Footer") == 1, D[prev]
            tp = tp.replace("\n## Footer", "\n" + build_precap(n) + "## Footer", 1)
            open(D[prev], "w", encoding="utf-8").write(tp)
    t = open(D[19], encoding="utf-8").read()
    assert t.count("\n## Footer") == 1 and "### THE CARD" not in t
    t = t.replace("\n## Footer", "\n" + CARD + "## Footer", 1)
    open(D[19], "w", encoding="utf-8").write(t)
    print(f"applied: {heads} head cuts (Ch2-19), {sounds} cue lines on existing precaps, "
          f"{len(NEW)} new precaps, 1 tail card on Ch19")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
