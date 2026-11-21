#!/usr/bin/env python3
"""picture_check — the visual layer (canon/PICTURE.md §3-§4).

Per scene: does it open on a place with its light? does it give an object its own frame?
how much of it is nothing but speech? A scene passes on three counts: it opens on a place with its light,
    it gives at least two objects their own frame, and no more than 65% of its paragraphs are bare speech.
    A precap is not a scene and is not scored.

usage: picture_check.py [chapters/Chapter_XX.md ...]   (default: all chapters)
exit 1 if any chapter carries more than two failing scenes.
"""
import glob
import re
import sys

LIGHT = ("light", "lamp", "lamps", "bulb", "tube", "sun", "sunlight", "moon", "moonlight", "dark", "darkness",
         "chandelier", "night", "morning", "evening", "afternoon", "noon", "dawn", "dusk", "grey", "shade",
         "shadow", "shadows", "glare", "glow", "halogen", "neon", "flame", "fire", "smoke", "dust", "shadow")
PLACE = ("room", "hall", "house", "street", "lane", "road", "yard", "gate", "corridor", "passage", "floor", "wall",
         "ceiling", "roof", "terrace", "stairs", "stairwell", "landing", "kitchen", "veranda", "drive", "market",
         "ghat", "temple", "mandir", "office", "floor", "desk", "shed", "pit", "ground", "lawn", "garden", "yard",
         "platform", "lift", "station", "hospital", "police", "library", "study", "balcony", "window", "door")
SIGHT = LIGHT + PLACE + ("brass", "steel", "glass", "gold", "golden", "silver", "marigold", "red", "green", "blue",
         "white", "black", "brown", "yellow", "orange", "colour", "colour of", "dust", "ash", "water", "wet",
         "rain", "cloth", "paper", "papers", "register", "ledger", "thali", "diya", "diyas", "sindoor", "bangle",
         "bangles", "spectacles", "camera", "phone", "bucket", "file", "folder", "card", "cards", "print", "ink",
         "mirror", "window", "curtain", "curtains", "fan", "clock", "tape", "plastic", "concrete", "stone", "tile",
         "tiles", "wood", "iron", "sheet", "cloth", "flame", "smoke", "hair", "hands", "feet", "face")
OBJECT = ("register", "ledger", "thali", "diya", "diya", "lamp", "glass", "cup", "tray", "file", "folder", "card",
          "cards", "phone", "camera", "bucket", "knife", "reed", "been", "knife", "sheet", "cloth", "sari", "dupatta",
          "spectacles", "bangle", "bangles", "ring", "paper", "papers", "pen", "pencil", "key", "keys", "door",
          "shutter", "mirror", "clock", "bottle", "plate", "spoon", "box", "tin", "bag", "envelope", "printout",
          "tape", "card", "list", "receipt", "receipts", "bill", "screwdriver", "lens", "coil", "rope", "shovel")


def words(s):
    return re.findall(r"[A-Za-z']+", s)


def count(s, table):
    low = " " + s.lower() + " "
    return sum(1 for w in table if " " + w + " " in low or " " + w + "," in low or " " + w + "." in low)


def is_speech(p):
    t = p.strip()
    return t.startswith('"') or t.startswith('*"') or t.startswith("*A precap")


def scenes(text):
    out, cur, buf = [], None, []
    for line in text.split("\n"):
        if line.startswith("## Footer"):
            break
        if line.startswith("## "):
            if cur:
                out.append((cur, buf))
            cur, buf = line[3:].strip(), []
        elif cur is not None:
            buf.append(line)
    if cur:
        out.append((cur, buf))
    return out


def check(path):
    text = open(path, encoding="utf-8").read()
    rows, fails = [], 0
    for name, body in scenes(text):
        paras = [p.strip() for p in "\n".join(body).split("\n\n") if p.strip()]
        if not paras or name.lower().startswith("what comes next"):
            continue
        n = len(paras)
        sp = sum(1 for p in paras if is_speech(p))
        share = 100.0 * sp / n
        first = paras[0]
        opens = (not is_speech(first)) and count(first, PLACE) > 0 and count(first, LIGHT) > 0
        inserts = [p for p in paras[1:] if not is_speech(p) and len(words(p)) <= 45 and count(p, OBJECT) > 0]
        ok = opens and len(inserts) >= 2 and share <= 65.0
        if not ok:
            fails += 1
        rows.append((name, n, share, opens, len(inserts), ok))
    sp_all = sum(r[2] for r in rows) / max(1, len(rows))
    print(f"\n{path.split('/')[-1]}  —  {len(rows)} scenes, mean speech share {sp_all:.0f}%, "
          f"{fails} scene(s) short of the picture")
    for name, n, share, opens, ins, ok in rows:
        flag = "ok  " if ok else "SHORT"
        print(f"  {flag} {name[:34]:36} paras {n:3}  speech {share:3.0f}%  opens-on-place "
              f"{'yes' if opens else 'NO ':3}  inserts {ins}")
    return fails




GOOD_FIXTURE = """# Chapter 90 · The Fixture

**Episode 1 · 00:00:00 → 00:01:00.**

## A scene that passes

The hall at six in the morning was grey and the tube light over the desk was already on.

The register lay open on the desk and the pen beside it had its cap off.

He put the file on the table and the card inside it, and left the card where it was.

"Who told you to open the ledger?" she said.

"The night watchman, sir."

## Footer

---
"""

BAD_FIXTURE = GOOD_FIXTURE.replace("""## A scene that passes""", """## A scene that is nothing but speech""").replace(
    """The hall at six in the morning was grey and the tube light over the desk was already on.

The register lay open on the desk and the pen beside it had its cap off.

He put the file on the table and the card inside it, and left the card where it was.

""", """Why.

Because.

Then shut it.

And open it again.

""")


def selftest():
    """A scene built to pass must return 0 short scenes; the same scene with its furniture deleted
    and its paragraphs turned into talk must return 1. If the first ever reads as short, the gate has
    become a description of one chapter; if the second reads as fine, it is not scoring anything."""
    import os
    import tempfile
    ok = True
    d = tempfile.mkdtemp(prefix="picture_fix_")
    good = os.path.join(d, "Chapter_90_Good.md")
    bad = os.path.join(d, "Chapter_90_Bad.md")
    for p, t in ((good, GOOD_FIXTURE), (bad, BAD_FIXTURE)):
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(t)
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        g = check(good)
        b = check(bad)
    print("selftest the furnished scene is not short:", "ok" if g == 0 else f"FAILED ({g})")
    print("selftest the bare one is:", "ok" if b == 1 else f"FAILED ({b})")
    ok &= (g == 0 and b == 1)
    print("\nSELFTEST " + ("green" if ok else "RED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    files = sys.argv[1:] or sorted(glob.glob("chapters/Chapter_*.md"))
    bad = 0
    for f in files:
        if check(f) > 2:
            bad += 1
    print(f"\n{'RED' if bad else 'GREEN'}: {bad} chapter(s) with more than two picture-short scenes.")
    sys.exit(1 if bad else 0)
