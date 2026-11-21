#!/usr/bin/env python3
"""tools/doctor.py — does the workshop's own toolchain still work?

    python3 tools/doctor.py            # run every selftest, list the tools that have none
    python3 tools/doctor.py --brief    # just the counts and the red ones

Why this exists. The workshop has twenty-two scripts and the only proof any of them gives that it is
measuring what it claims is its own output. `tools/oc_check.py` was wrong for a whole build's length
(2026-11-13: it graded `111111.00` as a crore) and nothing could see it, because nothing tested the
checker. Then `tools/money_check.py` and `tools/patch.py` were written the same night with a
`--selftest` built in, and `tools/patch.py`'s own test found its first bug — two edits to one file in
one spec, where the second write discarded the first. A tool that can be tested gets tested.

So this is the rule, and it is cheap: **every tool in this folder takes `--selftest` and exits 0 on
green, 1 on red.** `doctor` runs them all in one command and prints which tools are covered and which
are not. A tool with no selftest is not a failure — the descriptive helpers (`screen_check.py`,
`franchise_check.py`, `contact_sheet.py`, `recount.py`, `build_frame.py`, `caption_hits.py`'s callers)
print matrices and frames for a human to read, and there is nothing to grade. But the list is printed
every time, so the gap stays visible instead of being discovered mid-build at one in the morning.

Exit 0 when every selftest is green, 1 otherwise.
"""
import glob
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

TIMEOUT = 240
SELF = os.path.relpath(os.path.abspath(__file__), ROOT)
# A nested doctor would run doctor, and each pass spawns the whole folder again, so this stops the
# recursion in its tracks rather than trusting the exclusion below to be complete.
if os.environ.get("NAAGIN7_DOCTOR"):
    print("doctor: already running, not recursing")
    sys.exit(0)
os.environ["NAAGIN7_DOCTOR"] = "1"


def selftest_paths():
    """Every tools/*.py that mentions a selftest, plus the two checkers kept outside the folder."""
    """A tool counts as covered only if it DEFINES a selftest. The word alone is not enough: this
    file says `selftest` a dozen times and runs none, and a runner that tests itself by running
    itself is how you get a recursion instead of a report."""
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "tools", "*.py"))):
        if os.path.relpath(p, ROOT) == SELF:
            continue
        try:
            with open(p, encoding="utf-8") as fh:
                src = fh.read()
        except OSError:
            continue
        if "def selftest" in src or "def _selftest" in src:
            out.append(os.path.relpath(p, ROOT))
    return out


def tools_paths():
    return [os.path.relpath(p, ROOT) for p in sorted(glob.glob(os.path.join(ROOT, "tools", "*.py")))
            if os.path.relpath(p, ROOT) != SELF]


def run_plain(rel):
    """Run a tool with no arguments — for the aggregate gate, whose subject is the workshop and not
    a fixture. `check.py` cannot have a selftest in the usual sense: to test it you need a whole
    workshop to point it at. So doctor runs it and reports what it says about THIS one, and a RED
    there is the book's state, not a broken tool, so it does not fail this command."""
    p = os.path.join(ROOT, rel)
    try:
        r = subprocess.run([sys.executable, p], capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return 124, f"(no output in {TIMEOUT}s)"
    return r.returncode, ((r.stdout or "") + ("\n" + r.stderr.strip() if r.returncode and r.stderr else "")).strip()


def run(rel):
    p = os.path.join(ROOT, rel)
    try:
        r = subprocess.run([sys.executable, p, "--selftest"], capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return 124, f"(no output in {TIMEOUT}s — the selftest hung)"
    out = ((r.stdout or "") + ("\n" + r.stderr.strip() if r.returncode and r.stderr else "")).strip()
    return r.returncode, out


def main():
    brief = "--brief" in sys.argv
    tools = tools_paths()
    covered = selftest_paths()
    bad = []
    for rel in covered:
        rc, out = run(rel)
        tail = [l for l in out.split("\n") if l.strip()]
        verdict = "green" if rc == 0 else ("TIMEOUT" if rc == 124 else "RED")
        if not brief:
            name = os.path.basename(rel)
            last = tail[-1] if tail else "(no output)"
            print(f"  {name:<24} {verdict:<8} {last[:96]}")
        if rc != 0:
            bad.append((rel, tail[-8:] if tail else ["(no output)"]))
    rc, out = run_plain("tools/check.py")
    tail = [l for l in out.split("\n") if l.strip()]
    verdict = "GREEN" if rc == 0 else ("TIMEOUT" if rc == 124 else "RED")
    print(f"  {'check.py (aggregate)':<24} {verdict:<8} runs as the workshop's own subject: {tail[-1][:70] if tail else ''}")
    if rc == 124:
        bad.append(("tools/check.py", [f"the aggregate gate did not finish in {TIMEOUT}s"]))
    # `check.py` has no fixture of its own because its subject is the workshop; doctor runs it instead,
    # so it is not a gap in the standard and must not be listed as one.
    missing = [t for t in tools if t not in covered and os.path.basename(t) != "check.py"]
    if bad:
        print(f"\nRED: {len(bad)} tool(s) fail their own test.")
        for rel, tail in bad:
            print(f"  - {rel}")
            for l in tail:
                print("      " + l[:110])
    print(f"\n{len(covered)} tool(s) carry a selftest and {'all are green' if not bad else str(len(covered) - len(bad)) + ' are green'}; "
          f"{len(missing)} do not.")
    if missing:
        print("  no selftest: " + ", ".join(os.path.basename(m) for m in missing))
        print("  (a descriptive helper may go without one; a gate may not — `L-36`)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
