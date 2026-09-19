"""Criterion: installed batch input aggregates records and fails atomically."""
import unittest

from acceptance._consumer import run_installed


class BatchRecordTests(unittest.TestCase):
    def test_valid_batch_emits_canonical_aggregate(self):
        result = run_installed("--batch", "apples:2,pears:3")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"apples","quantity":2},{"name":"pears","quantity":3}],"total_quantity":5}\n',
        )

    def test_invalid_batch_emits_no_partial_result(self):
        result = run_installed("--batch", "apples:2,pears:0")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "invalid batch record at index 2\n")


if __name__ == "__main__":
    unittest.main()
