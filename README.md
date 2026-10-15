# StallWatch (Option C: Stall alerter)
Reads a hiring-board CSV, finds candidates who have not moved for too long, and ranks who to follow up first, with a next action for each.

## Run (Python 3.9+, no installs)
```
python stall.py board.csv --today 2026-10-15
python stall.py board.csv --days 3          # one limit for every stage
python -m unittest -v                       # tests
```
CSV columns: `name,stage,last_moved` (extra columns are ignored). Dates: `YYYY-MM-DD` or `DD/MM/YYYY`.

## How it ranks
Each stage has its own limit: applied 5, screen 4, interview 3, offer 2 days. Score = (days idle - limit + 1) × stage weight (1–4). Later stages weigh more because you lose those candidates faster. Hired, rejected and withdrawn candidates are skipped. Bad rows are printed as SKIPPED instead of crashing the run.

## Known limits
- An unknown stage name silently falls back to a 5-day limit.
- No timezone handling. Dates are whole days.
