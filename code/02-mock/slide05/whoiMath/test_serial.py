"""
Tests send method of WhoiMath
"""

import unittest
import mock

from whoiMath import WhoiMath


class TestWhoiMathSend(unittest.TestCase):

    # Use a mock object for serial.Serial classes in this fixture, the
    # mocked object is passed along as an argument
    @mock.patch('serial.Serial')
    def testSend(self, mockSerial):
        "Test send method"

        # Create the class reference and set up test variables
        whoiMath = WhoiMath()

        # The number we'll give to the send method
        expected_result = 6.24512345

        # The string we're expecting to send along the serial port
        expected_serial_string = str(expected_result)

        # Run it
        whoiMath.send(expected_result)

        # The underlying Serial.write method should have been called once
        # with the expected string.  Use the convenience method
        # `assert_called_once_with` on the patched in mock
        whoiMath.serial.write.assert_called_once_with(expected_serial_string)
        #          ^      ^
        #          |      `------- write method automatically created by mock
        #          |               object
        #          `-------------- mock serial object created by patch
        #                          decorator
