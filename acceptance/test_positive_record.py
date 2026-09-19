"""Criterion: installed single-record input requires a positive quantity."""
import unittest

from acceptance._consumer import run_installed


class PositiveRecordTests(unittest.TestCase):
    def test_zero_and_negative_quantities_are_rejected(self):
        for record in ("apples:0", "apples:-2"):
            with self.subTest(record=record):
                result = run_installed(record)
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, "")
                self.assertEqual(result.stderr, "invalid record\n")


if __name__ == "__main__":
    unittest.main()
