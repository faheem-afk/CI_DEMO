import unittest
from app import add, sub


class TestMathFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(4, 5), -1)
        self.assertEqual(sub(-1, 1), -2)


if __name__ == '__main__':
    unittest.main()
