import unittest

from theme1.polynomial import Polynomial


class MyTestCase(unittest.TestCase):
    def test_str_1(self):
        self.assertEqual('1 + 2x + -3x^2', str(Polynomial([1, 2, -3])))

    def test_str_2(self):
        self.assertEqual('', str(Polynomial([])))

    def test_str_3(self):
        self.assertEqual('3x^2', str(Polynomial([0, 0, 3])))

    def test_equals_1(self):
        self.assertEqual(Polynomial([1, 2]), Polynomial([1, 2]))

    def test_equals_2(self):
        self.assertFalse(Polynomial([1, 2]) == Polynomial([1, 3]))

    def test_equals_3(self):
        self.assertFalse(Polynomial([1, 2]) == [1, 2])

    def test_len_1(self):
        self.assertEqual(2, len(Polynomial([2, 3])))

    def test_len_2(self):
        self.assertEqual(0, len(Polynomial([])))


if __name__ == '__main__':
    unittest.main()
