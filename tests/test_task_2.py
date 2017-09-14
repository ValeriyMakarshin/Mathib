import unittest

from theme1.task2 import field_order


class Test2Case(unittest.TestCase):
    def test_field_order_1(self):
        self.assertEqual(10, field_order(3, 11))

    def test_field_order_2(self):
        self.assertEqual(5, field_order(3, 22))

    def test_field_order_3(self):
        self.assertEqual(None, field_order(2, 22))


if __name__ == '__main__':
    unittest.main()
