# RIPPLE — every canon fact that this serial has changed, and what the prose must now say

**Owns: the propagation of the divergences. `foundation/BUTTERFLY.md` records *what was changed*; this file records *everything else that had to change because of it*, and `tools/ripple_check.py` makes a chapter prove it has read both. It exists because of the author's words of 2026-11-12: *"it's your mistake pasting canon, you need to add butterfly effects and others all things, that you don't do, core problem is that you paste canon."***

---

## 1 · The fault this file closes

A chapter of this workshop is written from two sources: the **show** (the episode beat files (`canon/E09_BEATS.md` and its siblings), `canon/sources/`) and the **serial's own rulings** (`OPEN.md`, `foundation/`). For nineteen chapters the second source has been applied at the **set-pieces** — the dance moves, the score is cut, the message is forged — and the first source has been copied **whole** into the sentences between them. The result is a book that contradicts itself at the level of a character's stated history, which is where a daily soap keeps all of its load-bearing facts.

**Chapter 19 is the case that caught it.** `canon/E09_BEATS.md` B20 gives the naagin, alone at a mirror, her own account of herself: *"Aryaman se pyaar Purvi ne kiya tha. Ahana Aryaman se sirf nafrat karti hai."* The chapter wrote that into prose on 2026-11-12 with the ripple unrun — while `OPEN.md` **O016** had said, since 2026-11-11, in the author's own confirmed words: **"Purvi loves Vihaan."** One sentence of canon pasted over one standing ruling of the fan fiction. Both were in the workshop. Nothing counted.

## 2 · The law

1. **A line does not enter prose from a beat file until every divergence whose subject appears in it has been read.** The subject can be a person, a feeling, an object, a place, or who knows what.
2. **Verbatim canon is allowed, and it must be owned.** If a show line appears in a chapter's scenes, the footer carries it on a `PASTED:` line with a verdict: `same` (nothing here contradicts it), `changed (BF-nn)` (the wording is this serial's), or `account (R-nn)` (the show's words stay in the mouth, and the chapter shows them being *used* rather than being true).
3. **A rule that touches a chapter must be owned on that chapter's footer**: `RIPPLED: R-01 (why) · R-03 (why)`. A footer with no `RIPPLED:` line is not a clean chapter; it is an unaudited one, and `tools/ripple_check.py` says so.
4. **A new divergence that changes a *stated fact* needs a rule here in the same pass that registers it in the ledger.** A divergence that only adds a scene does not.
5. **Why the check reads the beat files and not the caption track** — measured, not assumed: **512** of the show's lines are used verbatim in the nineteen chapters' prose and every one of them is present in `canon/E09_BEATS.md` and its siblings, while **zero** are matchable against the raw track in `captions` (which is Devanagari; the prose is romanised, and the transliteration happens in the beat file). The beat files are therefore the only road the show's words take into this book, so a verdict on a line found there covers every way it can arrive. A chapter drafted from a recap instead would show up as pastes the registry has never seen, and the corpus is widened then.

6. **What this file is not, said plainly.** It is not a full viewing of twenty-odd episodes: the rules cover what the
   beat ledgers record, and the ledgers are sampled — the same limit The Twin puts in writing at the head of its canon
   disposition file, where it records that selected captions and official features were reviewed and no complete episode,
   continuous clip or audio was. Where a rule's reach is not measured it says so, and `tools/ripple_check.py` prints how
   many ledger entries are still untriaged against the rules (86 as of 2026-11-14) instead of pretending the number
   is zero. **No rule here may be used to force a canon outcome back onto the page** — the house law in
   `Sara/AGENT-OPERATING-PROFILE.md` §6 outranks every row in §3 below: canon survives through its *causes*, not its
   results; a changed cause is not repaired by making a character late, blind or irrational; **a public fact must produce
   public consequences**, which is why Chapter 19's private account now reaches Pinky at a door panel and changes what
   Parmeet decides, and why an invented mechanism may not be added to glue a broken cause back together.
7. **A rule that supersedes a fact has a forward duty as well as a backward one, and the forward duty lives in `foundation/FORWARD.md`.** Reading the ledger before copying a line is only half the job: the other half is knowing what each divergence still owes the story. The row that owns a chapter's debt says its magnitude, its horizon and the chapter that last paid it, and `tools/divergence_clock.py` reads it. Borrowed from the Soul Land kit's DIVERGENCE_LEDGER.md and its divergence engine, whose rule is worth keeping in these words — *no forced canon, no forced divergence, both directions must derive*.
8. **Magnitude, borrowed from the Soul Land kit's ledger and used here by hand.** Each rule states the size of what it
   moves — dust, current, bend — and how far ahead it runs. A rule that claims to change everything is a rule nobody
   can obey, and an effect with no cause on the page is a claim, not a butterfly.

## 3 · The rules

Machine-read by `tools/ripple_check.py` from the `superseded:` / `allow:` fields on each row below. A hit is RED unless the chapter footer owns that rule id.

**R-01 · Aryaman is not in her love story, in any mouth: the slot is Vihaan's, by substitution, never by deletion.** `O016`; `BF-13`, `BF-15`, `BF-76`, `BF-82` (withdrawn), `BF-84`; the author's ruling of 2026-11-13
- **Reach:** a break, and it is the book's busiest one. It runs the length of the book: her love, the pair, and every sentence anyone uses to describe either.
- **Superseded:** every register of the grammar in which Purvi's love is *Aryaman's* — as narration's fact, as her own account of herself, as a lie she tells the house, as another character's summary of her, and as an accusation. There is no licence for it, including the licence of showing it being used. **But the fix is not an emptying, and this rule was misread that way for one whole sitting.** The show's sentence stands in this book with its second word changed: *"Vihaan se pyaar Purvi ne kiya tha. Ahana Vihaan se sirf nafrat karti hai."* The slot transfers wholesale — his sentence, his timecode, his place in the episode, our man in it — and that is what a butterfly effect *is*. A canon line with the name deleted out of it is a canon scene with a hole in it, and it reads as one. The author, twice on 2026-11-13: *"there should never mention of Aryaman…you just need to replace vihaan instead of aryman due to everything, but you do but not this."* What the house may be told, and what it already believes on its own, is still money and a son.
- **What the serial says instead:** she loved the man in that house who never looked at her, and the book's pair is **Vihaan's** (`OPEN.md` O016, O029, O033). Canon's Aryaman material survives as *specific events*: the forged message that put *"pyaar mujhe bhi hua hai aapse"* out of her mouth in front of him (`BF-15`); the shoulder turned at the *jodi* game (`BF-13`); her respect for a boss who is rude about love (`Chapter 13`, footer note 3). An event is not a history.
- **superseded:** `Aryaman se pyaar|pyaar (mujhe )?(bhi )?hua hai aapse[^.]{0,40}Purvi|Purvi[^.]{0,50}Aryaman[^.]{0,25}(pyaar|love|chaah|ishq)|Aryaman[^.]{0,25}(pyaar|love|chaah|ishq)[^.]{0,30}Purvi|in love with Aryaman|loved Aryaman|Aryaman ka pyaar|pyaar Aryaman ko|Aryaman ko kiya tha|Aryaman se kiya tha|still loves Aryaman|loves Aryaman|loves him still|Purvi ne kiya tha`
- **allow:** `BF-15|forged|jodi` — the two canon events this rule still owes a decision to (see §4 and `OPEN.md` O045), and nothing else. A phrase about how a line is spoken is not an escape.

**R-02 · The pull is played, never explained.** `O033`, `O034`; `canon/SUPERNATURAL.md` §2 rule 5; `BF-81`
- **Reach:** a current. Every shared scene until the pull is named; nothing outside them.
- **Superseded:** narration that resolves the recognition into knowledge — *he knows her*, *his heart tells him she is the one*, *she was made for him* — or that lets the naag's side of it be *thought* by the man.
- **superseded:** `his heart (knows|knew|recogni[sz]|tells him)|he knows her face|he recognised her|he recognized her|the one (he|who) was made for|she is his|his naagrani|uski naagrani`
- **allow:** `does not know|he does not understand|no reason|not the reason`

**R-03 · Nobody may write him out of his own scenes.** `O040`; `foundation/OC_PRESENCE.md` law 9
- **Reach:** a dust, chapter by chapter. It moves who talks in a room, not what the room is.
- Owned by `tools/oc_check.py` OC9 and OC10, which are the enforcement. Recorded here so a chapter does not treat a passed voice check as a passed ripple check: `O040` exists because the *fence* on the pull was read as a *ban* on speech.
- **superseded:** `(says|speaks|answers|tells) nothing to (anybody|anyone)|he keeps it to himself and says nothing`
- **allow:** `SILENT:`

**R-04 · No romantic score between Aryaman and Purvi.** `BF-76`; `canon/SOUND_AND_SCREEN.md` §9.4
- **Reach:** a dust, absolute. It forbids one colour of sentence and asks nothing of plot.
- Owned by `tools/score_check.py` (SC4, SC5). Recorded here because the cut was made in the **music** file and in `TITLES_SEQUENCE.md` and never propagated into the beat files, which is how R-01 came to be pasted at all.
- **superseded:** `Aryaman[^.]{0,40}(theme|music|score)[^.]{0,30}(soft|romantic|love)|romantic music[^.]{0,40}Aryaman`
- **allow:** `nothing of the score's own|no romantic cue|is struck out|gets no romantic music`

## 3b · The machine lines

Read literally by `tools/ripple_check.py`, one regex per line, in this order: `rule | kind | pattern`. A chapter may own a hit by naming the rule on a footer `RIPPLED:` line.

- `R-01 | superseded | (?:Aryaman|Arya)[^.]{0,30}\b(pyaar|love|ishq)\b|\b(pyaar|love|ishq)\b[^.]{0,40}\bAryaman\b|in love with Aryaman|loved Aryaman`
- `R-01 | allow | BF-15|forged|jodi|O045`
- `R-02 | superseded | his heart (?:knows|knew|recogni[sz]\w*|tells him)|he (?:knows|knew) her face|(?:recogni[sz]ed|recogni[sz]es) her|the one (?:who|that) (?:was|is) made for|(?:his|her) naagrani\b|she was made for him`
- `R-02 | allow | does not know|do(?:es)? not understand|not the reason|no reason|without knowing|and does not say`
- `R-03 | superseded | \b(?:he|Vihaan)\b[^.]{0,30}?\b(?:says|speaks|tells)\b[^.]{0,14}?nothing to (?:anybody|anyone)`
- `R-03 | allow | SILENT:`
- `R-04 | superseded | Aryaman[^.]{0,45}\b(?:theme|music|score|cue)\b[^.]{0,35}(?:romantic|soft|love)|romantic (?:music|cue|theme)[^.]{0,45}Aryaman`
- `R-04 | allow | nothing of the score's own|no romantic cue|is struck out|gets no romantic music|never romantic`

## 4 · The state of it, and the backlog that is still owed

- **Every chapter declares itself.** All nineteen footers carry a `RIPPLED:` line, and `RP5` makes it impossible to be clean simply because nobody looked: a chapter names the rules it touches or declares `none`. Seventeen declare `none`; the two that do not are Chapter 19 (R-01 to R-04, with the show's spine line owned on its `PASTED:` key) and Chapter 10 (whose sideboard beat carried the same muzzle clause Chapter 19 had, and where he now speaks).
- **What the registry does not do, honestly:** four rules against **91** live ledger entries (86 of them still untriaged, and the tool prints that number on every run — this line said 83 and 79 and 78 until the sweep of 2026-11-14 read it back against `tools/ripple_check.py`, which is the only reason to believe a number like this). So the gap is visible instead of implied. Those 86 are triaged only in this sense: the four rules cover the divergences that change a *stated fact the show also states*, and nobody has read the other entries line by line against the beat files. That reading is owed, and it is done per chapter as the style pass reaches it.
- **The forward duty, which is the one that matters:** a new `BF` row that changes what a character feels, knows, owns, or has lived through must either add a rule to §3b in the same pass or say on the row that no canon sentence depends on it. Then no future chapter can copy the show's version of a fact this serial has already changed.
