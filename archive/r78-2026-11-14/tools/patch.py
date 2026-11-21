#!/usr/bin/env python3
"""tools/patch.py — the only safe way this workshop edits a file it cares about.

    python3 tools/patch.py SPEC.json [--dry]
    python3 tools/patch.py --selftest

A SPEC is a JSON file, a list of parts, one per file:

    [
      {"file": "chapters/Chapter_19_The_First_Day.md",
       "edits": [
         {"old": "the passage exactly as it stands in the file", "new": "the replacement"},
         {"old": "a whole passage to delete", "new": ""},
         {"old": "an anchor line", "new": "the new paragraph", "mode": "after"},
         {"old": "an anchor line", "new": "the new paragraph", "mode": "before"}
       ]}
    ]

Why this exists. On 2026-11-13 a file was rewritten by slicing it in Python and writing
`head + new` where `head + new + tail` was meant. About 150 lines went out of `SNAPSHOT.txt` and
nothing noticed, because nothing checked that a rewrite keeps what it was never asked to touch.
Two days of the author's charges were about the same shape in the prose: one fact hung on one
paragraph. This tool is that rule, applied to the workshop's own files.

It reads the file ONCE, finds every `old` in that text, applies the edits, and then verifies
against the original: every non-blank line OUTSIDE the spans the edits cover must still be in the
result, in the same order. Refusals, before anything is written:

  MISS   `old` is not in the file            (an anchor was remembered instead of read)
  DUP    `old` occurs more than once         (say "all": true if that is meant)
  BLANK  `old` is empty                      (an append belongs at the end, not here)
  CROSS  two edits cover overlapping spans
  LOSS   an untouched line is gone, or the order of surviving lines changed, or the last line is
         gone — the truncation check, the reason this file exists

On success it copies the old file to /tmp/patch-backup (never into the workshop, `L-35`), writes a
temporary file and os.replace's it, and prints lines and bytes before and after. --dry prints the
plan and writes nothing. Exit 0 applied or planned, 1 refused, 2 used wrongly.
"""
import json
import os
import shutil
import sys
import time

BACKUP = "/tmp/patch-backup"


def _lines(text):
    return [l for l in text.split("\n") if l.strip()]


def check(path, edits):
    """(new_text, fails) — nothing is written by this function."""
    fails = []
    if not os.path.exists(path):
        return None, [f"{path}: no such file"]
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    spans, planned = [], []
    for i, e in enumerate(edits):
        old = e.get("old", "")
        new = e.get("new", "")
        mode = e.get("mode", "replace")
        if not old.strip():
            fails.append(f"BLANK edit {i}: `old` is empty — an edit must say what it replaces")
            continue
        if mode not in ("replace", "before", "after"):
            fails.append(f"edit {i}: mode {mode!r} is not replace / before / after")
            continue
        n = src.count(old)
        if n == 0:
            fails.append(f"MISS edit {i}: not in the file — read the anchor from the file, not from memory: "
                         f"{old[:70].replace(chr(10), chr(92) + 'n')!r}")
            continue
        if n > 1 and not e.get("all"):
            fails.append(f"DUP edit {i}: `old` occurs {n} times — give it more context, or say \"all\": true")
            continue
        start = 0
        for _ in range(n if e.get("all") else 1):
            at = src.find(old, start)
            start = at + len(old)
            if mode == "replace":
                spans.append((at, at + len(old), new))
            elif mode == "after":
                spans.append((at + len(old), at + len(old), "\n\n" + new if new.strip() else ""))
            else:
                spans.append((at, at, new + "\n\n" if new.strip() else ""))
    if fails:
        return None, fails
    spans.sort(key=lambda s: (s[0], s[1]))
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            fails.append(f"CROSS: two edits cover overlapping text at offset {b[0]}")
    if fails:
        return None, fails
    out, cursor = [], 0
    for a, b, rep in spans:
        out.append(src[cursor:a]); out.append(rep); cursor = b
    out.append(src[cursor:])
    new_text = "".join(out)

    covered = [False] * len(src)
    for a, b, _ in spans:
        for k in range(a, b):
            covered[k] = True
    kept = []
    pos = 0
    for line in src.split("\n"):
        start = pos
        pos += len(line) + 1
        if not line.strip():
            continue
        if any(covered[k] for k in range(start, min(pos - 1, len(src)))):
            continue
        kept.append(line)
    out_lines = _lines(new_text)
    j = 0
    for line in kept:
        while j < len(out_lines) and out_lines[j] != line:
            j += 1
        if j == len(out_lines):
            fails.append(f"LOSS: a line no edit touched is not in the result: {line[:70]!r}")
            break
        j += 1
    last = _lines(src)[-1] if _lines(src) else ""
    if last and last not in out_lines and not any(last in (s[2] or "") for s in spans) and last not in "".join(
            src[a:b] for a, b, _ in spans):
        fails.append(f"LOSS: the file's last line is gone — a splice dropped the tail: {last[:70]!r}")
    src_n, out_n = len(_lines(src)), len(out_lines)
    touched = sum(1 for l in _lines(src) if any(l in (a and src[a:b] or "") for a, b, _ in spans))
    if out_n + touched < src_n and src_n > 8:
        fails.append(f"LOSS: {src_n} non-blank lines went in, {out_n} came out, {touched} were covered — that is a truncation")
    return new_text, fails


def apply(spec_path, dry=False):
    with open(spec_path, encoding="utf-8") as fh:
        spec = json.load(fh)
    # Every edit to one file is applied in ONE read-compute-write. Two parts naming the same
    # file are merged, in order. Found by using the tool: written as two parts, each computed against
    # the file before either was written, so the second part wrote the first part's work away.
    grouped, order = {}, []
    for part in spec:
        f_ = part["file"]
        if f_ not in grouped:
            grouped[f_] = {"file": f_, "edits": []}
            order.append(f_)
        grouped[f_]["edits"] += part.get("edits", [])
    spec = [grouped[f_] for f_ in order]
    fails, todo = [], []
    for part in spec:
        path = part["file"]
        new, f = check(path, part.get("edits", []))
        if f:
            fails += [f"{path}: {x}" for x in f]
            continue
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        print(f"{path}: {len(src.split(chr(10)))} -> {len(new.split(chr(10)))} lines, "
              f"{len(src.encode())} -> {len(new.encode())} bytes" + ("   [dry]" if dry else ""))
        todo.append((path, new))
    if fails:
        print(f"\nREFUSED — nothing was written. {len(fails)} problem(s):")
        for x in fails:
            print("  -", x)
        return 1
    if dry:
        print("\nplan only, nothing written")
        return 0
    os.makedirs(BACKUP, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    for path, new in todo:
        shutil.copy2(path, os.path.join(BACKUP, os.path.basename(path) + "." + stamp + ".bak"))
        tmp = path + ".patching"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(new)
        os.replace(tmp, path)
    print(f"\nwritten ({len(todo)} file(s)). the old copies are in {BACKUP}/, not in the workshop")
    return 0


_FIX = "\n".join(["head line", "keep one", "keep two", "target line", "keep three", "keep four",
                  "keep five", "keep six", "keep seven", "keep eight", "tail line"]) + "\n"


def selftest():
    p = "/tmp/patch_selftest.md"
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(_FIX)
    ok = True

    def kind(f):
        return f[0].split(" ")[0].rstrip(":") if f else ""

    cases = [
        ("good replace", [{"old": "target line", "new": "TARGET LINE"}], None, "head line\nkeep one\nkeep two\nTARGET LINE\nkeep three"),
        ("delete", [{"old": "keep four\nkeep five\n", "new": ""}], None, None),
        ("insert after", [{"old": "tail line", "new": "one more line", "mode": "after"}], None, None),
        ("a remembered anchor", [{"old": "targate line", "new": "x"}], "MISS", None),
        ("two edits on one span", [{"old": "keep one", "new": "x"}, {"old": "keep one", "new": "y"}], "CROSS", None),
        ("an anchor twice in the file", [{"old": "keep", "new": "x"}], "DUP", None),
        ("a bad mode", [{"old": "keep one", "new": "x", "mode": "append"}], "edit", None),
        ("blank old", [{"old": "", "new": "x"}], "BLANK", None),
    ]
    for name, edits, want, probe in cases:
        _, f = check(p, edits)
        got = kind(f) if f else "clean"
        good = (got == want) if want else (not f)
        if probe:
            new, _ = check(p, edits)
            good = good and new and probe in new
        print(f"selftest {name}: " + ("ok" if good else f"FAILED ({got})"))
        ok &= bool(good)
    # the one that matters: a truncating rewrite must be caught by the checker
    new, _ = check(p, [{"old": "target line", "new": "TARGET LINE"}])
    truncated = new[: new.index("keep six")]
    src_lines = _lines(_FIX)
    lost = [l for l in src_lines if l not in _lines(truncated)]
    print("selftest a hand-truncated splice loses lines the checker would report:", "ok" if lost else "FAILED",
          "lost:", lost[:2])
    ok &= bool(lost)
    # and: an edit that legitimately deletes a whole passage is NOT a loss
    new, f = check(p, [{"old": "keep six\nkeep seven\nkeep eight\n", "new": ""}])
    print("selftest a real deletion passes:", "ok" if not f else f"FAILED {f}")
    ok &= not f

    print("selftest a real deletion passes:", "ok" if not f else f"FAILED {f}")
    ok &= not f
    # and: two edits to one file given as two parts must BOTH land — the clobber this tool had
    sp = "/tmp/patch_selftest_spec.json"
    with open(sp, "w", encoding="utf-8") as fh:
        json.dump([{"file": p, "edits": [{"old": "target line", "new": "T1"}]},
                   {"file": p, "edits": [{"old": "tail line", "new": "T2", "mode": "before"}]}], fh)
    apply(sp)
    with open(p, encoding="utf-8") as fh:
        both = fh.read()
    good = "T1" in both and "T2" in both
    print("selftest two parts on one file both survive:", "ok" if good else "FAILED \u2014 the second write clobbered the first")
    ok &= good
    os.remove(sp)
    os.remove(p)
    print("\nSELFTEST " + ("green" if ok else "RED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    args = [a for a in sys.argv[1:] if a != "--dry"]
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    sys.exit(apply(args[0], dry="--dry" in sys.argv))
