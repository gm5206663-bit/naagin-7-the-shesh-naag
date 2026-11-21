# RULE — the scene that would happen if he were real

**Owns: the test that catches the fault this book keeps making — a character who is always a guest in somebody else's scene. Read with `OC_VIHAAN.md` §0, §0bis and §0a.**

---

## 1 · The author's correction, 2026-11-14

***"There is not single scene of vihaan original scene, that naturally should happen or needed, understand naturally needed."***

He is describing something worse than a weak scene, and it took a list to see it. The original 2026-11-14 audit listed four candidate OC scenes across the first twenty chapters — `The Study`, `Chauthi Manzil`, `The Attari File`, and `Sameer's Door`. **After Chapter 20's location repair, only `The Attari File` is declared OC-owned in Chapter 20; `Sameer's Door` no longer contains Vihaan and is not his scene.** The older list below is historical where it says otherwise. The current one-scene declaration is not to be expanded solely to satisfy `oc_check.py`'s conflicting two-scene floor.

- `The Study` — Parmeet summons him.
- `Chauthi Manzil` — **him and Ahana in a hotel room**, and it exists because canon's plot needs Aryaman framed.
- `The Attari File` — canon's engagement, with him in it.
- `Sameer's Door` — formerly staged with him outside the murder. After the location repair, Vihaan is not in this scene; the earlier placement is superseded.

**The one act in the entire book that belongs to nobody but him — his private request to Verma for a missing-person file for Purvi, in his own name and with the house's name excluded — now has its own scene, `Teen Baje, Teesra Kamra`, not a paragraph on a landing.** The scene's clock is unresolved: the title/opening and dialogue say three in the morning; narration places the phone action at four; the file is requested for eight, and its filing time is not shown.

---

## 2 · The distinction that has been missing

Not every scene a character is in has to be his. But **a character with no scene of his own is a character the plot uses, and readers feel it long before they can name it.** The difference is not length, and it is not POV. It is **whose problem the scene exists to advance.**

| | **A guest scene** | **His own scene** |
|---|---|---|
| Why it exists | to advance somebody else's beat, with him present | to advance **his** problem, on his clock |
| Who chose the time and place | the plot, or another character | **him** |
| What he wants in it | nothing he could not want anywhere | something specific, and it can fail |
| How it can end | only the way the plot needs | **badly, for him** |
| The test | *if he were cut, the beat still happens* | *if he were cut, there is no scene* |

---

## 3 · The four engines of a Vihaan-only scene

**A scene of his must be driven by one of these, and it must be a thing he chose to do.**

1. **The paper.** He is the man every paper in this book passes through — the licence, the feed, the register, the file, the missing-person report, the sheet with the duplicated line, the bill nobody has paid. **A man alone with a document at an hour he chose** is the most natural scene this character can have. Chapter 18 now gives him `Teen Baje, Teesra Kamra` as one; the scene's exact hour and the filing time remain unresolved.
2. **The work.** The half of his life that is not that house: the London end, the desk, the call at six in the morning to a man whose name nobody in Delhi knows. Six months of it happened off the page, and `§3a-ter` says it has to be shown and not summarised.
3. **The thing he is not saying.** His whole arc is a man doing the wrong paperwork for the right reason. **A scene in which he almost says it and does not** is his by right, and nobody else can be in it.
4. **The errand he invented.** When he decides something on his own authority — a car, a room, an inspector at eight in the morning, a file kept out of somebody's hands — **the consequences come back to him in a scene of his own**, and that scene is where the bill is paid.

**What does not count as an engine:** somebody summoning him, a canon beat that needs a witness, a conversation somebody else starts, and the supernatural — **he is not allowed a scene inside the naag material** (`SUPERNATURAL.md` §2, `OC_STATUS.md`).

---

## 4 · The standing requirement

**One declared OC scene per chapter is his own — his clock, his problem, his engine — from Chapter 17 onward, and every chapter already written is audited against this.** Chapter 17 was repaired on 2026-11-14; the checker’s `FIRST = 17` records that extension. `tools/original_scene_check.py` holds the register (§5), and `check.py --all` runs it.

**It must not be:** a scene where he watches, a scene where the engine is another character's need, or a scene that could be moved to a different character without changing anything.

**It must be:** small, physical, and about a thing rather than a feeling — a page, a tape, a room, a phone, a closed door. **He does not get a monologue and he does not get an interior chapter.** One act, one object, one person who is not a Suri if possible, and one thing that is different at the end of it.

---

## 5 · The register — what exists, and what each one is missing

| Ch | His own scene | Engine | Verdict |
|---|---|---|---|
| 16 | `The Papers` | **1 · the paper** | **His.** He reads a document and decides what to do with it. The nearest thing to a working model. |
| 17 | `The Newsroom` | **1 · the paper** | **His, repaired 2026-11-14.** It was already his in substance — three hours in a car with a house's children asleep behind him while he kills his own wedding bulletin — but **every phone call in it came to him.** He now opens the call with a phone number in Bombay and **a slip of paper out of his own wallet**: three numbers Verma brought him at ten and a fourth line in another hand, an amount, and the word *advance*, dated the night before the wedding. The paper is in his hand for the length of the call. |
| 18 | `Teen Baje, Teesra Kamra` | **1 · the paper** | **His, and written 2026-11-14 on the author's correction.** In the closed third room, he calls Verma to request a missing-person file; the title/opening and dialogue say three, narration says “At four”; the file is requested by eight, and its filing time is unstated. The call was taken out of Aryaman's landing to make this scene possible. |
| 19 | `Attari` | **2 · the work** | **His, and the first full one.** He runs the investigation, and nobody in that episode told him to. |
| 19 P2 | `Bhai Ho Na` | **1 · the paper** | **His, and written the same day.** The scene opens on Pinky and Aryaman and ends on **thirteen missing chairs, a guest who took two of them to Delhi, and a list that is in Vihaan's own pocket** — and he writes it in the margin of the register before he thinks about her. |
| 20 | `The Attari File` | **4 · the errand he invented** | **His.** He claims the file at his father's table and sets a term on Vikram. |
| 20 | `Sameer's Door` | — | **Not Vihaan's scene.** The current Chapter 20 does not put him at Sameer's house; the former corridor/witness staging is superseded by the location repair. |
| 21 | `The Feed Sheet` | **1 · the paper** | **His.** He takes the existing Kumbh feed sheet, routes the unnamed instruction through the London desk under his name, and creates a record that makes the next paper come to him. The own-scene ruling is separate from BF-22: Chapter 21's unaccepted draft marks this as a candidate payment, but the recorded human review date (2026-11-18) is future-dated relative to 2026-11-14, so BF-22 payment remains unverified pending correction/confirmation. |
| 21 | `Vikram's Door` | — | **Not Vihaan's scene.** Pinky's need starts it and sets its errand, so it is a guest scene by §3 even though the snag he files there is his. Ch21's own scene stays `The Feed Sheet`. |
| 21 | `Pinky's Glass` | — | **Not Vihaan's scene.** Canon's B06 appeal-and-vow; his authored tail-beat (Pinky turning to Viju on the stairs) is a guest beat inside it. |
| 22 | `The Six O'Clock Call` | **2 · the work** | **His.** At six in the morning, in his own room, on the standing twice-weekly London call that he dials himself, he reads the renewal page to the last line, finds the fault in it, and holds the signature till the next call. Nobody summoned him, no canon beat needs him, and the decision is his alone; London waits on his word. The diary entry is the act's record, and the unopened folder under the ledger is the room's second object. |
| 22 | `The Hall` | — | **Not Vihaan's scene.** He witnesses canon's hall confrontation; a canon beat that needs a witness does not count (§3). |
| 22 | `Pinky's Door` | — | **Not Vihaan's scene.** Pinky's need starts it and sets its errand, so it is a guest scene by §3 — the report-back half of Ch21's `Vikram's Door`, which this register already reads that way. |
| 23 | `The Signing` | **2 · the work** | **His.** Late at night, in his own room, the servant brings the London courier to his door; he reads the corrected renewal page to the last line, finds the figure single and the month right, signs, scans it into London's evening, and diaries the signing. Nobody summoned him, no canon beat needs him, and the decision is his alone; it closes Chapter 22's hold and opens no new person, figure, place or thread. |
| 23 | `The Mines Office` | — | **Not Vihaan's scene.** He witnesses canon's fraud-and-hug confrontation; a canon beat that needs a witness does not count (§3). |
| 23 | `The Second Meeting` | — | **Not Vihaan's scene.** Canon's unattributed B19 meeting; his authored overhear is a guest beat inside it — he follows, hears, does not look, and files it shut. |
| 24 | `Outside Pinky's Door` | **3 · not-saying** | **His.** Through the fallout he stands guard at his sister's shut door with his back to the wood; he tells her the sehra's truth plain through a finger's width, refuses her pleas gently, carries Vikram's public refusal upstairs unsoftened, and shuts the door by his hand — and stays. Nobody summoned him, no canon beat needs him, and the decision is his alone. |
| 25 | `The Shared Night` | **3 · not-saying** | **His, and staged 2026-11-19 inside canon's B01 night room.** The corridor half is his alone: sleepless with the file turning, back on guard at his sister's door, her door opens, he asks to come in for the second night, asks none of the questions he carries, and sleeps sitting in her chair. Nobody summoned him, no canon beat needs the corridor, and the ask is his decision alone; Ananta's congratulations play inside his sleep as canon's beat. |
| 26 | `Where She Was` | **3 · not-saying** | **His, and staged 2026-11-19 inside canon's B19 dawn-confrontation slot.** He shuts the door himself, asks where she was through the night and states his claim — then takes her temple-half into his file shut without asking the question underneath (BF-118 held past the confrontation); the withheld question is the engine, and the scene would not exist without the husband in it. |
| 26 | `Possible` | — | **Not Vihaan's scene.** Canon's B18 joke-geometry and B19 repair; his chase-and-repair half is authored, but the scene starts with her dream-wake and runs on canon's track with Vikram's burn as its cost. |
| 26 | `Rudra Abhishek` | — | **Not Vihaan's scene.** Canon's B22–B23 ritual; his apple, cover and sitting-down care are guest beats inside it. |
| 27 | `The Call` | **3 · not-saying** | **His, and staged 2026-11-19 inside canon's B13 call.** The passage half is his alone: he carries her home, gives the call its privacy past the curtain, overhears Vikram's certainty through the ajar door unmeant, files it as a lover's belief and not a witness's — and says nothing of it to her. Nobody summoned him, no canon beat needs the passage, and the keeping is his decision alone. |
| 28 | `The Silent File` | **1 · the paper** | **His, and staged 2026-11-19 in the board night's small hours.** Alone in the study, he opens Verma's unanswered report, writes Rishabh's unanswered calls into its margin under the date, weighs the call and holds it, and squares the Ghaziabad paper and leaves it shut. Nobody summoned him, no canon beat needs the desk, and the holding is his decision alone. |
| 28 | `The Mask` | — | **Not Vihaan's scene.** Staged 2026-11-19 as tagged turns inside canon's B11 to satisfy the gate; the author rejected it as manufactured the same night — gate-serving staging is not a scene. Superseded by The Silent File. |
| 28 | `London` | — | **Not Vihaan's scene — Min-ji's, staged 2026-11-19 for BF-113.** The London evening simultaneous with the party midnight: the spend-alert, her arithmetic, her unsent flight east. One quoted line. |
| 28 | `The Leaving` | **1 · the letting-go** | **His and hers, staged 2026-11-19 where canon's cut B12 left the hole.** Their room after the mirror: her thin excuse, his unasked nod, her hand at the door — she must reach the cave, and in our story the leaving happens between husband and wife. His line declared. |
| 29 | `The Clash` | **1 · the intervention** | **His, and staged 2026-11-19 inside canon's B04 clash.** The fight half is his alone: he follows his stormed-out brother past the doors, steps between the fighters, takes the swing on his forearm, and ends it flat-voiced (O075 — answers, never files). Canon gave the brawl no usable cause; the cause is ours (drink, old wounds, the witnessed spin). |
| 29 | `The Landing` | — | **Not Vihaan's scene — Min-ji's, staged 2026-11-19 for BF-113.** The Mumbai night simultaneous with the desh-warning: the eastbound flight lands, unannounced by her own design, one quoted line. No contact with canon's London-exit (separate tracks, §2.8). |
| 29 | `The Valentine` | **2 · the kept promise** | **His, and staged 2026-11-20 between B13's confiding and B14's refusal.** The Ch28 promise kept (his *romance-ka-chance* line at the Valentine's party, Ch28 P2): the night gave him everything except her, so at the veranda he hopes aloud for a gift, takes a kiss when she has none to give, blesses her use of his card gladly (BF-129 fed, purpose unasked), and clasps his prepared pendant at her nape; she softens one breath and wears it into the last-dark. O077-clean — the book's own marriage. |
| 30 | `The Empty Room` | **3 · the unasked question** | **His, and staged 2026-11-20 inside canon's B04 bedroom.** The bedroom half is his alone: he wakes to her empty room, searches the dark floor, hears the water lie, reads the pillow-dent alibi and holds her look one beat past comfort — and the ringing phone cuts off his unasked question. Canon's couch-gag premise is cut (no transferable mouth, §2.4); the search, the filing and the held look are the marriage's (BF-112 costs running). |
| 30 | `The Confession` | **3 · the held-back question** | **His #2, and staged 2026-11-20 as the chapter's last-dark coda.** He empties his Purvi file aloud to his wife — lobby, bulletin-name, too-late love, death-news, Verma file, Rishabh's calls, sister-column, gasped Ananta, glimpses, jealousy — and owns the not-knowing (her, or Purvi seen in her); the identity question rises and he does not ask it, and she stays without answering. Engine 3: the held-back question. |

**After the split of 2026-11-14.** Fourteen chapters are in two files. **This register is kept by chapter, not by file**: a chapter's own scene lives in whichever half carries it — Ch17's in `Part_2` (`The Newsroom`), Ch18's in `Part_2` (`Teen Baje, Teesra Kamra`), Ch19's `Bhai Ho Na` in `Part_2` — and `original_scene_check.py` judges a chapter as the sum of its halves, so a half that does not hold it is not charged for not holding it. The chapter numbers below are the register's own and have never moved; only the file that carries them has.

**Two chapter-level debts this register found, both older than today:** **Chapter 17 has no scene of his at all**, and **Chapter 18 charges its best Vihaan act to another scene's account.**
