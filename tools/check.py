#!/usr/bin/env python3
"""tools/check.py - the workshop's shape, checked.

Run from the project folder:   python3 tools/check.py
Exit 0 when nothing is red, 1 otherwise.

What it checks
  1. OWNER    every working .md file states what it owns near its top
  2. ROWS     every cited ruling exists: O### and OPEN-## and S-## in OPEN.md,
              R# in CANON.md
  3. PATHS    every `path/to/file` named in backticks exists
  4. CHAPTERS each chapter has its title, episode line, acceptance line and a
              footer with all six keys; no timecode above the footer
  5. BEATS    every beat number a chapter footer cites exists in a ledger
  6. SARA     the self-file passes its own checker
  7. DESK     nothing heavy or stray is sitting in the workshop

What it cannot check: whether a scene is true to the episode, whether a voice
is right, whether the author accepts a chapter. Green here is none of those.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# Files carried whole from another workshop, or fetched from outside: not ours to shape.
CARRIED = {
    "Sara/SARA.md",
    "Sara/AGENT-OPERATING-PROFILE.md",
    "Sara/docs/03_the_growth_ledger.md",
    "Sara/provenance/COPIES-AND-TWINS.md",
    "Sara/provenance/ARCHIVE_INDEX.md",
}
SKIP_DIRS = ("canon/sources", "captions", "canon/frames", "chapters")
# Files that live in the author's other repositories and are cited here by name.
# Listed so the path check can tell "elsewhere" from "missing". Each names its home.
EXTERNAL = {
    "AGENTS.md": "dbz-twin, repository root",
    "CRAFT.md": "dbz-twin, The Twin/",
    "lessons-absorbed.md": "adaptation-talent, practice/",
    "storyos-master-skill.md": "adaptation-talent, practice/",
    "MASTER-FOUNDATION.md": "adaptation-talent, canon/",
    "LEVEL-FRAMEWORK.md": "adaptation-talent, canon/",
    "modules/vihaan-naagin7.md": "adaptation-talent",
    "practice/lessons-absorbed.md": "adaptation-talent",
    "canon_first_oc_woven_chapter_style.md": "soul-land-universal-kit, adaptive_prodigy/library/",
    "GENESIS_CODEX.md": "soul-land-universal-kit, CODEX/",
}
DESK_LIMIT_MB = 8.0
BIG_FILE_MB = 1.0
FOOTER_KEYS = ("BASE:", "EVIDENCE:", "WITNESS:", "STAGING:", "CHANGED:", "DEFERRED:")

fails = []
notes = []


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def md_files():
    out = []
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if not x.startswith(".") and x != "__pycache__"]
        for f in sorted(files):
            if f.endswith(".md"):
                out.append(rel(os.path.join(d, f)))
    return sorted(out)


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as fh:
        return fh.read()


def working(p):
    return p not in CARRIED and not any(p.startswith(s + "/") for s in SKIP_DIRS)


files = md_files()
work = [p for p in files if working(p)]

# 1. OWNER
for p in work:
    head = "\n".join(read(p).split("\n")[:8])
    if "**Owns:" not in head:
        fails.append(f"OWNER  {p}: no '**Owns:' line in its first eight lines")

# 2. ROWS
open_text = read("OPEN.md") if os.path.exists("OPEN.md") else ""
canon_text = read("CANON.md") if os.path.exists("CANON.md") else ""
have_O = set(re.findall(r"\*\*(O\d{3})\*\*", open_text))
have_OPEN = set(re.findall(r"\*\*(OPEN-\d{2})", open_text))
have_S = set(re.findall(r"^\| (S-\d{2}) \|", open_text, re.M))
have_R = set(re.findall(r"^\| (R\d{1,2}) \|", canon_text, re.M))


def expand(prefix, a, b, width):
    return [f"{prefix}{str(n).zfill(width)}" for n in range(int(a), int(b) + 1)]


for p in work:
    t = read(p)
    cited_O = set(re.findall(r"\bO(\d{3})\b", t))
    for a, b in re.findall(r"\bO(\d{3})[–-]O(\d{3})\b", t):
        cited_O.update(x[1:] for x in expand("O", a, b, 3))
    for n in sorted(cited_O):
        if f"O{n}" not in have_O:
            fails.append(f"ROWS   {p}: cites O{n}, which OPEN.md does not have")
    cited_OPEN = set(re.findall(r"\bOPEN-(\d{2})\b", t))
    for a, b in re.findall(r"\bOPEN-(\d{2})\.\.(\d{2})\b", t):
        cited_OPEN.update(x[5:] for x in expand("OPEN-", a, b, 2))
    for n in sorted(cited_OPEN):
        if f"OPEN-{n}" not in have_OPEN:
            fails.append(f"ROWS   {p}: cites OPEN-{n}, which OPEN.md does not have")
    cited_S = set(re.findall(r"\bS-(\d{2})\b", t))
    for a, b in re.findall(r"\bS-(\d{2})\.\.(\d{2})\b", t):
        cited_S.update(x[2:] for x in expand("S-", a, b, 2))
    for n in sorted(cited_S):
        if f"S-{n}" not in have_S:
            fails.append(f"ROWS   {p}: cites S-{n}, which OPEN.md does not have")
    cited_R = set(re.findall(r"(?<![A-Za-z0-9])R(\d{1,2})(?![A-Za-z0-9])", t))
    for a, b in re.findall(r"(?<![A-Za-z0-9])R(\d{1,2})[–-]R(\d{1,2})(?![A-Za-z0-9])", t):
        cited_R.update(str(n) for n in range(int(a), int(b) + 1))
    for n in sorted(cited_R, key=int):
        if f"R{n}" not in have_R:
            fails.append(f"ROWS   {p}: cites R{n}, which CANON.md does not have")

# 3. PATHS
# The raw record — caption tracks, recaps, stills — lives in the workshop and is not published. In a copy
# that does not hold it (the public repository), a file cited from it is reported as not held, not as missing.
RECORD = ("captions/", "canon/sources/", "canon/frames/")
record_absent = [r for r in RECORD if not os.path.isdir(os.path.join(ROOT, r.rstrip("/")))]
if record_absent:
    print("NOTE   the raw record is not in this copy: " + ", ".join(record_absent))
PATH_RE = re.compile(r"`((?:\.\./)?[A-Za-z0-9_./#<> -]+?\.(?:md|py|sh|json|txt|jpg))`")
for p in work:
    base = os.path.dirname(p)
    for m in PATH_RE.finditer(read(p)):
        ref = m.group(1)
        if any(c in ref for c in "#<>*") or " " in ref.strip():
            continue  # a pattern such as canon/E##_BEATS.md, not one file
        if ref in EXTERNAL:
            continue
        candidates = [ref, os.path.normpath(os.path.join(base, ref)), os.path.join("foundation", ref)]
        if "/" not in ref:
            candidates += [os.path.join(d, ref) for d in ("canon", "tools", "Sara", "captions")]
        if not any(os.path.exists(os.path.join(ROOT, c)) for c in candidates):
            if any(ref.startswith(r) for r in RECORD) and record_absent:
                continue  # cited from the raw record, which this copy does not hold
            fails.append(f"PATHS  {p}: names `{ref}`, which does not exist")

# 4 and 5. CHAPTERS and BEATS
chapter_dir = os.path.join(ROOT, "chapters")
chapters = sorted(f for f in os.listdir(chapter_dir) if f.endswith(".md")) if os.path.isdir(chapter_dir) else []
ledger_beats = {}
for f in sorted(os.listdir(os.path.join(ROOT, "canon"))):
    m = re.match(r"E(\d{2})_BEATS\.md$", f)
    if m:
        ledger_beats[m.group(1)] = set(re.findall(r"\bB(\d{2})\b", read("canon/" + f)))
for f in chapters:
    p = "chapters/" + f
    t = read(p)
    lines = t.split("\n")
    if not re.match(r"# Chapter \S+ — .+", lines[0]):
        fails.append(f"CHAPTER {p}: first line is not '# Chapter N — Title'")
    head = "\n".join(lines[:8])
    if not re.search(r"^\*Episode reference: Naagin, season 7, Episode \d+", head, re.M):
        fails.append(f"CHAPTER {p}: no episode reference line under the title")
    if not re.search(r"^\*(Draft; not yet accepted|Accepted by the author)", head, re.M):
        fails.append(f"CHAPTER {p}: no acceptance line under the title")
    if "\n## Footer" not in t:
        fails.append(f"CHAPTER {p}: no '## Footer'")
        continue
    body, footer = t.split("\n## Footer", 1)
    for k in FOOTER_KEYS:
        if k not in footer:
            fails.append(f"CHAPTER {p}: footer lacks {k}")
    if re.search(r"\b\d{1,2}:\d{2}(:\d{2})?\b", body):
        fails.append(f"CHAPTER {p}: a timecode stands in the story, above the footer")
    if re.search(r"\b(B\d{2}|O\d{3}|OPEN-\d{2})\b", body):
        fails.append(f"CHAPTER {p}: a ledger or ruling number stands in the story, above the footer")
    ep = re.search(r"Episode (\d+)", head)
    if ep:
        e = ep.group(1).zfill(2)
        for b in sorted(set(re.findall(r"\bB(\d{2})\b", footer))):
            if e in ledger_beats and b not in ledger_beats[e]:
                fails.append(f"BEATS  {p}: footer cites B{b}, which canon/E{e}_BEATS.md does not have")
        if e not in ledger_beats:
            fails.append(f"BEATS  {p}: Episode {int(e)} has no beat ledger")
    # the camera (WRITING.md §2): comparisons and reported feeling in narration; the 60-word cap
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import camera_check
    cam_fails, cam_notes = camera_check.check(t)
    for x in cam_fails:
        fails.append(f"CAMERA {p}: {x}")
    notes.append(f"CAMERA {p}: " + cam_notes[0])

# 6. SARA
sara_check = os.path.join(ROOT, "Sara", "tools", "check_sara.py")
if os.path.exists(sara_check):
    r = subprocess.run([sys.executable, sara_check], capture_output=True, text=True)
    first = (r.stdout.strip().split("\n") or [""])[0]
    notes.append("SARA   " + first)
    if r.returncode != 0:
        fails.append("SARA   the self-file failed its own checker; run python3 Sara/tools/check_sara.py")
else:
    fails.append("SARA   Sara/tools/check_sara.py is missing")

# 7. DESK
total = 0
for d, dirs, fs in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x != "__pycache__"]
    for f in fs:
        full = os.path.join(d, f)
        size = os.path.getsize(full)
        total += size
        r_ = rel(full)
        if f.endswith((".zip", ".tar", ".gz", ".mp4", ".mkv", ".webm")):
            fails.append(f"DESK   {r_}: archives, backups and video belong on Drive, not in the workshop")
        elif size > BIG_FILE_MB * 1024 * 1024:
            fails.append(f"DESK   {r_}: {size / 1048576:.1f} MB in one file")
mb = total / 1048576
notes.append(f"DESK   {mb:.1f} MB in the workshop (limit {DESK_LIMIT_MB:.0f} MB)")
if mb > DESK_LIMIT_MB:
    fails.append(f"DESK   the workshop weighs {mb:.1f} MB; move raw material to Drive")

print(f"FILES  {len(work)} working .md files, {len(chapters)} chapters")
print(f"ROWS   OPEN.md has {len(have_O)} O rows, {len(have_OPEN)} open questions, {len(have_S)} source questions; CANON.md has {len(have_R)} R rows")
for n in notes:
    print(n)
if fails:
    print(f"\nRED: {len(fails)} problem(s)")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("\nGREEN. This says the workshop's shape holds. It is not a canon proof and not the author's acceptance.")
