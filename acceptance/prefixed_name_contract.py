"""Observe optional name prefixing through the installed parser entrypoint."""
import unittest

from acceptance._consumer import run_installed


class PrefixedNameContract(unittest.TestCase):
    def test_single_name_is_prefixed_without_changing_quantity(self):
        result = run_installed("--prefix", "pre-", "apples:2")
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual(result.stdout, '{"name":"pre-apples","quantity":2}\n')

    def test_batch_prefix_precedes_existing_grouping_and_scaling(self):
        result = run_installed(
            "--batch", "--scale", "2", "--group", "--prefix", "pre-",
            "apples:2,pears:3,apples:4",
        )
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual(
            result.stdout,
            '{"items":[{"name":"pre-apples","quantity":12},{"name":"pre-pears","quantity":6}],"total_quantity":18}\n',
        )


if __name__ == "__main__":
    unittest.main()
