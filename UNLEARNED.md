# What I Unlearned
> DRAFT: rewrite it in your own words.

1. **Code first, think later.** I used to open the editor straight away. Now intent.md and a directive come first, and the AI builds from them. Writing the spec became the real work.
2. **Typing every line myself.** I stopped treating hand-typed code as the only "real" work. My job moved to stating constraints exactly and reviewing what comes back.
3. **Trusting output that looks right.** The AI's first ranking looked fine but was just oldest-first. Now I check results against a case I worked out by hand.
4. **Happy-path sample data.** I used to test with clean data. Now I add broken rows on purpose, and that is where the real bugs showed up (Day 3).
5. **One big prompt.** A vague prompt gave me invented numbers. Small, exact, testable prompts plus iteration beat one long ask.

**What failed:** my first prompts were too loose, one test was wrong because I misread my own formula, and unknown stages are still handled silently.
