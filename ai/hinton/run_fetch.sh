#!/usr/bin/env bash
set -euo pipefail
cd /Users/iharahap/claude-code-psn/max_health

# Read video IDs into a bash array and convert to full URLs
mapfile -t URLS < <(awk '{print "https://www.youtube.com/watch?v=" $1}' ai/hinton/video_ids.txt)

echo "Fetching transcripts for ${#URLS[@]} videos..."

python3 carn/fetch_transcript.py "${URLS[@]}" \
  --output ai/hinton/transcripts.txt \
  --cookies-from-browser chrome
