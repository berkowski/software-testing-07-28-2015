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

    def testIdentity(self):
        "Test anything dividied by 1 remains the same"

        for _ in range(self.num_samples):
            a = randint(self.min_value, self.max_value)

            expected = a
            actual = self.whoiMath.divide(a, 1)

            self.assertEqual(
                expected, actual,
                "%f != %f, Failed test with a=%d b=%d" % (expected, actual, a, 1)
            )

    def testZero(self):
        "Test zero divided by anything = 0"

        for _ in range(self.num_samples):
            b = randint(self.min_value, self.max_value)

            expected = 0
            actual = self.whoiMath.divide(0, b)

            self.assertEqual(
                expected, actual,
                "%f != %f, Failed test with a=%d b=%d" % (expected, actual, 0, b)
            )

    def testDivideByZero(self):
        "Test divide by zero raises ZeroDivisionError"

        with self.assertRaises(ZeroDivisionError):
            self.whoiMath.divide(1,0)
