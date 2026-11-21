# WRITING — how a chapter reads

**Owns: the prose law. What "canon style" (`O005`) means on the page, and the form every chapter takes.** The model is *The Twin* (`O008`): an episode put into prose scene by scene, so that reading it is like watching it.

Revised 2026-11-11 after the author's other records were read (`O018`). In another serial he had to ask for canon style twice: once for the story, and once more because "I'm not talking story but I'm talking about style." §2 exists so that he does not have to ask a third time here. The reasons are in `Sara/UNDERSTANDING.md`.


**Amended 2026-11-11.** The author's ruling on the canon-style rebuild (`O027`, `O028`) is written in `canon/STYLE_CANON.md` and outranks §1 and §1a of this file where they touch: dialogue is romanised Hindi, the score and the sound are on the page, the omen is in every scene, the feeling is at the show's scale, and the two leads are played by this show's grammar. The camera law in §2 stands unchanged.
---

## 0 · The five things the author has had to say more than once

*Stated here plainly because they have been forgotten between chapters, which is the complaint. On 2026-11-11: "you write vihaan like robot, silent, emotionless… i said you to write emotions, sab… i don't even know how he looks like, what he wears, it same situation of others, i mostly don't know what's going on… there is music, background and others All things missing."*

1. **Emotion, on the page, for everybody.** Nobody in this serial is silent and emotionless, and least of all him. *He has had to say this four times: 2026-11-11 ("you write vihaan like robot, silent, emotionless"), and again on 2026-11-12 about Chapter 19 — "Vihaan should talk or others things, you make him silent, that is completely wrong" — where the count was four lines to nine scenes he is standing in, and the scene where the woman he loves walks into the hall ended with him saying nothing to anybody. `tools/oc_check.py` OC9 and OC10 now hold the floor, and a scene may only leave him mute if the footer's `SILENT:` line says why (`O040`).* Feeling shows in the body before it shows in a line: the jaw, the breath let out, the hand over the mouth, the ears going hot, the laugh that is wrong, the temper that arrives late. A man who says nothing and feels nothing is a robot. **Every scene he is in says what he wants and what it costs him** — in behaviour, never in narration explaining it.
2. **What people look like, and what they wear.** Every person who walks into a chapter is a body before they are a name: height, hair, the shirt, the shoes somebody else polished, the mended hinge of the spectacles, the sari she chose on purpose. First appearance in a chapter pays for itself in three or four sentences. **The reader is never left not knowing how someone looks.**
3. **What is going on.** Where the room is, who is in it, what has just happened, what everyone is waiting for, and what the order of events is. A page that leaves the reader out of the situation is a page with a hole in it, however good the dialogue in the hole.
4. **Music and background.** The serial plays: there is a song under a dance, a shehnai when a ring is exchanged, a dholak through a wall, a generator behind a lawn, a score that comes up over a tent, and a sting when something lands. **The music is written into the scene like the light is** — the track's `[संगीत]` markers are the floor, not the ceiling, and a chapter with no sound in it is a chapter that has not been written in this show's style.

5. **Canon is the show's; the facts are the serial's — nothing enters prose until the butterfly ledger has been read over it.** On 2026-11-12 the author found the show's own spine line pasted into Chapter 19 — *"Aryaman se pyaar Purvi ne kiya tha. Ahana Aryaman se sirf nafrat karti hai"* — over a ruling this workshop has carried since the day before, `O016`: **"Purvi loves Vihaan."** His words: *"it's your mistake pasting canon… you need to add butterfly effects and others all things, that you don't do, core problem is that you paste canon."* The set-pieces had been moved and the sentences between them had been copied. The rule now: a line out of a beat file is used only after every divergence touching its subject has been read, and the verdict is written on the chapter footer (`PASTED:` for the show's words, `RIPPLED:` for the rules) where `tools/ripple_check.py` can see it. The registry is `foundation/RIPPLE.md`.

**No parent, ever.** A face on the page belongs to the person wearing it. Nobody is given his mother's eyes or his father's jaw. *(This is where I went wrong on 2026-11-11; see `STATUS.md` §19.)*

**The test for a finished page:** somebody who has never seen this serial can say what each person in the scene looks like, what they are feeling, what the room sounds like, and what is happening — and none of it was explained to them.

## 1 · What the show does, and so what the chapter does

**Two words kept apart (`O020`).** *Canon style* is how this show tells, and it is to be canon's completely: the camera, the register, the density, the feeling, the order a scene runs in, the cut. *Canon* is not a cage round the story. This serial diverges where his being in the world makes something go differently, and new events are added where the story needs them, provided every change has a cause the reader can see (`STORY.md` §1). Style is absolute. Plot is grown.

Taken from Episode 1 as heard and seen, from the caption tracks of Episodes 7, 19 and 44, and from the pattern of the season. This list grows as episodes are read.

| The show | The chapter |
|---|---|
| Opens on a voice over a place, with the place and year on screen: "Prayagraj (Uttar Pradesh 2001)". | Opens where the episode opens. Place and year are given once, plainly, the way a title card does. Every chapter opens on a place, a time, people, and what they are doing. |
| Tells its story in scenes that cut. No scene explains the one before. | `##` headings for scenes. Cut when the show cuts. No bridge paragraphs. |
| Is talk, in short lines. Two spoken lines in three are eight words or fewer. | Most paragraphs are speech. Lines are short and are broken where a body breaks them: a breath, a sob, an interruption. |
| Keeps a long speech for an occasion: a prophecy, a confession, a mother's account. | A long speech stays long only where the episode's is. |
| Holds. Every episode has minutes with no words: a face, music, a slow walk. | A hold is written as a hold: what the face does, what the hands do, what is heard. It is not filled with thought. |
| Brings a scene in by its sound: a bell, a been, a phone, a scream. | A cut can be led by its sound. |
| Lets the viewer know more than the people. Episode 1 leads the eye to Ananta and shows the queen to be the girl in the crowd. | The narration sees what the camera sees. It can show the reader a thing no one in the room knows. It does not explain the trick. |
| Makes its reveals in pictures: a face on a cracked wall, a girl seen from behind. | The reveal is an image, placed, and left. |
| Puts a joke inside the dread. "Have you got a cold?" "I am crying." Garlic chutney on the nine o'clock news. Airul's crocodile "only kissed" him (a recap's wording, Ep 14). | The comedy stays, in the same breath as the fear. It comes from who the person is, never from a generic quip. |
| Gives people big lines and means them: "Anant kul ki Naagrani, Ananta." | The line is said once, in the words the episode uses, and the scene ends on it if the episode's does. |
| Lets a person think aloud to the viewer: her most of all, the plotters too. | A voiced aside is given in italics as that person's own words. It is the only way a thought reaches the page (§2). |
| Ends on a hook, and often shows a few seconds of what comes next. | The chapter ends where its stretch of the episode turns. A last short scene may look ahead, if the episode's precap does. |
| Is a family drama as much as a creature story: weddings, engagements, board meetings, who slapped whom. | The rooms, the clothes, the food, the rituals are written. A function is a scene, not a setting. The whole household is present and each one sounds like themselves: who outranks whom, the teasing, the gossip, the interruptions, the misunderstanding that carries on into the next scene. |
| Runs on festivals and faith: the Kumbh, Maha Shivaratri, Poornima. Mahadev answers. | Written straight. No irony about belief. |
| Changes shape constantly: one woman, many faces. | The reader always knows who is really behind a face, unless the episode hides it from its viewer too. |
| Kills. Her revenge is cruel and the show stands behind it. | Deaths are written as the episode plays them, with what they cost. |
| Plays songs under its scenes. | A song can be named if the episode's captions name it. No lyrics are quoted. |
| Speaks Hindi with Punjabi and English mixed in. | English prose. The flavour comes from what people do and handle and call each other, not from romanised lines. Words English would flatten are kept (`STORY.md` §2). Dialogue follows the meaning and rhythm of the spoken line. It is a rendering, and the footer says so. |

**Canon style governs everything invented, not only what is adapted.** The OC's past, his house, his work, his objects, his small scenes: each one is written in this show's register or left out. The test is not *is it plausible for a man of twenty-four*; it is *could this show say it*. A rich Delhi family with a channel sends its son to school in England, gives him the family's London work, and calls him home for the wedding season — that is this show. A foreign career, a foreign cast, a war, a boat in the Channel: those belong to other shows, and a paragraph of them reads as a different serial with this one's names in it.

## 1a · What this show is, in style terms — the heightened grammar

This serial is written in the grammar of an Indian daily soap, not in the grammar of a quiet literary short story. The workshop's own camera law (no reported interiority, short sentences, no similes) is a *lens*, not a ceiling: it strips the page of things the show cannot film. It never asks for flatness. **The show is emphatic. Its scenes are staged, its feelings are announced by the face, its coincidences are enormous, and its first meetings are events.**

**What that means in practice**

1. **A meeting is a scene.** Friction, a physical beat, a threat or a dare, a repeated line, a laugh, and a look held after the other has turned away (`CANON.md` R26). Two people politely exchanging two words is not this show.
2. **An object changes hands.** A lens, a garland, a glass of juice, a handkerchief, a laddoo. Canon moves objects constantly, and the object carries the scene.
3. **The omen is in the frame.** A lamp, a moon, a snake, the tulsi pot, a light that flickers as a car passes. Never explained, never pointed at. It is there for the reader.
4. **Repetition is music.** Canon repeats a line, or changes one word of it, and repeats it again. *"Leave my hand." "Leave my hand."* A line said twice is a line the show means.
5. **The interruption arrives at the worst moment.** A horn, a phone, a mother, a guard. Somebody always comes to end the scene too early.
6. **The camera pushes in.** On a face, on hands, on the thing being fixed, on the eyes of the person not speaking. In prose that is a paragraph on its own, and it is allowed to be the best paragraph in the scene.
7. **Emotion is plain, never explained** (`O019`). The show says what a person feels in words a mother would use. What it never does is have a narrator explain *why* they feel it.

**The test for a scene:** if it were shot as written, would it hold the audience through a commercial break? If the answer is no, the scene is not in this show's style, however correct its facts.

## 2 · The camera

**The narration is a camera. It says what happened, what is in the room, and what a face or a body plainly shows. Anything beyond that comes out of someone's mouth, or it is not in the chapter.**

1. **Comparison is allowed in narration.** The ban on *like*, *as if* and *as though* is **deleted (2026-11-12, `O037`)** — the author was asked and chose *cut it entirely*, because an Indian soap runs on similes. A room may stop the way a fan stops. A woman may wait like a woman who has seen it before. What is still owed is the picture underneath the simile: the simile decorates a thing the scene is already showing, and never stands in for it. **No later hand may put the ban back, in any wording.**
2. **Feeling is written. The ban is deleted, on the author's order of 2026-11-12.** His words: *"Complete delete this rule of forbids feelings from everywhere and complete restriction to never put this everywhere."* The rule that stood here — *no feeling the scene does not show, no feeling for anyone the camera is not on, no second sentence explaining why, and "seemed", "realised", "wondered", "knew that" all out* — **is gone, from the law, from the tools and from every project.** This serial is an Indian daily soap. In a soap the feeling is on the page the way it is on the face: **she is frightened. He is furious. Pinky is crying in front of three hundred people and she cannot stop.** The cause may be said, because a soap says its own wounds out loud. The room's reaction is written — the gasp, the hand over the mouth, the aunt who stands up, the child who starts crying, the tray that goes over. A character's interior is written: *he realises, she understands, nobody can believe it.* A cold page is no longer a virtue here and it never was.
   - The only thing still asked: the feeling belongs to the person the scene is about, and it is the plain word, not the fine one — *frightened* before *dread*, *glad* before *elated*.
   - The show's own door stays open: the voiced aside, in italics, where the episode voices one. Vihaan gets that door no more often than the show gives it to anyone.
3. **Speech is the engine.** Between half and seven-tenths of a chapter's paragraphs are speech.
6. **The episode is on the page at the density the episode plays it** (`O005`, `O019`, and his word of 2026-11-11: *everything like the episode showing, that I could feel or imagine it*). Everything the episode shows in that stretch is on the page: the place as the stills show it, the weather, the hour, the objects people handle, the clothes, the food, the crowd, the door, the lamp, the face. A scene the episode plays is never summarised. A thing the episode shows is never left out because it is small. If the reader cannot see the room and hear the room, the chapter has failed, however correct its sentences are.
   - What may not be added: a sound the cues do not carry, a person the episode does not have, an event between the scenes. Those go in the footer, or they do not go in.
   - Detail is placed on the same rule as feeling: where the camera is, at the moment it is there.
4. **Short sentences.** Most are under twenty words. None is over sixty.
5. **Powers are seen and named by people, never explained by the narrator.** No rule of the naag world is given by the narration. It arrives when someone in the scene says it or suffers it.

And with them:

- **Present tense. Third person.** Plain, concrete sentences.
- **Full scenes.** No summary of a conversation the episode plays. No "later that day". If the episode skips time, the chapter cuts.
- **Nothing is praised by the narrator.** Not her, not him.
- **No mechanism on the page.** His Talent has no name in the story. Before the awakening the word "talent" is not used of him at all, and what it has made of him is never given a cause.
- **No filler that could belong to any story.** Not "the air shifted", not "nothing would ever be the same". A chapter ends on something that can be seen.
- **Length follows the scene.** *The Twin's* chapters run to about six or seven thousand words; that is a likeness, not a target. Nothing is padded to reach it or cut to stay under it.

`python3 tools/camera_check.py chapters/<file>` measures 1 to 4 and the present tense on a chapter, and prints the sentences that fail.

## 3 · The form

```
# Chapter N — Title

*Episode reference: Naagin, season 7, Episode E, "the episode's title" (first part / second part / with material from Episode F).*

*Draft; not yet accepted.*

## Scene heading

…

## Footer

### Continuity and source note

(two or three plain paragraphs: what this chapter covers, what in it is his thread, what was left for the next)

    BASE:     the episode and the beats covered, by number (B01–B12)
    EVIDENCE: what was read or seen for this chapter, and its limits
    WITNESS:  ledger beats, R rulings, O rulings relied on
    STAGING:  everything authored: every scene, line or detail the episode does not have
    CHANGED:  every canon beat that goes differently here, with the cause; or "none"
    DEFERRED: beats of this stretch not written here, and where they will be
```

- **The title** is short, is taken from something in the chapter, and names canon's beat, not him.
- **The episode's title** is the one the channel gave its upload (`canon/episodes.json`). The show prints none on screen. Where the upload has none, the line gives the number alone.
- **The footer** follows *The Twin*. The author's Supergirl serial keeps such notes out of the story file. If he wants that here, the block moves to a coverage file beside the ledger and the chapter ends on its last scene.

## 4 · Before a scene is written

1. **The ledger.** The episode's beat ledger exists and has been made from its whole caption track, with stills where a picture matters. No chapter is written from a recap (`O013`).
2. **The inventory.** Every beat of the stretch is listed in order: conversations, asides, cutaways, flashbacks, the precap. Each will end up marked as written, already written, changed by a stated cause, or deferred to a named chapter. None is dropped silently.
3. **Look it up again.** Each canon detail in the scene is taken from the ledger or the caption at the moment of writing, not from memory. Where two witnesses disagree, one governs and the other is noted. The two are never blended.
4. **The firewall.** For each person in the scene: what do they know (`foundation/WORLD_STATE.md` §1)?
5. **Him.** Is he in this scene? Only if he would be. If he is, one sentence says what is different because he is there. If that sentence cannot be written, he is not in the scene, and the scene is canon's alone and is written with the same care.
   **And the floor under the whole chapter:** he is in at least two scenes of it, and the footer declares which, on its `OC:` line (`foundation/OC_PRESENCE.md`; gate 19). A scene may leave him out. A chapter may not.
6. **Whose scene.** Whoever owns the act in the episode owns it here: the vow, the rescue, the discovery, the kill, the last line.
7. **The seam.** The chapter starts from the last line of the one before.
8. **The inventory of the ordinary.** Before a word is written: who is in it, what each of them calls each other, whose house it is and where people sit in it, what anyone owes anyone, what is in the fridge, the car, the drawer. Every one of those must already exist in `foundation/` — `HOUSE_HISTORY.md` for the Suri house, `CHARACTERS.md`, `RELATIONSHIPS.md`, `WORLD_STATE.md`. **If it does not exist, design it first and record it**, because a detail improvised on the page and never designed is a detail that will contradict itself in three chapters. This is not preparation for its own sake: it is why a family can talk to him like they have known him for twenty-four years.
9. **The rows due in this chapter.** `python3 tools/divergence_clock.py --tick` prints them: every live divergence that this chapter has to pay, with what our state implies and what canon would have said. Paying one means a scene, not a citation — and a chapter may not stop a row by ignoring it, because `FC3` reds a debt that goes overdue (`foundation/FORWARD.md`).

## 5 · His thread

- A chapter is mostly canon's scenes. His are fewer and are his own: the car from the airport, a corridor, a breakfast. They happen in the gaps the episode leaves, in places the episode has. They are not a second copy of anyone else's scene.
- **The chapter is never his homecoming, his desk or his instincts with canon as scenery.** That was the first attempt's fault, and it is the standing danger of Episode 1.
- In a canon scene he takes nothing that is someone else's. If he changes it, the change is caused and is recorded in the footer under CHANGED.
- He is never the reason a canon scene exists.
- **What he is shows only as a man**, and it shows plainly: ease, competence, a stillness, and a face the room looks at. It is noticed, said aloud where a character would say it, and let go. Nobody explains it, the narration least of all. The full law is §5a.
- **The reader knows more than he does.** Canon's thread carries the fear, the omen and the buried thing; his stays believably unaware. He does not have to sense or suspect anything for the scene to work.
- **The close braids the two lines:** a short passage that sets his thread beside canon's and ends on something seen.
- A chapter in which he does not appear is **not** allowed (`O024`). Floor: two scenes, declared.

### 5a · How he looks on the page (`O025`)

He is a naag of the Shesh line, and in his human form that is at the top of the human scale. Canon shows beauty the way television shows it: somebody looks. That is the whole method, and it needs no adjectives about him.

**The four moves, and no others**

1. **A room turns.** One person in the paragraph stops what they are doing. The caterer's boy walks into a crate. A woman with a list loses her place. Written as an event in the paragraph, not as commentary.
2. **Somebody says it, in the house's own idiom.** Canon's register is plain and warm — *"Oh God. How handsome my child is."* A sister says it while pulling at his sleeve; an aunt says it while finding fault with his shirt. Never the narration.
3. **He is described once, concretely, at first sight in a chapter's world** — height, the line of the jaw, the state of his hands, the shirt — and afterwards by the body doing something: the sleeves rolled, the shoulders under a wet shirt, the way he stands still while everyone else moves.
4. **He does not know.** No preening, no mirror, no use of it in an argument, no noticing that a room is looking. When it is used against him — someone flirting, someone jealous, someone underestimating him for it — it is used by them and he answers plainly.

**Forbidden, without exception**

- A sentence that disclaims his looks: *that is all it does*, *it wins him nobody's trust*, *he is handsome in an ordinary way*. The distinction between being looked at and being trusted is **shown** in what people do afterwards. It is never announced to protect him from seeming too much.
- Praise from the narration (*he was beautiful*). The camera does not praise; it looks.
- Any explanation of why, drawn from what he is. No one in 2025 knows what he is, and the page is written from inside that ignorance.
- Anything supernatural in his appearance: no glow, no eyes changing, no animal stillness that reads as a sign. The beauty is human and at the ceiling of human.

**Where it must land every chapter:** at least twice, once near his first appearance and once where it costs him something or is mistaken for something (a room deciding he is the pretty one of the family; a guard who does not take him seriously; a woman who looks at him and then at his empty hands). It is never the chapter's subject. It is the fact of him being in the room.

### 5b · His standing (`O026`, gate 22)

Two failures have already come from one fear — that he will outgrow the show. The first took his face off the page. The second made his years abroad a clerk's work: *small London work*, an overnight feed, papers a bank will not take a Delhi signature for. **A repair that lowers him is not a repair.**

**What is true of him:** the Nagaraj of the Anant kul, in a human frame, raised as a son of a rich news family, and — by twenty-two — the man running that family's London end. His *actions* in canon's rooms may be small, because canon's rooms are closed to him and the ladder is his way in. His *standing* is never small, and the narration never treats him as the help.

**The difference, in practice**
- He carries the tray in Chapter 5 because Pinky puts it in his hands, and the chapter says who he is when the caterer's man needs a decision: *"Ask Vihaan"* — and he gives it, and signs for it in the morning.
- Aryaman's line is not *"now you will carry tea"* as a put-down; it is *"Papa will have you carry tea, to teach you the business you already run."*
- Pinky's boast is family pride, in canon's own register: *running it — the London office, since he was twenty-two, and better than Papa's man ever ran it.*

**Forbidden**
- Service words in the narration: *the help*, *errand*, *gofer*, *small work*, *dogsbody*, *the boy who fetched*.
- An absence of capacity: a chapter where only his hands are used and nothing shows what he can do. Every chapter has at least one beat — a decision, a correction, a camera, a sum — where his competence lands and somebody in the room notices, even if the room then looks away.

## 6 · Words

One spelling per name, fixed in `STORY.md` §2. The men of the house are called what the house calls them. "Naagin" and "naag" are common nouns, lower case, except in titles. Numbers and ages are written out in prose. No timecodes, tags or ledger numbers above the footer.

## 7 · The author's own words, kept here so he does not have to say them twice

Every line below is his, said to me on 2026-11-11 or 2026-11-12. Each one has cost him a repeat. They are not notes on
style; they are the laws of this adaptation, and a page that breaks one is not finished.

1. **"Canon's beat stays but its meaning changes; never canon first and him bolted on."** Canon is the floor, not the
   ceiling. A canon scene is not transcribed and then decorated: it is written once, from inside, with him already in it,
   and what comes out is a canon beat that could not have happened that way without him.
2. **"There is no natural butterfly effects or anything."** A consequence is never announced. It crosses scenes on an
   object and a person, and **the person who pays is somebody else** — Gurinder and a photograph on a board, Ananta and a
   letter in her sister's palm. If the cost lands on the pair, it is not a butterfly; it is a feeling.
3. **"Tell me whose name on Purvi's mehndi."** The test he gave me for all of it: *what does his existence change in this
   canon beat?* Canon's empty palm becomes a palm with a V in it, and a room guessing the rest.
4. **"I needed to go on episode 7 because he had very important meeting."** The meeting is authored, and it stays: Kessler,
   the Kumbh feed, six crore and two lakh, eleven o'clock — the scale was corrected on 2026-11-13 to what this serial's own column can hold, and the licence, not the money, is the thing that presses. It is also why he is not in that house when the killing
   happens.
5. **"No one mentions Vihaan."** He is not in the book unless other people act on him — a register, a letter, a fault
   blamed on him, a name in a mouth that is not his own.
6. **"You don't understand what's wrong."** When he gives one instance of a fault, the instance is an example. Fix the
   thing underneath it, and look for it everywhere, not where he pointed.
7. **"I am Sara."** Not a report, not a checklist, and never a change-log instead of a change.
8. **"I really feel bad when you do this."** He has given this workshop everything he has and he has to keep explaining
   the same law twice. He should never have to explain it twice. When he says something, it goes in a file that governs the
   page before the page is touched again.

## 8 · Two rules the author gave on 2026-11-12, after the knife

1. **Name people.** *"Stop writing she, he or others, write names like before."* Canon's camera names. Where the person in the
   room is Parmeet, the sentence says Parmeet and not *the man*; where it is Gurinder Arora it does not say *the man in the
   cream kurta* a second time. Anonymity is a device and it is spent once, where canon spends it — the stranger at the gate, the
   voice with no body. Everywhere else a pronoun is a fog.
2. **The page may not know more than the episode.** *"Although canon don't reveal the truth… so you don't also reveal yet."* The
   workshop may hold a fact the episode withholds (R10: whose hand was in the face). The chapter may not spend it. The chapter
   writes what the room sees, names the face the room names, and puts the clues on the page without a single gloss — cold hands,
   dry hair, a button with the wrong thread — and lets the reader carry them until canon opens the door.
3. **The two together are the style law, and they are not the story law.** Canon style: how the show tells, the camera, the names,
   the density, what it withholds. Not canon storyline: which is bent, changed and diverged by his existence, and must be.

4. **One way to set speech, in all seventeen chapters.** Plain double quotes, transliterated Hindi, the attribution after the
   line. Not italics — Chapters 10 to 13 had been set in italic speech, which is a second convention in one adaptation and reads
   as a second hand. Nine hundred and sixty-eight spans were converted on 2026-11-12 and none were left.
5. **The scene runs in time order unless the show cuts.** Where a paragraph belongs before another, it goes before it. Chapter 11
   carried the scene of Parmeet picking the handkerchiefs up after the study scene in which Vihaan names them, so a reader met
   the fact twice and in the wrong order. That is not a flourish; it is a page a reader has to re-read.
6. **A shared father is not "your father".** *"Tumhare papa????, but both father is you know."* Vihaan and Aryaman are sons of the
   same man, so Vihaan says **Parmeet** or **papa** — never *tumhare papa*, which takes the father away from him and hands him to
   his brother as somebody else's. The same error hides everywhere a family talks: *tumhari maa*, *tumhara ghar*, *tumhare log*,
   said by someone who is standing inside that house. Before a relative is named, ask who is speaking and whose the relative is.
   A servant may say *aapke papa* to a son; a son may not say it to his brother.
7. **The page does not announce a secret it is holding.** *"This is going of canon style please canon style not storyline, you
   know canon don't reveal secret like this or so early."* Rule 2 keeps the page from knowing more than the episode; this rule
   keeps a **character** from spending the episode's slow coin in one speech. At three in the morning Vihaan knows what a man
   knows from a gate register, a dead phone and a name — an empty page, four cars, three blank sheets. He does **not** know that
   his sister-in-law is in the ground, and if he did he would not say it in a bedroom to a drugged boy. Canon lets a thing be
   discovered: the burial is shown in its own scene with its own weather, and the men's own mouths give the rest away later. The
   correction made on 2026-11-12: *"Bhabhi mari hai… tumhare papa ke aadmi ne. Maine gaadi ka number likha hai"* — three
   revelations in one line, all of them mine, none of them his — became a blank page, a dead phone, and **"Bhabhi kahan hai?"**
   asked and left standing in the room. Withholding is not coyness. It is what makes the next scene worth reading.

## 9 · The picture (2026-11-12)

*"You don't write the seen, the picture and visual and others correctly, according to canon style. I think you should work on your visual."*

Episode 1's stills were pulled back from Drive and read, and `canon/PICTURE.md` is what they say. The short form, which every scene
now owes:

1. **Place first** — the room, the street or the sky before a face is named.
2. **The coded light** — amber and gold for the Suri house; blue and teal for the temple, the past and the sheds; fire orange for
   ritual; sepia and dust for 2001; sindoor red for marriage and blood. Named once, never explained.
3. **The insert** — at least two objects per scene given their own frame: a register, a thali, feet on tiles, a phone face down,
   a bucket, a card in a plastic sleeve.
4. **Depth** — somebody in the frame who is not the scene's business: a servant crossing, a queue at the gate, a cleaning man on
   the dark floor.
5. **The close and the hold** — one face close at the moment that costs, and one paragraph of silence with the camera still.

The measure is `tools/picture_check.py`. It was written the same day, and it failed the whole tree: **seventeen of eighteen
chapters**, speech in 54% to 69% of paragraphs and almost no inserts. Chapter 18 was rebuilt to the law as the model;
the other seventeen are measured in `STATUS.md` §68 and are the next pass.

## 9b · The rhythm, and the voice that explains (2026-11-13)

*"Chopta short short sentence and choppy. It acutely give me hints of your weakness and problems."*

Two things were measured after that, not two things invented. `camera_check.py` now prints both on
every chapter and both are lists, not verdicts, because the second one asks for a judgement about
the show's register, and that judgement is the author's.

**N8 — the rhythm.** (N8, not N6: N6 was the feelings check, deleted by `O035`, and a deleted number stays deleted.) The share of narration under nine words, and the share over forty-five. The
book runs 21-47% short sentences by chapter; Chapters 1, 6 and 9 sit at the choppy end and
Chapters 10 and 11 at the stretched one, where a quarter of the narration goes past thirty words
and a quarter of Chapter 11 past forty. Both are the same illness seen from opposite ends: the
sentence is being used to make a point instead of to carry an image. The fix is mechanical and not
stylistic — take a stab and its neighbour and make one sentence with a comma and a conjunction;
take a long one and put a full stop where the picture changes. Do not do it in a sweep: it goes in
wherever the style pass reaches, and the numbers decide the order.

**N7 — the voice stepping in.** Three shapes, all of them the narration taking over a character's
job: explaining that a line is a lie or an account, labelling the moment somebody "will remember",
or turning to the reader with an aphorism. Chapter 19's mirror scene is the worked example. The fix
there was not to delete the account and not to soften it: it was to delete the *telling* and keep
the *telling of it by her* — she says the two lines, then says them again more softly, and stops;
nothing on the page says what to think. The meaning then arrives from outside her head, from a
sister-in-law at a door panel and a mother who decides that a woman repeating herself at midnight
has understood who is listening. A private line must produce a public consequence, which is the
house butterfly law applied to prose rather than to canon.

Six N7 flags survive in nineteen chapters. They stay until the author rules on each one; three of
the six are sentences he may well keep.
## 10 · The supernatural (2026-11-12)

*"Please special careful with super natural ones."* `canon/SUPERNATURAL.md` is the law; the four that matter at the desk:

1. **Never explain a naag thing.** Not the change, not the pearl, not the kechuli, not the thirteen faces, not the voice over a
   burial ground with no body attached to it. A character may believe it wrongly and say so; the page never glosses.
2. **The world reacts first.** Lamp, bell, dog, wind, score — one omen a scene, never pointed at, never named by anybody in the
   room.
3. **Every use costs a person in the scene.** A woman in the ground, thirteen faces in a pair of eyes, a guard who cannot say
   whose order he had. A miracle with no bill is decoration and comes out.
4. **The snake is a body and a sound, not an effect.** Spine, skin, hands, eyes, the cold off a sleeve, a ridge turning over in
   muddy water. Never the graphics; never the change described as a change.

And the fence around him (`canon/SUPERNATURAL.md` §2): he may see effects and never the cause; he does not explain the magic to
the audience; his scepticism is real and is not a debate; the naag world may smell what he is and it buys tension and no power;
the pull is not knowledge — **when he comes back after the leap and meets Ahana, he does not recognise her.**
