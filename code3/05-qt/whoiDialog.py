#Need PyQt5, PyQt4 doesn't expose the QSignalSpy class
from PyQt5 import (QtWidgets, QtCore)

from ui import ui_whoiDialog

class WhoiDialog(QtWidgets.QDialog, ui_whoiDialog.Ui_Dialog):

    # Emitted with the lineEdit text when the user clicks the push button
    textChanged = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):

        QtWidgets.QDialog.__init__(self, parent=parent)

        self.setupUi(self)

        # Connect the pushbutton to our handleClick slot
        self.pushButton.clicked.connect(self.handleClick)

    @QtCore.pyqtSlot()
    def handleClick(self):

        # Get the text from the lineEdit
        lineText = self.lineEdit.text()

        # Set the label
        self.label.setText(lineText)

        # Send it with our textChanged signal
        self.textChanged.emit(lineText)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    gui = WhoiDialog()
    gui.show()
    app.exec_()
