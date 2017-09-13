import unittest
from utils import arithmetic


class TestArithmeticCase(unittest.TestCase):
    def test_find_prime_numbers_1(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], arithmetic.find_prime_numbers(20))

    def test_find_prime_numbers_2(self):
        self.assertEqual([2, 3, 5, 7, 11, 13], arithmetic.find_prime_numbers(13))

    def test_find_prime_numbers_negative(self):
        self.assertEqual([2, 3, 5], arithmetic.find_prime_numbers(-6))

    def test_find_prime_numbers_small(self):
        self.assertEqual([], arithmetic.find_prime_numbers(1))

if __name__ == '__main__':
    unittest.main()
