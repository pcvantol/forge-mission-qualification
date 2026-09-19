"""Criterion: a positive scale applies to single records and batch totals."""
import unittest

from acceptance._consumer import run_installed


class ScaledQuantityTests(unittest.TestCase):
    def test_single_record_scales_quantity(self):
        result = run_installed("--scale", "3", "apples:2")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, '{"name":"apples","quantity":6}\n')

    def test_batch_scales_each_record_and_total(self):
        result = run_installed("--batch", "--scale", "2", "apples:2,pears:3")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"apples","quantity":4},{"name":"pears","quantity":6}],"total_quantity":10}\n',
        )

    def test_non_positive_scale_rejected_without_result(self):
        result = run_installed("--scale", "0", "apples:2")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
