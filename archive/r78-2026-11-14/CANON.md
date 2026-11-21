# CANON — sources, the episode map, and what is known

**Owns: what the show is, where each fact comes from, and how far the reading has gone.**
Last updated 2026-11-11.

Canon here means the 50 broadcast episodes of *Naagin* Season 7 (Colors TV, 27 Dec 2025 – 14 Jun 2026, Sat–Sun). Nothing in this file is taken from memory.

---

## 1 · Witnesses, strongest first

| Rank | Witness | What it is | What it cannot do |
|---|---|---|---|
| 1 | **The episode itself**, official Colors TV upload on YouTube | 49 of 50 full episodes are on the channel. Episode 1 has been looked at as sampled stills (`canon/frames/E01/`). | Stills at 240p, one every 5–15 seconds: no sound, no motion, nothing between samples. Episodes 2–50 not looked at. |
| 2 | **Caption tracks** in `captions/` (`E##.hi.srt`, reading copy `E##.hi.txt`) | YouTube's automatic Hindi captions of those official uploads; 47 tracks, each running to the end of its video | Speech recognition: no speaker labels, misheard names, nothing for silent action, songs or looks |
| 3 | **Written updates** in `canon/sources/` | Per-episode recaps: TellyReviews (35 episodes), TellyBoosters (40 episodes) | Recaps. They compress, reorder and sometimes misname. Two publishers at most. |
| 4 | Wikipedia season summary and cast list | Season-level outline, actor credits | Tertiary. Already wrong once (the scientist's name). Pointer only. |
| 5 | News and review articles | Launch coverage, finale explainers | Pointer only |

Rules that follow from this:
- A line of dialogue is written from rank 2. An action or a look is written from the frames where they have been sampled, otherwise from rank 3 and declared as such.
- The secondary sources have already been wrong three times on Episode 1 alone, each caught by the episode: the scientist's name (Wikipedia), foxes for wolves, and Purvi entering the temple at the end (both TellyReviews).
- Two copies of one recap are one witness. Independence is by publisher.
- When witnesses disagree, the disagreement is recorded and ruled in §4. Never averaged.
- A recap that is absent, or silent on a point, proves nothing about the episode.

How the captions were fetched: `tools/fetch_captions.sh` (yt-dlp, automatic captions only), converted by `tools/json3_to_txt.py`. Video ids are in `captions/youtube_full_episodes.json`. How the stills were made: `tools/contact_sheet.py` over a 240p copy of the official upload; only the sheets are kept, not the video.

## 2 · Gaps in the record

| Episode | Gap |
|---|---|
| 37 (2 May) | Not found on the Colors TV channel. **Caption track taken on 2026-11-11 from the sister channel Colors Rishtey** (`snpcjxmimqg`, "Pasha Pays a Surprise Visit at Aryaman's Wedding, Full Ep 37", 24:28). A different upload and possibly a different cut. One recap (TellyBoosters). |
| 43, 44 (23–24 May) | The Colors TV uploads open only in one other country. **Caption tracks taken on 2026-11-11 from Colors Rishtey** (`mFSF4d0ePJg`, Full Ep 43, 26:41; `Rf2m1RdOfdc`, Full Ep 44, 32:12). The Rishtey cut of 44 is shorter than the Colors upload (36:42), so something is missing from it. Recaps exist. |
| 19 (28 Feb) | Captions exist. No written update from either publisher. |
| 1–4, 12, 20, 22, 27, 28 | Captions exist. One recap publisher only (TellyReviews). |
| 23, 24, 26, 35–38, 44–50 | One recap publisher only (TellyBoosters). |
| 2–50 | No video looked at. Staging, faces, costume and silent action rest on recaps. Episode 1 was sampled as stills only. |
| 2–50 | **Read at digest depth only** (`canon/SEASON.md`): every held recap in full, one per episode, with caption checks at the points listed under R9–R15. No episode after the first has a beat ledger yet. Read from their whole caption tracks: Episode 19 (it has no recap) and Episode 7 (the wedding night). Episode 44 read from 02:48 to 13:19 (the curse). **All fifty episodes now have a caption track.** |

## 3 · The episode map

"Read so far" is the honest depth of reading on 2026-11-11. A dash means the episode has not been read at all: only its title and the season summary are known.

| Ep | Air date | Official upload title (Colors TV) | Captions | Written updates | Read so far |
|---|---|---|---|---|---|
| 01 | 2025-12-27 Sat | Naagin Legacy Unleashed | yes | TR | full: captions + TR + sampled stills |
| 02 | 2025-12-28 Sun | Naagin Rescues Purvi and Anantha | yes | TR | TR full |
| 03 | 2026-01-03 Sat | Parmeet's Shield against the Naagin | yes | TR | TR full |
| 04 | 2026-01-04 Sun | Naagin's Deadly Battle | yes | TR | TR full |
| 05 | 2026-01-10 Sat | Ravish Confesses the Truth | yes | TR + TB | TR part; captions 28:28–30:25 only |
| 06 | 2026-01-11 Sun | Gurinder Hunts Parmeet's Secret | yes | TR + TB | TR full |
| 07 | 2026-01-17 Sat | Parmeet's Family Takes a Dark Turn | yes | TR + TB | TR full |
| 08 | 2026-01-18 Sun | Purvi Awakens as Naagin | yes | TR + TB | TR full |
| 09 | 2026-01-24 Sat | Purvi Disguises as Ahana | yes | TR + TB | — |
| 10 | 2026-01-25 Sun | Naagin's Revenge Claims Swarna | yes | TR + TB | — |
| 11 | 2026-01-31 Sat | Samir Faces Naagin's Revenge | yes | TR + TB | — |
| 12 | 2026-02-01 Sun | Ahana's Bold Defiance | yes | TR | — |
| 13 | 2026-02-07 Sat | Naagin's Revenge Claims Swarna | yes | TR + TB | — |
| 14 | 2026-02-08 Sun | Ahana's Love Becomes Her Weakness | yes | TR + TB | — |
| 15 | 2026-02-14 Sat | Bharani's Plot against Love Fails | yes | TR + TB | — |
| 16 | 2026-02-15 Sun | Ahana Performs Shiv Tandav | yes | TR + TB | — |
| 17 | 2026-02-21 Sat | (untitled / not located) | yes | TR + TB | — |
| 18 | 2026-02-22 Sun | (untitled / not located) | yes | TR + TB | — |
| 19 | 2026-02-28 Sat | Aryaman's Battle to Save India | yes | none | — |
| 20 | 2026-03-01 Sun | Can Ahana Save the Amarnath Yatris? | yes | TR | — |
| 21 | 2026-03-07 Sat | Aryaman's Secret Past Unveiled | yes | TR + TB | TR full |
| 22 | 2026-03-08 Sun | Ahana's Deadly Discovery | yes | TR | — |
| 23 | 2026-03-14 Sat | The Dragon Targets Radhika! | yes | TB | — |
| 24 | 2026-03-15 Sun | Aryaman Loves Ahana | yes | TB | — |
| 25 | 2026-03-21 Sat | Ahana's Revenge Strikes Dimple | yes | TR + TB | — |
| 26 | 2026-03-22 Sun | The Dragon Pearl's Secret Power | yes | TB | — |
| 27 | 2026-03-28 Sat | Ahana Unmasks Pinky's Fiancé | yes | TR | — |
| 28 | 2026-03-29 Sun | Yaman's Arrival Flips the Script | yes | TR | — |
| 29 | 2026-04-04 Sat | Bharni Falls to Ravish’s Wrath | yes | TR + TB | — |
| 30 | 2026-04-05 Sun | Ahana’s Spooky Scheme | yes | TR + TB | — |
| 31 | 2026-04-11 Sat | Ahana Faces Dragon King | yes | TR + TB | — |
| 32 | 2026-04-12 Sun | Today's Episode | yes | TR + TB | — |
| 33 | 2026-04-18 Sat | Radhika Plots Against Ahana | yes | TR + TB | — |
| 34 | 2026-04-19 Sun | The Dragon Conspiracy Unfolds | yes | TR + TB | — |
| 35 | 2026-04-25 Sat | Aryaman Hands Divorce Papers | yes | TB | — |
| 36 | 2026-04-26 Sun | Ahana's Revenge Awakens | yes | TB | — |
| 37 | 2026-05-02 Sat | (untitled / not located) | NO | TB | — |
| 38 | 2026-05-03 Sun | Radhika’s Deadly Betrayal | yes | TB | — |
| 39 | 2026-05-09 Sat | Ahana's Revenge Begins | yes | TR + TB | — |
| 40 | 2026-05-10 Sun | Apara's Hidden Naagin Past | yes | TR + TB | — |
| 41 | 2026-05-16 Sat | Radhika's Hidden Agenda | yes | TR + TB | — |
| 42 | 2026-05-17 Sun | Apara Is Rescued | yes | TR + TB | — |
| 43 | 2026-05-23 Sat | Apara Regains Her Lost Memory | NO | TR + TB | — |
| 44 | 2026-05-24 Sun | Apara's Bold Plan to Find Nagmani | NO | TB | — |
| 45 | 2026-05-30 Sat | First Rescue, Then Revenge! | yes | TB | — |
| 46 | 2026-05-31 Sun | Apara Plots against Radhika | yes | TB | — |
| 47 | 2026-06-06 Sat | Naagin's Quest for Revenge | yes | TB | — |
| 48 | 2026-06-07 Sun | The Battle for Naagmani | yes | TB | — |
| 49 | 2026-06-13 Sat | The Naagvansh in Danger | yes | TB | — |
| 50 | 2026-06-14 Sun | The Rise of Naagrani Ahana | yes | TB | — |

Machine copy: `canon/episodes.json`. Episode 1's full beat ledger: `canon/E01_BEATS.md`.

Notes on the titles: they are the Colors TV upload titles. Episodes 17 and 18 are untitled on the channel, Episode 32 is titled "Today's Episode", and Episodes 10 and 13 carry the same title there.

## 4 · Rulings

| # | Question | Ruling | Basis |
|---|---|---|---|
| R1 | The scientist: Tushar Sinha or Vishal Puri | **Tushar Sinha** | Episode 1 captions, his own line at 13:22: "मैं तुषार सिन्हा, मैं एक साइंटिस्ट हूं". Wikipedia's "Dr. Vishal Puri" is outranked. |
| R2 | The mother: Pragati or Prarthana | **Pragati**, third birth after Pratha and Prarthana | Episode 1 captions, her own account at 17:42 |
| R3 | Who are the Suris | The real Suri family (Parmeet, Nimrat, a son, and others of the same names the impostors now use) were the Aroras' neighbours in Attari and vanished in 2001. The Suris of 2025 are the infiltrators, living under those names. | Episode 1 captions (the killing set-up, "that whole Suri family vanished", "killing our people and taking their places"); Episode 5 captions 28:50–30:25 (Gurinder works it out aloud to Shalini, who laughs it off); Episode 6 captions 00:30–02:25 (he says it to "Parmeet", who then ties the Aroras to the door where the scientist was taken); recaps of Episodes 3, 6, 7 state it outright |
| R4 | Whose family are the two sisters | **Arora** (Gurinder, Shalini, Ananta, Purvi, Rohan). Not Suri. | Wikipedia cast list for the surname; captions and recaps for the household |
| R5 | Which sister is the naagin | The girl raised as **Purvi** is the born Ananta. The girl raised as Ananta is the Aroras' own daughter. | Episode 1 captions at 40:35 |
| R6 | The clan | **Anant kul**, of Sheshnaag's line | Captions throughout; one mishearing as "Anantpur" |
| R7 | Is the professor's son of Episode 1 Aryaman | **Yes.** "Parmeet" adopted the scientist's son to reach the father's work: a book, and a locker that cannot be opened until the son turns 30. Aryaman knows he is adopted. He does not know why, or who killed his father. Others in the house know he is adopted; one says, "Aryaman is Indian. We are not." | Captions: Ep 21 24:36, Ep 22 11:44, Ep 23 28:57, Ep 24 06:23, Ep 25 28:59, Ep 34 23:09, Ep 38 24:09. Passages only; those episodes are not otherwise read. **Episode 1 does not say it.** |
| R8 | The enemy state's name | Heard as **"Changistan"**: 139 of 161 hearings across the caption tracks, first spoken in Ep 6 (30:48). One recap publisher writes "Chengistan", the other "Jungistan". No on-screen spelling has been seen. | Captions, all tracks. Before Episode 6 it is only "the enemy country". |
| R9 | The curse on the Anant kul and how it ends | Sushanta, keeper of the Naagmani, loved a human (Airul) and let him hold it; she turned to stone and Mahadev made the clan human. It ends when an ichchhadhari naagin **marries a naag and bears a child**. The child that was to be Sushanta's was born of Pragati instead. | Captions Ep 44 02:48–10:30, the family's own account ("by marrying a naag you must give us back all our powers"); TellyBoosters Ep 44 for Mahadev's words; captions Ep 48 19:56 ("she will marry Aditya and, by bearing the next generation, wipe out the curse on our clan"); Ep 50 03:57 ("I, who was to be born of your womb, had to be born of Pragati's") |
| R10 | Who stabbed Purvi on the wedding night | **Bharani, in Aryaman's shape.** Purvi runs upstairs to Aryaman for help; "he" promises that nothing will happen to her, stabs her, and mocks her for thinking a man like him could love a girl like her. Bharani struck away from the spine on purpose, so that she would seem dead and live. Aryaman himself had been made unconscious that day by the house, because he "was hard to make understand"; afterwards he believes the "robber bride" story and says so on air. | Captions: Ep 7 22:34–24:28 (the scene as the viewer first sees it); Ep 15 02:36 (Bharani tells it) and 11:32 (why Aryaman had to be unconscious); Ep 17 04:39 and 08:15 (Ahana confronts her); Ep 8 16:01 (Aryaman on air). |
| R16 | How many she vows to kill | **Thirteen.** The men burying her see the faces printed in her eyes and count thirteen. | Captions Ep 8 01:07. Wikipedia says twelve. |
| R17 | The wedding night: who is in the room | When the inspector arrives, "Parmeet" clears the girls of the house out before a word of truth is spoken: "call the car and take the girls home… Rishabh, take these girls to your house." Later he says it outright: "we sent the girls away on purpose." The sons stay. At least one of them hears for the first time what the family is ("the truth you did not know till now"). Ravish: "What a relief, Dad. Finally." The priest is their own man. The inspector is bought, and says a man who complained before was killed, and his girlfriend after him. | Captions Ep 7 02:32, 05:33, 06:47–08:11. No speaker labels: who says each line is inferred. |
| R18 | Who the impostors are | Five came across in 2001: "I, my brother, my sister and my two friends." He gives real names; the track hears them badly: his own as something like "Aran", Baljeet's as **Karim**, and a third as "Tari…". The minister Sameer is one of the friends. The names are not fixed until heard with sound; none is printed in a chapter before then. The enemy state is "two hundred kilometres from India". | Captions Ep 7 05:02–06:15 |
| R19 | How a naagin is killed | A blow to the spine, then a brass dagger in the chest, while the been is playing. Said by the Mahasapera on the wedding night, and it is how Uttara is killed. Bharani knew it and struck Purvi away from the spine. | Captions Ep 7 14:38, 18:42; Ep 15 02:36 |
| R22 | **The full moon and the kechuli** | "Tonight is the night of Purnima. Within twenty-four hours of the moon's rising, every naag and naagin sheds its kechuli." Uttered over Purvi's first transformation. | C, Ep 2 26:09 |
| R23 | **A mirror shows a naagin her true face** | "Whether anyone else looks or not, a mirror sees her." Spoken over the transformation; the speaker is not established. | C, Ep 2 30:50; speaker **open** |
| R27 | **Nobody in canon calls the plain girl beautiful** | Across the first arc (Episodes 1–8) the material the workshop holds has no line in which anyone praises Purvi's face — not a relative, not a colleague, not a guard. The first man canon has say it is Aryaman, drunk, to **Ahana**, down to her "naagin walk" — the same girl, after the awakening, living in the Suri house under another name. The show keeps the world's eyes off her until she is no longer the girl in spectacles. Ruling `O033` puts Vihaan in those years as the one man who is looking, and forbids the page from letting the room agree with him or the narration from grading her. | C, Episodes 1–8 (as silence) and the second arc (`canon/SEASON.md`); `O033` |
| R24 | **One foot is enough** | Uttara: the Maharani came "not to the temple but into it and back out. She has put one foot inside. Her becoming a naagin has begun." The awakening is begun, not completed, by the temple. | C, Ep 2 15:00 |
| R26 | **How this show stages a first meeting, and heightened scenes generally** — a meeting is never a courtesy. Episode 2's corridor (00:01:16) gives the template: somebody offers help, a hand is taken hold of, *"leave my hand"*, *"or I will scream and bring the whole channel out here"*, *"scream, then"*, *"I will kill you"*, *"kill me"* — and then one of the two laughs. Friction first, a physical beat, a threat and a dare, a repetition of the line, a laugh, and only then the look. Canon elsewhere gives the held look after the other has turned away, the object that changes hands, the interruption at the exact moment, and the omen (a lamp, the moon, a snake) set in the same frame. **A first meeting written as two people politely exchanging two words is not this show's style, however clean the prose.** | Captions Ep 2 00:01:16 and 00:01:56; Ep 1's own first meetings; the stills of Ep 1. The corridor's speakers are uncertain (S-09), which does not change what the exchange teaches |
| R25 | **The king's lines never entered the rumour** | The litany is quoted twice in Episode 2 — by Aryaman's sister and by the men recalling the scientist — and both times canon gives the queen's half and stops. Ruling: the four lines of `R21` were said once, in 2001, to men who did not understand them, and the version that circulates in 2025 has no king in it. Nothing in the enemy's hands needs changing, and `OPEN-17` holds. | C, Ep 2 24:19 and 25:02 against `R21` |
| R21 | **The prophecy names the king** | Declared divergence, on the author's instruction (`O023`, 2026-11-11). Tushar Sinha's litany in Episode 1 names the queen; it now also names, in four short lines, the one who comes with her — "Nagaraj of the Anant kul. Sheshnaag. King of Naaglok. Anantveer." — and the blow that follows takes the next word. The name is **Anantveer**, the short form *Veer* being what almost nobody in this world knows to say (`O032`). Cause on the page: his torturers keep demanding who is coming, and canon already strikes him mid-speech. The men do not understand what they hear, and the episode never returns to it. Rendered in `chapters/Chapter_01_Who_Is_Coming.md`; accounted for in `canon/E01_BEATS.md` B12. | `O023`; C Ep 1 21:06–23:14 for the scene it stands in |
| R20 | The dragon | "We changed its genes and bred it again." It sleeps until it scents an ichchhadhari naagin. | Captions Ep 7 26:14–28:27 |
| R11 | Who Radhika is | Pragati's elder daughter, left at three; made a dragon in Airul's laboratory; the dragon of the Kumbh and of the basement; the writer of the letters. | TellyReviews Ep 32, 34; TellyBoosters Ep 35, 46. Captions Ep 49 27:46 (Pragati to her: "you are my blood; naagin blood is in you") |
| R12 | How canon lets a naagin marry Aryaman | Mahadev: after Vishakha's bite naagin blood ran in him; most was drawn out, some remains; "he is no longer only human; therefore your union is acceptable to nature and to destiny." | Captions Ep 50 25:52 |
| R13 | "Parmeet's" own children; is Roma dead | **Ravish is "Parmeet's" own son.** He calls him Dad on the wedding night and is called "son" back; Karan and Arjun tell him Aryaman "is not your real brother". So when Aryaman says "Parmeet" loved him "more than his own real son", there is a real son, and it is Ravish. The line gives no ground for any *other* son. Karan and Arjun are Baljeet's children. **Roma is alive**: Karan says "had Roma died", not that she did. | Captions Ep 7 08:11; Ep 24 06:23; Ep 21 10:18 and 04:16; Ep 23 28:57 ("my children"; the speaker is taken to be Baljeet). **Corrected 2026-11-11:** this row first said a son of his own was "not established". That was written from a note and not from the lines. |
| R14 | Ravish | Younger than Aryaman ("his elder brother, that Hitler"). He killed Ananta Arora and, with her, their unborn child. | Captions Ep 3 17:39; Ep 50 07:39 |
| R15 | The mother's name in the late episodes | Recaps write Pratha (Ep 34), Prarthana (Ep 46) and Pragati (Ep 41, 47, 49, 50) for the same portrait. **Pragati**, as R2. In Ep 49 she says she was once called Prarthana and Pratha. | TellyReviews, TellyBoosters; R2 |

## 5 · People

Moved. `foundation/CHARACTERS.md` owns who everyone is, with the same tags.

## 6 · What happens in each episode

Moved. `canon/SEASON.md` owns the digest of all fifty episodes, the arcs, and the table of who dies by whose hand. `canon/E##_BEATS.md` owns the full beat ledger of an episode; Episode 1 has one.
