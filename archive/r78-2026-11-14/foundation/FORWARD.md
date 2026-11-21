# FORWARD — what each live divergence still owes

> **Owns: the forward duty of the divergences this serial has already made.** `foundation/BUTTERFLY.md`
> is the register: everything that was changed, numbered, with its cost. This file is smaller and it is
> not polite: it holds only the changes that are **still working on the story**, says what each one must
> still produce, and names the chapter it is due in. A row that has nothing left to pay is marked
> `ABSORBED` and stays here as a standing fact of the world, not as a debt.
>
> **Where this came from.** Not invented at this desk. The Soul Land kit's DIVERGENCE_LEDGER.md runs
> exactly this shape — `ID · STATUS · MAG · THREAD · cause · standing effect · horizon · last paid` — under
> its LAW pp (*"canon is ORE, not fate… When our state implies a different outcome than canon, OURS WINS.
> No snap-backs. Paying a row may spawn 0–2 children… No forced canon. No forced divergence. Both
> directions must derive"*), and its checks/divergence_engine.py prints a **forward tick** before writing:
> for each live row, *canon would say…? our state implies…? decide, then record the cause*. The Twin does
> the same job with its canon disposition file, which "records open chains and evidence limits rather than
> claiming full episode viewing or forcing source outcomes". What this workshop had, until 2026-11-13, was a
> register and a backward check (`tools/ripple_check.py`) and nothing that asked **what a change owes the
> next chapter** — which is how eighty-two divergences coexisted with sentences copied out of the show.
>
> **Machine-read** by `tools/divergence_clock.py`, which reads the table below and the chapter footers and
> is wired into `tools/check.py`. Statuses: `ACTIVE` (pressure on the now-story) · `HELD` (pays on its own
> horizon, do not force it) · `ABSORBED` (paid; the world is simply built this way now). Magnitude:
> `dust` (a word) · `current` (a scene changed) · `bend` (an outcome changed) · `break` (a canon event is now
> impossible or replaced — **do not resurrect it**) · `storm` (wholly original, no canon anchor, and it pays
> on *its* horizon, never canon's).

---

## The live rows

| ID | STATUS | MAG | THREAD | cause | standing effect | horizon | last paid |
|---|---|---|---|---|---|---|---|
| BF-13 | ACTIVE | bend | the-dance | he crossed a floor of three hundred people and held his hand out after Aryaman turned his shoulder | the pair is public; Parmeet's reading of her character has three hundred witnesses, and every later kindness from Aryaman is read by the house against this | ch20–ch24 | ch10 |
| BF-15 | ACTIVE | bend | the-forged-message | three cousins' joke put her on a terrace where Aryaman stood, and she said *pyaar mujhe bhi hua hai aapse* | Aryaman knows she said it and cannot be un-told; she cannot take it back; the account she gives the house (R-01) is built on this night | when he acts on it | — |
| BF-10 | ACTIVE | current | the-file | he found the two cuts in the minister's file and said so out loud in his father's house | his father keeps him on it; the house knows he can read a tampered story, which is why the pass gets signed by him and why the audit will come looking | when the feed is audited | — |
| BF-22 | ACTIVE | current | kumbh-readiness | Parmeet's question about Pasha, three calls and the readiness, came to the man nobody names things to | he answers with figures; the house starts routing the unnameable work through him | ch20–ch21 | — |
| BF-36 | ACTIVE | bend | the-vans | the route to the Kumbh was given in his own house, on a pass with his signature, with a generator van that never ran | his name is on the movement of the vans; the wreck is a paperwork question with his signature on it | when the vans are questioned | — |
| BF-40 | ACTIVE | bend | the-pass | the Kumbh pass was signed on the feed Kessler bought | Verma's call is his; the file exists and can be pulled by anyone with the standing to ask | when the vans are questioned | — |
| BF-45 | ACTIVE | bend | the-report | a missing-person report for Purvi Arora, filed at three in the afternoon in his own name, the house's name kept off it | the police hold his name against a search for her; the family's cover for that day has a hole in it with his signature | when the report is answered | — |
| BF-35 | HELD | break | the-face | the thing that came down the stairs with the promise, the laugh and the knife wore his face while he was on the Ring Road | canon's accusation now points at a man with an alibi the show never had to build; the page never says what wore it | the confrontation — far, and not to be forced | — |
| BF-48 | ACTIVE | current | the-door | the man with the camera case in her doorway is named, and bows, and offers to carry half her files | she has a reason to be wrong about him; every later kindness reads against that door | ch20+ | ch19 |
| BF-56 | ACTIVE | current | the-report-said | the report was said out loud in front of her instead of being left on a desk | she knows what is being done for her, which she is not supposed to know, and she cannot unread it | when the pair next share a scene | — |
| BF-81 | ACTIVE | current | his-voice | he is not written silent: the heart recognises its owner and the head does not | he talks — **twenty-two lines in Chapter 19 and ten in Chapter 10**, counted by `tools/oc_check.py` on the swept files on 2026-11-14 (the row said twenty and eight; eight stopped being true the day Chapter 10 got its lane scene back, and a row that counts lines ages at the speed of the page it counts) — jealous of Vikram without knowing why, and never explained; `tools/oc_check.py` prints the number under *lines the page gives him* | every chapter | ch19 |
| BF-82 | WITHDRAWN | bend | the-account | the account was made the fix for the pasted sentence; his word 2026-11-13 undid it — a label is not a re-derivation | replaced by `BF-84`: the scene is re-written, not re-tagged (`OPEN.md` O044) | — | ch19 |
| BF-83 | ACTIVE | bend | overheard | Pinky at the panel of the small room carrying a price told twice, and Parmeet deciding at two in the morning what a repetition means (re-pointed 2026-11-13, `O044`: it is no longer a love-story told wrong) | being believed buys her being managed: a schedule, a room she is sent from, a protection that is a fence; and nobody in that house slept | ch20 | ch19 |
| BF-84 | ACTIVE | break | no-name | Aryaman is struck out of her history in every register — narration, her own mouth, a lie she tells, another character's summary — and the mirror scene in Chapter 19 and the sisters' scene in Chapter 15 are re-derived without him: the hate keeps the house for its object and her cover is money and whichever son is offered | nine scenes in seven chapters still name him beside her, and `BF-13`/`BF-15` are built on him being the man — `OPEN.md` O045 holds that, this row does not decide it | ch20 | ch19 |
| BF-85 | ACTIVE | break | consequence-not-volume | the pair stops being a reaction added to a pasted canon scene and becomes the fact the scene has to be re-derived around, beginning with the midnight room | every kindness of his is now a risk to her cover, and eighteen chapters still have him present without the plot running through him (`O046`) | ch20 | ch19 |
| BF-86 | ACTIVE | break | substitution | where the show pairs her with a man, ours pairs her with Vihaan — same words, same timecode, same place; the name changes, the sentence survives | the pairing machinery across the book is now governed by one rule and cannot be repaired by deletion; Ch4, Ch6, Ch8, Ch9, Ch13, Ch14, Ch16 still hold the old grammar in other registers | standing | ch19 |
| BF-87 | ACTIVE | break | money-not-name | the change reaches the scene through his wealth and staff (a room ordered on a phone, a lock paid for at eight at night, a register page) instead of through a substituted word | the house cannot move her without him and must work around that; two facts now sit in front of her that her mission does not explain | ch20 | ch19 |
| BF-89 | ACTIVE | current | the-book | the scientist's child and the metal-covered book are put in the ruined room together, so the season's evidence enters the house on the first night | nothing may destroy, lose, give away or explain the book before it is asked for; the locker is a second thing and stays shut in the bank; Chapter 11's claim about the book now has a floor | when the book is next asked for | ch1 |
| BF-90 | ACTIVE | bend | the-bulletin | the same bulletin that gives Aryaman his third award reads the Mahakumbh coverage's name out over the Aroras' television, and nobody there has heard it before | she carries a name heard on a screen into every later sight of him; Baljeet's fault note and the fourth-floor drawer are the house's half; the surname is held until she asks, and the first name was given at half past one in a lobby and noticed | when she asks the surname | ch4 |
| BF-88 | ACTIVE | break | pressure-not-size | the season's money is one ₹40 lakh figure owed twice, and the family's whole dig lives inside a licence in Vihaan's name | the plot's machinery now runs through his papers in every chapter (Ch16 warrant, Ch17 trade, Ch18 vans, Ch19 sheds and her land), and his kindnesses become evidence | ch20 | ch18, ch19 |
| BF-76 | ABSORBED | break | the-score | canon's romantic background music for Aryaman and Purvi is struck out and the opening forty seconds become the pair's | no soft cue attaches to that pairing anywhere in this book, ever; when the two of them are alone the room's own music stops | standing | ch1 |
| BF-01 | ABSORBED | break | the-child | the Suri child canon only mentions is shown: the cake, the candle, the name, the man with the moustache lifting him out of the cot | he is Vihaan, and the family's reason for everything in Episode 1 is a person rather than a sentence | standing | — |
| BF-02 | ABSORBED | break | he-exists | a son of that house comes home from London and the house goes quiet around him | every scene in this serial is one man wider than the show's; the ledger was built on this row | standing | — |
| BF-53 | ABSORBED | bend | the-lobby | the pair meet at half past one in the channel lobby, three episodes before canon brings them together; the 03:09 steps were handed back to the sisters line for line | the priced water, the list, the name with the surname left off, the car at two | standing | ch4 |
| BF-47 | ABSORBED | bend | the-return | canon's returning brother is this serial's man, six months gone, whose going Chapter 18 wrote | *Karan ki shaadi ho gayi aur tu gayab raha* is said to Vihaan, and the house's guilt has an address | standing | — |
| BF-92 | ACTIVE | bend | the-fifth-stop | the building's lift contract bills five stops against four floors, and he reads it in the accounts office at half past one (Ch9) | an engineer at nine, twenty-four years of signed visits, and the name the servicing company is registered to; the basement is a paper trail before it is a room | ch17 | ch9 |
**Twenty-six rows**, and the count is the tool's rather than this file's: `tools/divergence_clock.py`, re-run on 2026-11-14, prints `forward ledger: 26 rows — 19 ACTIVE · 1 HELD · 5 ABSORBED · size: bend 11 break 9 current 6`, and `the register holds 92 rows and 28 of them are cited in any chapter footer`. The ones not here have nothing outstanding — a restored name, a
moved object, a scene written and spent. `tools/divergence_clock.py` prints that count on every run and
reds any row here whose number is not in the register, and any chapter footer that cites a number which is
not.

## The rules of this file

1. **A row is not closed by being written here.** It closes when a chapter pays it, and the chapter's footer
   carries the number: a footer that cites `BF-36` is the receipt the tool reads (`last paid` is harvested
   from the footers, and a claim in this table that no footer supports is red).
2. **Paying a row may spawn a child.** A consequence that becomes a standing change gets its own number in
   `foundation/BUTTERFLY.md`, and then, if it still has work to do, a row here. That is how BF-82 → BF-83
   happened: a private line became a public fact the moment an ear moved into the corridor. And how BF-82 came to be **withdrawn** the next sitting — the row
   survived and the prose it was a ruling on did not, which is the one use a kept number has.
3. **`break` means dead.** A canon event this serial has made impossible is not revived because the episode
   had it. Re-derive what the causes now produce.
4. **`HELD` is not a to-do.** It pays on its own horizon. Manufacturing its payment early is the same
   weakness as forcing a divergence, wearing the opposite face.
5. **Before writing a chapter:** read the rows due in it. That list is the forward tick, and
   `tools/divergence_clock.py` prints it.
