#!/usr/bin/env bash
# publish_git.sh — build a clean git repository of the workshop, and push it to GitHub.
#
#   tools/publish_git.sh                 build + commit into /tmp/publish, print what is in it (no network)
#   tools/publish_git.sh --push          the same, then create/push the repo (needs GITHUB_TOKEN)
#   REPO_NAME=my-repo tools/publish_git.sh --push
#
# What goes in: the workshop as it stands — the files the author reads, the foundation, the canon digests,
# the chapters, the tools and Sara.
# What stays out, by name, always: the raw record. The caption tracks are YouTube transcripts, the recaps
# belong to the sites that wrote them, and the stills are frames of the show. They are held in the workshop
# for checking and are not published.
#
# GITHUB_TOKEN must be a fine-grained token with "Administration: read and write" and "Contents: read and
# write" on the account, or a classic token with the "repo" scope. It is read from the environment and is
# never written to a file or printed.
set -euo pipefail

SRC="$(cd "$(dirname "$0")/.." && pwd)"
BUILD="${BUILD:-/tmp/publish}"
REPO_NAME="${REPO_NAME:-naagin-7-the-shesh-naag}"
OWNER="${OWNER:-gm5206663-bit}"
PUSH=0
[ "${1:-}" = "--push" ] && PUSH=1

# The raw record, never published.
EXCLUDES=(captions canon/sources canon/frames __pycache__)

echo "== source : $SRC"
echo "== build  : $BUILD"

rm -rf "$BUILD"
mkdir -p "$BUILD"

# Copy the tree, minus the raw record and any caches.
tar -C "$SRC" \
    $(for e in "${EXCLUDES[@]}"; do printf -- '--exclude=%s ' "$e"; done) \
    --exclude='__pycache__' --exclude='*.pyc' --exclude='*.zip' \
    -cf - . | tar -C "$BUILD" -xf -

# The published repository keeps its own .gitignore so that a later clone cannot add the record by accident.
cat > "$BUILD/.gitignore" <<'IGNORE'
# The raw record stays in the workshop and is never published.
captions/
canon/sources/
canon/frames/
__pycache__/
*.pyc
*.zip
IGNORE

cd "$BUILD"
git init -q -b main
git config user.name  "${GIT_NAME:-Gaurav Meena}"
git config user.email "${GIT_EMAIL:-gm5206663-bit@users.noreply.github.com}"
git add -A
git -c commit.gpgsign=false commit -q -m "Naagin 7 — The Shesh Naag: Episode 1 in three chapters

The workshop as it stands on 2026-11-11: the author's rulings, the canon record for Episode 1,
the foundation files, the three chapters of Episode 1, the checking tools, and Sara's ledger.

The raw record (caption tracks, recaps, stills) is not published."

echo "== commits:"
git --no-pager log --oneline
echo "== files: $(git ls-files | wc -l) tracked, $(du -sk --exclude=.git . | cut -f1) KB"
echo "== tree:"
git ls-files | sed 's/^/   /'

if [ "$PUSH" -eq 0 ]; then
    echo
    echo "Built and committed. Nothing was sent anywhere."
    echo "To publish:  GITHUB_TOKEN=<token> tools/publish_git.sh --push"
    exit 0
fi

: "${GITHUB_TOKEN:?GITHUB_TOKEN is not set}"
API="https://api.github.com"

echo "== repository: $OWNER/$REPO_NAME"
code=$(curl -s -o /tmp/repo.json -w '%{http_code}' "$API/repos/$OWNER/$REPO_NAME" \
        -H "Authorization: Bearer $GITHUB_TOKEN")
if [ "$code" = "404" ]; then
    echo "   creating it (public)"
    curl -s -X POST "$API/user/repos" \
        -H "Authorization: Bearer $GITHUB_TOKEN" \
        -H "Accept: application/vnd.github+json" \
        -d "{\"name\":\"$REPO_NAME\",\"private\":false,\"description\":\"Naagin 7 — The Shesh Naag, told in prose, episode by episode.\"}" \
        -o /tmp/repo.json
elif [ "$code" != "200" ]; then
    echo "   could not read the repository (HTTP $code):"; sed -n '1,5p' /tmp/repo.json; exit 1
else
    echo "   already exists"
fi

git remote remove origin 2>/dev/null || true
git remote add origin "https://x-access-token:$GITHUB_TOKEN@github.com/$OWNER/$REPO_NAME.git"
git push -q -u origin main
git remote set-url origin "https://github.com/$OWNER/$REPO_NAME.git"

echo "== pushed: https://github.com/$OWNER/$REPO_NAME"
git --no-pager log -1 --format='   %h %s'
