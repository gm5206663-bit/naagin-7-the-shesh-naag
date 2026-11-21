# STYLE SHEET — one page, and everything on it

**Owns: the operating sheet. What canon style is, what the supernatural owes every scene, how the butterflies are kept, which file owns which part, and the order the gates run in.** It rules nothing of its own: every line points at the file that owns it. Written 2026-11-12, after the author's order that the workshop be *clean, clear, systematic, organised, synergetic*.

---

## 1 · What canon style is, in one sentence

**Everything the episode shows, the page shows; everything the episode says, the page says in the episode's own words; and the room is as big on the page as it is on screen** — the sound, the score, the omen, the crowd, the tears, the shout. (`WRITING.md` §1–§2; `canon/STYLE_CANON.md` §1a–§1h; `O005`, `O020`, `O027`, `O028`.)

**Never again:** a quiet literary paragraph where the show plays a scene. That fault has a name in this workshop — *correct facts, clean prose, wrong show* — and it has been diagnosed four times. **Feeling is written, its cause may be said, and the room reacts** (`O035`, 2026-11-12: the ban is deleted from every file).

## 2 · What every scene owes — the six things the show never skips

| # | The thing | Where it lives | The test |
|---|---|---|---|
| 1 | **Place, hour, light** — named once, in the opener | `canon/PICTURE.md` | Can a reader say where this is and what time it is? |
| 2 | **Sound and score** — a hiss, a bell, a been, a drum, the strings going out, and since 2026-11-12 one of **three named identities** (`SOUND_AND_SCREEN.md` §9) | `STYLE_CANON` §1b, `canon/SOUND_AND_SCREEN.md` §1–§2, §9 | Is one sound in the scene, is the music named where it behaves, and does the cue belong to the pair it is attached to? |
| 3 | **One omen**, unattended and unexplained | `STYLE_CANON` §1c | Is there one, and does nobody in the room point at it? |
| 4 | **The room as chorus** — gasp, hand to the mouth, a child pulled back, a name called | `STYLE_CANON` §1d | Does anybody who is not speaking react? |
| 5 | **Feeling named, plainly, once** | `WRITING.md` §2 law 2 (**rewritten**) | Is the feeling on the page in the plain word? |
| 6 | **The supernatural as the show plays it** — never explained | `canon/SUPERNATURAL.md` §1, §2 | Is it shown, said by a mouth, or suffered — and never explained? |

## 3 · The supernatural, restored — the inventory

The show's own furniture, and the page's. **A chapter that has none of these is not this serial**:

- **The hiss with no snake in the frame** — the oldest device in the show.
- **The eyes**: gold in the dark; the hood that is there in the mirror and not in the room.
- **The change**: skin coming away, the spine, the cold, the heat in the hands — shown in the body, never described as a mechanism.
- **Wind, thunder, a sky going the colour of a bruise** — the show's punctuation before a reveal.
- **The lamp**: a diya that gutters for the wrong person and stands straight for the right one.
- **The mirror and the water** — where naag things show true.
- **The animal and the street**: dog, crow, flies, ants, the horse that will not pass.
- **Naagriit and the kul's own language**: the ritual words, the vows, the throne, the cloth over the seat.
- **The been** — the instrument that finds, or fails to find, and says so in a mouth.
- **The stone** — the claim of healing and waking, always as a claim in somebody's mouth, never tested by the page.
- **The score** — the theme for the pair, the drum for the reveal, the silence that lasts one face. **Three named identities since 2026-11-12** (`canon/SOUND_AND_SCREEN.md` §9): her question on the been (canon, untouched), his **`Ek Taar`** — one low string, struck and left hanging, no melody, never in a naag room — and theirs, **`Woh Do Log`**, his note with her second phrase over it, a woman's voice only on contact, resolving nowhere. **And the cut: nothing soft ever plays on Aryaman and Purvi.** `tools/score_check.py` fails a chapter that forgets.

**The hard rule that survives everything:** none of it is ever explained. `SUPERNATURAL.md` §1 rule 1 — no mechanism, on any page, ever. Vihaan in particular never knows (`§2` rule 5), and he is fenced out of the rooms where the naag world is spoken (`thread_check.py` `FENCE:`).

## 4 · Butterflies — one register, no forgetting

Every divergence from canon is numbered in **`foundation/BUTTERFLY.md`** — **seventy-six entries, `BF-01` to `BF-76`, and every one of the nineteen chapters has at least one**, each with where it was made, what it does to canon, and what it costs later. **The rule:** one entry the day it is made; a withdrawn one keeps its number and is marked `WITHDRAWN`; a correction of the page is not a butterfly and goes in the chapter's `FIXED:`/`RESTORED:` key instead.

**The chain the book actually runs on:** the child in the cot (BF-01) → the man who exists (BF-02) → the child he saves and the dance that is his (BF-12, BF-13) → the file he finds and the Kumbh question he answers (BF-10, BF-22) → the vans on his own signature (BF-36) → the face worn by something that is not him (BF-35) → the missing-person report (BF-45) → the brother who comes back (BF-47).

## 5 · Who owns what — the map

| Question | File |
|---|---|
| What does canon say, beat by beat, with timecodes? | `canon/E01–E09_BEATS.md` |
| What is the show's style, sound, omen, scale? | `canon/STYLE_CANON.md`, `WRITING.md` |
| What may never be explained? | `canon/SUPERNATURAL.md` |
| Who knows what, and when? | `foundation/WORLD_STATE.md` (checkpoints to Chapter 18) |
| What has this serial changed, and what did it cost? | `foundation/BUTTERFLY.md` |
| What is in whose hand, and what is open? | `OPEN.md`, `foundation/OC_STATUS.md` |
| Where is he, and how much? | `foundation/OC_PRESENCE.md`, `tools/thread_check.py` |
| What is the state of the whole workshop? | `STATUS.md` (newest section is the edge) |
| What is the order of the next work? | `STATUS.md` line 4, and the author's latest section |

## 6 · The order the gates run

1. `tools/oc_check.py` — he is in the chapter, seen, and not made small.
2. `tools/gap_check.py` — every beat of the episode is on the page, in order.
3. `tools/thread_check.py` — a chapter with fewer than 60% of its counted scenes carrying him fails; `FENCE:` is declared, never assumed.
4. `tools/picture_check.py` — the room is on the page before anybody speaks in it.
5. `tools/camera_check.py` — the past tense out, the sixty-word cap. **The comparison ban is deleted (`O037`): a simile is ordinary narration now.**
6. `tools/score_check.py` — the score's loyalties: no soft cue on Aryaman and Purvi, never two registers at once, no melody for Vihaan (`SOUND_AND_SCREEN.md` §9).
7. `tools/check.py` — the shape of the whole tree.

**A chapter is never accepted by a tool.** Nothing in this workshop is accepted until the author says so.
