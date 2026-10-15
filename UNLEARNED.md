# What I Unlearned

**1. Starting in the editor.**
My reflex is to open a file and start typing. This week the first artifact was `intent.md`, then a directive. The AI only got involved once the problem was written down precisely. Most of the real engineering moved into the spec: limits, scoring, failure behaviour. Code became the cheap part.

**2. Treating my own typing as the measure of my work.**
I stopped measuring my contribution by lines written. My job was deciding what the tool should do, stating it with no room for interpretation, and judging what came back. When the model picked its own stage weights, that wasn't the model failing. It showed me I'd left a decision unmade.

**3. Trusting output that looks right.**
The first version ran cleanly and produced a sensible-looking list. It was just sorted by age. Plausible isn't correct. Now I check output against a case I've worked out by hand before I accept it, and that applies to the tests too (Day 4: the test was right and I was wrong).

**4. Testing on clean data.**
I used to build sample data that showed the tool working. Now I build data meant to break it: bad dates, future dates, short rows, unknown stages. Every real bug this week came from that data.

**5. One big prompt.**
A long, loose prompt gave me confident guesses. Short prompts with exact constraints and a test to check against, iterated quickly, gave me something I could trust. I also had tests generated from the spec, not from the code, so they couldn't just mirror the implementation.

**What I'd still fix:** stages are hard-coded, there's no timezone handling, and duplicate candidates aren't detected. I've listed these in the log rather than hiding them.
