#!/usr/bin/env python3
"""Make timestamped contact sheets from a video, for checking what an episode shows.
Usage: contact_sheet.py VIDEO OUT_PREFIX START_S END_S STEP_S [COLS] [THUMB_W]"""
import sys, cv2
from PIL import Image, ImageDraw
def main():
    video, prefix = sys.argv[1], sys.argv[2]
    start, end, step = float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
    cols = int(sys.argv[6]) if len(sys.argv) > 6 else 6
    tw = int(sys.argv[7]) if len(sys.argv) > 7 else 284
    cap = cv2.VideoCapture(video)
    frames = []
    t = start
    while t <= end:
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
        ok, fr = cap.read()
        if not ok: break
        fr = cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(fr)
        th = int(im.height * tw / im.width)
        im = im.resize((tw, th))
        d = ImageDraw.Draw(im)
        label = f"{int(t)//60:02d}:{int(t)%60:02d}"
        d.rectangle([0, 0, 44, 13], fill=(0, 0, 0))
        d.text((3, 1), label, fill=(255, 255, 0))
        frames.append(im)
        t += step
    if not frames:
        print('no frames'); return
    th = frames[0].height
    rows = (len(frames) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * tw, rows * th), (20, 20, 20))
    for i, im in enumerate(frames):
        sheet.paste(im, ((i % cols) * tw, (i // cols) * th))
    out = f"{prefix}_{int(start):04d}-{int(end):04d}.jpg"
    sheet.save(out, quality=80)
    print(out, sheet.size, len(frames), 'frames')
main()
