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


if __name__ == "__main__":
    unittest.main()
