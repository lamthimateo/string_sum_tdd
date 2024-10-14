import unittest

class TestStringSum(unittest.TestCase):
    def test_two_valid_numbers(self):
        self.assertEqual(stringSum("2", "3"), "5")

if __name__ == '__main__':
    unittest.main()