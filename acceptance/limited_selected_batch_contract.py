"""Observe a batch limit applied after selection and before grouping."""
import unittest

from acceptance._consumer import run_installed


class LimitedSelectedBatchContract(unittest.TestCase):
    def test_limit_keeps_the_first_selected_record(self):
        result = run_installed(
            "--batch", "--prefix", "pre-", "--select", "pre-apples",
            "--limit", "1", "apples:2,pears:3,apples:4",
        )
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"pre-apples","quantity":2}],"total_quantity":2}\n',
        )

    def test_limit_precedes_grouping_after_quantity_scaling(self):
        result = run_installed(
            "--batch", "--scale", "2", "--group", "--prefix", "pre-",
            "--select", "pre-apples", "--limit", "1",
            "apples:2,pears:3,apples:4",
        )
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"pre-apples","quantity":4}],"total_quantity":4}\n',
        )

    def test_limit_requires_batch_mode(self):
        result = run_installed("--limit", "1", "apples:2")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
