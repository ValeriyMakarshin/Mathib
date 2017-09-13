import unittest
from theme1.task1 import fun_euler


class Test1Case(unittest.TestCase):
    def test_fun_euler_1(self):
        self.assertEqual(8, fun_euler(24))

    def test_fun_euler_prime(self):
        self.assertEqual(10, fun_euler(11))


if __name__ == '__main__':
    unittest.main()
