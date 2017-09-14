import unittest

from theme1.task6 import is_prime_witnesses


class Test6Case(unittest.TestCase):
    def test_is_prime_witnesses_1(self):
        self.assertEqual(True, is_prime_witnesses(3, 29))

    def test_is_prime_witnesses_2(self):
        self.assertEqual(True, is_prime_witnesses(87, 3996001))

    def test_is_prime_witnesses_3(self):
        self.assertEqual(True, is_prime_witnesses(87, 1999))

    def test_is_prime_witnesses_4(self):
        self.assertEqual(False, is_prime_witnesses(3, 342))

    def test_is_prime_witnesses_5(self):
        self.assertEqual(False, is_prime_witnesses(11, 253))

    def test_is_prime_witnesses_6(self):
        self.assertEqual(False, is_prime_witnesses(9, 636))

    def test_is_prime_witnesses_false_witnesses(self):
        self.assertEqual(True, is_prime_witnesses(87, 3996001))


if __name__ == '__main__':
    unittest.main()
