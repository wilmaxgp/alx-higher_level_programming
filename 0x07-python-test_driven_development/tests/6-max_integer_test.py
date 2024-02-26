#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from ..6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_negative_values(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_max_integer_mixed_values(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([-1, -2, 0]), 0)

    def test_max_integer_duplicate_values(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

if __name__ == '__main__':
    unittest.main()
