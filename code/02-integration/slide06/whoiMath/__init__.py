"""
WHOI Math Class.

Simple math class for use in WHOI software.... because why not?

Now sends results over serial!  Because it's helpful!

author:  Zac Berkowitz <zberkowitz@whoi.edu>
"""

import serial

class WhoiMath(object):
    """
    Simple math operators for WHOI software.

    methods:
        add(a,b)       Return sum of a and b
        subtract(a,b)  Return difference of a and b
        multiply(a,b)  Return product of a and b
        divide(a,b)    Return quotient of a and b
    """

    def __init__(self, port=None):

        self.serial = serial.Serial(port)

    def send(self, result):
        "Send result over serial connection."

        str_result = str(result)
        self.serial.write(str_result)

    def divide(self, a, b, send=False):
        """
        Return the quotient of two numbers.

        If `send` is True the result will be sent over the serial port.

        >>> whoiMath = WhoiMath()
        >>> whoiMath.divide(6, 3)
        2.0

        # >>> WhoiMath.divide(10, 2.5)
        # 4
        """
        result = float(a) / b

        if send:
            self.send(result)

        return result
