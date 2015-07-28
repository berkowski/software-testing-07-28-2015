import unittest
from unittest import mock
import sys

from PyQt5 import (QtWidgets, QtTest)
from PyQt5.Qt import Qt

from whoiDialog import WhoiDialog


class WhoiDialogTest(unittest.TestCase):
    """
    Test WhoiDialog signals.
    """

    @classmethod
    def setUpClass(cls):
        "Create the QApplication once before any test"

        cls.app = QtWidgets.QApplication(sys.argv)

    def setUp(self):
        self.dialog = WhoiDialog()

    def testHandleClickSetsLabel(self):
        """
        Test handleClick slot sets the label.
        """

        # Text we'll set the line edit to, which will be emitted
        text = "New label text!!!"

        # Set the line edit text
        self.dialog.lineEdit.setText(text)

        # Call the method
        self.dialog.handleClick()

        # Make sure the label text matches
        self.assertEqual(self.dialog.label.text(), text)

    def testHandleClickCalledByButton(self):
        """
        Test handleClick is called when the user presses the pushButton
        """

        # Patch the handleClick slot here -- have to re-intialize the
        # self.dialog version though
        with mock.patch('whoiDialog.WhoiDialog.handleClick'):

            self.dialog = WhoiDialog()

            # Simulate pushing the button with the left mouse button
            QtTest.QTest.mouseClick(self.dialog.pushButton, Qt.LeftButton)

            # slot should be called once with 'False' (pushButton's
            # 'clicked' signal actually has a 'checked' parameter, that defaults
            # to False)
            self.dialog.handleClick.assert_called_once_with(False)

    def testHandleClickEmitsTextChanged(self):
        """
        Test handleClick emits the textChanged signal
        """

        # Connect a spy to our dialog's textChanged signal
        spy = QtTest.QSignalSpy(self.dialog.textChanged)

        # Text we'll set the line edit to, which will be emitted
        text = "New label text!!!"

        # Set the line edit text
        self.dialog.lineEdit.setText(text)

        # No signals caught by our spy
        self.assertEqual(len(spy), 0)

        # Call the slot
        self.dialog.handleClick()

        # Verify that one signal was emitted
        self.assertEqual(len(spy), 1)

        # ... and it only had one element
        self.assertEqual(len(spy[0]), 1)

        # Get that element...
        emittedText = spy[0][0]

        # Verify the value of the signal
        self.assertEqual(emittedText, text)
