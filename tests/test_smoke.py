"""Baseline delivery check; behavioral acceptance has separate controls."""
import unittest

from mission_parser.cli import main


class SmokeTests(unittest.TestCase):
    def test_installed_entrypoint_target_exists(self):
        self.assertTrue(callable(main))


if __name__ == "__main__":
    unittest.main()
