# Daily Log
> DRAFT: edit each day so it matches what really happened.

**Day 1:** Picked C. Wrote intent.md *before* any code (my old habit was to open the editor first). Asked the AI for a first version with one global day limit. It worked, but the ranking was just "oldest first".
**Day 2:** Raised the load: per-stage limits plus weighted scoring. My first prompt was vague, and the AI invented a stage weight table I didn't want. I rewrote the prompt with exact numbers. That became the start of directive.md.
**Day 3:** Added messy data to the sample (bad date, future date, short row). **Broke:** the tool crashed on `not-a-date`, and a short row raised AttributeError on `None.strip()`. Fixed it by collecting errors per row.
**Day 4:** Had the AI write tests from the directive, then ran them. One test expected the wrong rank order because I had misread my own score formula. I checked by hand before trusting either side.
**Day 5:** Added DD/MM/YYYY dates and `--today` for repeatable demos. Wrote the README and recorded the video. **Still weak:** an unknown stage silently gets a 5-day limit.
