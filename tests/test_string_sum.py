import unittest
from src.string_sum import stringSum

class TestStringSum(unittest.TestCase):
    def test_two_valid_numbers(self):
        self.assertEqual(stringSum("2", "3"), "5")

    def test_invalid_inputs(self):
        self.assertEqual(stringSum("a", "3"), "3")
        self.assertEqual(stringSum("2", "b"), "2")
        self.assertEqual(stringSum("a", "b"), "0")
        self.assertEqual(stringSum("", "3"), "3")
        self.assertEqual(stringSum("2", ""), "2")
        self.assertEqual(stringSum("", ""), "0")

    def test_large_numbers(self):
        self.assertEqual(stringSum("12345678901234567890", "98765432109876543210"), "111111111011111111100")

if __name__ == '__main__':
    unittest.main()