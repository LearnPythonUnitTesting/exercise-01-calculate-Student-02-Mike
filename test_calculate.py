import unittest
import calculate


class TestCalculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate.add(5, 10), 15)

    def test_subtract(self):
        self.assertEqual(calculate.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculate.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calculate.divide(10, 5), 2)

    def test_reminder(self):
        self.assertEqual(calculate.reminder(10, 3), 1)

    def test_square(self):
        self.assertEqual(calculate.square(5), 25)

    def test_ceil(self):
        self.assertEqual(calculate.ceil(5.3), 6)

    def test_floor(self):
        self.assertEqual(calculate.floor(7.9), 7)
