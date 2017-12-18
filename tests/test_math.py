import unittest
import mock
from app import demo


class MathTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        result = demo.add(10, 10)
        self.assertEqual(result, 20)

    def test_subtract(self):
        result = demo.subtract(10, 10)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = demo.multiply(10, 10)
        self.assertEqual(result, 100)

    def test_divide(self):
        result = demo.divide(10, 10)
        self.assertEqual(result, 1)

    def test_default_route(self):
        result = demo.default()
        self.assertEqual(result, "Default Route")
