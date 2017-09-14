import unittest

from theme1.task7 import is_prime_mr


class Test7Case(unittest.TestCase):
    def test_is_prime_mr_1(self):
        self.assertEqual(True, is_prime_mr(2147483647))

    def test_is_prime_mr_2(self):
        self.assertEqual(False, is_prime_mr(2147483646))

    def test_is_prime_mr_3(self):
        self.assertEqual(False, is_prime_mr(4))


if __name__ == '__main__':
    unittest.main()
