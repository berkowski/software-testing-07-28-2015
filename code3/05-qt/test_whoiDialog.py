import unittest

from PyQt4 import (QtGui, QtTest)

from whoiDialog import WhoiDialog

def WhoiDialogTest(unittest.TestCase):
    """
    """


    def testHandleClick(self):

        text = "New label text!!!"

        whoiDialog = WhoiDialog()
        whoiDialog.label.setText(text)

        spy = QtTest
