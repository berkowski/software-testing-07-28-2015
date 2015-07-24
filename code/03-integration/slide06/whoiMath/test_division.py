"""
Tests division method of WhoiMath
"""

import unittest
from random import randint

from whoiMath import WhoiMath


def trusted_division(a, b):
    """
    Returns the quotient of a and b


    Used for testing as 'trusted' implemntation of division.
    """

    return a * 1.0 / b


class TestWhoiMathDivision(unittest.TestCase):

    def setUp(self):
        self.whoiMath = WhoiMath()
        self.min_value = 1
        self.max_value = 100
        self.num_samples = 100

    def testDivision(self):
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
