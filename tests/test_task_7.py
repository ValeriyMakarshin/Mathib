import unittest
from theme1.task7 import fast_mod_pow, is_prime_mr


class Test7Case(unittest.TestCase):
    def test_fast_mod_pow_1(self):
        self.assertEqual(445, fast_mod_pow(4, 13, 497))

    def test_fast_mod_pow_2(self):
        self.assertEqual(40, fast_mod_pow(9, 2, 41))

    def test_is_prime_mr_1(self):
        self.assertEqual(True, is_prime_mr(2147483647))

    def test_is_prime_mr_2(self):
        self.assertEqual(False, is_prime_mr(2147483646))

    def test_is_prime_mr_3(self):
        self.assertEqual(False, is_prime_mr(4))

if __name__ == '__main__':
    unittest.main()
