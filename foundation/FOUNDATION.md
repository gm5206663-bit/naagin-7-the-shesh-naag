# NAAGIN 7 — THE SHESH NAAG · foundation and working map

**Owns: what this project is, whose word governs, and where each kind of fact lives.**

---

## The story

- **World:** *Naagin*, season seven (Colors TV, fifty episodes, 27 December 2025 to 14 June 2026). The episodes themselves are the source. Recaps and encyclopaedia pages are weaker witnesses and are marked as such.
- **Canon's lead:** the girl raised as Purvi, born Ananta, Naagrani of the Anant kul. The story stays hers (`STORY.md` §1).
- **The one added:** Vihaan Suri (`O001`, `O011`). In 2001 he is the small son of Parmeet and Nimrat Suri, the couple whose house the infiltrators take in Episode 1 (working: a year old, `OPEN-01`). In 2025 he is a son of the house that wears their name, brother to Aryaman, home from London to the family's news channel. He is a naag of the Shesh line and does not know it. He holds the Adaptation Talent, unawakened.
- **Premise:** canon's season happens. One more person is inside it, and he is the one living piece of the family the villains replaced. Whatever changes, changes because he is there, by a cause the page shows.
- **Form:** English prose chapters that read like the show plays (`O005`, `O014`). Each chapter opens with a visible episode reference. Several chapters to an episode. `WRITING.md` owns how.

## Authority

1. The author's latest word. Rulings live in `OPEN.md` §1 as `O` rows.
2. The project's own locks: `RULES.md`, `WRITING.md`, `STORY.md`, this folder.
3. The Adaptation Talent master foundation and level framework (the author's public `adaptation-talent` repository), for anything touching his Talent.
4. The latest checkpoint in `WORLD_STATE.md`.
5. Verified canon: `CANON.md`, `canon/SEASON.md`, the beat ledgers.
6. Earlier chapters.

A chapter never teaches canon. If the prose needs a fact no ledger holds, the work goes back to the episode.

## Evidence, strongest first

| Rank | Witness | Tag | Good for | Not good for |
|---|---|---|---|---|
| 1 | The episode's own picture | **V** | what is seen | — |
| 2 | The episode's caption track (speech recognition, Hindi) | **C** | what is said, and when | who says it; names are often misheard |
| 3 | Written recaps, two publishers | **TR**, **TB** | the order of events, who did what | pictures, exact words, names (both have been wrong) |
| 4 | Encyclopaedia cast and plot | **W** | actors, air dates | story detail (wrong on the scientist's name) |

Two recaps from one publisher are one witness. Nothing tagged only TR, TB or W is written as fact without a line in the captions or a frame behind it.

## Where everything is

| You want | Go to |
|---|---|
| What the author has ruled; what is still his to decide | `OPEN.md` |
| Where the work stands today | `STATUS.md` |
| What happens in any episode | `canon/SEASON.md` (digest of all fifty) |
| Every beat of an episode about to be written | `canon/E##_BEATS.md` (Episode 1 exists) |
| Which witness says what; conflicts ruled | `CANON.md` |
| Dates and order | `TIMELINE.md` |
| Who anyone is | `CHARACTERS.md` |
| Who is what to whom; the romance record | `RELATIONSHIPS.md` |
| Who knows what and who holds what, right now | `WORLD_STATE.md` |
| Vihaan as a person | `OC_VIHAAN.md` |
| His Talent, and his panel | `ADAPTATION_MODULE.md`, `STATUS_PANEL.md` |
| The story's laws and what the powers are | `STORY.md` |
| How a chapter reads | `WRITING.md`; measured by `tools/camera_check.py` |
| When a chapter is done | `RULES.md` |
| What was done on which day | `HISTORY.md` |
| Who is doing the work | `Sara/SARA.md` |
| What the author's other sessions teach, and the point of view it gives | `Sara/UNDERSTANDING.md` |
| Raw captions, recaps and stills | `captions/` (reading copies), `canon/sources/`, `canon/frames/`; the full raw set is on Drive (`README.md`, "On Drive") |

## Continuity locks

These do not move without the author.

1. Canon events happen as the episodes give them unless his presence, by a shown cause, changes them. No canon outcome is forced back and none is changed for convenience.
2. He never takes a canon character's beat, line or victory.
3. No power appears in him before the awakening. Before it the Talent shows only as what a body and mind do well, and that is a great deal: he is gifted, and nobody sees a cause.
4. Nobody knows what they have no path to knowing. The reader may be ahead of the characters, as the show's viewer is.
5. The men of the house are called by the names they wear. The workshop writes "Parmeet" in quotation marks when it means the impostor; the prose does not.
6. Her name follows what she is called in the scene: Purvi, then Ahana, then Apara, and Ananta when the truth is spoken.
7. The earlier attempt's inventions stay out (`O013`).

## After every chapter, in the same pass

`python3 tools/camera_check.py` on the chapter, then `python3 tools/check.py` · `TIMELINE.md` · `RELATIONSHIPS.md` · `WORLD_STATE.md` · his panel or a status delta · the episode's beat ledger (each beat marked written, deferred or changed) · `OPEN.md` if a question was raised or closed · `HISTORY.md` · `STATUS.md` · Sara's ledger. The chapter is labelled unaccepted until the author accepts it. Earlier versions are kept, not overwritten.
