---
description: Fetch or incrementally update YouTube transcripts for a health/carnivore channel
---

Fetch YouTube transcripts for a registered health channel and save them under carn/<channel-key>/.

## Channel Registry

| Key | Channel URL | Transcript file |
|-----|-------------|-----------------|
| zerocarb | https://www.youtube.com/@zerocarb | carn/zerocarb/transcripts.txt |
| anthonychaffeemd | https://www.youtube.com/@anthonychaffeemd | carn/anthonychaffeemd/transcripts.txt |
| shawnbakermd | https://www.youtube.com/@ShawnBakerMD | carn/shawnbakermd/transcripts.txt |
| lovelesshealthsolutions | https://www.youtube.com/@LovelessHealthSolutions | carn/lovelesshealthsolutions/transcripts.txt |
| homestead | https://www.youtube.com/@Homesteadhow | carn/homestead/transcripts.txt |

> To add a new channel: create a new row above and a matching folder under carn/<key>/.

## Instructions

The user may invoke this as:
  /fetch-transcripts <key>         — fetch/update a specific channel
  /fetch-transcripts               — list available channels and prompt the user to pick one

STEP 1 — Resolve the channel:
- If $ARGUMENTS is empty, print the registry table and ask the user which channel to fetch.
- Match $ARGUMENTS (case-insensitive) to a key in the registry.
- If no match, tell the user the valid keys.

STEP 2 — Check if transcripts already exist:
  ls carn/<key>/transcripts.txt

- If the file EXISTS → use --incremental mode (append new videos only).
- If the file does NOT exist → fresh run (no --incremental).
- Progress file lives alongside the transcript: carn/<key>/transcripts.progress.json

STEP 3 — Run the fetch (background, max 1700 videos):

  Fresh run:
    cd /Users/iharahap/claude-code-psn/max_health && \
    python3 carn/fetch_transcript.py "<channel_url>" \
      --channel --max 1700 \
      --cookies-from-browser chrome \
      --output carn/<key>/transcripts.txt

  Incremental update:
    cd /Users/iharahap/claude-code-psn/max_health && \
    python3 carn/fetch_transcript.py "<channel_url>" \
      --channel --max 1700 \
      --incremental \
      --cookies-from-browser chrome \
      --output carn/<key>/transcripts.txt

Run the command with run_in_background=true.

STEP 4 — Monitor and report progress, re-arm monitor each hour until job completes.

STEP 5 — On completion, confirm total transcripts, file size, and output location.
