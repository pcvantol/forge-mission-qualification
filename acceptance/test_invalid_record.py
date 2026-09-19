"""Criterion: malformed records are rejected by the installed command."""
import unittest

from acceptance._consumer import run_installed


class InvalidRecordTests(unittest.TestCase):
    def test_invalid_record_is_rejected_with_stable_error(self):
        result = run_installed("nonsense")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "invalid record\n")


if __name__ == "__main__":
    unittest.main()
