"""
WHOI Math Class.

Simple math class for use in WHOI software.... because why not?

author:  Zac Berkowitz <zberkowitz@whoi.edu>
"""


class WhoiMath(object):
    """
    Simple math operators for WHOI software.

    methods:
        add(a,b)       Return sum of a and b
        subtract(a,b)  Return difference of a and b
        multiply(a,b)  Return product of a and b
        divide(a,b)    Return quotient of a and b
    """

    @staticmethod
    def add(a, b):
        "Return the sum of two numbers."
        raise NotImplementedError

    @staticmethod
    def subtract(a, b):
        "Return the difference of two numbers."
        raise NotImplementedError

    @staticmethod
    def multiply(a, b):
        "Return the product of two numbers."
        raise NotImplementedError

    @staticmethod
    def divide(a, b):
        "Return the quotient of two numbers."
        raise NotImplementedError
