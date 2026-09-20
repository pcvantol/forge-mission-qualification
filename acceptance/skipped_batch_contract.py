"""Acceptance control for skipping selected records before limiting/grouping."""
import unittest

from acceptance._consumer import run_installed


class SkippedBatchContract(unittest.TestCase):
    def test_skip_runs_after_selection_and_before_limit(self):
        result = run_installed(
            "--batch", "--select", "pear", "--skip", "1", "--limit", "1",
            "pear:2,apple:3,pear:4,pear:5",
        )
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"pear","quantity":4}],"total_quantity":4}\n',
        )

    def test_skip_requires_batch_mode(self):
        result = run_installed("--skip", "1", "pear:2")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_zero_skip_preserves_prefixed_grouped_batch(self):
        result = run_installed(
            "--batch", "--prefix", "ripe-", "--skip", "0", "--group",
            "pear:2,pear:3",
        )
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"ripe-pear","quantity":5}],"total_quantity":5}\n',
        )

    def test_negative_skip_is_rejected(self):
        result = run_installed("--batch", "--skip", "-1", "pear:2")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
