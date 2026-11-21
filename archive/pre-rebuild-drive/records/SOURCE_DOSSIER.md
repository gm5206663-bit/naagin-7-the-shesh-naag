# SOURCE DOSSIER — everything obtainable, per episode

**Owns: the source-hunt order of work: the video machine, per-episode source entries, and the coverage matrix.**

Author order 2026-11-20 (§185): before the rebuild continues, find
sources for the episodes — full details, information, video,
pictures, everything possible.

## The machine (proven on E1, 2026-11-20)

1. IDs: `captions/youtube_full_episodes.json` (official Colors TV uploads).
2. Pull: `pip install yt-dlp imageio-ffmpeg` (per-turn; not persisted),
   `yt-dlp -f 134` (360p mp4, ~60MB) to /tmp, never the workspace.
3. Frames: static ffmpeg `fps=1/10` (~250 frames/episode) to /tmp.
4. View: PIL contact sheets (8×8 cells, yellow second-labels) via read_file.
5. Subs: `yt-dlp --write-sub --write-auto-sub --sub-langs hi --sub-format vtt`
   (1345 timed cues for E1 vs 76 merged local lines).
6. Archive: key frames → Drive stills folder
   (`11Zu84LyGTO-mo-ttAGjGzv027ufIV7Kd`); VTT → Drive md folder;
   NOTHING heavy stays local (DESK). Staging deleted after upload.
7. DEAD END (do not retry blind): storyboard tiles — spec extracts but
   every tile 404/403 (sigh rejected, exact yt-dlp URLs included).

## E1 (27 Dec 2025, 41:08) — COMPLETE 2026-11-20

- Video: https://www.youtube.com/watch?v=Q7XHVgQuKvg ("Naagin S7 |
  Full Episode - 1 | Naagin Legacy Unleashed | Colors TV").
- Viewed: full, 247 frames at 10s (4 contact sheets).
- Subs: E01_2025-12-27_subs_hi.vtt (1345 timed cues, Drive md folder `1fivV8fTIbcmIbNtHA6k5gtCd4TlnA-7Q`).
- Captions local: captions/E01.hi.txt (76 merged lines).
- Recaps local: TR (full), OTTPlay.
- Beats: canon/E01_BEATS.md (B01–B24).
- Closed by video: the 02:30–06:58 no-still gap; wolves re-confirmed;
  keeper-in-car (B07), painted face (B24), professor-to-camera (B24)
  all frame-verified.
- Open kept: moustached-2001-man vs grey-2025-Parmeet visual identity
  (inconclusive at 360p; narrative inference stands, CHARACTERS §3).
- 26 stills (Drive stills folder):

| # | File | Shows |
|---|---|---|
| 1 | E01_02-00_kumbh_lamps.jpg `1kxPHhh50lg7gu8fzc5g94iaa-NQ8gvs9` | Kumbh night lamps road (B01) |
| 2 | E01_03-30_akhara.jpg `1rgaj31gKwnY6HCH4Q1hWgH7_8YSKBx8K` | Akhara gathering (B02) |
| 3 | E01_05-40_nadi_leaf.jpg `14wBtCSi-oAa8yDgueopopCW1sAT2LYmp` | Nadi sage, palm leaf (B02) |
| 4 | E01_07-00_suri_birthday.jpg `1TVdcK9LnDy9J487jE1G37vSAgy0aOKlf` | Suri birthday room (B03) |
| 5 | E01_07-40_moustached_gate.jpg `1gStCC5k8xV-AWSPtHZl-b3mkCtxAYUMi` | Moustached man at gate (B03) |
| 6 | E01_08-30_nimrat_cry.jpg `1V7B8ZDxWXIveDDQS-WOIlD-E8iARD3Rg` | Nimrat cries out (B03) |
| 7 | E01_11-40_professor_son_book.jpg `16VvwhC5eK2MzUYH2wNuZyIU-ZsOeKZ76` | Farewell, metal book (B05) |
| 8 | E01_13-00_aroras_worry.jpg `1hGlbhDoRS3JennRhDt6xBodNws3hYLDm` | Aroras, locked house (B06) |
| 9 | E01_14-00_professor_door.jpg `1ck8LLvpODcdbalQ6VEyastXP8Z_jLfgy` | Professor refused (B07) |
| 10 | E01_14-30_keeper_car.jpg `1Z9dEalvCeYQC5ftqnci-sd764239WeNu` | Keeper watching, car (B07) |
| 11 | E01_15-20_wounded_door.jpg `1C6D2rJMoBMAidYzJEJZTQgWdQpuCNb3K` | Wounded woman (B08) |
| 12 | E01_17-00_mother_baby.jpg `1zA_vQ3lKJMQm_PVJbYORYnuxXs0tMQrY` | Mother and newborn (B09) |
| 13 | E01_18-10_ridge_walk.jpg `1XBz88Sp6wNSQIAR7gj4D7UB9t9H1vMoq` | Ridge walk (B10) |
| 14 | E01_19-40_wolf.jpg `1lP-yOWfuHNP1M_bVzG9nU_1jpUZ-O0Mq` | Wolf close-up (B10) |
| 15 | E01_22-10_moustached_torture.jpg `19_M9ejRXcQPqyoYOt7Yr3A6Cp4sBafBw` | Torture room (B12) |
| 16 | E01_26-00_ananta_cobra.jpg `16XgZK38IB-8qJcYjz8AW4KC3Mgk2Is9c` | Ananta holds cobra (B15) |
| 17 | E01_27-40_purvi_fall.jpg `1z1Fp_ak09I8L5Fm52DQeQ6_wlaUVNLzX` | Purvi mud fall (B16) |
| 18 | E01_28-40_purvi_look.jpg `1kW9zln8KIhtkQ4PrVrMuzvwPUbLlt8Xf` | Purvi look, layers (B16) |
| 19 | E01_29-00_tickets_table.jpg `1rRCOAn0SHMlagYaBWYUp004ivPk3RF3s` | Tickets table (B17) |
| 20 | E01_33-50_aryaman_newsroom.jpg `1tyWofl5xsbezHcH7Mb-9pOb1oszCq1vB` | Aryaman newsroom (B20) |
| 21 | E01_37-10_father_son.jpg `1_hRT4q98MvbE1jSOIp1UVG5KuY-f0CNG` | Father-son party (B21) |
| 22 | E01_38-00_road_car.jpg `1QPrv38RVmBDXEQ6fxdymM-OSW5aKdgCE` | Car dead, road (B22) |
| 23 | E01_38-20_mandir.jpg `1xRwr2h5p6D48GPUSZ8F3VpbvILkBvHON` | Naag Mandir (B23) |
| 24 | E01_40-20_painted_face.jpg `1AEy_kFeKodH7nCt_GMfneT_6T1AebjuM` | Painted face (B24) |
| 25 | E01_40-40_swap_bedroom.jpg `123o03av5IYNwk1Go_qnMN2ZWOzCi6D0r` | Swap bedroom (B24) |
| 26 | E01_41-00_professor_camera.jpg `1_EzjnuWi8ioatolePuTAqvr57YPEbHAl` | Professor to camera (B24) |

## Coverage matrix (rebuild needs E1–E20; E21+ later)

Legend: V video viewed · S stills · T timed subs · C captions · R recaps (count).
E1: V✓ S26 T✓ C✓ R2 (TR, OTTPlay) — COMPLETE.
E2–E20: V·S·T pending; C✓ all; R as held (TR E2–E18+E20; TB E2–E11+E13–E18; TOI E4+E13/14+E16–E18; TE E18; BT E12+E18; JSB E12+E15; KB E12–E14; SG E19; TE E19; TOI E19).
Recap gaps to fill alongside video: E19 TR/TB; E1/E2/E3 TOI/TE/BT/SG-depth;
E20 TR held, TB pending. Fiction247/serialxpress spot-checks per episode.
Next: E2 (ID XbMCxKjkU8Q, 2363s).
