#!/usr/bin/env bash
# Join each real clip to its AI continuation.
#
# The real half keeps its own audio (site noise, wind — that's what makes the
# first three seconds read as genuine) and fades out across the join. The AI
# half is silent. A short crossfade hides the seam, and the last frame holds
# so the finished house lands before the loop.
set -euo pipefail

RAW="Y:/My Folders/Nathan"
OUT="assets/video"
IMG="assets/img"

CLIPS=("20260814_111158" "20260814_111209" "20260814_111233")
XF=0.35          # crossfade seconds
HOLD=1.2         # freeze on the final frame

for i in 1 2 3; do
  src="$RAW/${CLIPS[$((i-1))]}.mp4"
  ai="$OUT/raise-ai-$i.mp4"
  out="$OUT/reel-$i.mp4"

  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$src")
  offset=$(python -c "print(round(float('$dur') - $XF, 3))")
  afade=$(python -c "print(round(float('$dur') - 0.6, 3))")

  echo "reel $i: real ${dur}s, crossfade at ${offset}s"

  ffmpeg -v error -y -i "$src" -i "$ai" -filter_complex "\
[0:v]scale=1080:1920,setsar=1,fps=30,setpts=PTS-STARTPTS[a];\
[1:v]scale=1080:1920,setsar=1,fps=30,setpts=PTS-STARTPTS[b];\
[a][b]xfade=transition=fade:duration=$XF:offset=$offset,tpad=stop_mode=clone:stop_duration=$HOLD[v];\
[0:a]afade=t=out:st=$afade:d=0.6,apad[aud]" \
    -map "[v]" -map "[aud]" -shortest \
    -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 26 -preset slow \
    -c:a aac -b:a 128k -movflags +faststart "$out"

  # poster from the finished-house end, not the building site
  end=$(python -c "print(round($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out") - 1.4, 2))")
  ffmpeg -v error -y -ss "$end" -i "$out" -frames:v 1 -q:v 4 "$IMG/reel-$i-poster.jpg"

  printf '  -> %s  %s KB\n' "$out" "$(( $(stat -c%s "$out") / 1024 ))"
done

echo "done"
