"""Observe batch selection on the names emitted after optional prefixing."""
import unittest

from acceptance._consumer import run_installed


class SelectedBatchContract(unittest.TestCase):
    def test_selection_uses_prefixed_names_and_preserves_order(self):
        result = run_installed(
            "--batch", "--prefix", "pre-", "--select", "pre-apples",
            "apples:2,pears:3,apples:4",
        )
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"pre-apples","quantity":2},{"name":"pre-apples","quantity":4}],"total_quantity":6}\n',
        )

    def test_selection_combines_with_grouping_after_scaling(self):
        result = run_installed(
            "--batch", "--scale", "2", "--group", "--prefix", "pre-",
            "--select", "pre-apples", "apples:2,pears:3,apples:4",
        )
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"pre-apples","quantity":12}],"total_quantity":12}\n',
        )

    def test_selection_requires_batch_mode(self):
        result = run_installed("--select", "apples", "apples:2")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
