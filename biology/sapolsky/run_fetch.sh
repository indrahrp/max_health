#!/usr/bin/env bash
# Fetch Sapolsky lectures (Stanford channel search) into biology/sapolsky/transcripts.txt
set -euo pipefail
cd /Users/iharahap/claude-code-psn/max_health

# Read video IDs (one per line, format: ID<TAB>title) and build URLs
mapfile -t URLS < <(awk '{print "https://www.youtube.com/watch?v=" $1}' biology/sapolsky/video_ids.txt)

echo "Fetching transcripts for ${#URLS[@]} Sapolsky videos..."

python3 carn/fetch_transcript.py "${URLS[@]}" \
  --output biology/sapolsky/transcripts.txt \
  --cookies-from-browser chrome
