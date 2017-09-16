import unittest

from theme1.task5 import is_primary


class Test5Case(unittest.TestCase):
    def test_is_prime_zero(self):
        self.assertEqual(False, is_primary(0))

    def test_is_prime_1(self):
        self.assertEqual(False, is_primary(4))

    def test_is_prime_2(self):
        self.assertEqual(True, is_primary(5))

    def test_is_prime_3(self):
        self.assertEqual(False, is_primary(6))

    def test_is_prime_4(self):
        self.assertEqual(True, is_primary(7))

    def test_is_prime_5(self):
        self.assertEqual(False, is_primary(9))


if __name__ == '__main__':
    unittest.main()