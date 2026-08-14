#!/usr/bin/env bash
# Wrap the wide knockdown-rebuild master into a branded 9:16 Reel.
#
# The master is 2.38:1 because it was generated from Sabre's own wide
# photograph. Cropping that to full-bleed vertical would throw away three
# quarters of the frame, so instead the video sits in the middle of a Sabre
# black canvas with the headline above it and the CTA below — which is what
# the empty space in a Reel is for anyway.
set -euo pipefail

SRC="assets/video/rebuild-hero.mp4"
OUT="assets/video/rebuild-reel-9x16.mp4"
F="tools/fonts/BebasNeue-Regular.ttf"
LOGO="assets/img/sabre-logo-white.png"

RED="0xFF1A1A"
INK="0x0B0B0C"

ffmpeg -v error -y -i "$SRC" -i "$LOGO" -filter_complex "\
[0:v]scale=1080:-2,setsar=1,fps=25[vid];\
color=c=$INK:s=1080x1920:d=20,fps=25[bg];\
[bg][vid]overlay=(W-w)/2:700:shortest=1[base];\
[1:v]scale=300:-1[lg];\
[base][lg]overlay=(W-w)/2:150[wl];\
[wl]drawtext=fontfile='$F':text='SAME STREET.':fontcolor=white:fontsize=104:x=(w-tw)/2:y=300,\
drawtext=fontfile='$F':text='SAME SCHOOL.':fontcolor=white:fontsize=104:x=(w-tw)/2:y=400,\
drawtext=fontfile='$F':text='A WHOLE NEW HOUSE.':fontcolor=$RED:fontsize=104:x=(w-tw)/2:y=500,\
drawtext=fontfile='$F':text='KNOCKDOWN REBUILDS \· BRISBANE BAYSIDE':fontcolor=0xA9A7A3:fontsize=38:x=(w-tw)/2:y=1240,\
drawbox=x=190:y=1360:w=700:h=130:color=$RED:t=fill,\
drawtext=fontfile='$F':text='BOOK A FREE SITE VISIT':fontcolor=white:fontsize=64:x=(w-tw)/2:y=1392,\
drawtext=fontfile='$F':text='FAMILY OWNED SINCE 1990 \· QBCC 328475':fontcolor=0x86868E:fontsize=34:x=(w-tw)/2:y=1580[v]" \
  -map "[v]" -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 28 -preset slow -an \
  -movflags +faststart "$OUT"

ffmpeg -v error -y -ss 14 -i "$OUT" -frames:v 1 -q:v 4 assets/img/rebuild-reel-poster.jpg

printf '%s  %s KB\n' "$OUT" "$(( $(stat -c%s "$OUT") / 1024 ))"
ffprobe -v error -show_entries stream=width,height,duration -of default=noprint_wrappers=1 "$OUT"
