#!/usr/bin/env bash
# Fetch YouTube's automatic Hindi captions for one official Colors TV full-episode upload.
# Downloads captions only, never the video. Usage: tools/fetch_captions.sh <episode number> <youtube id>
# Video ids are listed in captions/youtube_full_episodes.json. Needs: pip install yt-dlp
set -euo pipefail
n=$(printf "%02d" "$1"); id="$2"
cd "$(dirname "$0")/.."
tmp=$(mktemp -d)
python3 -m yt_dlp --skip-download --write-auto-subs --sub-langs "hi-orig" --sub-format json3 \
  -o "$tmp/E${n}.%(ext)s" "https://www.youtube.com/watch?v=${id}"
python3 tools/json3_to_txt.py "$tmp/E${n}.hi-orig.json3" "captions/E${n}.hi.srt" "captions/E${n}.hi.txt"
rm -rf "$tmp"
