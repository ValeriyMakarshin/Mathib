import unittest

from theme1.finite_field import FiniteField
from theme1.polynomial import Polynomial


class TestArithmeticCase(unittest.TestCase):
    ff1 = FiniteField(5)
    ff2 = FiniteField(11)
    lst1 = Polynomial([1, 2, 3, 4])
    lst2 = Polynomial([-5, 7])
    lst3 = Polynomial([8, 2, 1])
    lst_empty = Polynomial([])

    def test_add_1(self):
        self.assertEqual(self.lst1, self.ff1.add(self.lst1, self.lst_empty))

    def test_add_2(self):
        self.assertEqual(Polynomial([1, 4, 3, 4]), self.ff1.add(self.lst1, self.lst2))

    def test_add_3(self):
        self.assertEqual(Polynomial([3, 9, 1]), self.ff2.add(self.lst2, self.lst3))

    def test_sub_1(self):
        self.assertEqual(self.lst1, self.ff1.sub(self.lst1, self.lst_empty))

    def test_sub_2(self):
        self.assertEqual(Polynomial([1, 0, 3, 4]), self.ff1.sub(self.lst1, self.lst2))

    def test_sub_3(self):
        self.assertEqual(Polynomial([9, 5, 10]), self.ff2.sub(self.lst2, self.lst3))

    def test_mul_1(self):
        self.assertEqual(self.lst_empty, self.ff1.mul(self.lst1, self.lst_empty))

    def test_mul_2(self):
        self.assertEqual(Polynomial([0, 2, 4, 1, 3]), self.ff1.mul(self.lst1, self.lst2))

    def test_mul_3(self):
        self.assertEqual(Polynomial([4, 2, 9, 7]), self.ff2.mul(self.lst2, self.lst3))


if __name__ == '__main__':
    unittest.main()
