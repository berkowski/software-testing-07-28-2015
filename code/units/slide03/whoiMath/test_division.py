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

    def testDivision(self):
        "Test division"

        whoiMath = WhoiMath()
        min_value = 1
        max_value = 100
        num_samples = 100

        for _ in range(num_samples):
            a = randint(min_value, max_value)
            b = randint(min_value, max_value)

            expected = trusted_division(a, b)
            actual = whoiMath.divide(a, b)

            self.assertEqual(
                expected, actual,
                "%f != %f, Failed test with a=%d b=%d" % (expected, actual, a, b)
            )
