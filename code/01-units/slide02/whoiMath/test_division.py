"""
Tests division method of WhoiMath
"""

import unittest

from whoiMath import WhoiMath


class TestWhoiMathDivision(unittest.TestCase):

    def testDivision(self):
        "Test division"

        whoiMath = WhoiMath()
        self.assertEqual(2, whoiMath.divide(6, 3))
