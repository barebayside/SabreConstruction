#!/usr/bin/env bash
# Concept 03 — finish the vertical testimonial cut.
#
# Takes the raw 9:16 Veo clip and does two things:
#   1. Burns in the AI DEMO label. This is NOT decoration — the person in the
#      clip is not a Sabre customer, and the label has to survive the file
#      leaving the page.
#   2. Pans across to a Sabre end card once the person stops talking, so the ad
#      finishes on the brand instead of on a stranger's face.
#
# The end card copy is all from docs/reference/client-facts.md. Nothing on it
# is a claim Sabre hasn't already published about itself.
set -euo pipefail

SRC="assets/video/testimonial-v-raw.mp4"
PHOTO="assets/img/rb-c-real.jpg"
LOGO="assets/img/sabre-logo-white.png"
OUT="assets/video/testimonial-vertical.mp4"
F="tools/fonts/BebasNeue-Regular.ttf"

RED="0xFF1A1A"
INK="0x0B0B0C"

TALK=8.0        # length of the talking head
CARD=4.0        # length of the end card
XF=0.7          # the pan across
OFF=$(awk "BEGIN{print $TALK-$XF}")

ffmpeg -v error -y \
  -i "$SRC" \
  -loop 1 -t "$CARD" -i "$PHOTO" \
  -i "$LOGO" \
  -filter_complex "\
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=25,\
drawbox=x=0:y=1690:w=1080:h=80:color=black@0.66:t=fill,\
drawtext=fontfile='$F':text='AI DEMO \· NOT A REAL CUSTOMER':fontcolor=0xF2C94C:fontsize=44:x=(w-tw)/2:y=1708[talk];\
[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=25,\
drawbox=x=0:y=0:w=1080:h=1920:color=${INK}@0.80:t=fill[cardbg];\
[2:v]scale=440:-1[lg];\
[cardbg][lg]overlay=(W-w)/2:640[c1];\
[c1]drawtext=fontfile='$F':text='FAMILY HOMES ON THE':fontcolor=white:fontsize=76:x=(w-tw)/2:y=880,\
drawtext=fontfile='$F':text='BAYSIDE SINCE 1990':fontcolor=$RED:fontsize=76:x=(w-tw)/2:y=960,\
drawbox=x=440:y=1080:w=200:h=5:color=$RED:t=fill,\
drawtext=fontfile='$F':text='07 3823 3200':fontcolor=white:fontsize=64:x=(w-tw)/2:y=1140,\
drawtext=fontfile='$F':text='CAPALABA \· BRISBANE BAYSIDE':fontcolor=0xA9A7A3:fontsize=36:x=(w-tw)/2:y=1230,\
drawtext=fontfile='$F':text='QBCC 328475 \· FAMILY OWNED':fontcolor=0x8E8C88:fontsize=34:x=(w-tw)/2:y=1300[card];\
[talk][card]xfade=transition=slideleft:duration=$XF:offset=$OFF[v];\
[0:a]afade=t=out:st=$OFF:d=$XF,apad=whole_dur=$(awk "BEGIN{print $TALK+$CARD-$XF}")[a]" \
  -map "[v]" -map "[a]" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 30 -preset slow \
  -c:a aac -b:a 96k -movflags +faststart "$OUT"

ffmpeg -v error -y -ss 2 -i "$OUT" -frames:v 1 -q:v 4 assets/img/testimonial-vertical.jpg

printf '%s  %s KB\n' "$OUT" "$(( $(stat -c%s "$OUT") / 1024 ))"
ffprobe -v error -show_entries stream=width,height,duration -of default=noprint_wrappers=1 "$OUT" | head -6
