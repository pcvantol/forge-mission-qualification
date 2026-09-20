"""Acceptance control for reversing remaining batch records before grouping."""
import unittest

from acceptance._consumer import run_installed


class ReversedBatchContract(unittest.TestCase):
    def test_reverse_runs_after_skip_and_limit(self):
        result = run_installed(
            "--batch", "--skip", "1", "--limit", "2", "--reverse",
            "pear:2,apple:3,banana:4,grape:5",
        )
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"banana","quantity":4},{"name":"apple","quantity":3}],"total_quantity":7}\n',
        )

    def test_reverse_requires_batch_mode(self):
        result = run_installed("--reverse", "pear:2")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
