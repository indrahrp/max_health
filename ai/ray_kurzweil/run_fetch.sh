#!/usr/bin/env bash
set -euo pipefail
cd /Users/iharahap/claude-code-psn/max_health

mapfile -t URLS < <(awk '{print "https://www.youtube.com/watch?v=" $1}' ai/ray_kurzweil/video_ids.txt)

echo "Fetching transcripts for ${#URLS[@]} videos..."

python3 carn/fetch_transcript.py "${URLS[@]}" \
  --output ai/ray_kurzweil/transcripts.txt \
  --cookies-from-browser chrome
