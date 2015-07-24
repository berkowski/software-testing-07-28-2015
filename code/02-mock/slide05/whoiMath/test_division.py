"""
Tests division method of WhoiMath
"""

import unittest
import mock
from random import randint

from whoiMath import WhoiMath


def trusted_division(a, b):
    """
    Returns the quotient of a and b


    Used for testing as 'trusted' implemntation of division.
    """

    return a * 1.0 / b


@mock.patch('whoiMath.WhoiMath.send')
class TestWhoiMathDivision(unittest.TestCase):

    def setUp(self):
        self.whoiMath = WhoiMath()
        self.min_value = 1
        self.max_value = 100
        self.num_samples = 100

    def testDivision(self, mockSerial):
        "Test division"

        for _ in range(self.num_samples):
            a = randint(self.min_value, self.max_value)
            b = randint(self.min_value, self.max_value)

            expected = trusted_division(a, b)
            actual = self.whoiMath.divide(a, b)

            self.assertEqual(
                expected, actual,
                "%f != %f, Failed test with a=%d b=%d" % (expected, actual, a, b)
            )

    def testDivisionSend(self, mockSerial):
        "Test send hook"

        a = 6
        b = 3

        result = self.whoiMath.divide(a, b, send=True)
        self.whoiMath.send.assert_called_once_with(result)

