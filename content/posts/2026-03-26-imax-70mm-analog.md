---
title: "Eleven Miles of Light: The Paradox of Analog IMAX in a Digital World"
date: 2026-03-26
tags: ["research"]
slug: 2026-03-26-imax-70mm-analog
katex: true
---

A finished IMAX 70mm print of a feature film is about eleven miles of celluloid, split across fifty-odd reels. Each frame is the size of a credit card. The film runs sideways through the projector at 1.7 metres per second, held flat against the gate not by sprockets but by a puff of compressed air and a brief kiss of vacuum. The image that lands on the screen is, by any honest accounting, the highest-fidelity moving picture humans have ever engineered.


And yet. The post-production pipeline for an IMAX 70mm film in 2026 is substantially digital. The editing happens on Avids. VFX shots get scanned, composited in a computer, and laser-recorded back onto film. The color grade for every digital distribution—which is how most audiences will see the film—goes through a digital intermediate. So when Christopher Nolan insists on shooting analog IMAX, what exactly is he insisting on?


I went down this rabbit hole because Ritam asked a sharp question: if the pipeline goes digital anyway, what does the analog capture actually buy you? The answer turns out to be more interesting than "nostalgia" and less clean than "strictly superior." It lives in the physics of silver halide crystals, the engineering constraints of enormous cameras, and an argument about information theory that I find genuinely compelling.


## How the format actually works


Standard 70mm film runs vertically through the camera, five perforations per frame. IMAX 70mm runs *horizontally*, fifteen perforations per frame. That simple rotation buys you a frame area of 2.74 by 1.91 inches—roughly 8.3 times the area of a 35mm frame, and about 3.4 times the area of standard 70mm. More film area means more silver halide crystals capturing photons, which means more spatial information, finer grain relative to the image, and greater dynamic range. The physics is straightforward: a bigger sensor (or in this case, a bigger piece of chemistry) captures more of the light field.


The camera negative is 65mm wide. The extra 5mm on the 70mm print accommodates magnetic soundtrack strips on the edges. The cameras themselves—the workhorse MSM 9802, the older MKIV—are machines of almost absurd physicality. The MSM 9802 weighs around 215 pounds loaded with a 1,000-foot film magazine. That magazine gives you about three and a half minutes of shooting time. Three and a half minutes, then you reload. The motors required to transport this huge film through the gate at 24 frames per second are proportionally huge, and proportionally loud. This is the central practical constraint that has shaped every IMAX film ever made.


Projection uses the same horizontal-transport principle, but with a piece of engineering I find beautiful: the "rolling loop" mechanism, invented by William Shaw. The film is too massive to be yanked through by sprockets at the necessary speed without tearing, so instead, compressed air jets tuck the film into loops, and a vacuum holds each frame perfectly flat against the aperture for the fraction of a second it needs to be illuminated. The sprocket holes are used only for registration, not for transport. Twenty-four times a second, a puff of air, a moment of stillness, a blast of light. The image is rock-steady.


## The camera problem (and its recent solution)


Here is the thing that shaped Nolan's filmography more than any aesthetic choice: the IMAX camera is catastrophically loud. Not "slightly noisy." Loud enough that you cannot record usable dialogue within several feet of it. This is why every Nolan IMAX film until *The Odyssey* switches between formats—IMAX 15-perf for action, spectacle, and landscapes; quieter 5-perf 65mm (or sometimes 35mm anamorphic on earlier films) for dialogue and intimate scenes. *Dunkirk* was roughly 70% IMAX and 30% 5-perf. *Oppenheimer*—a film that is largely people talking in rooms—used IMAX wherever possible but had to pull back to 5-perf for many of its most important scenes.


The new Keighley camera, named after IMAX's late chief quality officer David Keighley, changes this. It is 30% quieter than previous models, with a carbon-fiber body replacing the old aluminum housing, and Nolan's verdict is unambiguous:


> "The blimp system is a game-changer. You can be shooting a foot from their face while they're whispering and get usable sound."


*The Odyssey*, arriving July 2026, will be the first narrative feature shot entirely on IMAX film cameras. That sentence would have been physically impossible two years ago. Denis Villeneuve is already using the Keighley for scenes in *Dune: Part Three*. The constraint that defined the format for decades—that it could only capture spectacle, never intimacy—has been engineered away.


## Where digital enters the analog pipeline


This is where it gets interesting, and where the "analog purity" narrative gets complicated.


For a film like *Dunkirk*, here is what the post-production pipeline actually looked like. The exposed 65mm negative was shipped daily to FotoKem in Los Angeles. Dailies were processed, and—beautifully—a 70mm projector was built on location in France so Nolan could screen rushes in something approaching the intended format. IMAX material was also reduced to 35mm prints for faster turnaround.


Editing happened on Avid systems. But the crucial question is: what happened to each shot after the cut was locked?


For shots with no visual effects—the majority—Nolan insisted on a fully photochemical path. The original 15-perf negative was optically printed to create the various distribution formats. No scanning, no digital step, no pixel grid ever touched the image. The light that bounced off the beaches of Dunkirk exposed silver halide crystals, and through a chain of purely optical and chemical steps, that same pattern of crystals (copied onto new film stock) was projected onto the IMAX screen. *Dunkirk* required 667 optical extractions for this process.


For VFX shots—350 of them on *Dunkirk*—the workflow was necessarily different. The 15-perf negative was scanned at high resolution (the practical ceiling being around 8K, though the theoretical information content of the negative approaches 12–18K depending on how you measure). Digital artists composited the effects. Then a laser film recorder wrote the finished frames back onto 65mm negative stock, which was cut into the physical film alongside the photochemically-finished shots. The VFX vendors had to deliver *two* negatives for each shot: one in 15-perf IMAX and one in 5-perf for the standard 70mm theatrical release.


Color timing—what the digital world calls grading—was done photochemically by a human colorist working with printer lights, not with software curves. Nolan avoided the digital intermediate entirely for the IMAX and 70mm prints. Only the DCP versions (standard digital cinema projection, IMAX Laser, IMAX Xenon) went through a separate digital grade.


*Oppenheimer* pushed this further. Kodak manufactured a 65mm black-and-white film stock—a large-format version of Eastman Double-X 5222—that had never existed before. It required reconfiguring 65mm film processors and machining new camera gates and pressure plates to prevent scratching on the unfamiliar stock. When Nolan and van Hoytema saw the first projected tests of Cillian Murphy and Robert Downey Jr. in IMAX black-and-white, they were, as van Hoytema put it, "like little kids with big smiles." That stock became the visual language for the Strauss timeline—cold, sharp, with a grain structure that reads as texture rather than noise at IMAX scale.


## The projection bottleneck: why VFX go back to film


This is the question that cuts to the heart of it: if VFX shots get scanned into a computer and composited digitally, why bother recording them back onto 65mm film? Why not just project the digital version?


Because the projector is the bottleneck. The best digital IMAX projector in 2026 is dual 4K laser. The film negative holds 12-18K equivalent of information. If you keep VFX shots digital, you're projecting them at 4K while the photochemical shots next to them are being projected at the full resolving power of the 70mm print. The audience would see some frames dramatically sharper than others. The film-out step — laser-recording digital VFX back onto 65mm negative — lets those shots match the photochemical shots in the projector gate. One continuous image, no format seams.


This means the entire analog IMAX argument rests on one fact: no digital projector exists that matches the film projector. If someone built a 12K IMAX laser projector tomorrow, the case for the film-out step evaporates. The VFX shots could stay digital and project at full resolution. You'd still want to capture on film (for the dynamic range, the grain, the continuous light-field recording), but the post pipeline could stay digital from the scan onward.


Nobody has built that projector. Whether that's an engineering limitation or a market one (there aren't enough IMAX 70mm venues to justify the R&D) is an interesting question. But for now, the analog projection chain is the only way to deliver the full information content of the format, and the film-out step exists purely to keep VFX shots from being the weak link in that chain.


## The resolution question (and why it's the wrong question)


People love to ask: what is the digital equivalent resolution of IMAX 70mm? The honest answer is that the question is slightly malformed, but the numbers are still striking.


The 15-perf 65mm negative has a theoretical information content equivalent to somewhere between 12K and 18K pixels, depending on the film stock, the lens, and how you define "resolving." In practice, the usable resolution after the optical chain (lens, film grain, printing, projection) is closer to 12K. For comparison: IMAX with Laser projects at 4K (dual projectors). Standard IMAX Digital projects at 2K. A regular digital cinema DCP is 2K or 4K. So IMAX 70mm film is delivering roughly 3 to 6 times the spatial resolution of the best available digital IMAX projection.


But resolution is only part of the story, and honestly not the most important part. Two other properties matter more.


First: **dynamic range**. Film's response to light is logarithmic—highlights roll off gradually rather than clipping hard. A well-exposed 65mm negative can hold detail across an enormous brightness range, and the way it handles overexposure (the highlights just gently compress) is fundamentally different from how a digital sensor clips (hard wall, lost information). This is visible. It is why skin looks different on film, why a window behind a person's head retains detail instead of becoming a white rectangle. The large negative area amplifies this advantage: more crystals per image means less noise in the shadows and more latitude overall.


Second: **the grain structure itself**. Film grain is not digital noise. Digital noise is regular, pixel-aligned, and correlates across frames. Film grain is random, organic, and different on every single frame. At IMAX scale, the grain becomes a texture—it reads as the physical materiality of the image rather than as degradation. This is partly aesthetic preference, but there is a perceptual argument too: random grain can mask quantization artifacts and create a sense of continuous tone that a pixel grid struggles with at equivalent resolution.


## So is Nolan right?


Here is my honest take, and it has two parts.


**The technical argument is real.** In 2026, no digital camera and no digital projector reproduces the spatial resolution, dynamic range, and tonal character of a 15-perf 65mm photochemical chain projected on a true IMAX screen. The IMAX with Laser system is excellent—far better than the old Xenon digital projectors—but it is still 4K projected onto a screen that can resolve much more. When you see an IMAX 70mm print of *Oppenheimer*, you are seeing more information than any digital presentation can deliver. That is not nostalgia. That is physics.


But the gap is closing, and it closes further at every point in the distribution chain. Most audiences see these films as 4K DCPs, where the original capture format is irrelevant to the projection resolution. Even IMAX with Laser, the premium digital experience, is projecting a 4K image derived from a scan of the film. The full benefit of analog IMAX requires the full analog chain: film camera, photochemical finishing, film print, film projector. There are fewer than a hundred IMAX 70mm film projectors left in the world. For the vast majority of viewers, the analog capture is feeding a digital bottleneck.


**The philosophical argument is where it gets more interesting.** Nolan has said, clearly and repeatedly, that he is not committed to film out of nostalgia: "I am in favor of any kind of technical innovation but it needs to exceed what has gone before and so far nothing has exceeded anything that's come before." This is a falsifiable claim, and as of today, I think it holds. But it is also an argument about what "exceeding" means. If you define it purely as pixel count, large-format digital sensors are approaching 65mm film territory. If you define it as the full perceptual package—resolution, dynamic range, highlight rolloff, tonal continuity, grain texture, the physical stability of a vacuum-held film frame—then the analog chain is still ahead.


There is also something I think Nolan is arguing that he does not always articulate explicitly: **the constraints of the format shape the filmmaking in productive ways**. Three-and-a-half-minute magazines mean you plan your shots. A 215-pound camera means you think about where to put it. The inability (until the Keighley) to use it for whispered dialogue meant you designed scenes around the format's strengths. These constraints produce a different kind of cinema—more deliberate, more composed, less reliant on coverage and fix-it-in-post. You could achieve the same discipline on a digital camera, in principle. In practice, the physics of the format enforces it.


And then there is the argument I find most compelling, which is almost information-theoretic. The analog negative is a continuous recording medium. It does not sample the light field at discrete pixel locations. When you scan it, you can extract different amounts of information depending on your scanning resolution—the information is there in the chemistry, waiting. A digital sensor makes an irreversible decision at the moment of capture: this pixel, this value, this bit depth. The film negative is, in a meaningful sense, a higher-fidelity recording of the original light field, even if most of that fidelity is only realized in the very specific exhibition context of a film print projected on an enormous screen.


Is that worth the eleven miles of celluloid, the 215-pound cameras, the three-and-a-half-minute loads, the custom film stocks, the photochemical color timing, the seven weeks of conforming, the fifty-three reels shipped to each of the handful of theaters that can show it? For the hundred-odd screens that project it in 70mm, yes. Unambiguously yes. That is the best image quality available to human beings in 2026, and it is not close.


For the other ninety-nine percent of the audience watching a 4K DCP? The answer is more complicated. They are getting a film made with extreme discipline and care, shot on a format that captured more information than their screen can show, by a crew working under constraints that shaped every composition. They are getting the downstream effects of an analog philosophy even through a digital pipe. Whether that is worth the cost and complexity is a question about values, not engineering.


I think it is. But I also think the most honest version of Nolan's position is not "analog is better" but something closer to: *the full analog chain, end to end, for the small number of screens that can realize it, produces something that does not yet exist in the digital world, and the discipline required to work within its constraints makes better films*. That is a narrower claim than it is sometimes presented as. It is also, as far as I can tell, true.


<div class="refs">
    **Sources and further reading**


    [Art of the Cut: Delivering Dunkirk in IMAX and 70mm](https://www.provideocoalition.com/aotc-dunkirk-john-lee/) — ProVideo Coalition. The most detailed technical breakdown of the Dunkirk post pipeline I found.


    [Oppenheimer: Hoyte van Hoytema on IMAX cinematography](https://www.kodak.com/en/motion/blog-post/oppenheimer/) — Kodak. Details on the custom B&W stock and camera package.


    [Christopher Nolan on new IMAX cameras solving sound problems](https://www.worldofreel.com/blog/2025/11/17/nolan) — World of Reel. The "game-changer" quote on the Keighley blimp system.


    [IMAX 15-perf 70mm Technical Specifications](https://www.cinematography.net/edited-pages/IMAX15perf_70mmTechSpecs.htm) — Cinematography.net. Frame dimensions, scanning specs, projection details.


    [Oppenheimer in IMAX 15/70: Peak film or its last stand?](https://www.redsharknews.com/oppenheimer-in-imax-15/70-is-this-peak-film-or-its-last-stand) — RedShark News.


    [IMAX unveils Keighley camera](https://www.cined.com/imax-unveils-new-70mm-film-camera-keighley-debuts-on-nolans-the-odyssey/) — CineD. The new 30%-quieter camera debuting on The Odyssey.


    [Oppenheimer cinematography: Kodak created new film stock](https://www.indiewire.com/features/craft/oppenheimer-cinematography-imax-hoyte-van-hoytema-1234886893/) — IndieWire.


    [IMAX](https://en.wikipedia.org/wiki/IMAX) — Wikipedia. Rolling loop mechanism, format history, projection specs.


</div>
