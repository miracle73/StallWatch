"""StallWatch: find hiring-board candidates who have not moved, ranked by urgency."""
import argparse
import csv
from datetime import date, datetime

STAGE_LIMIT = {"applied": 5, "screen": 4, "interview": 3, "offer": 2}
STAGE_WEIGHT = {"applied": 1, "screen": 2, "interview": 3, "offer": 4}
ACTION = {
    "applied": "Screen the CV or send a polite rejection",
    "screen": "Book the interview slot",
    "interview": "Chase interviewer feedback and decide",
    "offer": "Call the candidate about the offer today",
}
DONE = {"hired", "rejected", "withdrawn"}


def parse_date(text):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(text.strip(), fmt).date()
        except ValueError:
            pass
    raise ValueError(f"bad date {text!r}")


def find_stalled(rows, today, days=None):
    """Return (stalled, errors). stalled is sorted most urgent first."""
    stalled, errors = [], []
    for line, row in enumerate(rows, start=2):
        try:
            stage = row["stage"].strip().lower()
            if stage in DONE:
                continue
            idle = (today - parse_date(row["last_moved"])).days
            if idle < 0:
                raise ValueError("last_moved is in the future")
            limit = days if days is not None else STAGE_LIMIT.get(stage, 5)
            if idle >= limit:
                stalled.append({
                    "name": row["name"].strip(),
                    "stage": stage,
                    "idle": idle,
                    "score": (idle - limit + 1) * STAGE_WEIGHT.get(stage, 1),
                    "action": ACTION.get(stage, "Ask the owner what is blocking this"),
                })
        except (KeyError, ValueError, AttributeError) as e:
            errors.append(f"line {line}: {e}")
    stalled.sort(key=lambda s: (-s["score"], s["name"]))
    return stalled, errors


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv")
    p.add_argument("--days", type=int, help="one limit for all stages (overrides per-stage limits)")
    p.add_argument("--today", type=parse_date, default=date.today())
    a = p.parse_args(argv)
    with open(a.csv, newline="", encoding="utf-8") as f:
        stalled, errors = find_stalled(csv.DictReader(f), a.today, a.days)
    if not stalled:
        print("No stalled candidates.")
    for i, s in enumerate(stalled, 1):
        print(f"{i}. {s['name']} ({s['stage']}, {s['idle']} days idle, score {s['score']}) -> {s['action']}")
    for e in errors:
        print(f"SKIPPED {e}")


if __name__ == "__main__":
    main()
