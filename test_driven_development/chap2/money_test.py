import unittest
from test_driven_development.chap2.money import Dollar
class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five=Dollar(5)
        tmp=five.times(2)

        self.assertEqual(10,tmp.amount)
        tmp=five.times(3)

        self.assertEqual(15,tmp.amount)

