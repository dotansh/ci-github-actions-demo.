import unittest
from main import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_mixed_signs(self):
        self.assertEqual(add_numbers(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()
