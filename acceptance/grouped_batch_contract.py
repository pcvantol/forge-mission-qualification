"""Criterion: a grouped batch sums duplicate names in first-seen order."""
import unittest

from acceptance._consumer import run_installed


class GroupedBatchTests(unittest.TestCase):
    def test_grouped_batch_preserves_first_seen_order(self):
        result = run_installed("--batch", "--group", "apples:2,pears:3,apples:4")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"apples","quantity":6},{"name":"pears","quantity":3}],"total_quantity":9}\n',
        )

    def test_grouping_uses_scaled_quantities(self):
        result = run_installed("--batch", "--scale", "2", "--group", "apples:2,apples:3")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"apples","quantity":10}],"total_quantity":10}\n',
        )

    def test_group_option_requires_batch(self):
        result = run_installed("--group", "apples:2")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
