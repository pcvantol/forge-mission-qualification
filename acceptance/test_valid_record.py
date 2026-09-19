"""Criterion: valid records are emitted as canonical JSON by the installed command."""
import unittest

from acceptance._consumer import run_installed


class ValidRecordTests(unittest.TestCase):
    def test_valid_record_emits_canonical_json(self):
        result = run_installed("apples:42")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, '{"name":"apples","quantity":42}\n')


if __name__ == "__main__":
    unittest.main()
