#!/usr/bin/env bash
# Fetch Rhonda Patrick / FoundMyFitness sauna & heat therapy videos into biology/rhonda_patrick/transcripts.txt
set -euo pipefail
cd /Users/iharahap/claude-code-psn/max_health

mapfile -t URLS < <(awk '{print "https://www.youtube.com/watch?v=" $1}' biology/rhonda_patrick/video_ids.txt)

echo "Fetching transcripts for ${#URLS[@]} FoundMyFitness sauna videos..."

python3 carn/fetch_transcript.py "${URLS[@]}" \
  --output biology/rhonda_patrick/transcripts.txt \
  --cookies-from-browser chrome
