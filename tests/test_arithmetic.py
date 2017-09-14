import unittest

from utils.arithmetic import find_st, fast_mod_pow, find_prime_numbers, egcd, mod_inv


class TestArithmeticCase(unittest.TestCase):
    def test_find_st_1(self):
        self.assertEqual((1, 1), find_st(3))

    def test_find_st_2(self):
        self.assertEqual((4, 3), find_st(49))

    def test_find_st_3(self):
        self.assertEqual((0, 255), find_st(256))

    def test_fast_mod_pow_1(self):
        self.assertEqual(445, fast_mod_pow(4, 13, 497))

    def test_fast_mod_pow_2(self):
        self.assertEqual(40, fast_mod_pow(9, 2, 41))

    def test_find_prime_numbers_1(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], find_prime_numbers(20))

    def test_find_prime_numbers_2(self):
        self.assertEqual([2, 3, 5, 7, 11, 13], find_prime_numbers(13))

    def test_find_prime_numbers_negative(self):
        self.assertEqual([2, 3, 5], find_prime_numbers(-6))

    def test_find_prime_numbers_small(self):
        self.assertEqual([], find_prime_numbers(1))

    def test_egcd_1(self):
        self.assertEqual((11, 3, -2), egcd(55, 77))

    def test_egcd_2(self):
        self.assertEqual((1, 6, -5), egcd(11, 13))

    def test_mod_inv_1(self):
        self.assertEqual(6, mod_inv(11, 13))

    def test_mod_inv_2(self):
        self.assertEqual(8, mod_inv(7, 11))

    def test_mod_inv_3(self):
        self.assertEqual(None, mod_inv(6, 14))

if __name__ == '__main__':
    unittest.main()
