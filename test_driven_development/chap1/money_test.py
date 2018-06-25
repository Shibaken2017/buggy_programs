import unittest
from test_driven_development.chap1.money import Dollar
class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five=Dollar(5)
        five.times(2)

        self.assertEqual(10,five.amount)

