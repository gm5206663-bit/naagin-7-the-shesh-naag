# PICTURE — what the camera sees, and how this page is short of it

**Owns: the visual law. The author's correction of 2026-11-12 — *"you don't write the seen, the picture and visual and others
correctly, according to canon style; I think you should watch canon episode full; you should work on your visual."* — and the
frames of Episode 1 that were used to answer it.** `canon/STYLE_CANON.md` owns the sound, the omen and the scale of feeling;
this file owns the frame: what is in it, how it is lit, what the camera stops on, and what the page must therefore contain.

---

## 1 · What the stills actually show

Episode 1's fourteen contact sheets were pulled back from Drive on 2026-11-12 (`E01_0000-0150` … `E01fine_2395-2466`) and
read. Broad-stroke, the episode looks like this:

| Stretch | What is on screen |
|---|---|
| 00:00–02:30 | **No dialogue at all.** Ganesh on a plinth with a city skyline behind it; the sun coming up behind cloud; birds crossing; temple spires in haze; a shrine under marigold; the ghat at dusk with thousands of diyas on the water; the trishul in blue fire; sadhus in orange, in rows, in crowds; a sea of lamps at night |
| 07:00–08:20 | The house from outside at night — white fence, gravel, garden lamps, wet leaves — then a woman in a doorway with a bag, then **her feet on the tiles**, then a man walking through a door |
| 08:30–09:50 | Faces: the bearded man in a dark room, half of each cheek in shadow; the lead in amber light with marigold gone to bokeh behind him; a walk down a corridor with pandits in orange in the background; an over-the-shoulder frame with a blurred head in the corner |
| 10:00–10:30 | The idol in smoke; a stone corridor with one lamp; blue-black night outside a carved door |
| 11:00–12:00 | The hall with red and gold and a crowd round an aarti thali; the ancient temple steps; a study with books floor to ceiling and papers on the desk; a child in a man's arms in warm sepia; a wall of photographs; the lead in a maroon turtleneck under a lamp |

**Three things follow from that, and they are the whole of this file.** (1) The show spends its first two and a half minutes
on *place* before a single line is spoken. (2) In a dialogue scene it never stays on faces only: it cuts to feet, hands, a
thali, a lamp, a wall. (3) Its light is coded and its colour is loud — and the page has been writing like a radio play.

## 2 · The coded light

| Code | Where it is used | What the page writes |
|---|---|---|
| **Amber and gold** | the Suri house, the family, money, weddings, the fire in the hall | lamps, brass, marigold, a bulb's yellow, warmth on skin, the fire out or burning |
| **Blue and teal dark** | the temple at night, the past, the naag world, the sheds | the blue outside a door, the corridor's cold tube light, water at night |
| **Fire orange** | ritual, the aarti, the cremation ground, the Kumbh | flame on water, orange on faces, oil and smoke |
| **Sepia and dust** | 2001, and any memory | dust in a shaft of light, paper going yellow, the colour of old photographs |
| **Sindoor red** | marriage, threat to marriage, blood | a thali, a border, a stain, a hand |

**The rule.** A scene carries one of these, named once, in its opening paragraph. It is never explained and never a metaphor.
Red is not "danger"; red is the thali in the room.

## 3 · The shot list the page has to keep

Every scene, in this order, though not always all of them:

1. **Place first.** One sentence of the room, the street or the sky — what a wide would hold — before a face is named.
2. **The light.** One clause of the coded light above, in that same first sentence or the one after.
3. **The insert.** At least one object given its own frame in a scene of any length: feet on tiles, a hand on a register, a
   thali, a lamp, a phone face-down, a bucket, a printer's proof, a card in a plastic sleeve. The show cuts to it; the page
   gives it a sentence.
4. **Depth.** Something in the frame that is not the scene's business — a servant crossing, a crowd at the gate, a band, a
   queue, a dog. The show is never alone in a room.
5. **The close.** One face, close, at the moment that costs something, with the light on half of it.
6. **The hold.** Silence with the camera still on something. Written as a paragraph with no dialogue in it.

## 4 · How it fails, and the measure

`tools/picture_check.py` counts, per chapter and per scene: the share of paragraphs that are nothing but speech, the number
of sight-words (light, lamp, brass, dust, smoke, glass, gold, shadow, water, fire, colour), whether the scene's first
paragraph is a place sentence, and whether an insert is present. **Read it before the prose is called done.**

The failure mode is the one this file exists to stop. Across eighteen chapters the speech share of paragraphs runs **54% to
69%**. Canon's own scenes are the opposite way round: the camera talks first.
