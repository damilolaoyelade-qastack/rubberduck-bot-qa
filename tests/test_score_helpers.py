"""Stdlib tests for average_score."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from score_helpers import average_score


class AverageScoreTests(unittest.TestCase):
    def test_empty_input_returns_zero(self):
        self.assertEqual(average_score([]), 0.0)

    def test_one_value_returns_that_value(self):
        value = 5.0
        self.assertEqual(average_score([value]), value)

    def test_two_four_six_returns_four(self):
        self.assertEqual(average_score([2.0, 4.0, 6.0]), 4.0)

    def test_negative_four_and_two_returns_negative_one(self):
        self.assertEqual(average_score([-4.0, 2.0]), -1.0)


if __name__ == "__main__":
    unittest.main()
