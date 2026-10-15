# Final Directive (the prompt behind the final version)
Build a Python 3 CLI `stall.py` using only the standard library.
- Input: a CSV with `name,stage,last_moved`. Accept dates as YYYY-MM-DD and DD/MM/YYYY.
- Stage limits: applied 5, screen 4, interview 3, offer 2 days. `--days N` overrides all of them.
- Skip hired, rejected and withdrawn.
- Score = (idle - limit + 1) × stage weight (1–4). Sort by score descending, then by name.
- Give each stalled candidate one concrete next action based on their stage.
- Never crash on a bad row. Collect "line N: reason" and print each one as SKIPPED.
- Add a `--today` flag so the output is reproducible.
- Write unittest tests for: limits, the override, skipped stages, ranking, bad rows, and both date formats.
- Keep it under about 100 lines and readable. No classes unless needed.
