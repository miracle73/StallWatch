import unittest
from datetime import date

from stall import find_stalled, parse_date

TODAY = date(2026, 10, 15)


def row(name, stage, moved):
    return {"name": name, "stage": stage, "last_moved": moved}


class StallTests(unittest.TestCase):
    def test_per_stage_limits(self):
        out, _ = find_stalled([row("A", "offer", "2026-10-13"), row("B", "applied", "2026-10-13")], TODAY)
        self.assertEqual([s["name"] for s in out], ["A"])

    def test_global_days_override(self):
        out, _ = find_stalled([row("B", "applied", "2026-10-13")], TODAY, days=2)
        self.assertEqual(len(out), 1)

    def test_finished_candidates_ignored(self):
        out, _ = find_stalled([row("H", "Hired", "2020-01-01")], TODAY)
        self.assertEqual(out, [])

    def test_ranking_late_stage_first(self):
        out, _ = find_stalled([row("Early", "applied", "2026-10-08"), row("Late", "offer", "2026-10-11")], TODAY)
        self.assertEqual(out[0]["name"], "Late")

    def test_bad_rows_reported_not_crash(self):
        rows = [row("X", "screen", "nope"), row("Y", "offer", "2026-12-01"), {"name": "Z"}]
        out, err = find_stalled(rows, TODAY)
        self.assertEqual(out, [])
        self.assertEqual(len(err), 3)

    def test_unknown_stage_warns_but_still_flags(self):
        out, err = find_stalled([row("U", "Onsite", "2026-10-01")], TODAY)
        self.assertEqual(len(out), 1)
        self.assertIn("unknown stage", err[0])

    def test_two_date_formats(self):
        self.assertEqual(parse_date("13/10/2026"), parse_date("2026-10-13"))


if __name__ == "__main__":
    unittest.main()
