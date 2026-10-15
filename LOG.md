# Daily Log

**Day 1 — Scope before code.**
Picked C. Before writing any code I wrote `intent.md`: the problem, what "done" means, and what's out of scope. I used to start in the editor and work out scope along the way. This time I kept the AI out until the intent was settled, because a vague ask gets a vague tool back. First pass: one global day threshold and an oldest-first sort. It ran, but the ranking was useless, because "oldest" isn't the same as "most at risk".

**Day 2 — Raised the load: risk-weighted ranking.**
Added per-stage limits (offer 2d, interview 3d, screen 4d, applied 5d) and a score = days over limit × stage weight. My first prompt said "weight later stages higher", and the model picked its own numbers. That was my mistake, not the model's: I'd left a decision unstated. I put the exact limits and formula in the prompt, which became the first version of `directive.md`. From then on I treated the directive as the spec and the code as output.

**Day 3 — Adversarial data. Things broke.**
Rewrote `board.csv` to look like real exports: a malformed date, a future date, a short row, mixed date formats. **Broke:** the run crashed on `not-a-date`, and a short row gave `None.strip()` → `AttributeError`. One bad row stopped the whole report, which isn't acceptable for a tool people check every morning. Changed it to per-row error collection: bad rows get reported with their line number and the rest still runs.

**Day 4 — Tests as the contract.**
Had the model write tests from the directive only, without seeing the implementation, so they'd check the spec rather than restate the code. One ranking test failed. I worked the scores out by hand, and the *test* was right; I'd misread my own formula. Lesson: verify against a hand-worked case, not against whichever side seems more confident.

**Day 5 — Hardening and honest gaps.**
Added `DD/MM/YYYY` support and a `--today` flag so the demo is reproducible. Found that an unknown stage (e.g. "Onsite") silently fell back to a 5-day limit. It now still flags the candidate but prints a warning, and there's a test for it. README, video.
**Still not handled:** stage names are a fixed list, not configurable; no timezone handling; no de-duplication if the same candidate appears twice.
