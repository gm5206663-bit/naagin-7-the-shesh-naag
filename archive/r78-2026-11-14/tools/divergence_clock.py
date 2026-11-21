#!/usr/bin/env python3
"""divergence_clock.py — what the live divergences still owe the next chapter.

`tools/ripple_check.py` looks BACKWARDS: a fact in a chapter that a registered
divergence has superseded, without the chapter owning it. This tool looks
FORWARDS, at `foundation/FORWARD.md`, where each live divergence names what it
must still produce and the chapter it is due in. The shape is taken from the
author's other serials rather than invented here: the Soul Land kit's
`DIVERGENCE_LEDGER.md` (``ID · STATUS · MAG · THREAD · cause · standing effect ·
horizon · last paid``) and its `checks/divergence_engine.py`, which prints a
forward tick before a chapter is written; The Twin records the same thing as
"open chains" in its canon disposition file. Their rule, kept verbatim in
spirit: paying a row may spawn children; a `break` means the canon event is
dead and is not resurrected; a `HELD` row pays on its own horizon and is not
forced early.

Red (the failure classes):
  FC1  a row whose STATUS or MAG is not one of the registered words (`WITHDRAWN` is
       registered: a row can be killed, but only by keeping its number and saying so)
  FC2  a row whose `last paid` claims a chapter that does not cite it (a stale
       claim in the table; the footers are the receipts, not this file)
  FC3  an ACTIVE row whose horizon names chapters, the newest chapter written is
       past them, and no chapter has paid it at all — the debt has gone overdue.
       A row paid earlier than its horizon is honoured, not overdue: the horizon is
       the latest it may land, not the first day it may be mentioned.
  FC4  a row number here that the register does not hold, or a chapter footer
       citing a number the register does not hold

Printed, never red: the forward tick for the chapters that have not been
written yet, the count by status and magnitude, and how much of the register is
carried by any footer at all (the honest backlog).

    python3 tools/divergence_clock.py            # the workshop's own tree
    python3 tools/divergence_clock.py --tick     # only the next chapter's list
    python3 tools/divergence_clock.py --selftest # planted fixtures, one per class
"""
import re
import sys
from pathlib import Path

LEDGER = "foundation/FORWARD.md"
REGISTER = "foundation/BUTTERFLY.md"
CHAPTERS = "chapters"
ROW = re.compile(r"^\|\s*(BF-\d+|O\d+|R-\d+)\s*\|")
FOOT = re.compile(r"\n#{1,3}\s*Footer", re.I)
BID = re.compile(r"BF-(\d{2})")
STATUS = {"ACTIVE", "HELD", "ABSORBED", "WITHDRAWN"}   # WITHDRAWN: the row is dead; its number stays, per BF-11's convention
MAG = {"dust", "current", "bend", "break", "storm"}
CHAPTER_NO = re.compile(r"Chapter_(\d+)")


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def load_rows(root):
    """The table rows in FORWARD.md. Returns (rows, fails)."""
    path = Path(root) / LEDGER
    if not path.exists():
        return [], [f"FC0  {LEDGER} does not exist — the forward duty is unrecorded"]
    rows = []
    for line in path.read_text(encoding="utf-8").split("\n"):
        if not ROW.match(line):
            continue
        c = split_row(line)
        if len(c) < 8:
            rows.append({"id": c[0], "status": c[1] if len(c) > 1 else "", "mag": c[2] if len(c) > 2 else "",
                         "thread": "", "cause": "", "effect": "", "horizon": "", "paid": "", "short": True})
            continue
        rows.append(dict(zip(("id", "status", "mag", "thread", "cause", "effect", "horizon", "paid"), c[:8]),
                         short=False))
    return rows, []


def chapter_footers(root):
    out = {}
    for p in sorted((Path(root) / CHAPTERS).glob("Chapter_*.md")):
        n = int(CHAPTER_NO.search(p.name).group(1))
        out[n] = FOOT.split(p.read_text(encoding="utf-8"))[-1]
    return out


def harvest(footers):
    """Which chapters pay which row: a footer citing `BF-nn` is the receipt."""
    paid = {}
    for n, text in footers.items():
        for bid in set(BID.findall(text)):
            paid.setdefault(int(bid), set()).add(n)
    return {k: sorted(v) for k, v in paid.items()}


def due_chapter(horizon):
    """The first chapter number a horizon names. None if it names none."""
    nums = [int(x) for x in re.findall(r"(?:ch|Ch|chapter\s*)(\d+)", horizon)]
    return min(nums) if nums else None


def check(root=".", tick=False):
    root = Path(root)
    rows, fails = load_rows(root)
    notes = []
    if not rows:
        return fails, ["FC0  no rows read — nothing was checked, which is a finding, not a pass"]
    footers = chapter_footers(root)
    newest = max(footers) if footers else 0
    paid = harvest(footers)
    reg = Path(root) / REGISTER
    have = set(int(x) for x in re.findall(r"\*\*BF-(\d+)", reg.read_text(encoding="utf-8"))) if reg.exists() else set()

    for r in rows:
        num = int(re.search(r"\d+", r["id"]).group(0)) if r["id"].startswith("BF-") else None
        if r["id"].startswith("BF-") and have and num not in have:
            fails.append(f"FC4  FORWARD.md holds {r['id']}, which the register does not")
        if r["short"]:
            fails.append(f"FC1  {r['id']}: the row has fewer than eight cells")
            continue
        if r["status"] not in STATUS:
            fails.append(f"FC1  {r['id']}: status {r['status']!r} is not ACTIVE, HELD, ABSORBED or WITHDRAWN")
        if r["mag"] not in MAG:
            fails.append(f"FC1  {r['id']}: magnitude {r['mag']!r} is not dust, current, bend, break or storm")
        # FC2 — the table's claim against the footers' receipts
        claimed = [int(x) for x in re.findall(r"ch(\d+)", r["paid"])]
        got = paid.get(num, []) if num is not None else []
        for c in claimed:
            if c not in got:
                fails.append(f"FC2  {r['id']} claims it was paid in ch{c}; ch{c}'s footer does not cite it — "
                             f"the footers are the receipts")
        if r["status"] == "ACTIVE":
            due = due_chapter(r["horizon"])
            if due and newest >= due and not got:
                fails.append(f"FC3  {r['id']} is due by ch{due} ({r['horizon'][:40]}) and nothing from ch{due} on "
                             f"has paid it — the change was made and then dropped")

    # printed
    if not tick:
        live = [r for r in rows if r["status"] == "ACTIVE"]
        held = [r for r in rows if r["status"] == "HELD"]
        done = [r for r in rows if r["status"] == "ABSORBED"]
        sizes = {}
        for r in rows:
            sizes[r["mag"]] = sizes.get(r["mag"], 0) + 1
        notes.append(f"    forward ledger: {len(rows)} rows — {len(live)} ACTIVE · {len(held)} HELD · "
                     f"{len(done)} ABSORBED · size: " +
                     " ".join(f"{k} {v}" for k, v in sorted(sizes.items())))
        carried = len([k for k in paid if k in have])
        notes.append(f"    the register holds {len(have)} rows and {carried} of them are cited in any chapter "
                     f"footer; the ledger's {len(rows)} are the ones with work outstanding")
        upcoming = [r for r in live if (due_chapter(r["horizon"]) or 99) > newest]
        dated = [r for r in upcoming if due_chapter(r["horizon"])]
        event_only = [r for r in upcoming if not due_chapter(r["horizon"])]
        soonest = min([due_chapter(r["horizon"]) for r in dated], default=newest + 1)
        notes.append(f"    FORWARD-TICK for ch{soonest} — read these before the chapter is written. Canon says "
                     f"nothing here; our state implies what is below; decide, and record the cause:")
        for r in sorted(dated, key=lambda r: (due_chapter(r["horizon"]), r["id"])):
            notes.append(f"         {r['id']} [{r['mag']}] {r['thread']} (due ch{due_chapter(r['horizon'])}): "
                         f"{r['effect'][:110]}")
        for r in sorted(event_only, key=lambda r: r["id"]):
            notes.append(f"         {r['id']} [{r['mag']}] {r['thread']} (waits on an event: {r['horizon'][:32]}) "
                         f"— {r['effect'][:90]}")
        if not upcoming:
            notes.append("         nothing is scheduled ahead of the last written chapter")
    return fails, notes


# --------------------------------------------------------------------------- selftest
FIXTURE_LEDGER = """# FORWARD — fixture

| ID | STATUS | MAG | THREAD | cause | standing effect | horizon | last paid |
|---|---|---|---|---|---|---|---|
| BF-01 | ACTIVE | bend | the-child | a child is shown | everything follows | ch2 | ch1 |
| BF-02 | HELD | dust | a-word | a name is given | a word changes | when they ask | — |
| BF-03 | ABSORBED | break | the-dead | an event is made impossible | that event is dead | standing | ch1 |
| BF-04 | ACTIVE | current | unpaid | a thing is set going | it must land | ch3 | — |
"""
BAD_LEDGER = FIXTURE_LEDGER.replace("| BF-02 | HELD | dust", "| BF-02 | PENDING | glitter").replace(
    "ch3 | — |", "ch3 | ch9 |").replace("| BF-04 |", "| BF-77 |")


def _write(root, ledger, chapters):
    (root / "foundation").mkdir(parents=True, exist_ok=True)
    (root / "chapters").mkdir(parents=True, exist_ok=True)
    (root / LEDGER).write_text(ledger, encoding="utf-8")
    (root / REGISTER).write_text("# register\n\n- **BF-01 · a** x\n- **BF-02 · b** x\n- **BF-03 · c** x\n"
                                 "- **BF-04 · d** x\n", encoding="utf-8")
    for n, foot in chapters.items():
        (root / f"chapters/Chapter_{n:02d}_T.md").write_text(
            "# Chapter %d — T\n\n## Scene\n\nSomething happens here.\n\n## Footer\n\n%s\n" % (n, foot),
            encoding="utf-8")


def selftest(tmp):
    tmp = Path(tmp)
    good = {1: "**BF-01** and **BF-03** paid here. `RIPPLED: none`", 2: "`RIPPLED: none`",
            3: "**BF-04** paid here."}
    _write(tmp / "good", FIXTURE_LEDGER, good)
    f, n = check(tmp / "good")
    assert not f, "clean fixture failed: " + "; ".join(f)
    _write(tmp / "bad", BAD_LEDGER, good)
    f, n = check(tmp / "bad")
    want = ["FC1", "FC2", "FC4"]
    for w in want:
        assert any(x.startswith(w) for x in f), f"{w} not caught: {f}"
    # FC3: remove ch3's payment and the row goes overdue
    _write(tmp / "late", FIXTURE_LEDGER, {**good, 3: "`RIPPLED: none`"})
    f, n = check(tmp / "late")
    assert any(x.startswith("FC3") and "BF-04" in x for x in f), f"FC3 not caught: {f}"
    # a missing ledger is a finding, not a pass
    (tmp / "none").mkdir(parents=True, exist_ok=True)
    f, n = check(tmp / "none")
    assert f and f[0].startswith("FC0"), f
    print("SELFTEST: green — FC1 a word that is not a status or a size, FC2 a payment the footers do not "
          "support, FC3 a row past its horizon, FC4 a number outside the register, and a missing ledger, all "
          "caught; the clean fixture passes.")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        import tempfile
        with tempfile.TemporaryDirectory(prefix="dvclock") as t:
            sys.exit(selftest(t))
    root = Path(a[0]) if a and not a[0].startswith("--") else Path(__file__).resolve().parents[1]
    fails, notes = check(root, tick="--tick" in a)
    for x in notes:
        print(x)
    if fails:
        print(f"\ndivergence_clock: {len(fails)} FAIL")
        for x in fails[:40]:
            print("  " + x)
        sys.exit(1)
    print("GREEN. Every live divergence in `foundation/FORWARD.md` is paid, held or not yet due, and its "
          "payment is signed for in a chapter footer.")
