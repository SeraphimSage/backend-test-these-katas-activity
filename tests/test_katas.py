import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(10, 10), 20)
        self.assertEqual(katas.add(4, -3), 1)
        self.assertEqual(katas.add(-1, -5), -6)

    def test_multiply(self):
        self.assertEqual(katas.multiply(10, 10), 100)
        self.assertEqual(katas.multiply(4, -3), -12)
        self.assertEqual(katas.multiply(-1, -5), 5)

    def test_power(self):
        self.assertEqual(katas.power(2, 4), 16)
        self.assertEqual(katas.power(3, 4), 81)

    def test_factorial(self):
        self.assertEqual(katas.factorial(4), 24)
        self.assertEqual(katas.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(5), 3)
        self.assertEqual(katas.fibonacci(9), 21)


if __name__ == '__main__':
    unittest.main()
